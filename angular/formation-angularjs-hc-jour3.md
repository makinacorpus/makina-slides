# AngularJS - Jour 3

--------------------------------------------------------------------------------

# Echanger avec un serveur

--------------------------------------------------------------------------------

# Requête HTTP

* ``$http``
* Asynchrone.
* Les objets envoyés sont transformés en JSON.
* Le JSON reçu est transformé en objet.

--------------------------------------------------------------------------------

# Requête HTTP - ``$http``

    !javasript
    $http({method: 'GET', url: 'http://www.google.com/'})
      .success(function(data, status, headers, config) {
        // Success
      })
      .error(function(data, status, headers, config) {
        // Error
      });

* ``$http.get``
* ``$http.head``
* ``$http.post``
* ``$http.put``
* ``$http.delete``

        !javascript
        $http.get('http://www.google.com/');

        $http.post('/users', {
          data: {
            username: 'Toto',
            password: 's3cret',
          }
       });

https://code.angularjs.org/1.2.26/docs/api/ng/service/$http

--------------------------------------------------------------------------------

# Requête HTTP - Configuration d'``$http``

* ``params`` : Paramètres de la requête (``?key1=value1&key2=value2``).
* ``headers`` : En-têtes à ajouter à la requête.
* ``cache`` : Activer le cache.
* ``timeout`` : Changer le timeout de la requête.

--------------------------------------------------------------------------------

# Utiliser un backend REST

* GET : Récuperer une liste d'objets (``/users``) ou un objet en particulier (``/users/123``).
* POST : Créer un nouvel objet (``/users``).
* PUT : Modifier un objet existant (``/users/123``).
* DELETE : Supprimer un objet existant (``/users/123``).

http://www.restapitutorial.com/lessons/httpmethods.html

--------------------------------------------------------------------------------

# Utiliser un backend REST - ngResource

* Module à part : ``angular-resource``.
* ``$resource``

        !javascript
        var User = $resource('/users/:userid', {
          userId: '@id',
        });

        // GET /users
        User.get(function(users) {
          // Success
        }, function(err) {
          // Error
        });

        // GET /users/123
        User.get({
         id: '123',
        }, function(user) {}, function(err) {});

        // GET /users
        User.query(function(users) {
          var user = users[0];
        }, function(err) {});

--------------------------------------------------------------------------------

# Utiliser un backend REST - ngResource

    !javascript
    // POST /users/123
    User.save({}, {
      username: 'Toto',
      password: 's3cret',
    }, function(user) {}, function(err) {});

    // DELETE /users/123
    User.delete({
      id: '123'
    }, {}, function(resp) {}, function(err) {});

    User.remove({
      id: '123'
    }, {}, function(resp) {}, function(err) {});

    // Exactement la même chose qu'au dessus
    User.delete({}, {
      id: '123'
    }, function(resp) {}, function(err) {});

--------------------------------------------------------------------------------

# Utiliser un backend REST - ngResource

## ``$save`` / ``$delete`` / ``$remove``

    !javascript
    // POST /users/123
    User.get({id: '123}, function(user) {
      user.password = 'n0t s0 s3cret';
      user.$save;
    });

## Reference

    !javascript
    // Asynchrone, référence vide pour le moment.
    $scope.user = User.get({id: '123'});

    User.get({id: '123}, function(user) {
      $scope.user = user;
    });

--------------------------------------------------------------------------------

# WebSockets

* Permet à un client et un serveur d'échanger en temps réél.
* API toujours en cours de standardisation par le W3C.
* Disponible dans ``angular-websocket``.

    !javascript
    var ws = new WebSocket("ws://localhost:8000/socket/");

    ws.onopen = function(){
      // WebSocket ouverte
    };

    ws.onmessage = function(message) {
      // Nouveau message
    };

    ws.send('Message');

https://github.com/gdi2290/angular-websocket

--------------------------------------------------------------------------------

# API Promise

Une promesse permet de résoudre une valeur de manière asynchrone (ou non) d'une manière "synchrone".

## L'enfer des callback

    !javascript
    User.get(fromId, function(user){
      user.friends.find(toId, function(friend) {
        user.sendMessage(friend, message, function(){
          // Message envoyé
        }, function(err) {
         // Erreur lors de l'envoi du message
        });
      }, function(err) {
        // Impossible de trouver l'ami
      })
    }, function(err) {
      // Impossible de trouver l'utilisateur
    });

## Avec des promesses

    !javascript
    User.get(fromId)
      .then(function(user){
        return user.friends.find(toId);
      }, function(err) {
        // Impossible de trouver l'utilisateur
      })
      .then(function(friend) {
        return user.sendMessage(friend, message);
      }, function(err) {
        // Impossible de trouver l'ami
      }).then(function() {
        // Message envoyé
      }, function(err) {
        // Erreur lors de l'envoi du message
      });

* Les appels sont correctement enchainées.
* Les erreurs sont gérées au niveau de l'appel concerné ou remontées.
* ``$http``, ``$timeout``, ``$interval`` retourne des promesses !

--------------------------------------------------------------------------------

# API Promise - $q

# Créer une promesse

    !javascript
    var deferred = $q.defer();

    // Résoud la promesse
    deferred.resolve(value);

    // Rejette la promesse
    deferred.reject(reason);

    // Informe sur le status de la promesse
    deferred.notify(value);

* ``$q.all(promises)``
* ``$q.reject(reason)``
* ``$q.when(value)``

# Utiliser la promesse

* ``.then(successFn, errFn, notifyFn)``
* ``.catch(errFn)``

--------------------------------------------------------------------------------

# API Promise - Exemple : Création de promesse

    !javascript
    angular.module('myApp', [])
      .factory('UserService', ['$q', '$resource', function($q, $resource) {
        var User = $resource('/users/:userid', {
          userId: '@id',
        });

        return {
          getUsers: function() {
            var deferred = $q.defer();

            User.query(function(users) {
              deferred.resolve(users);
            }, function(err) {
              deferred.reject(err);
            });

            return deferred;
          },
        };
      }]);
      .controller('UserController', function($scope) {
        $scope.users = '';

        UserService.getUsers().then(function(users) {
          $scope.users = users;
        }, function(err) {
          // Erreur
        }, function(value){
          // Notification
        });
      });

--------------------------------------------------------------------------------

# API Promise - Exemple : $q.all() et chainage

    !javascript
    angular.module('myApp', [])
      .controller('ViewController', function($scope, $http, $q) {
        $scope.vocabularies = {};
        $scope.cities = {};

        $http.get('/vocabularies/cities').then(function(cities) {
          $scope.vocabularies.cities = cities;

          var promises = [];
          for (var i = 0; i < $scope.vocabularies.cities.length; i++) {
            city = $scope.vocabularies.cities[i];
            promises.push($http.get('/cities/'+ city.id));
          }
          return $q.all(promises);
        }).then(function(cities) {
          $scope.cities = values;
        });
      });
    });

--------------------------------------------------------------------------------

# API Promise - Exemple : gestion des erreurs

    !javascript
    angular.module('myApp', [])
      .controller('ViewController', function($scope, $http, $q) {
        $scope.vocabularies = {};
        $scope.cities = {};

        // Ira dans la fonction "Erreur 1" si il y a une erreur
        $http.get('/vocabularies/cities').then(function(cities) {
          $scope.vocabularies.cities = cities;

          // Ira dans la fonction "Erreur 1" si il y a une erreur
          $http.get('/cities/1').then(function(city) {
            // OK
          });

          // Ira dans la fonction "Erreur 2" si il y a une erreur
          $http.get('/cities/2').then(function(city) {
            // OK
          }, function(err) {
            // Erreur 2
          });

        }, function(err) {
          // Erreur 1
        });
      });
    });


--------------------------------------------------------------------------------

# TP - Lister les projets GitHub

* Créer un nouveau module sur l'application ``todo``.
* Ajouter une route pour ``/github``.
* Récuperer la liste des projets de l'organisation ``angular``.
    * https://api.github.com/orgs/angular/repos
    * Lister les projets
* Ajouter une route pour ``/github/:projet``.
    * Affiche le détail d'un projet (nom, description, lien vers la page GitHub).
    * Afficher également les "pull requests" (url, titre).
        * https://api.github.com/repos/angular/{projet}/pulls
    * Ajouter un lien vers la page détaillant le projet dans la liste de projets.

--------------------------------------------------------------------------------

# Outils

--------------------------------------------------------------------------------

# Installer les dépendances Node.js avec npm

``npm`` permet d'installer des paquets Node.js.
Un fichier ``package.json`` permet de décrire un projet et contient ses dépendances ainsi que les commandes permettant de le tester/lancer.

    !console
    npm init  # Créer un fichier package.json
    npm install  # Utilise package.json
    npm install bower  # Installe un paquet de manière locale
    npm install --save bower  # Installe un paquet et l'ajoute aux dépendances
    npm install --save-dev bower  # Installe un paquet et l'ajoute aux dépendances de développements
    npm install -g bower  # Installe un paquet de manière globale
    npm install bower==1.3.12  # Installe une version précise

https://www.npmjs.org/
https://www.npmjs.org/doc/cli/npm-install.html

--------------------------------------------------------------------------------

# Installer les dépendances web avec Bower

``Bower`` est une application Node.js permettant de gerer les dépendances web.
Un fichier ``bower.json`` contient les dépendances.

* Frameworks
* Bibliothèques
* ...

        !console
        bower init  # Créer un fichier bower.json
        bower install  # Installe les dépendances du projet
        bower install angular  # Installe un paquet
        bower install --save angular  # Installe un paquet et l'ajoute aux dépendances
        bower install --save-dev angular  # Installe un paquet et l'ajoute aux dépendances de développements
        bower install git://github.com/user/package.git
        bower install http://example.com/script.js

``angular-seed`` contient un fichier ``package.json`` et ``bower.json``.

http://bower.io/
http://bower.io/search/

--------------------------------------------------------------------------------

# Builder son projet avec Grunt

Grunt permet d'automatiser des taches. Il se base sur un système de plugins permettant une gestion souple des taches à effectuer.

* concat
* uglify
* watch

    !console
    npm install -g grunt-cli
    npm install --save-dev grunt grunt-contrib-concat grunt-contrib-uglify grunt-contrib-watch

Les taches sont enregistré dans un fichier ``Gruntfile.js``.

http://gruntjs.com/

--------------------------------------------------------------------------------

# Builder son projet avec Grunt - Gruntfile.js

    !javascript
    module.exports = function(grunt) {

      // Project configuration.
      grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        concat: {
          build: {
            src: ['app/**/*.js', 'app/bower_components/angular/angular.min.js'],
            dest: 'app/app.js',
          }
        },
        uglify: {
          build: {
            src: 'src/app.js',
            dest: 'build/app.min.js'
          }
        },
        watch: {
          build: {
            files: ['app/**/*.js'],
            tasks: ['default'],
          }
        }
      });

      // Load the plugin that provides the "uglify" task.
      grunt.loadNpmTasks('grunt-contrib-concat');
      grunt.loadNpmTasks('grunt-contrib-uglify');
      grunt.loadNpmTasks('grunt-contrib-watch');

      // Default task(s).
      grunt.registerTask('default', ['concat', 'uglify']);
    };

--------------------------------------------------------------------------------

# Builder son projet avec Grunt - Lancer les taches

    !console
    grunt  # Effectue la tache "default"
    grunt concat  # Effectue toute les taches du module "concat"
    grunt concat:build  # Effectue uniquement la tache "build" de "concat"
    grunt watch  # Surveille les changements

--------------------------------------------------------------------------------

# Builder son projet avec Gulp

``Gulp`` est également un automatiseur de tache et fonctionne également sur un systeme de plugins.

* Effectue les taches en parallèles.
* Syntaxe un peu plus logique.
* Sépare les taches véritablement plutot que de devoir les concentrer par modules.

Les taches sont enregistré dans un fichier ``gulpfile.js``.

http://gulpjs.com/

--------------------------------------------------------------------------------

# Builder son projet avec Gulp - Gulpfile.js

var gulp = require('gulp');

gulp.task('default', function() {
  TODO
});

--------------------------------------------------------------------------------

# Yeoman

TODO

--------------------------------------------------------------------------------

# TP - Créer un nouveau projet avec Yeoman et minifier les ressources

TODO

--------------------------------------------------------------------------------

* Debugger
    * Méthodes utiles
    * Batarang
* Modules indispensables
    * Internationalisation
    * Bootstrap
    * Router
* Aller plus loin
    * Dirty Checking
    * Astuces

--------------------------------------------------------------------------------

# Questions ?

--------------------------------------------------------------------------------

# Extras

* $cache
* jQlite / jQuery
* Form validation
* Jasmine Spy
* Animation
* ngMin
* Restangular