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

.fx: tighter

    !javascript
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

--------------------------------------------------------------------------------

# Requête HTTP - Configuration d'``$http``

* ``params`` : Paramètres de la requête (``?key1=value1&key2=value2``).
* ``headers`` : En-têtes à ajouter à la requête.
* ``cache`` : Activer le cache.
* ``timeout`` : Changer le timeout de la requête.

[``$http``](https://code.angularjs.org/1.2.26/docs/api/ng/service/$http)

--------------------------------------------------------------------------------

# Utiliser un backend REST

Les différentes [méthodes HTTP pour le REST](http://www.restapitutorial.com/lessons/httpmethods.html).

* ``GET`` : Récupérer une liste d'objets (``/users``) ou un objet en particulier (``/users/123``).
* ``POST`` : Créer un nouvel objet (``/users``).
* ``PUT`` : Modifier un objet existant (``/users/123``).
* ``DELETE`` : Supprimer un objet existant (``/users/123``).

--------------------------------------------------------------------------------

# Utiliser un backend REST - ngResource

* Module à ajouter : ``angular-resource``.
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

# Presenter Notes

``$resource`` est un service permettant de faciliter la gestion d'objets par requêtes REST.
``$resource`` est dans le module ngResource.

``.get()`` permet de récupérer un ou des objets. ``query()`` permet de récupérer une liste d'objet.

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

# Presenter Notes

``save(parametres, data)`` pour sauvegarder les données.

``delete`` alias de ``remove``

Les "paramètres" de ``delete`` peuvent être mis en tant que "data".

--------------------------------------------------------------------------------

# Utiliser un backend REST - ngResource

## ``$save`` / ``$delete`` / ``$remove``

    !javascript
    // POST /users/123
    User.get({id: '123'}, function(user) {
      user.password = 'n0t s0 s3cret';
      user.$save;
    });

## Référence

    !javascript
    // Asynchrone, référence vide pour le moment.
    $scope.user = User.get({id: '123'});

    User.get({id: '123}, function(user) {
      $scope.user = user;
    });

# Presenter Notes

``$save``, ``$delete`` et ``$remove`` feront les requêtes HTTP en fonction de l'objet.

L'appel est asynchrone est la valeur est vide tant que la requête n'est pas fini.

--------------------------------------------------------------------------------

# Utiliser un backend REST - Restangular

[Restangular](https://github.com/mgonto/restangular) est un service plus avancé pour la gestion des backend REST.

    !javascript
    // GET /users
    Restangular.all('users').getList().then(function(users){
      $scope.users = users;
    });

    // GET /users/123
    Restangular.one('users', 123).get().then(function(user){
      $scope.user = user;
    });

    // GET /users/123/friends
    Restangular.one('users', 123).all('friends').getList().then(function(friends){
      $scope.user = user;
    });

# Presenter Notes

Ajoute des dépendances (``Lodash``).
Utilise les promesses.

--------------------------------------------------------------------------------

# WebSockets

* Permet à un client et à un serveur d'échanger en temps réél.
* API toujours en cours de standardisation par le W3C.
* Disponible dans [``angular-websocket``](https://github.com/gdi2290/angular-websocket).

        !javascript
        var ws = new WebSocket("ws://localhost:8000/socket/");

        ws.onopen = function(){
          // WebSocket ouverte
        };

        ws.onmessage = function(message) {
          // Nouveau message
        };

        ws.send('Message');

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

# Presenter Notes

Imaginont un service User permettant de récuperer un utilisateur.

--------------------------------------------------------------------------------

# API Promise

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

# API Promise - $http

    !javascript
    $http.get('http://www.google.com/').then(function(data) {
      // data – {string|Object} – Le corps de la réponse transformé (JSON => Objet).
      // status – {number} – Code HTTP de la réponse.
      // headers – {function([headerName])} – Fonction permettant de récuperer les en-têtes.
      // config – {Object} – La configuration utilisé lors de la requête.
      // statusText – {string} – Le status HTTP en texte.

      var response = data.data;
    });

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

# Presenter Notes

``reject`` et ``when`` crééent des promesses à partir d'une valeurs.

--------------------------------------------------------------------------------

# API Promise - $q

# Utiliser la promesse

* ``.then(successFn, errFn, notifyFn)``
* ``.catch(errFn)``


# Presenter Notes

``then`` retourne une promesse. Les promesses peuvent donc être chainées.
``catch`` peut être utilisé à la place du parametre errFn.

--------------------------------------------------------------------------------

# API Promise - Exemple : Création de promesse

    !javascript
    angular.module('myApp', [])
      .factory('UserService', ['$q', '$resource', function($q, $resource) {
        var User = $resource('/users/:userid', {userId: '@id'});
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
        });
      });

# Presenter Notes

Dans cet exemple on va juste récuperer une liste d'utilisateur depuis un backend REST.

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

# Presenter Notes

Dans cet exemple on va récuperer une liste de ville depuis un vocabulaire
puis récupérer les informations de toutes les villes.

``$q.all()`` permet d'attendre que toutes les requêtes pour les villes aient été faites.

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

# Presenter Notes

L'erreur remonte jusqu'a la promesse qui pourra la gérer.

--------------------------------------------------------------------------------

# TP - Lister les projets GitHub - 10

.fx: tighter

* Créer un nouveau module sur l'application ``todo`` avec :
    * Une route pour ``/github``.
    * Un contrôleur.
    * Un template.
* Récuperer la liste des projets de l'organisation ``angular`` avec ``$http``.
    * ``https://api.github.com/orgs/angular/repos``
    * Lister les projets
* Ajouter une route pour ``/github/:project``.
    * Ajouter ``angular-resource`` au fichier ``bower.json``.
    * Ajouter ``angular-resource.js`` dans ``index.html``.
    * Affiche le détail d'un projet (nom, description, lien vers la page GitHub) (utiliser ``$resource``).
        * ``https://api.github.com/repos/angular/{projet}``
    * Afficher également les "pull requests" (url, titre)
        * ``https://api.github.com/repos/angular/{projet}/pulls``
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

[Paquets](https://www.npmjs.org/) - [``npm install``](https://www.npmjs.org/doc/cli/npm-install.html)

<img src="https://www.npmjs.org/static/img/npm.png" width="10%" height="10%" />

# Presenter Notes

Voir le fichier ``package.json`` d'``angular-seed``.

--------------------------------------------------------------------------------

# Installer les dépendances web avec Bower

``Bower`` est une application Node.js permettant de gerer les dépendances client.
Un fichier ``bower.json`` contient les dépendances. Un fichier ``.bowerrc`` permet la configuration.

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

[Paquets](http://bower.io/search/)

[<img src="http://bower.io/img/bower-logo.png" width="10%" height="10%" />](http://bower.io/)

# Presenter Notes

Voir le fichier ``bower.json`` et ``.bowerrc`` d'``angular-seed``.

--------------------------------------------------------------------------------

# Builder son projet avec Grunt

Grunt est une application Node.js permettant d'automatiser des taches.
Il se base sur un système de plugins permettant une gestion souple des taches à effectuer.

* concat
* uglify
* watch
* ...

        !console
        npm install -g grunt-cli
        npm install --save-dev grunt grunt-contrib-concat grunt-contrib-uglify grunt-contrib-watch

Les taches sont enregistré dans un fichier ``Gruntfile.js``.

[<img src="http://gruntjs.com/img/grunt-logo.png" width="10%" height="10%" />](http://gruntjs.com/)

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

      // [...]

# Presenter Notes

Définition des taches.

--------------------------------------------------------------------------------

# Builder son projet avec Grunt - Gruntfile.js

    !javascript
      // [...]

      // Load the plugins.
      grunt.loadNpmTasks('grunt-contrib-concat');
      grunt.loadNpmTasks('grunt-contrib-uglify');
      grunt.loadNpmTasks('grunt-contrib-watch');

      // Default task(s).
      grunt.registerTask('default', ['concat', 'uglify']);
    };

# Presenter Notes

Chargement des plugins + enregistrement des taches (dont la tache 'default').

--------------------------------------------------------------------------------

# Builder son projet avec Grunt - Lancer les taches

    !console
    grunt  # Effectue la tache "default"
    grunt concat  # Effectue toute les taches du plugin "concat"
    grunt concat:build  # Effectue uniquement la tache "build" de "concat"
    grunt watch  # Effectue la tache watch : surveille les changements

--------------------------------------------------------------------------------

# Builder son projet avec Gulp

``Gulp`` est également un automatiseur de tache et fonctionne également sur un système de plugins.

* Effectue les taches en parallèles.
* Syntaxe un peu plus logique.
* Sépare les taches véritablement plutot que de devoir les concentrer par plugin.

Les taches sont enregistré dans un fichier ``gulpfile.js``.

[![Gulp](https://raw2.github.com/gulpjs/artwork/master/gulp.png)](http://gulpjs.com/)

--------------------------------------------------------------------------------

# Builder son projet avec Gulp - Gulpfile.js

    !javascript
    var gulp = require('gulp');
    var concat = require('gulp-concat');
    var rename = require('gulp-rename');
    var uglify = require('gulp-uglify');

    gulp.task('js', function () {
      return gulp.src(['app/**/*.js',
                       'app/bower_components/angular/angular.min.js'])
        .pipe(concat('app/app.js'))
        .pipe(gulp.dest('./app/'))
        .pipe(uglify())
        .pipe(rename('app.min.js'))
        .pipe(gulp.dest('./app/'));
    });

    gulp.task('default', ['js']);

    gulp.task('watch', function () {
      gulp.watch(['./app/**/*.js'], ['js']);
    });

--------------------------------------------------------------------------------

# Yeoman

``Yeoman`` facilite la création d'un projet et des différents composants.

    !console
    npm install -g yeoman
    yo

[![Yeoman](http://yeoman.io/assets/img/yeoman-02.901d.png)](http://yeoman.io/)

--------------------------------------------------------------------------------

# Yeoman - Générateurs

* Permet de générer un projet avec un workflow particulier.
    * ``angular-generator``
        * Bower + Grunt + Angular
    * ``generator-gulp-angular``
        * Bower + Gulp + Angular
* Installer un générateur :

        !console
        yo
        > Install a generator
        # ou
        npm install -g angular-generator

[Liste de générateurs](http://yeoman.io/generators/)

--------------------------------------------------------------------------------

# Yeoman - Création du projet

    !console
    mkdir myapp
    cd myapp
    yo
    > Run the Angular generator
    # ou
    yo angular
    grunt serve
    grunt test

[Exemple angular.js](http://yeoman.io/codelab.html)

--------------------------------------------------------------------------------

# Yeoman - Création des composants

    !console
    yo --help
    yo angular:route myRoute
    yo angular:controller myController
    yo angular:directive myDirective
    yo angular:filter myFilter
    yo angular:view myView
    yo angular:service myService
    yo angular:factory myService
    yo angular:value myService
    yo angular:constant myService

--------------------------------------------------------------------------------

# Yeoman - Mise en production

    !console
    grunt build
    ls dist

--------------------------------------------------------------------------------

# TP - Création d'une TODO-list - 11

* Installer Font Awesome en utilisant Bower.
    * Ajouter le également au fichier ``bower.json`` (``--save``).
* L'inclure dans l'application.
* Ajouter quelques icones.
    * ``http://fortawesome.github.io/Font-Awesome/examples/``
* Automatiser la minification de tout les fichiers JavaScript en utilisant ``Grunt`` ou ``gulp``.
    * Ajouter une tache permettant de surveiller la modification des fichiers JavaScript pour minifier automatiquement.
    * N'oublier pas de modifier les fichiers JavaScript inclus dans votre ``index.html``. Il ne doit rester que le fichier minifié.
* (Notez qu'il est également possible d'automatiser la minification des fichiers CSS).

--------------------------------------------------------------------------------

# Debugger

--------------------------------------------------------------------------------

# Méthodes utiles - JavaScript

    !javascript
    console.log();
    console.table();
    debugger;

--------------------------------------------------------------------------------

# Méthodes utiles - AngularJS

## Récuperer l'élément angular

    !javascript
    var rootEle = document.querySelector("html");
    var ele = angular.element(rootEle);
    // Ou bien, avec l'inspecteur
    var ele = angular.element($0);

## L'utiliser

    !javascript
    ele.scope();
    ele.controller();
    ele.inheritedData();

--------------------------------------------------------------------------------

# Batarang

Extension Chrome permettant d'inspecter :

* Les modèles ($scope).
* Les performances.
* Les dépendances des services entre eux.

[Batarang](https://chrome.google.com/webstore/detail/angularjs-batarang/ighdmehidhipcmcojjgiloacoafjmpfk)

--------------------------------------------------------------------------------

# TP - Création d'une TODO-list - 12

* Ajouter des ``console.log()`` pour afficher les taches à leur création.
* Utiliser Batarang pour observer les différents scopes.

--------------------------------------------------------------------------------

# Modules indispensables

--------------------------------------------------------------------------------

# Internationalisation - angular-translate

Fichier JS :

    !javascript
    app = angular.module('myApp', ['pascalprecht.translate']);

    app.config(function($translateProvider){
      $translateProvider.translations('en', {
        WELCOME: 'Welcome',
      });
      $translateProvider.translations('fr', {
        WELCOME: 'Bienvenue',
      });
      $translateProvider.preferredLanguage('fr');
    });
    app.controller('TranslateController', function($translate, $scope){
      $scope.changeLanguage = function(lang) {
        $translate.uses(lang);
      };
    });

Fichier HTML :

    !html
    <h1>{{ 'WELCOME' | translate }}</h1>
    <div ng-controller="TranslateController">
      <button ng-click="changeLanguage('en')">English</button>
      <button ng-click="changeLanguage('fr')">Français</button>
    </div>

# Presenter Notes

Fournit un filtre ``translate``. Les traductions sont en JSON.
Peu pratique pour des applications complexes.

--------------------------------------------------------------------------------

# Internationalisation - angular-translate - Loaders

## angular-translate-loader-url

    !javascript
    app.config(function($translateProvider){
      $translateProvider.useUrlLoader('/locales/translations.json');
      $translateProvider.preferredLanguage('fr');
      // Fichier '/locales/tranlsations.json?lang=fr'
    });


## angular-translate-loader-static-files

    !javascript
    app.config(function($translateProvider){
      $translateProvider.useStaticFilesLoader({
        prefix: '/locales/',
        suffix: '.json',
      });
      $translateProvider.preferredLanguage('fr');
      // Fichier '/locales/fr.json'
    });

# Presenter Notes

Toujours peu pratique pour une personne non technique.

--------------------------------------------------------------------------------

# Internationalisation - angular-gettext

Fichier JS :

    !javascript
    app = angular.module('myApp', ['gettext']);

    app.config(function(gettextCatalog){
      gettextCatalog.setCurrentLanguage('fr');
      // Vérifier que toutes les traductions soit présentes.
      // Les éléments non traduits auront "[MISSING]:" de préfixés.
      gettextCatalog.debug = true;
    });

    app.controller('TranslateController', function($scope, gettextCatalog){
      $scope.changeLanguage = function(lang) {
        gettextCatalog.setCurrentLanguage(lang);
      };
    });

    app.controller('ExampleController', function($scope, gettextCatalog){
      $scope.persons = 2;
      $scope.name = "Foo";
    });

# Presenter Notes

Un fichier ``.js`` supplémentaire contenant les traduction est ajouté à l'application.
Nous verrons plus loin comment générer ce fichier JS.

--------------------------------------------------------------------------------

# Internationalisation - angular-gettext

Fichier HTML :

    !html
    <div ng-controller="ExampleController">
      <h1 translate>Welcome</h1>
      <input type="text" placeholder="{{ 'Username' | translate }}" />
      <div translate translate-n="personsCount"
           translate-plural="{{$count}} persons">One person</div>
      <div translate-comment="Hello message" translate>Hello {{ name }}</div>
    </div>

    <div ng-controller="TranslateController">
      <button ng-click="changeLanguage('en')">English</button>
      <button ng-click="changeLanguage('fr')">Français</button>
    </div>

# Presenter Notes

Filtre et directive disponible. Permet la traduction des pluriels.
Permet la traduction avec variables.

--------------------------------------------------------------------------------

# Internationalisation - angular-gettext - Le workflow

1. Extraction (``.pot``)
2. Mise à jour du fichier de langue (``.po``)
3. Compilation (``.js``)

# Presenter Notes

Extraction des textes à traduires.
Intégration de ces textes dans le fichier de traduction.
Traduction.
Compilation.

--------------------------------------------------------------------------------

# Internationalisation - angular-gettext - Extraction

## ``grunt-angular-gettext``

    !javascript
    nggettext_extract: {
      pot: {
        files: {
          'po/template.pot': ['src/views/*.html']
        }
      },
    },

## ``gulp-angular-gettext``

    !javascript
    gulp.task('pot', function () {
      return gulp.src(['src/views/*.html'])
        .pipe(gettext.extract('template.pot'))
        .pipe(gulp.dest('po'));
    });

--------------------------------------------------------------------------------

# Internationalisation - angular-gettext - Traduction

[``poedit``](http://poedit.net/) permet de modifier les fichiers ``.po``.

# Créer un fichier de traduction ``.po`` à partir du ``.pot``

![File/New Catalog from POT File...](https://angular-gettext.rocketeer.be/dev-guide/translate/new-catalog.png)
![](https://angular-gettext.rocketeer.be/dev-guide/translate/catalog-properties.png)

--------------------------------------------------------------------------------

# Internationalisation - angular-gettext - Traduction

# Mettre à jour un fichier de traduction ``.po`` à partir du ``.pot``

![Catalog/Update from POT File...](https://angular-gettext.rocketeer.be/dev-guide/translate/update.png)

# Traduire le fichier de traduction ``.po``

Puis sauvegarder.

--------------------------------------------------------------------------------

# Internationalisation - angular-gettext - Compilation

## ``grunt-angular-gettext``

    !javascript
    nggettext_compile: {
      all: {
        files: {
          'src/js/translations.js': ['po/*.po']
        }
      },
    },

## ``gulp-angular-gettext``

    !javascript
    gulp.task('po', function () {
      return gulp.src(['po/*.po'])
        .pipe(gettext.compile())
        .pipe(gulp.dest('src/js/'));
    });

# Presenter Notes

Pensez à inclure le fichier JS ainsi créer dans l'application.

--------------------------------------------------------------------------------

# TP - Création d'une ToDo List - 13

* Traduire l'application en utilisant ``angular-gettext``.

--------------------------------------------------------------------------------

# Bootstrap

[Bootstrap](http://getbootstrap.com/) sans jQuery et avec des directives.

## [angular-bootstrap](http://angular-ui.github.io/bootstrap/)

    !html
    <progressbar class="progress-striped" value="22" type="warning">22%</progressbar>
    <timepicker ng-model="mytime" ng-change="changed()" hour-step="hstep"
                minute-step="mstep" show-meridian="ismeridian"></timepicker>

## [angular-strap](http://mgcrea.github.io/angular-strap/)

    !html
    <input type="text" class="form-control" size="8" ng-model="time" name="time" bs-timepicker>


# Presenter Notes

Pas forcément les meme composant d'implémentés. Logique différente (directive element ou attribues).

--------------------------------------------------------------------------------

# Router - angular-ui-router

## index.html

    !html
    <body>
      <div ui-view></div>
      <a ui-sref="state1">State 1</a>
      <a ui-sref="state2">State 2</a>
    </body>

## partials/state1.html

    !html
    <h1>State 1</h1>
    <hr/>
    <a ui-sref="state1.list">Show List</a>
    <div ui-view></div>

## partials/state1.list.html

    !html
    <h3>List of State 1 Items</h3>
    <ul>
      <li ng-repeat="item in items">{{ item }}</li>
    </ul>

# Presenter Notes

Permet de faire des vues dans des vues ainsi que des vues multiples sur la même page.
Permet également de nommer ses vues.

--------------------------------------------------------------------------------

# Router - angular-ui-router

## partials/state2.html

    !html
    <h1>State 2</h1>
    <hr/>
    <a ui-sref="state2.list">Show List</a>
    <div ui-view></div>

## partials/state2.list.html

    !html
    <h3>List of State 2 Things</h3>
    <ul>
      <li ng-repeat="thing in things">{{ thing }}</li>
    </ul>

[ui-router](https://github.com/angular-ui/ui-router)

--------------------------------------------------------------------------------

# Router - angular-ui-router

    !javascript
    myApp.config(function($stateProvider, $urlRouterProvider) {
      $urlRouterProvider.otherwise("/state1");
      $stateProvider
        .state('state1', {
          url: "/state1",
          templateUrl: "partials/state1.html"
        })
        .state('state1.list', {
          url: "/list",
          templateUrl: "partials/state1.list.html",
          controller: function($scope) {
            $scope.items = ["A", "List", "Of", "Items"];
          }
        })
        .state('state2', {
          url: "/state2",
          templateUrl: "partials/state2.html"
        })
        .state('state2.list', {
          url: "/list",
          templateUrl: "partials/state2.list.html",
          controller: function($scope) {
            $scope.things = ["A", "Set", "Of", "Things"];
          }
      });
    });

--------------------------------------------------------------------------------

# Router - angular-ui-router - Vues multiples

## Fichier HTML :

    !html
    <body>
      <div ui-view="viewA"></div>
      <div ui-view="viewB"></div>
      <a ui-sref="route1">Route 1</a>
      <a ui-sref="route2">Route 2</a>
    </body>

--------------------------------------------------------------------------------

# Router - angular-ui-router - Vues multiples

## Fichier JS :

    !javascript
    myApp.config(function($stateProvider) {
      $stateProvider
        .state('index', {
          url: "",
          views: {
            "viewA": { template: "index.viewA" },
            "viewB": { template: "index.viewB" }
          }
        })
        .state('route1', {
          url: "/route1",
          views: {
            "viewA": { template: "route1.viewA" },
            "viewB": { template: "route1.viewB" }
          }
        })
        .state('route2', {
          url: "/route2",
          views: {
            "viewA": { template: "route2.viewA" },
            "viewB": { template: "route2.viewB" }
          }
      });
    });

--------------------------------------------------------------------------------

# TP - Création d'une ToDo List - 14

* Modifier l'application TODO pour avoir les deux vues sur la meme page.

--------------------------------------------------------------------------------

# Aller plus loin

--------------------------------------------------------------------------------

# Dirty Checking

Surveille les modifications de variables et les propages dans l'application.

* La boucle "$digest"
    * $watch
    * $evalAsync

--------------------------------------------------------------------------------

# Dirty Checking

# $watch

En HTML :

    !html
    <input ng-model="name" type="text" />

Ou en JS :

    !javascript
    $scope.name = 'Toto';
    var unregister = $scope.$watch('name', function(newVal, oldVal){
      console.log('name changed : '+ oldVal +' => '+ newVal);
    });
    // Remove the $watch
    unregister();

# $evalAsync

Execute une fonction plus tard.

    !javascript
    $scope.$evalAsync(function(){
      console.log('evalAsync');
    });


--------------------------------------------------------------------------------

# Astuces

## angular.foreach

    !javascript
    angular.forEach([1, 2, 3, 4], function(value){
      console.log(value);
    });
    angular.forEach({firstname: 'Foo', lastname: 'Bar'}, function(value, key){
      console.log(key +' = '+ value);
    });

## angular.fromJson / angular.toJson

    !javascript
    var json = angular.toJson({firstname: 'Foo', lastname: 'Bar'});
    var obj = angular.fromJson("{firstname: 'Foo', lastname: 'Bar'}");

--------------------------------------------------------------------------------

# Astuces

.fx: tighter

## angular.is*

* Array
* Date
* Defined
* Element
* Function
* Number
* Object
* String
* Undefined

        !javascript
        if (angular.isArray([1, 2, 3])) {
          console.log('OK !');
        }

--------------------------------------------------------------------------------

# Astuces

## angular.copy

    !javascript
    var obj = {firstname: 'Foo', lastname: 'Bar'};
    var newObj = angular.copy(obj);
    newObj.name = "Toto";
    obj.name == "Foo"; // OK

## Désactiver les infos de débug

Infos nécessaire pour ``Protractor`` ou ``Batarang``. À n'utiliser qu'en production.

    !javascript
    app.config(['$compileProvider', function ($compileProvider) {
      $compileProvider.debugInfoEnabled(false);
    }]);

    // Réactiver avec :
    angular.reloadWithDebugInfo();

--------------------------------------------------------------------------------

# Questions ?

--------------------------------------------------------------------------------

# Extras

* $cache
* jQlite / jQuery
* [Form validation](http://www.yearofmoo.com/2014/09/taming-forms-in-angularjs-1-3.html)
* ng-annotate
* [One-way binding](http://blog.thoughtram.io/angularjs/2014/10/14/exploring-angular-1.3-one-time-bindings.html)

# Presenter Notes

One-way binding : {{ ::expression }}
