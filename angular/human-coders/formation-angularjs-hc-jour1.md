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

* Créé en 2009, basé sur le langage JavaScript.
* 1.0 sortie en juin 2012.
* 1.2 sortie en novembre 2013 (version actuelle).
* 1.3 sortie en octobre 2014 (non-stable).
* 2.0 en cours de développement.

# Presenter Notes

AngularJS 2.0 utilisera pleinement ECMAScript6, qui est la prochaine standardisation du JavaScript
(et utilisera un compilateur EM6 => EM5 pour la compatibilité).

--------------------------------------------------------------------------------

.fx: tighter

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

Ou comment ne plus utiliser jQuery.

* Ne pas créer une page pour manipuler son DOM.
* Ne pas augmenter jQuery avec AngularJS.
* Les directives ne sont pas des modules jQuery.
* Penser en terme d'architecture (service, contrôleur, ...).
* Les données doivent être chargées dans des objets JavaScript.
* Eviter autant que possible d'inclure un plugin jQuery.

[Penser AngularJS depuis jQuery](http://stackoverflow.com/questions/14994391/how-do-i-think-in-angularjs-if-i-have-a-jquery-background).

--------------------------------------------------------------------------------

# Les frameworks MV*

.fx: white-background-image

![Modèle MVC](http://upload.wikimedia.org/wikipedia/commons/a/a0/MVC-Process.svg)

# Presenter Notes

Ce paradigme regroupe les fonctions nécessaires en trois catégories :

* un modèle (modèle de données),
* une vue (présentation, interface utilisateur)
* un contrôleur (logique de contrôle, gestion des événements, synchronisation)

--------------------------------------------------------------------------------

# Le fonctionnement interne

AngularJS est un framework JavaScript qui permet :

* D'étendre le langage HTML (directives).
* De réaliser des applications web monopage ("single-page application").
* D'embarquer plusieurs applications.
* De mettre à jour les valeurs automatiquement dans l'ensemble de l'application ("dirty checking").

--------------------------------------------------------------------------------

# Pourquoi utiliser AngularJS

* Ultra testé et donc testable.
* Le modèle MVC.
* Les données sont des objets natifs JavaScript.
* Les différents composants ; directives, filtres, contrôleurs, services, ...

--------------------------------------------------------------------------------

# Pourquoi ne pas utiliser AngularJS

.fx: tighter

* IE < 8
* SEO
* Courbe d'apprentissage

![Courbe d'apprentissage](http://www.bennadel.com/resources/uploads/2013/feelings_about_angularjs_over_time.png)

# Presenter Notes

La courbe d'apprentissage est en grande partie du au fait qu'AngularJS est un ensemble de composants et
qu'il est impossible de tous les apprendre en meme temps. On se demandera souvent "pourquoi je dois faire comme ca"
pour utiliser un certain composant avant d'avoir compris son fonctionnement.

--------------------------------------------------------------------------------

# Les premiers pas

--------------------------------------------------------------------------------

# Intégrer la bibliothèque

## Le JavaScript

    !javascript
    <script src="chemin/vers/angular.js"></script>

## ``ng-app``

    !html
    <html ng-app="myApp">

# Presenter Notes

Le JavaScript sera plutot mis à la fin du <body> afin de s'assurer que
l'application s'affiche bien avant que les scripts soit télécharger.

Le nom de l'application ("myApp") sera définis plus tards dans ce que l'on appelle un "module".
ng-app n'est pas obligatoirement sur la balise html, mais là où l'application se trouve
(d'où le fait de pouvoir faire plusieurs applications sur une seul page).

--------------------------------------------------------------------------------

# Data Binding

* Lie les vues et les modèles.
* Mise à jour automatiquement.
    * Plus d'évenements à surveiller.
    * Plus de manipulation du DOM manuel.

![template & data binding](https://docs.angularjs.org/img/guide/concepts-databinding1.png)

# Presenter Notes

Mise à jour automatiquement gràce au "dirty checking".
Le "Scope" contient les modèles.
``ng-model`` permet de lier un champs de formulaire à une valeur du modèle.
{{ qty * cost }} est une expression permettant l'affichage de valeur, également mis à jour automatiquement.

[jsfiddle](http://jsfiddle.net/LLx2f7k8/2/)

--------------------------------------------------------------------------------
# Templating

Basé sur des fichiers ``partials`` (HTML).

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

        !javascript
        <input ng-model="cost" />

[Liste des directives](https://docs.angularjs.org/api/ng/directive).

# Presenter Notes

Permet de modifier le DOM. Définis une nouvelle balise ou un nouvel attribut HTML.
Les directives s'écrivent en camelCase mais s'utilisent en lower-case.

--------------------------------------------------------------------------------

# Commencer un projet avec AngularJS

* [angular-seed](https://github.com/angular/angular-seed)
* Yeoman

# Presenter Notes

* angular-seed : Projet minimaliste avec des tests.
* Yeoman : Générateur de projets.

--------------------------------------------------------------------------------

# Déployer un projet AngularJS

* Resources statiques.
    * Simple serveur HTTP.
* Minifier les script pour la production.

# Presenter Notes

Apache, nginx, ...
Grunt, gulp.

--------------------------------------------------------------------------------

# TP - Création d'une ToDo List - 1

* Créer un nouveau projet AngularJS grâce à angular-seed.
    * Cloner le projet avec ``git``.
    * Installer les dépendances (``npm install``).
    * Lancer l'application (``npm start``).
    * Tester l'application (``http://localhost:8000/app/``).
* Modifier ``view1`` (``app/view1/view1.html``) pour :
    * Afficher un ``input``.
    * Afficher un paragraphe affichant la valeur de cette ``input``.

.notes: Lier l'input à une valeur en utilisant ``ng-model``.

# Presenter Notes

Expliquer les dossier ``node_modules`` et ``bower_components``.

--------------------------------------------------------------------------------

# Contrôleur

--------------------------------------------------------------------------------

# Définition

Un contrôleur :

.fx: tighter

* Est un contrôleur au sens MVC.
* Fait le lien entre les données / services et les vues.
* Orchestre l'exécution de l'application.
* Contient le ``scope`` de l'application.
* S'occupe d'une partie spécifique de l'application.

![controller](https://docs.angularjs.org/img/guide/concepts-databinding2.png)

# Presenter Notes

Un service permet de réutiliser du code métier.
Le scope est vu à la prochaine slide.

S'occupe d'une partie de l'application, il y aura donc plusieurs controleur.
Un controleur peut etre inclus dans un autre pour s'occuper d'une sous-partie spécifique.

[jsfiddle](http://jsfiddle.net/k8nz4tkf/1/)

--------------------------------------------------------------------------------

# Notion de scope

Un scope :

* Apporte la visibilité des modèles à une vue.
* Est un simple objet JavaScript.
* Est définis en tant que ``$scope`` sur chaque contrôleur.
* Ou en tant que ``$rootScope`` pour le scope de l'application.

Quelque caractéristiques :

* Contexte d'exécution ``{{ username }}`` -> ``$scope.username``.
* Hiérachique (hérite des propriétés des scopes parents).
* ``$scope.$apply`` / ``$scope.$broadcast`` (propager les changements qui ont lieu en dehors d'AngularJS).

--------------------------------------------------------------------------------

# Création

Fichier JS :

    !javascript
    angular.module('myApp.view1', [])
      .controller('View1Controller', function($scope) {
        $scope.name = 'Toto';
      });

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

# Presenter Notes

[Plunker](http://plnkr.co/edit/WLUDuoKUOf6RQMHkfFzR?p=preview)

--------------------------------------------------------------------------------

# TP - Création d'une ToDo List - 2

.fx: tighter

* Supprimer les dossiers ``components``, ``view1`` et ``view2`` dans ``app``.
    * Vider le ``body`` en ne laissant que les scripts ``angular.js`` et ``app.js``.
* Vider le fichier ``app.js`` et recréer un module ``todo`` avec un controlleur ``TodoController``.
    * Pensez à mettre ``ng-app`` égale à ``todo``.
* Ajouter une liste d'objet au scope du module ``todo`` de la forme donné (``id`` doit etre différent pour chaque objet).

        !javascript
        {'id' : 1, 'date': Date, 'title': 'Finir le TP', 'done': false}

* Afficher la liste de taches avec le titre et le statut de chaque tache (``done``).
* Permettre la validation de taches.
* Permettre l'ajout et la suppression de taches.

.notes: Utiliser ``ng-repeat`` pour lister les taches. Utiliser un bouton avec ``ng-click`` pour les actions.

# Presenter Notes

[Trouver des caractères Unicode](http://shapecatcher.com/)

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

[Documentation](https://docs.angularjs.org/api/ng/filter).

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

# Presenter Notes

[jsfiddle](http://jsfiddle.net/9zyajwg5/1/)

--------------------------------------------------------------------------------

# $filter

$filter est un service permettant d'utiliser les filtres en javascript :

    !javascript
    var upercase = $filter('upercase');
    var uper = upercase('Bonjour');  // uper === 'BONJOUR'

--------------------------------------------------------------------------------

# TP - Création d'une ToDo List - 3

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

# TP - Création d'une ToDo List

* Inclure ``ngRoutes``.
* Créer une route pour la ToDo List.
* Créer une route permettant l'affichage d'une tache en détail avec :
    * Date à la seconde.
    * Titre.
    * Statut.

--------------------------------------------------------------------------------

# Questions ?
