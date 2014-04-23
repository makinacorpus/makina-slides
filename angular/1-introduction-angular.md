# Introduction à AngularJS

--------------------------------------------------------------------------------

> HTML enhanced for web apps!

<cite> — angularjs.org</cite>

.fx: quoteslide

--------------------------------------------------------------------------------

# Qu'est-ce-que AngularJS ?

AngularJS est un framework JavaScript qui permet :

* d'étendre le language HTML (directives)
* de réaliser des Single.Page.App.
* d'embarquer plusieurs applications

## Historique

* Créé en 2009, basé sur le langage Javascript
* 1.0 sortie en juin 2012
* 1.2 sortie en novembre 2013 (version actuelle)
* Prochaine version: 2.0


--------------------------------------------------------------------------------

# Pourquoi utiliser AngularJS

* Ultra testé et donc testable
* Les directives (html étendu)
* Le modèle MVC
* Les données sont des objets natifs javascript


--------------------------------------------------------------------------------

# Pourquoi ne pas utiliser AngularJS

* IE < 8
* SEO
* Courbe d'apprentissage

![Courbe d'apprentissage](http://www.bennadel.com/resources/uploads/2013/feelings_about_angularjs_over_time.png)


--------------------------------------------------------------------------------

# Architecture

* template
* directive
* contrôleur
* scope
* expression
* service
* injection de dépendances

--------------------------------------------------------------------------------

# Template et directive

* Un template est fichier HTML parsé par AngularJS
* Une directive c'est l'extension d'HTML (ici ng-model)

![template & data binding](https://docs.angularjs.org/img/guide/concepts-databinding1.png)

--------------------------------------------------------------------------------

# Contrôleur

Il s'agit du contrôleur au sens MVC, lien entre les données / services et les vues. Il orchestre l'exécution de l'application.

![controller](https://docs.angularjs.org/img/guide/concepts-databinding2.png)


--------------------------------------------------------------------------------

# Scope

Le scope apporte la visibilité des modèles à une vue. C'est un objet JavaScript attaché à l'application, un contexte d'exécution. Voici quelques caractéristiques :

* $scope.$watch (observer les changements dans les modèles)
* $scope.$apply (propager les changements qui ont lieu en dehors d'AngularJS)
* hiérachique (hérite des propriétés des scopes parents)
* contexte d'exécution {{username}} -> $scope.username


--------------------------------------------------------------------------------

# Expression

Les expressions ressemblent à du code JavaScript et sont écrites avec des doubles accolades {{ expression }}.

Voici quelques expressions valides :

* 1+2
* a+b
* user.name
* items[index]



--------------------------------------------------------------------------------

# Service

Les services sont des objets JavaScript qui sont cablés ensembles via l'injection de dépendances. Ils sont :

* des singletons
* chargés uniquement si besoin (lazy load)
* utilisés pour organiser et partager du code dans l'application

Exemples de services natif à AngularJS :

* $http
* $document
* $log
* $location
* $q


--------------------------------------------------------------------------------

# Injection de dépendances (DI)


C'est un patron de conception sur la manière dont les composants récupèrent leurs dépendances.

AngularJS utilise une approche de résolution des dépendances à la création des componsants.

Ainsi ci-dessous nous apprenons à AngularJS à créer un service 'greet' dépendant d'un autre componsant '$window' :

    someModule.factory('greet', ['$window', function($window) {
      // ...
    }]);

--------------------------------------------------------------------------------

# Commencer un projet avec AngularJS

* https://github.com/angular/angular-seed


--------------------------------------------------------------------------------

# Le projet créé

    !console
    app/
    ├── css/                --> css files
    │   └── app.css         --> default stylesheet
    ├── img/                --> image files
    ├── index.html          --> app layout file
    ├── js/                 --> javascript files
    │   ├── app.js          --> application
    │   ├── controllers.js  --> application controllers
    │   ├── directives.js   --> application directives
    │   ├── filters.js      --> custom angular filters
    │   └── services.js     --> custom angular services
    └── partials/           --> angular view partials
        ├── partial1.html
        └── partial2.html


--------------------------------------------------------------------------------

# Démonstration : Application de création de carte

.fx: alternate

--------------------------------------------------------------------------------

# Où obtenir des informations ?

* [site officiel](http://www.angularjs.org) [EN]
* [ng-book](https://www.ng-book.com/) [EN]
* [protractor](https://github.com/angular/protractor) [EN]
* [built with angular](http://builtwith.angularjs.org/) [EN]
* [angular seed](https://github.com/angular/angular-seed) [EN]
* [angular ui](http://angular-ui.github.io) [EN]

--------------------------------------------------------------------------------

# Merci !

