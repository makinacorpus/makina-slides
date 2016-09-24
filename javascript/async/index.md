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
