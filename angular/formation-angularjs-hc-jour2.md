# AngularJS - Jour 2

--------------------------------------------------------------------------------

* Module et Injection de dépendance
    * Principe de l'injection de dépendance
    * Notion de module
    * Découper son application
* Services
    * Services disponibles
    * Services vs Factory
* Tests Unitaires
    * Karma et Jasmine
    * Injection et mocks
* Tests End to End
    * Protractor
    * Simuler un serveur HTTP
* Directive
    * Créer ses directives
    * Vers des composants réutilisables

--------------------------------------------------------------------------------

# Module et Injection de dépendance

--------------------------------------------------------------------------------

# Principe de l'injection de dépendance

Comment AngularJS sait-il quelles services doivent-être passés au contrôleur ?

    !javascript
    angular.module('todo', [])
      .controller('TodoController', function($scope, $routeParams) {
        $scope.id = $routeParams.id;
        $scope.todo = ...;
      });

Et en cas de minification ?

--------------------------------------------------------------------------------

# Injection explicite

    !javascript
    angular.module('todo', [])
      .controller('TodoController', ['$scope', '$routeParams', function($scope, $routeParams) {
        $scope.id = $routeParams.id;
        $scope.todo = ...;
      }]);

--------------------------------------------------------------------------------

# Notion de module

Un module :

* Permet de séparer le code du reste de l'application.
* Est la manière principal de définir une application AngularJS (grâce à ``ngApp``).

Une application :

* Peut contenir plusieurs modules.

--------------------------------------------------------------------------------

# Définir un module

    !javascript
    // Créer le module 'nom', le deuxième paramètre est la liste des dépendances du module.
    angular.module('nom', []);

    // Récupère le module.
    angular.module('nom');

--------------------------------------------------------------------------------

# Découper son application

``angular-seed`` est un bon modèle :

* Les fichiers de description (README, LICENSE, ...) et de configuration des outils du projet sont à la racine.
* L'applicaion en elle-même est contenue dans un dossier.
* Chaque partie logique de l'application est mis dans son propre module. Chaque module a son propre dossier.
    * Un module décrit ses propres contrôleurs, routes et templates.
    * Les directives et les filtres peuvent être mis dans des modules à part si ils sont réutilisable.

    !console
    README
    LICENSE
    bower.json
    package.json
    app/
    ├── app.js
    ├── css/
    │   └── app.css
    ├── img/
    ├── index.html
    └── todo/
        ├── partials/
        │   ├── todo_list.html
        │   └── todo_single.html
        ├── todo.js
        └── todo_test.js

--------------------------------------------------------------------------------

# TP - Création d'une TODO-list

* Re-cloner ``angular-seed``.
    * Regarder l'architecture du projet.
    * Regarder les fichier app.js, view1.js et view2.js.
    * Comprendre le découpage de l'application.
* Découper l'application de TODO-list pour reproduire la même architecture.

--------------------------------------------------------------------------------

# Services

--------------------------------------------------------------------------------

# Définition

Un service :

* Est un singleton.
* Permet de partager du code métier et/ou des objets entre contrôleurs.

        !javascript
        angular.module('todo', [])
          .controller('TodoController', ['$scope', '$routeParams', function($scope, $routeParams) {
            $scope.id = $routeParams.id;
            $scope.todo = ...;
          }]);

--------------------------------------------------------------------------------

# Services disponibles

Les services du core commencent par ``$``.

* ``$filter`` : Appliquer des filtres.
* ``$http`` : Faire des requêtes HTTP.
* ``$interpolate`` : Évaluer des expressions.
* ``$location`` : Récupérer ou agir sur l'URL.
* ``$q`` : Faire des promesses.
* ``$rootScope``
* ``$document``, ``$window``, ``$timeout``, ``$interval``
* ...

--------------------------------------------------------------------------------

# Services vs Factory

Ou comment créer un service.

## Factory

Une ``factory`` retourne le service demandé.

    angular.module('myApp', [])
      .factory('hello', function() {
        return {
          hello: function(name) {
            return "Hello " + name;
          },
        };
      });

## Service

``service`` peut être utilisé en tant que constructeur du service.

    angular.module('myApp', [])
      .service('hello', function() {
        this.hello: function(name) {
            return "Hello " + name;
          };
      });

--------------------------------------------------------------------------------

# Constant et Value

    angular.module('myApp', [])
      .constant('version', '0.1');

    angular.module('myApp', [])
      .value('version', '0.1');

``constant`` peut être utilisé dans un ``config``. ``value`` ne peut pas.

    angular.module('myApp', [])
      .constant('version', '0.1');
      .config(['version', function(version) {
        // Ok
      }])

    angular.module('myApp', [])
      .value('version', '0.1');
      .config(['version', function(version) {
        // Error
      }])

--------------------------------------------------------------------------------

# TP - Création d'une TODO-list

* Créer un service permettant de :
    * Stocker la TODO-list.
    * Récuperer la liste.
    * Manipuler la liste (ajouter/supprimer).
    * Récuperer une tache par son ``id``.

--------------------------------------------------------------------------------

# Tests Unitaires

--------------------------------------------------------------------------------
    * Karma et Jasmine

--------------------------------------------------------------------------------
    * Injection et mocks

--------------------------------------------------------------------------------

# Tests End to End

--------------------------------------------------------------------------------
    * Protractor

--------------------------------------------------------------------------------
    * Simuler un serveur HTTP

--------------------------------------------------------------------------------

# Directive

--------------------------------------------------------------------------------

# Définitions

Une directive permet d'étendre le language HTML. Les formes les plus courantes de directives sont les suivantes :

    !html
    <div my-directive></div>
    <my-directive></my-directive>

    <div my-directive="value"></div>

--------------------------------------------------------------------------------

# Créer ses directives

    !javascript
    angular.module('myApp', [])
      .directive('myDirective', function() {
        return {
          // Options
        };
      });

--------------------------------------------------------------------------------

# Options

* ``restrict`` : Indique de quelle manière une directive peut être utilisé. ``A`` pour attribut et ``E`` pour element.
* ``template``/``templateUrl`` : Template ou url vers le template à utiliser.
* ``replace`` : Si ``true``, le template remplace le block plutot que d'etre ajouté.
* ``scope`` : Si ``true``, un nouveau scope sera créer pour la directive.
* ``controller`` : Le contrôleur à utiliser pour gérer la directive.
* ...

--------------------------------------------------------------------------------

# Exemple

Fichier JS :

    !javascript
    angular.module('myApp', [])
      .directive('myDirective', function() {
        return {
          restrict: 'AE',
          template: '<a href="google.com">Google</a>',
          replace: true,
        };
      });

Fichier HTML :

    !html
    <div my-directive></div>

--------------------------------------------------------------------------------

# Exemple

Fichier JS :

    !javascript
    angular.module('myApp', [])
      .directive('myDirective', function() {
        return {
          restrict: 'E',
          templateUrl: 'partials/my-directive.html',
          replace: true,
          controller: ['$scope', '$element', '$attrs', function($scope, $element, $attrs) {
            $scope.value = $attrs.value;
          }],
        };
      });

Fichier HTML :

    !html
    <my-directive value="foobar"></my-directive>

Fichier my-directive.html :

    <div>{{ value }}</div>

--------------------------------------------------------------------------------

# Vers des composants réutilisables

Les directives permettent d'étendre le langage HTML.

Les filtres permettent de modifier la manière dont les données sont affichées.

Les services mettent à disposition du code métier.

Plus un composant est générique, plus il est réutilisable. Au contraire, un composant qui n'est utilisé qu'une fois n'a pas besoin d'être générique. Il faut trouver le juste milieu.

Voir le dossier ``components`` de ``angular-seed``.

--------------------------------------------------------------------------------

# TP - Création d'une TODO-list

* Créer une directive permettant l'affichage d'une tache. Elle doit :
    * Prendre en paramètre l'id de la tache et la methode d'affichage de la date.
* Remplacer le listing des taches et l'affichage d'une tache simple par cette directive.

--------------------------------------------------------------------------------

# Questions ?