# L'asynchrone en JavaScript

---

# σύγ

*syn* : ensemble

Exemples : synthèse, synopsis, synchrétisme

# χρονος

chronos : le temps

Exemples : chronologie, chronomètre

# A-syn-chrone

Qui ne se fait pas en même temps.

* une partie du code s'exécute *maintenant*
* une partie s'exécute plus tard

---

# Exemple : timer

    !js
    print("D'abord");

    setTimeout(function() {
        print("Finalement");
    }, 10);

    print("Ensuite");

---

# Exemple : requête HTTP

    !js
    var xhr = new XMLHttpRequest();
    xhr.responseType = "document";
    xhr.addEventListener("load", function() {
       var doc = this.responseXML;
       console.log(doc.querySelector("title").textContent);
    });
    xhr.open("GET", "/exemple.txt", true);
    xhr.send(null);

---

# Les événements

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

## Implémentations en C

- [libuv](http://nikhilm.github.io/uvbook/basics.html) (Node.js) : 
- [libevent](http://www.wangafu.net/~nickm/libevent-book/Ref3_eventloop.html) (Chromium) : 

---

# La boucle d'évéments : caractéristiques

- un seul fil d'exécution
- inspection non bloquantes des descripteurs de fichiers (select, epoll, kqueue, etc.)
- gestion des timers (notion de temps)
- gestion des événement utilisateurs
- fonctions exécutés de manière atomique

---

# Exemple : timer sans délai

    !js
    print("D'abord");

    setTimeout(function() {
        print("Finalement");
    }, 0);

    print("Ensuite");

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
