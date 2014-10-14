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

# Karma

* Application NodeJS créer pour AngularJS.
* Tests unitaires.
* Detecte les modifications du code.
* Relance automatiquement les tests.
* Utilise les navigateurs pour faire tourner les tests. Karma peut :
    * Lancer automatiquement les navigateurs au démarrage.
    * Accepter les connexions de navigateurs distant (simplifie grandement les tests sur mobile, tablette, IE, ...).
* Plusieurs frameworks de tests disponible.

--------------------------------------------------------------------------------

# Karma - Installation, configuration et lancement

    !console
    npm install karma karma-chrome-launcher
    ./node_modules/.bin/karma init karma.conf.js
    ./node_modules/.bin/karma start

    sudo npm install -g karma-cli
    karma start

    # Ou avec angular-seed
    npm test

--------------------------------------------------------------------------------

# Jasmine

* Framework de test.
* "behavior-driven".
* Facile d'installation :

        !console
        npm install karma-jasmine

--------------------------------------------------------------------------------

# Jasmine - Suites

    !javascript
    describe('Unit test: TodoController', function(){
      // Specs go in here
    });


    describe('Unit test: TodoController', function(){
      describe('list', function(){
        // Specs go in here
      });
    });

--------------------------------------------------------------------------------

# Jasmine - Specs, Expectations

    !javascript
    describe('Unit test: TodoController', function(){
      it('should be true', function() {
        expect(true).toBe(true);
      });
    });

    describe('Unit test: TodoController', function(){
      var a;

      it('should be true', function() {
        a = true;

        expect(a).toBe(true);
      });
    });

https://github.com/pivotal/jasmine/wiki/Matchers

--------------------------------------------------------------------------------

# Jasmine - Setup, Teardown

    !javascript
    describe("A spec (with setup and tear-down)", function() {
      var foo;

      beforeEach(function() {
        foo = 0;
        foo += 1;
      });

      afterEach(function() {
        foo = 0;
      });

      it("is just a function, so it can contain any code", function() {
        expect(foo).toEqual(1);
      });

      it("can have more than one expectation", function() {
        expect(foo).toEqual(1);
        expect(true).toEqual(true);
      });
    });

--------------------------------------------------------------------------------

# Injection et mocks

Un mock permet de tester et de simuler le fonctionnement d'un composant métier.
Pensez à inclure ``angular-mocks.js`` dans la configuration de ``karma``.

    !javascript
    angular.module('myApp', [])
        .value('version', 'v1.0.1');

    describe('MyApp', function() {
      beforeEach(module('myApp'));

      it('should provide a version', inject(function(version) {
        expect(version).toEqual('v1.0.1');
      }));
    });

    describe('MyApp', function() {
      var version;

      beforeEach(module('myApp'));
      beforeEach(inject(function(_version_){
        version = _version_;
      }));

      it('should provide a version', inject(function(version) {
        expect(version).toEqual('v1.0.1');
      }));
    });

    describe('MyApp', function() {
      beforeEach(module(function($provide) {
        $provide.value('version', 'VERSION');
      }));

      it('should provide a version', inject(function(version) {
        expect(version).toEqual('VERSION');
      }));
    });

--------------------------------------------------------------------------------

# Tester les différents composants - Contrôleur

    !javascript
    describe('Unit test: controller', function(){
      var MyController, scope;

      beforeEach(module('myApp'));
      beforeEach(inject(function($controller, $rootScope){
        scope = $rootScope;
        MyController = $controller('MyController', {$scope: scope});
      }));
    });

--------------------------------------------------------------------------------

# Tester les différents composants - Service

    !javascript
    describe('Unit test: Service', function(){
      var service;

      beforeEach(module('myApp'));
      beforeEach(inject(function(_service_){
        service = _service_;
      });
    });

--------------------------------------------------------------------------------

# Tester les différents composants - Filtres

    !javascript
    describe('Unit test: Service', function(){
      var filter;

      beforeEach(module('myApp'));
      beforeEach(inject(function($filter){
        service = $filter;
      });
      it('should works', function(){
        expect(filter('number')(123, 2).toEqual('123.00'));
      });
    });

--------------------------------------------------------------------------------

# Tester les différents composants - Directives

    !javascript
    describe('Unit test: Service', function(){
      var element, scope;

      beforeEach(module('myApp'));
      beforeEach(inject(function($compile, $rootScope){
        scope = $rootScope;
        element = angular.element('<my-directive></my-directive>');
        $compile(element)(scope);
        scope.$apply();
      });
      it('should works', function(){
        scope.$apply(function(){
          scope.value = 'new value';
        });
        expect(element.html()).toContain('new value');
      });
    });

--------------------------------------------------------------------------------

# TP - Création d'une TODO-list

* Écrire une série de tests unitaires pour l'application ``todo``.

--------------------------------------------------------------------------------

# Tests End to End

--------------------------------------------------------------------------------

# Protractor

* Application NodeJS créer pour AngularJS.
* Tests fonctionnels.
* Basé sur WebDriverJS.
* Utilise les navigateurs pour faire tourner les tests.
* Plusieurs frameworks de tests disponible.

--------------------------------------------------------------------------------

# Protractor - Installation

    !console
    npm install protractor
    ./node_modules/.bin/webdriver-manager update

--------------------------------------------------------------------------------

# Protractor - Configuration

    !javascript
    exports.config = {
      specs: [
        '*.js'
      ],

      capabilities: {
        'browserName': 'chrome',
        // A partir de chrome 35
        'chromeOptions': {
              args: ['--test-type']
        },
      },

      baseUrl: 'http://localhost:8000/app/',

      framework: 'jasmine',
    };

--------------------------------------------------------------------------------

# Protractor - Lancement

    !console
    # Le serveur doit être lancé pour pouvoir lancer les tests fonctionnels
    ./node_modules/.bin/protractor protractor.conf.js

    # Ou avec angular-seed
    npm run-script protractor

--------------------------------------------------------------------------------

# Jasmine - End to End

    !javascript
    describe('angularjs homepage', function() {
      var firstNumber = element(by.model('first'));
      var secondNumber = element(by.model('second'));
      var goButton = element(by.id('gobutton'));
      var latestResult = element(by.binding('latest'));
      var history = element.all(by.repeater('result in memory'));

      function add(a, b) {
        firstNumber.sendKeys(a);
        secondNumber.sendKeys(b);
        goButton.click();
      }

      beforeEach(function() {
        browser.get('http://juliemr.github.io/protractor-demo/');
      });

      it('should have a history', function() {
        add(1, 2);
        add(3, 4);

        expect(history.count()).toEqual(2);

        add(5, 6);

        expect(history.count()).toEqual(3);
      });
    });

http://angular.github.io/protractor/#/locators


--------------------------------------------------------------------------------

# Simuler un serveur HTTP

Dans le cas des tests unitaires, il faut pouvoir simuler un serveur HTTP pour ne tester que la fonctionnalité recherchée et pas la connexion ou le serveur distant.

    !javascript
    describe('Unit Test: HTTP', function() {
      var $httpBackend, myService;

      beforeEach(inject(function(_$httpBackend_, _myService_){
        $httpBackend = _$httpBackend_;
        // Imaginons que myService est un service faisant des requêtes pour nous.
        myService = _myService_;
      }));

      afterEach(function(){
        // Il faut s'assurer qu'il ne reste pas de requêtes ou d'attentes à la fin de chaque test.
        $httpBackend.verifyNoOutstandingExpectation();
        $httpBackend.verifyNoOutstandingRequest();
      });

      it('should make a request', function(){
        $httpBackend.expect('GET', '/v1/api/current_user').respond(100, {userId: 123});
        myService.getCurrentUser();
        $httpBackend.flush();
      });
    });

https://code.angularjs.org/1.2.26/docs/api/ngMock/service/$httpBackend

--------------------------------------------------------------------------------

# TP - Création d'une TODO-list

* Écrire une série de tests fonctionnels pour l'application ``todo``.

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
* ``scope`` : Si ``true``, un nouveau scope sera créer pour la directive. Peut également être un objet décrivant les valeurs du scope.
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
          scope: {
            value: '=',
          }
        };
      });

Fichier HTML :

    !html
    <my-directive value="'foobar'"></my-directive>

Fichier my-directive.html :

    {{ value }}

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
    * Prendre en paramètre la tache et la methode d'affichage de la date.
* Remplacer le listing des taches et l'affichage d'une tache simple par cette directive.

--------------------------------------------------------------------------------

# Questions ?