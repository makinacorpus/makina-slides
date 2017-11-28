# Introduction à AngularJS

--------------------------------------------------------------------------------

# Jean-Michel FRANCOIS

* twitter: @toutpt & @toutpt_fr
* github: toutpt
* email: jeanmichel.francois@makina-corpus.com

--------------------------------------------------------------------------------

# Makina Corpus

* Société de Services en Logiciels Libres, indépendante, créée en 2001
* 35 collaborateurs dans 4 agences (Paris, Nantes, Toulouse, Pau)
* SIG / Portails / Système et réseaux
* Valeurs : Logiciel libre, OpenData, agilité, développement durable

--------------------------------------------------------------------------------

> HTML enhanced for web apps!

<cite> — angularjs.org</cite>

.fx: quoteslide


--------------------------------------------------------------------------------

# Qu'est-ce-que AngularJS ?

AngularJS est un framework JavaScript qui permet :

* d'étendre le langage HTML (directives)
* de réaliser des Single.Page.App.
* d'embarquer plusieurs applications

## Historique

* Créé en 2009, basé sur le langage JavaScript
* 1.0 sortie en juin 2012
* 1.2 sortie en novembre 2013 (version actuelle)
* Prochaine version: 2.0


--------------------------------------------------------------------------------

# Pourquoi utiliser AngularJS

* Ultra testé et donc testable
* Les directives (html étendu)
* Le modèle MVC
* Les données sont des objets natifs JavaScript


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

# [Architecture] Template et directive

* Un template est fichier HTML parsé par AngularJS
* Une directive c'est l'extension d'HTML (ici ng-model)

![template & data binding](https://docs.angularjs.org/img/guide/concepts-databinding1.png)

--------------------------------------------------------------------------------

# [Architecture] Contrôleur

Il s'agit du contrôleur au sens MVC, lien entre les données / services et les vues. Il orchestre l'exécution de l'application.

![controller](https://docs.angularjs.org/img/guide/concepts-databinding2.png)


--------------------------------------------------------------------------------

# [Architecture] Scope

Le scope apporte la visibilité des modèles à une vue. C'est un objet JavaScript attaché à l'application, un contexte d'exécution. Voici quelques caractéristiques :

* $scope.$watch (observer les changements dans les modèles)
* $scope.$apply (propager les changements qui ont lieu en dehors d'AngularJS)
* hiérachique (hérite des propriétés des scopes parents)
* contexte d'exécution {{username}} -> $scope.username


--------------------------------------------------------------------------------

# [Architecture] Expression

Les expressions ressemblent à du code JavaScript et sont écrites avec des doubles accolades {{ expression }}.

Voici quelques expressions valides :

* 1+2
* a+b
* user.name
* items[index]



--------------------------------------------------------------------------------

# [Architecture] Service

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

# [Architecture] Injection de dépendances


C'est un patron de conception sur la manière dont les composants récupèrent leurs dépendances.

AngularJS utilise une approche de résolution des dépendances à la création des composants.

Ainsi ci-dessous nous apprenons à AngularJS à créer un service 'greet' dépendant d'un autre componsant '$window' :

    someModule.factory('greet', ['$window', function($window) {
      // ...
    }]);


--------------------------------------------------------------------------------

# Passer de jQuery à AngularJS

Ou comment ne plus utiliser jQuery

* Ne pas créer une page pour manipuler son DOM
* Ne pas augmenter jQuery avec AngularJS
* Les directives ne sont pas des modules jQuery
* Penser en terme d'architecture (service, contrôleur, ...)
* Les données doivent être chargées dans des objets JavaScript
* Eviter autant que possible d'inclure un plugin jQuery


--------------------------------------------------------------------------------

# Commencer un projet avec AngularJS

* Angular seed (projet minimal avec les tests)
* Angular Yeoman generator (générateur de projet JavaScript)


--------------------------------------------------------------------------------

# Un projet créé avec Angular seed

    !console
    app/
    ├── css/                --> CSS files
    │   └── app.css         --> default stylesheet
    ├── img/                --> image files
    ├── index.html          --> app layout file
    ├── js/                 --> JavaScript files
    │   ├── app.js          --> application
    │   ├── controllers.js  --> application controllers
    │   ├── directives.js   --> application directives
    │   ├── filters.js      --> custom AngularJS filters
    │   └── services.js     --> custom AngularJS services
    └── partials/           --> AngularJS view partials (template)
        ├── partial1.html
        └── partial2.html


Cette architecture est discutable, je préfère l'approche un fichier par objet métier (maps, messages, ...)

--------------------------------------------------------------------------------

# Déployer un projet AngularJS

AngularJS est un framework JavaScript, vous avez donc juste à servir les ressources statiques par un simple serveur HTTP (apache / nginx).

L'idéale est de passer par une phase de 'build' pour minifier les ressources.


--------------------------------------------------------------------------------

# Outils (officiels)

* AngularJS Batarang (extension chrome pour le débug)
* Protractor (aka testacular, tests fonctionnels multi navigateurs)
* Karma (tests JavaScript)

# Outils (Communautaires)

* AngularUI (ensembles de directives pour réaliser vos interfaces)
* angular-gettext (traduction)
* Restangular (intégration d'API REST)
* Gulp / Grunt (build / minification des resources)
* Bower (gestionnaire de packages)

--------------------------------------------------------------------------------

# Démonstration : Application de création de carte

.fx: alternate

https://github.com/makinacorpus/openmapeditor

--------------------------------------------------------------------------------

# Où obtenir des informations ?

* site officiel : http://www.angularjs.org [EN]
* ng-book : https://www.ng-book.com/ [EN]
* protractor : https://github.com/angular/protractor [EN]
* built with angular : http://builtwith.angularjs.org/ [EN]
* angular seed : https://github.com/angular/angular-seed [EN]
* angular ui : http://angular-ui.github.io [EN]

--------------------------------------------------------------------------------

# Merci !

