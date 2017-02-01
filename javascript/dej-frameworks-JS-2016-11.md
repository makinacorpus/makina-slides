# Quel framework JS pour 2017 ?

.fx: extra-large

--------------------------------------------------------------------------------

# Le développement front-end

.fx: extra-large

# Presenter Notes

Donner une définition

- existe depuis longtemps, mais est devenu une discipline spécifique récemment
- dispose maintenant d'un tooling, de concepts, de frameworks, etc.

--------------------------------------------------------------------------------

# Qu'est-ce qu'un framework ?

.fx: extra-large

# Presenter Notes

Un ensemble de composants (au sens large) qui permet de construire rapidement et proprement des applications spécifiques.

Un framework peut être plus ou moins riche, et plus ou moins structurant.

--------------------------------------------------------------------------------

# Travailler sans framework ?

.fx: extra-large

# Presenter Notes

C'est possible. Mais c'est aussi idiot (ou pertinent, selon le point de vue) que de travailler sans framework côté backend.

On entend souvent "Moi, avec jQuery je m'en sors très bien et c'est quand même plus simple que tous ces trucs" => expliquer que c'est vrai, que ça reste valide, mais qu'à partir du moment où on part sur le frontend, c'est tout ou rien.

--------------------------------------------------------------------------------

# Écrire son propre framework ?

.fx: extra-large

# Presenter Notes

C'est possible aussi mais c'est comme choisir un framework peu connu.
C'est risqué.
Choisir un framework main stream est un gage de sécurité.

--------------------------------------------------------------------------------

# Les grands frameworks

.fx: extra-large

--------------------------------------------------------------------------------

# L' ère MVC

.fx: extra-large

--------------------------------------------------------------------------------

# AngularJS

- créé en 2009 par Google,
- très populaire,
- (va devenir) obsolète,
- 1 framework mobile.

.fx: extra-large

# Presenter Notes

- mobile = Ionic

--------------------------------------------------------------------------------

# AngularJS - Principes

- forte structuration (controllers, services, directives),
- 2-way data binding,
- injection de dépendances.

.fx: extra-large

# Presenter Notes

--------------------------------------------------------------------------------

# AngularJS - Avantages

- très large base de connaissances et de ressources,
- fortement structurant,
- solution tout-en-un,
- facile d'accès pour un développeur MVC backend.

.fx: extra-large

# Presenter Notes

--------------------------------------------------------------------------------

# AngularJS - Inconvénients

- de petites erreurs peuvent entrainer des problèmes de performances,
- se prête mal à l'intégration avec des composants exogènes,
- très verbeux.

.fx: extra-large

# Presenter Notes

--------------------------------------------------------------------------------

# Ember.js

- créé en 2007,
- plutôt lié à Ruby on Rails,
- vieillissant mais toujours vivant.

.fx: extra-large

# Presenter Notes

--------------------------------------------------------------------------------

# Ember.js - Principes

- un CLI puissant,
- un store central pour les données,
- templating Handlebars.

.fx: extra-large

# Presenter Notes

--------------------------------------------------------------------------------

# Ember.js - Avantages

- forte productivité,
- bonnes performances.

.fx: extra-large

# Presenter Notes

--------------------------------------------------------------------------------

# Ember.js - Inconvénients

- old school (jQuery),
- difficile à customiser,
- pas de logique composant.

.fx: extra-large

# Presenter Notes

--------------------------------------------------------------------------------

# Backbone.js

- volonté de simplicité,
- plus grande modularité.

.fx: extra-large

# Presenter Notes

--------------------------------------------------------------------------------

# Backbone.js - Principes

- basé sur Underscore.js,
- collections et évènements.

.fx: extra-large

# Presenter Notes

--------------------------------------------------------------------------------

# Backbone.js - Avantages

- pas de "magie",
- permet des utilisations partielles,
- s'intègre bien avec d'autres outils.

.fx: extra-large

# Presenter Notes

--------------------------------------------------------------------------------

# Backbone.js - Inconvénients

- beaucoup de cablage manuel.

.fx: extra-large

# Presenter Notes

--------------------------------------------------------------------------------

# L' ère Composants

--------------------------------------------------------------------------------

# React

- créé en 2011 par Facebook,
- très populaire,
- utilisé par de nombreux acteurs, dont Netflix et Airbnb,
- 1 framework mobile.

.fx: extra-large

# Presenter Notes

- créé par Jordan Walke, ingénieur logiciel chez Facebook
- utilisé dans Facebook newsfeed en 2011 et sur Instagram en 2012
- libéré à la JSConf US en 2013
- 6ème projet le plus étoilé sur GitHub (dépasse AngularJS)
- mobile = React native

--------------------------------------------------------------------------------

# React - Principes

- librairie s'occupant du View layer exclusivement,
- Virtual DOM,
- one-way data flow,
- isomorphism.

.fx: extra-large

# Presenter Notes

- one-way data flow en opposition au 2-way binding d'AngularJS.
- isomorphism = server-side rendering

--------------------------------------------------------------------------------

# React - Avantages

- très large base de connaissances et de ressources,
- écosystème très développé,
- communauté énorme,
- moteur dans l'évolution du développement front-end.

.fx: extra-large

# Presenter Notes

--------------------------------------------------------------------------------

# React - Inconvénients

- faiblement structurant,
- nécessite de l'optimisation manuelle.

.fx: extra-large

# Presenter Notes

- optimisation manuelle: shouldComponentUpdate par exemple

--------------------------------------------------------------------------------

# Angular 2

- sorti en 2016 par Google,
- refonte complète,
- système de version type semver,
- 2 frameworks mobiles.

.fx: extra-large

# Presenter Notes

- frameworks mobiles = Nativescript / Ionic 2.

--------------------------------------------------------------------------------

# Angular 2 - Principes

- TypeScript,
- approche par module et composant,
- Universal.

.fx: extra-large

# Presenter Notes

- universal = server-side rendering

--------------------------------------------------------------------------------

# Angular 2 - Avantages

- forte structuration,
- injection de dépendances plus simple,
- framework à très large couverture.
- un CLI façon Ember.js,

.fx: extra-large

# Presenter Notes

--------------------------------------------------------------------------------

# Angular 2 - Inconvénients

- peu adapté à des petites applications,
- moins facile à prendre en main pour un développeur front.

.fx: extra-large

# Presenter Notes

- moins facile à prendre en main par rapport à React ou Vue.

--------------------------------------------------------------------------------

# Vue.js

- créé en 2013,
- popularité en forte croissance,
- la voie du milieu par rapport à Angular et React,
- soutenu par de grosses entreprises.

.fx: extra-large

# Presenter Notes

- créé par Evan You, ancien employé Google et Meteor
- libération du code en 2014, v1 en 2015, v2 en 2016
- 1er framework dans les tendances JavaScript,
- http://bestof.js.org/tags/framework/trending/last-3-months
- utilisé par GitLab pour son front.


--------------------------------------------------------------------------------

# Vue.js - Principes

- librairie ne s'occupant que du View Layer
- Virtual DOM,
- one-way data flow,
- Framework Progressif,
- Server-side rendering.

.fx: extra-large

# Presenter Notes

- principe du framework progressif lié à l'image

--------------------------------------------------------------------------------

# Vue.js - Avantages

- courbe d'apprentissage douce,
- un socle officiel de plugins,
- très performant,
- très facile d'accès.

.fx: extra-large

# Presenter Notes

- socle de plugins officiels -> (vue-router, vuex, vue-cli, vue-devtools)

--------------------------------------------------------------------------------

# Vue.js - Inconvénients

- faiblement structurant,
- pas encore de gros projets.

.fx: extra-large

# Presenter Notes

--------------------------------------------------------------------------------

# Téléchargez notre livre blanc

<a href="https://makinacorpus.github.io/livre-blanc-front-end/">https://makinacorpus.github.io/livre-blanc-front-end/</a>