# Démystifier les entrées/sorties asynchrones

La programmation basée sur les entrées/sorties asynchrones en Python : cas
d'utilisations, fonctionnement interne, contraintes et styles de programmation.

![](img/petit_dej.jpg)

---

# CPU-bound

Temps d'exécution limité par le processeur.

Calculs bruts, encodage de données, etc.

**↪ l'asynchrone ne sert à rien**

Pour aller plus vite :

 * optimiser les algorithmes
 * rajouter des processus

---

# I/O bound

Temps d'exécution limité par les entrées/sorties

 * requêtes base de données
 * services REST externes
 * fork de processus externes
 * accès au système de fichiers

**↪ l'asynchrone peut être utile**

---

# Nombreux clients connectés

WebSockets **→ l'asynchrone est vite indispensable**

![](img/busy_restaurant.jpg)

---

# L'asynchrone peut-il nous aider ?

Nos processus passent leur temps à attendre ? Plus assez d'espace (mémoire) pour en ajouter d'autres ?

**↪ Les passer en asynchrone peut aider.**

Nos processus travaillent ?

**↪ Les passer en asynchrone ne va pas aider.**

On peut par contre envisager d'externaliser ce travail pour les passer en asynchrone.


---

# Tornado

    !python
    import tornado.ioloop
    import tornado.web


    class MainHandler(tornado.web.RequestHandler):
        def get(self):
            self.write("Hello, world")


    application = tornado.web.Application([
        (r"/", MainHandler),
    ])

    if __name__ == "__main__":
        print("Serve http://127.0.0.1:8888/")
        application.listen(8888)
        tornado.ioloop.IOLoop.instance().start()

10 000 requêtes par lots de 100 :

    !console
    $ ab -n 10000 -c 100 http://127.0.0.1:8888/
    Time taken for tests:   6.706 seconds
    Complete requests:      10000
    Requests per second:    1491.25 [#/sec] (mean)
    Time per request:       67.058 [ms] (mean)

---

# Tornado avec SQL bloquant

    !python
    class MainHandler(tornado.web.RequestHandler):
        def get(self):
            cur = self.application.db.cursor()
            cur.execute("SELECT 42, pg_sleep(0.300);")
            result = cur.fetchone()
            self.write("Result: %s" % result[0])

20 requêtes par lots de 10 :

    !console
    $ ab -n 20 -c 10 http://127.0.0.1:8888/ 
    Time taken for tests:   6.201 seconds
    Complete requests:      20
    Requests per second:    3.23 [#/sec] (mean)
    Time per request:       3100.513 [ms] (mean)

---

# Tornado avec SQL asynchrone

    !python
    from tornado import web, ioloop
    import momoko

    class MainHandler(tornado.web.RequestHandler):

        @tornado.web.asynchronous
        def get(self):
            self.application.db.execute(
                'SELECT 42, pg_sleep(0.300)', callback=self._done)

        def _done(self, cursor, error):
            result = cursor.fetchone()
            self.write("Result: %s" % result[0])
            self.finish()

    if __name__ == "__main__":
        application = tornado.web.Application([(r"/", MainHandler)])
        application.db = momoko.Pool(dsn='dbname=al user=al', size=10)
        application.listen(8888)
        ioloop.IOLoop.instance().start()


20 requêtes par lots de 10 :

    !console
    $ ab -n 20 -c 10 http://127.0.0.1:8888/
    Time taken for tests:   0.622 seconds
    Complete requests:      20
    Requests per second:    32.18 [#/sec] (mean)
    Time per request:       310.756 [ms] (mean)

---

# Structure d'une IO loop

Version extrêmement simplifiée de l'IOLoop de Tornado :

    !python
    def start(self):
        while True:
            # Appelle la fonction de polling de la plateforme
            # (epoll sous Linux, kqueue sous BSD). Celle-ci 
            # renvoie les événements survenus sur les
            # descripteurs de fichiers (sockets, etc.) surveillés
            event_pairs = self._impl.poll(poll_timeout)
            self._events.update(event_pairs)
            while self._events:
                # Appelle les handler d'événements enregistrés
                fd, events = self._events.popitem()
                fd_obj, handler_func = self._handlers[fd]
                handler_func(fd_obj, events)

Enregistrement des handlers :

    !python
    def add_handler(self, fd, handler, events):
        fd, obj = self.split_fd(fd)
        self._handlers[fd] = (obj, stack_context.wrap(handler))
        self._impl.register(fd, events | self.ERROR)

---

# Callbacks

    !python
    class MainHandler(tornado.web.RequestHandler):

        @tornado.web.asynchronous
        def get(self):

            def handle_db(cursor, error):
                db_value = cursor.fetchone()[0]

                def handle_http(response):
                    json_data = json.loads(response.body.decode())
                    result = db_value - json_data['value']
                    self.write("Result: %s" % result)
                    self.finish()

                http_client = tornado.httpclient.AsyncHTTPClient()
                http_client.fetch('http://127.0.0.1:8000/', handle_http)

            self.application.db.execute(
                'SELECT 42, pg_sleep(0.300)', callback=handle_db)

20 requêtes par lots de 10 :

    !console
    $ ab -c 10 -n 20 http://127.0.0.1:8888/
    Time taken for tests:   1.260 seconds
    Complete requests:      20
    Requests per second:    15.88 [#/sec] (mean)
    Time per request:       629.834 [ms] (mean)

---

# Coroutines

    !python
    class MainHandler(tornado.web.RequestHandler):

        @tornado.gen.coroutine
        def get(self):
            cursor = yield momoko.Op(self.application.db.execute,
                                     'SELECT 42, pg_sleep(0.300)')
            db_value = cursor.fetchone()[0]
            http_client = tornado.httpclient.AsyncHTTPClient()
            response = yield http_client.fetch('http://127.0.0.1:8000/')
            json_data = json.loads(response.body.decode())
            result = db_value - json_data['value']
            self.write("Result: %s" % result)
            self.finish()

20 requêtes par lots de 10 :

    !console
    $ ab -c 10 -n 20 http://127.0.0.1:8888/
    Time taken for tests:   1.281 seconds
    Complete requests:      20
    Requests per second:    15.61 [#/sec] (mean)
    Time per request:       640.527 [ms] (mean)

---

# Parallélisme

    !python
    class MainHandler(tornado.web.RequestHandler):

        @tornado.gen.coroutine
        def get(self):
            http_client = tornado.httpclient.AsyncHTTPClient()
            # Lancement des requêtes en parallèle
            cursor, response = yield [
                momoko.Op(self.application.db.execute,
                          'SELECT 42, pg_sleep(0.300)'),
                http_client.fetch('http://127.0.0.1:8000/'),
            ]
            db_value = cursor.fetchone()[0]
            json_data = json.loads(response.body.decode())
            result = db_value - json_data['value']
            self.write("Result: %s" % result)
            self.finish()

20 requêtes par lots de 10 :

    !console
    $ ab -c 10 -n 20 http://127.0.0.1:8888/
    Time taken for tests:   0.663 seconds
    Complete requests:      20
    Requests per second:    30.15 [#/sec] (mean)
    Time per request:       331.638 [ms] (mean)

---

# Depuis Python 3.5 : async/await

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod
tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At
vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren,
no sea takimata sanctus est Lorem ipsum dolor sit amet.

---

# Cas d'utilisation réel 1 : Circus

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod
tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At
vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren,
no sea takimata sanctus est Lorem ipsum dolor sit amet.

---

# Cas d'utilisation réel 2 : THR

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod
tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At
vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren,
no sea takimata sanctus est Lorem ipsum dolor sit amet.

---

# En conclusion

Quand utiliser de l'asynchrone ?

  1. le traitement des requêtes est ralenti par l'accès à des ressources externes : base de données, service externe, connexion persistante avec le navigateur, etc.
  2. pas assez de mémoire pour simplement rajouter des processus ou des threads
  3. On veut éviter les threads et les mécanismes d'exclusion mutuelle qui vont avec

Comment coder en asynchrone ?

  * utiliser une plateforme ou une bibliothèque faite pour ça (Tornado, Twisted, asyncio, etc.)
  * callbacks
  * generateurs
  * async/await
