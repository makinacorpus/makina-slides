# L'asynchrone en JavaScript

- Alex Marandon
- Simon Bats

.fx: extra-large

![](img/logo-black.png)

---

# σύγ

*syn* : ensemble

Exemples : synthèse, synopsis, synchrétisme

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
    xhr.open("GET", "/data/greeting.txt", true);
    xhr.send(null);
    log("Maintenant aussi");

<button class="run"></button>

---

# Exemple : lecture d'un fichier

Code du serveur répondant à la requête précédente :

    !js
    var fs = require('fs'), http = require('http');

    http.createServer(function (req, res) {
      fs.readFile(__dirname + req.url, function (err, data) {
        res.writeHead(200);
        setTimeout(function() {  // Délai artificiel pour la démo
          res.end(data);
        }, 2000);
      });
    }).listen(8080);

---

# Les événements

L'exécution du code asynchrone est déclenchée par des événements.

Exemples :

- Un descripteur de fichier est prêt pour la lecture ou l'ecriture
- Un timer arrive à échéance
- Un événement est créé par l'utilisateur (clic de souris)
- Un signal est envoyé au processus

---

# La boucle d'évéments

Algorithme très simplifié :

    !js
    // Pseudo code
    while (true) {  // Boucle sans fin

       // Recherche les événements actifs
       activeEvents = pollForActiveEvents(eventQueue);

       activeEvents.forEach(function(activeEvent) {
           // Exécute les fonctions associées
           activeEvent.callback();
           eventQueue.remove(activeEvent);
       });
    }

---

# La boucle d'évéments

## Implémentations notables

- [libevent](http://www.wangafu.net/~nickm/libevent-book/Ref3_eventloop.html) (Chromium, Tmux, Transmission)
- [libuv](http://nikhilm.github.io/uvbook/basics.html) (Node.js)

![](img/logo-libuv.png)

---

# La boucle d'évéments

## Caractéristiques

- un seul fil d'exécution : pas d'accès concurrent à la mémoire
- scrute les descripteurs de fichiers sans bloquer à l'aide des outils
  spécifiques au système hôte : epoll pour Linux, kqueue pour BSD/OSX, etc.
- gestion des timers (notion de temps)
- gestion des événement utilisateurs (souris, clavier, etc.)
- unité atomique d'exécution : **la fonction**

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

# Exemple : timer sans délai

    !js
    log("D'abord");

    setTimeout(function() {
        log("Finalement");
    }, 0);

    log("Ensuite");


![](img/execution-queue.jpg)

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
    request("/data/greeting.txt", function(data) {
      log("Réponse reçue : " + data);
    });

<button class="run"></button>

---

# Appels asynchrones multiples

    !js
    request("/data/data1.json", function(data) {
      log(data);
      var value1 = JSON.parse(data).value;
      request("/data/data2.json", function(data) {
        log(data);
        var value2 = JSON.parse(data).value;
        request("/data/data3.json", function(data) {
          log(data);
          var value3 = JSON.parse(data).value;
          log("Résultat : " + (value1 + value2 + value3));
        });
      });
    });

<button class="run"></button>

---

# Appels asynchrones multiples

    !js

    request("/data/data1.json", function(data) {
      var value1 = JSON.parse(data).value;
      getData2(value1);
    });

    function getData2(value1) {
      request("/data/data2.json", function(data) {
        var value2 = JSON.parse(data).value;
        getData3(value1, value2);
      });
    }

    function getData3(value1, value2) {
      request("/data/data3.json", function(data) {
        var value3 = JSON.parse(data).value;
        log("Résultat : " + (value1 + value2 + value3));
      });
    }

<button class="run"></button>

---

# L'enfer des callbacks

- difficulté à suivre le déroulement du code basé sur des callbacks
- difficulté à faire collaborer des callbacks entre elles

---

# Des promesses

---

# Qu'est-ce qu'une promesse ?

C'est une opération

* **unique**
* **asynchrone**
* **pas forcément complétée**
* **attendue dans le futur**
* 3 états : **en attente**, **satisfaite** ou **rejetée**

---

# Création d'une promesse

    !js
    function requestPromise(url) {
      return new Promise(function(resolve, reject) {
        var xhr = new XMLHttpRequest();
        xhr.addEventListener("load", function() {
          resolve(xhr.responseText);
        });
        xhr.open("GET", url, true);
        xhr.send(null);
      });
    }

---

# Utilisation d'une promesse

    !js
    var value1, value2, value3;
    requestPromise("/data/data1.json").then(function(data) {
      log(data); value1 = JSON.parse(data).value;
      return requestPromise("/data/data2.json");
    }).then(function(data) {
      log(data); value2 = JSON.parse(data).value;
      return requestPromise("/data/data3.json");
    }).then(function(data) {
      log(data); value3 = JSON.parse(data).value;
      log("Résultat : " + (value1 + value2 + value3));
    });


<button class="run"></button>

---

# Gestion des erreurs

    !js
    var value1, value2, value3;
    requestPromise("/data/data1.json").then(function(data) {
      log(data); value1 = JSON.parse(data).value;
      return requestPromise("/data/invalid.json");
    }).then(function(data) {
      log(data); value2 = JSON.parse(data).value;
      return requestPromise("/data/data3.json");
    }).then(function(data) {
      log(data); value3 = JSON.parse(data).value;
      log("Résultat : " + (value1 + value2 + value3));
    }).catch(function(err) {
      log(err);
    });


<button class="run"></button>

---

# Parallélisme

    !js
    Promise.all([
      requestPromise("/data/data1.json"),
      requestPromise("/data/data2.json"),
      requestPromise("/data/data3.json")
    ]).then(function(responses) {
        var values = responses.map(
          (text) => JSON.parse(text).value
        );
        log("Résultat : " + sum(values));
    });

<button class="run"></button>

---

# Polymorphisme synchrone/asynchrone

    !js
    var cache = new Map(), url = "data/data1.json";
    function getWithCache(url) {
      if (cache.has(url)) {
        return Promise.resolve(cache.get(url));  // Promesse déjà résolue
      } else {
        var promise = requestPromise(url)
        promise.then(function(value) {       // 1er then
          cache.set(url, value);
        });
        return promise;
      }
    }
    getWithCache(url).then(function(value) { // 2ème then
        log(value);
        getWithCache(url).then(log);
    });

<button class="run"></button>

---

# Cas d'utilisation réel : l'API Fetch

    !js
    fetch("/data/data1.json")
    .then((response) => response.json())
    .then((data) => log(data.value));

<button class="run"></button>

---

# Parallélisme avec fetch

    !js
    Promise.all([
      fetch("/data/data1.json"),
      fetch("/data/data2.json"),
      fetch("/data/data3.json")
    ]).then(function(responses) {
        Promise.all(
          responses.map(response => response.json())
        ).then(function(data) {
          var values = data.map((obj) => obj.value);
          log("Résultat : " + sum(values));
        });
    });

<button class="run"></button>

---

# Les générateurs

    !js
    function *mygen() {
      yield "Bonjour";
      var name = yield "Comment t'appelles-tu ?";
      yield "Enchanté " + name + " !";
    }

    var it = mygen();
    var yieldedValue = it.next(); // {"value":"Bonjour","done":false}
    log(JSON.stringify(yieldedValue));

<button class="run"></button>

---

# Les générateurs

    !js
    function *mygen() {
      yield "Bonjour";
      var name = yield "Comment t'appelles-tu ?";
      yield "Enchanté " + name + " !";
    }

    var it = mygen();
    log(it.next().value);
    log(it.next().value);
    log(it.next("Toto").value);   // Passage de valeur au générateur
    log(JSON.stringify(it.next()));

<button class="run"></button>

---

# yield

Deux significations :

- produire (récoltes, résultat d'investissement)
- céder (un bien, sa place)

---

# Générateur et callback

    !js
    function *main() {
      var response = yield requestWrapper("/data/greeting.txt");
      log(response);
    }

    function requestWrapper(url) {
      return request(url, function(data) {
        it.next(data);
      });
    }

    var it = main();
    it.next();

<button class="run"></button>

---

# Générateur et promise

    !js
    function *main() {
      var response = yield requestPromise("/data/greeting.txt");
      log(response);
    }

    var it = main();
    var promise = it.next().value;
    promise.then(log);

<button class="run"></button>

---

# Exécuteur de générateur

Fonction run issue de [You don't know JS: Async & Performance](https://github.com/getify/You-Dont-Know-JS/blob/master/async%20%26%20performance/ch4.md#promise-aware-generator-runner)

    !js
    run(function *main() {
      var response = yield fetch("/data/greeting.txt");
      var text = yield response.text();
      log(text);
      var responses = yield Promise.all([
        fetch("/data/data1.json"),
        fetch("/data/data2.json"),
        fetch("/data/data3.json")
      ]);
      var data = yield Promise.all(
        responses.map((response) => response.json())
      );
      var numbers = data.map((item) => item.value);
      log(sum(numbers));
    });

<button class="run"></button>


---

# async / await

    !js
    async function main() {
      var response = await fetch("/data/greeting.txt");
      var text = await response.text();
      log(text);
      var responses = await Promise.all([
        fetch("/data/data1.json"),
        fetch("/data/data2.json"),
        fetch("/data/data3.json")
      ]);
      var data = await Promise.all(
        responses.map((response) => response.json())
      );
      var numbers = data.map((item) => item.value);
      log(sum(numbers));
    }

    main();

- exécution du générateur directement par le moteur JavaScript
- sématique propre à l'asynchrone

---

# La programmation réactive (PR)

---

# PR - Introduction
<div style="text-align: center; font-size: 1.2em;">Développer via des flux de données asynchrone.</div>

* L'évènementiel à son paroxisme

* Tout devient un flux **observable** auquel on peut s'inscrire :
<br/>variables, propriétés, structures de données, ...

* Des outils de manipulation de flux déjà connus :
<br/>**merge**, **filter**, **map**

---

# PR - Les flux :
<div style="text-align: center; font-size: 1.2em;">Un flux est une séquence continue d'évènements.</div>

* Chaque évènement peut contenir :
<br/>une valeur, une erreur, ou un signal de fin de flux

* On s'**inscrit** alors au flux afin de **réagir** lors d'un évènement.

![](img/stream.png)

Les fonctions définis sont les **observers** alors que le flux lui est l'**observable**

---

# Création d'un Observable

    !js
    function requestObservable(url) {
      return Rx.Observable.create((observer) => {
        var xhr = new XMLHttpRequest();
        xhr.addEventListener("load", () => {
          observer.onNext(xhr.responseText);
          observer.onCompleted();
        });
        xhr.open("GET", url, true);
        xhr.send(null);
      });
    }

---

# Utilisation d'Observables

    !js
    var res = 0;
    var ob1 = requestObservable("/data/data1.json");
    var ob2 = requestObservable("/data/data2.json");
    var ob3 = requestObservable("/data/data3.json");
    var merged = Rx.Observable.merge(ob1, ob2, ob3);
    merged.subscribe(
      v => {
        var value = JSON.parse(v).value;
        log(value);
        res += value
      },
      e => log("Error: " + e),
      () => log("Résultats : " + res)
    );

<button class="run"></button>

---

# PR - Flux à émissions multiples

    !js
    var service = Rx.Observable.create(observer => {
      var counter = 0;
      setInterval(() => {
        observer.onNext(counter++);
        if (counter === 3) observer.onCompleted(42);
      }, 1000);
      return;
    });

    var component = service.subscribe(
      function (x) {log('onNext: ' + x)},
      function (e) {log('onError: ' + e)},
      function () {log('onCompleted')}
    );

<button class="run"></button>

---

# PR - Principale bibliothèques
* [RxJS](https://github.com/Reactive-Extensions/RxJS) (implémentation Javascript de Rx, par **Microsoft**)
* [Bacon.js](https://github.com/baconjs/bacon.js) (librairie **plus intuitive**, mais un peu **moins complète**)

---

# Ressources

## Event loop

[MDN: Concurrency model and Event Loop](https://developer.mozilla.org/en-US/docs/Web/JavaScript/EventLoop)

## Asynchronous Programming

[You Don't Know JS: Async & Performance](https://github.com/getify/You-Dont-Know-JS/tree/master/async%20%26%20performance)

## Reactive Programming
* [The introduction to Reactive Programming you've been missing](https://gist.github.com/staltz/868e7e9bc2a7b8c1f754)
* [Observer Design Pattern](https://en.wikipedia.org/wiki/Observer_pattern)
* [RxVision](http://jaredforsyth.com/rxvision/examples/playground/)
* [RxMarbles](http://rxmarbles.com/)
