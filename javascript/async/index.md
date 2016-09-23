# Asynchrone

.fx: extra-large

---

# σύγ

.fx: extra-large

---

# σύγ

*syn* : ensemble

Exemples : synthèse, synopsis, synchrétisme

.fx: extra-large

---

# χρονος

.fx: extra-large

---

# χρονος

*chronos* : le temps

Exemples : chronologie, chronomètre

.fx: extra-large

---

# A-syn-chrone

Qui ne se fait pas en même temps.

* une partie du code s'exécute *maintenant*
* une partie s'exécute *plus tard*

![](img/doc.jpeg)

.fx: extra-large

---

# Exemple : timer

    !js
    log("Maintenant");

    setTimeout(function() {
        log("Plus tard");
    }, 2000);

    log("Maintenant aussi");

<button class="run"></button>

---

# Exemple : requête HTTP

    !js
    var xhr = new XMLHttpRequest();
    log("Maintenant");
    xhr.addEventListener("load", function() {
       log("Plus tard : " + this.responseText);
    });
    xhr.open("GET", "http://localhost:8080/data/greeting.txt", true);
    xhr.send(null);
    log("Maintenant aussi");

<button class="run"></button>

---

# Exemple : lecture d'un fichier

    !js
    var fs = require('fs'), http = require('http');

    http.createServer(function (req, res) {
        fs.readFile(__dirname + req.url, function (err, data) {
          res.setHeader('Access-Control-Allow-Origin', '*');
          res.writeHead(200);
          setTimeout(function() {
            res.end(data);
          }, 2000);  // Délai artificiel pour la démo
        });
    }).listen(8080);

---

# Les événements

Exemples :

- Un descripteur de fichier est prêt pour la lecture ou l''ecriture
- Un timer arrive à échéance
- Un événement créé par l'utilisateur (clic de souris)
- Un signal envoyé au processus

---

# La boucle d'évéments : algorithme simplifié

    !js
    // Pseudo code
    while (true) {
       activeEvents = pollForActiveEvents(eventQueue);
       activeEvents.forEach(function(activeEvent) {
           activeEvent.callback();
           eventQueue.remove(activeEvent);
       });
    }

---

# La boucle d'évéments

## Caractéristiques

- un seul fil d'exécution
- inspection non bloquantes des descripteurs de fichiers (select, epoll, kqueue, etc.)
- gestion des timers (notion de temps)
- gestion des événement utilisateurs
- unité atomique d'exécution : **la fonction**

## Implémentations en C

- [libevent](http://www.wangafu.net/~nickm/libevent-book/Ref3_eventloop.html) (Chromium, Tmux, Transmission) 
- [libuv](http://nikhilm.github.io/uvbook/basics.html) (Node.js) 


---

# Exemple : timer sans délai

    !js
    log("D'abord");

    setTimeout(function() {
        log("Finalement");
    }, 0);

    log("Ensuite");


<button class="run"></button>

---

# Fonction pour requêtes HTTP

    !js
    function request(url, callback) {
      var xhr = new XMLHttpRequest();
      xhr.addEventListener("load", function() {
        callback(xhr.responseText);
      });
      xhr.open("GET", url, true);
      xhr.send(null);
    }

    log("Envoi de la requête");
    request("http://localhost:8080/data/greeting.txt", function(data) {
      log("Réponse reçue : " + data);
    }); 

<button class="run"></button>

---

# L'enfer des callbacks

- difficulté à suivre le déroulement du code basé sur des callbacks
- difficulité à faire collaborer des callbacks entre elles

---

# Des promesses

- chainer des tâches asynchrones
- attendre la fin de plusieurs tâches asynchrone
- traiter de manière polymorphique des tâches asynchrones et des taches synchrones : exemple du cache
- exemples d'API standard utilisant les promises : Fetch, Web Audio API, Service Workers, etc.

---

# jQuery

Montrer l'utilisation des Promises avec jQuery et les problèmes

---

# Les générateurs et les coroutines

---

# async / await

---

# Les observables
