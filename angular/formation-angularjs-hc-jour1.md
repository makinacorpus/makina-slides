# AngularJS - Jour 1

--------------------------------------------------------------------------------

# Yann FOUILLAT

* twitter: @Gagaro42
* github: Gagaro
* email: yann.fouillat@makina-corpus.com

# Makina Corpus

* Société de Services en Logiciels Libres, indépendante, créée en 2001
* 35 collaborateurs dans 4 agences (Paris, Nantes, Toulouse, Pau)
* SIG / Portails / Système et réseaux
* Valeurs : Logiciel libre, OpenData, agilité, développement durable
* [www.makina-corpus.com](http://www.makina-corpus.com)
--------------------------------------------------------------------------------

# AngularJS

* Créé en 2009, basé sur le langage JavaScript
* 1.0 sortie en juin 2012
* 1.2 sortie en novembre 2013 (version actuelle)
* Prochaine version: 1.3

--------------------------------------------------------------------------------

* Les principes de base
    * Rappel JavaScript et jQuery
    * Les frameworks MV*
    * Le fonctionnement interne
* Les premiers pas
    * Intégrer la librairie
    * Data Binding
    * Templating
    * Commencer un projet avec AngularJS
* Contrôleur
    * Notion de scope
    * Propagation des événements
* Filtres
    * Les filtres disponibles
    * Créer ses propres filtres
* Routage
    * Configuration des routes
    * Gestion de l'historique
    * Traitement avant affichage

--------------------------------------------------------------------------------

# Les principes de base

--------------------------------------------------------------------------------

# Rappel JavaScript

## Objets JavaScript

    !javascript
    var obj = {'foo': 'bar'};
    obj.foo == obj['foo'];
    obj.foobar = 42;
    obj['foobar'] = 21;
    obj.method = function(){
        console.log('I am here!');
    };
    obj.method();

--------------------------------------------------------------------------------

# Rappel jQuery

Ou comment ne plus utiliser jQuery

* Ne pas créer une page pour manipuler son DOM
* Ne pas augmenter jQuery avec AngularJS
* Les directives ne sont pas des modules jQuery
* Penser en terme d'architecture (service, contrôleur, ...)
* Les données doivent être chargées dans des objets JavaScript
* Eviter autant que possible d'inclure un plugin jQuery

[Penser AngularJS depuis jQuery](http://stackoverflow.com/questions/14994391/how-do-i-think-in-angularjs-if-i-have-a-jquery-background)

--------------------------------------------------------------------------------

# Les frameworks MV*

![Modèle MVC](http://upload.wikimedia.org/wikipedia/commons/a/a0/MVC-Process.svg)

--------------------------------------------------------------------------------

# Le fonctionnement interne

AngularJS est un framework JavaScript qui permet :

* D'étendre le langage HTML (directives)
* De réaliser des Single.Page.App.
* D'embarquer plusieurs applications

--------------------------------------------------------------------------------

# Pourquoi utiliser AngularJS

* Ultra testé et donc testable
* Les directives (html étendu)
* Le modèle MVC
* Les données sont des objets natifs JavaScript

--------------------------------------------------------------------------------

# Pourquoi ne pas utiliser AngularJS

* IE < 9
* SEO
* Courbe d'apprentissage

![Courbe d'apprentissage](http://www.bennadel.com/resources/uploads/2013/feelings_about_angularjs_over_time.png)

--------------------------------------------------------------------------------

# Les premiers pas

--------------------------------------------------------------------------------

# Intégrer la librairie

    !javascript
    <script src="chemin/vers/angular.js"></script>

## ng-app

    !html
    <html ng-app="myApp">

--------------------------------------------------------------------------------
# Data Binding

* Lie les vues et les modèles
* Mise à jour automatiquement
  * Plus d'évenements à surveiller
  * Plus de manipulation du DOM manuel

![template & data binding](https://docs.angularjs.org/img/guide/concepts-databinding1.png)

--------------------------------------------------------------------------------
# Templating

Basé sur des fichiers ``partials``.

## Expression

* Ressemblent à du code JavaScript
* Sont écrites avec des doubles accolades {{ expression }}.

Voici quelques expressions valides :

    !html
    {{ 1 + 2 }}
    {{ a + b }}
    {{ user.name }}
    {{ items[index] }}

--------------------------------------------------------------------------------
# Templating

## Directives

* ngModel
* ngClass
* ngShow / ngHide
* ngRepeat
* ngClick
* ...

--------------------------------------------------------------------------------

# Commencer un projet avec AngularJS

* [angular-seed](https://github.com/angular/angular-seed) (projet minimal avec les tests)
* Angular Yeoman generator (générateur de projet JavaScript)

--------------------------------------------------------------------------------

# Déployer un projet AngularJS

* Resources statiques
    * Simple serveur HTTP
* Minifier les script pour la production

--------------------------------------------------------------------------------

# TP - Création d'une TODO-list

* Créer un nouveau projet AngularJS grâce à angular-seed.
    * Cloner le projet avec ``git``.
    * Installer les dépendances.
    * Lancer l'application.
    * Tester sur son navigateur en utilisant ``npm start`` !
* Modifier ``view1`` pour :
    * Afficher un template avec un ``input``.
    * Afficher un paragraphe affichant la valeur de cette ``input``.

--------------------------------------------------------------------------------

# Contrôleur

--------------------------------------------------------------------------------

# Définition

Un contrôleur :

* Est un contrôleur au sens MVC
* Fait le lien entre les données / services et les vues
* Orchestre l'exécution de l'application.
* Contient le ``scope`` de l'application.
* S'occupe d'une partie spécifique de l'application.

![controller](https://docs.angularjs.org/img/guide/concepts-databinding2.png)

--------------------------------------------------------------------------------

# Notion de scope

Un scope :

* Apporte la visibilité des modèles à une vue.
* Est un simple objet JavaScript.
* Est définis en tant que ``$scope`` sur chaque contrôleur.
* Ou en tant que ``$rootScope`` pour le scope de l'application.

Quelque caractéristiques :

* Contexte d'exécution {{username}} -> $scope.username
* Hiérachique (hérite des propriétés des scopes parents)
* ``$scope.$apply``/``$scope.$broadcast`` (propager les changements qui ont lieu en dehors d'AngularJS)

--------------------------------------------------------------------------------

# Création

Fichier JS :

    !javascript
    angular.module('myApp.view1', [])
      .controller('View1Controller', [function($scope) {
        $scope.name = 'Toto';
      }]);

Fichier HTML :

    !html
    <div ng-controller="View1Controller">
      {{ name }}
    </div>
--------------------------------------------------------------------------------

# Hiérarchie

Fichier JS :

    !javascript
    angular.module('myApp.view1', [])
      .controller('View1Controller', function($scope) {
        $scope.name = 'Toto';
        $scope.welcome = 'Bienvenue !';
      });
    angular.module('myApp.view2', [])
      .controller('View2Controller', function($scope) {
        $scope.name = 'Tutu';
      });

Fichier HTML :

    !html
    <div ng-controller="View1Controller">
      {{ welcome }} {{ name }}
      <div ng-controller="View2Controller">
        {{ welcome }} {{ name }}
      </div>
    </div>

--------------------------------------------------------------------------------

# Propagation des événements

## $scope.$on(name, listener)

Écoute pour un événement, listener est une fonction de la forme ``function(event, args)``.

## $scope.$broadcast(name, args)

Propage l'événement vers le bas. L'événement ne peut pas être arrêté.

## $scope.$emit(name, args)

Propage l'événement vers le haut. L'événement peut être arrêté.

--------------------------------------------------------------------------------

# Exemple

Fichier JS :

    !javascript
    angular.module('eventExample', [])
      .controller('EventController', ['$scope', function($scope) {
          $scope.count = 0;
        $scope.$on('MyEvent', function() {
              $scope.count++;
        });
      }]);

Fichier HTML :

    !html
    <div ng-controller="EventController">
      Root scope <tt>MyEvent</tt> count: {{count}}
      <ul>
        <li ng-repeat="i in [1]" ng-controller="EventController">
          <button ng-click="$emit('MyEvent')">$emit('MyEvent')</button>
          <button ng-click="$broadcast('MyEvent')">$broadcast('MyEvent')</button>
          <br>
          Middle scope <tt>MyEvent</tt> count: {{count}}
          <ul>
            <li ng-repeat="item in [1, 2]" ng-controller="EventController">
              Leaf scope <tt>MyEvent</tt> count: {{count}}
            </li>
          </ul>
        </li>
      </ul>
    </div>

--------------------------------------------------------------------------------

# TP - Création d'une TODO-list

* Supprimer les dossiers ``components``, ``view1`` et ``view2``.
    * Vider le ``body`` en ne laissant que les scripts ``angular.js`` et ``app.js``.
* Vider le fichier ``app.js`` et recréer un module ``todo`` avec un controlleur ``TodoController``.
    * Pensez à mettre ``ng-app`` égale à ``todo``.
* Ajouter une liste d'objet au scope du module ``todo`` de la forme donné (``id`` doit etre différent pour chaque objet).

        !javascript
        {'id' : 1, 'date': Date, 'title': 'Finir le TP', 'done': false}

* Afficher la liste de taches avec le titre et le statut de chaque tache (``done``).
* Permettre la validation de taches.
* Permettre l'ajout et la suppression de taches.

--------------------------------------------------------------------------------

# Filtres

--------------------------------------------------------------------------------

# Définition

Un filtre :

* Permet de formatter les données affichées.
* Est utilisé dans une expression à l'aide d'un ``|``.
* Peut prendre des options à l'aide de ``:``.
* Peut être chainé avec d'autre filtres.

--------------------------------------------------------------------------------

# Les filtres disponibles

* date
* lowercase / upercase / number
* limitTo / orderBy / filter
* json
* currency

        !html
        {{ [3, 2, 1, 4] | limitTo:2 }}
        {{ "Bonjour" | lowercase }}

--------------------------------------------------------------------------------

# Créer ses propres filtres

Fichier JS :

    !javascript
    angular.module('myApp.filters', [])
      .filter('capitalize', function(){
        return function(input) {
          if (input) {
            return input[0].toUpperCase() + input.slice(1);
          }
        }
      });


Fichier HTML :

    !html
    {{ 'Je SuiS un TeXte uN peU biZaRRe' | lowercase | capitalize }}

--------------------------------------------------------------------------------

# $filter

$filter est un service permettant d'utiliser les filtres en javascript :

    !javascript
    var upercase = $filter('upercase');
    var uper = upercase('Bonjour');  // uper === 'BONJOUR'

--------------------------------------------------------------------------------

# TP - Création d'une TODO-list

* Afficher le jour et le mois de la date de création de la tache.
* Trier les taches par ordre alphabétique.
* Créer une section de recherche permettant de :
    * Afficher les taches faites ou non.
    * Faire une recherche plein texte sur les taches.

--------------------------------------------------------------------------------

# Routage

--------------------------------------------------------------------------------

# Définition

Une route :

* Permet de définir une vue avec :
    * Son template (``partial``).
    * Son contrôleur.
* Peut contenir des paramètres.

--------------------------------------------------------------------------------

# Configuration des routes

    !javascript
    angular.module('myApp', ['ngRoute'])
      .config(['$routeProvider', function($routeProvider){
        $routeProvider
          .when('/', {
            templateUrl: 'partials/home.html',
          });
          .when('/todo/:id', {
            templateUrl: 'partials/todo.html',
            controller: 'TodoController',
          });
          .otherwise({redirectTo: '/'});
      }]);

--------------------------------------------------------------------------------

# $routeParams

    !javascript
    angular.module('todo', [])
      .controller('TodoController', function($scope, $routeParams) {
        $scope.id = $routeParams.id;
        $scope.todo = ...;
      });

--------------------------------------------------------------------------------

# Configuration des templates

* index.html :

        !html
        <html ng-app="myApp">
          <head>[...]</head>
          <body>
            [...]
            <div ng-view></div>
            [...]
          </body>
        </html>

* partials/home.html :

        !html
        <h1>Bienvenue !</h1>

* partials/todo.html :

        !html
        <h1>{{ todo.name }}</h1>

--------------------------------------------------------------------------------

# URLs

## Mode Hashbang

* De la forme ``/#!/todo/42``.
* Supporté par tout les navigateurs.
* Activé par défaut.

## Mode HTML5

* De la forme ``/todo/42``.
* Utilise le mode hashbang si le navigateur ne le supporte pas.
* Configuration du serveur nécessaire.

--------------------------------------------------------------------------------

# Activer le mode HTML5

    !javascript
    angular.module('myApp', ['ngRoute'])
      .config(['$locationProvider'], function($locationProvider) {
        $locationProvider.html5Mode(true);
      });

--------------------------------------------------------------------------------

# Gestion de l'historique

``$location`` permet de récuperer ou de changer l'url actuelle. Il utilise l'api d'historique d'HTML5 si activée et disponible.

* ``.path()``
* ``.search()``
* ``.hash()``
* ``.url()``

![$location](https://code.angularjs.org/1.2.26/docs/img/guide/hashbang_vs_regular_url.jpg)

--------------------------------------------------------------------------------

# Traitement avant affichage

Quatre événements sont propagés par le service ``$route``.

* ``$routeChangeStart`` : Avant la résolution de l'URL.
* ``$routeChangeSuccess`` : Après la résolution de l'URL.
* ``$routeChangeError`` : En cas d'erreur.
* ``$routeUpdate`` : Si ``reloadOnSearch`` est mis à ``false``, et si le contrôleur est le même.

--------------------------------------------------------------------------------

# TP - Création d'une TODO-list

* Inclure ``ngRoutes``.
* Créer une route pour la TODO-list.
* Créer une route permettant l'affichage d'une tache en détail avec :
    * Date à la seconde.
    * Titre.
    * Statut.

--------------------------------------------------------------------------------

# Questions ?

