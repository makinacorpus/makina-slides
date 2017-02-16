# Formation Angular
## Éric Bréhault

--------------------------------------------------------------------------------

# 1 - Présentation générale

--------------------------------------------------------------------------------

# La version 2 ?

AngularJS est la version 1.

À partir de la verison 2, le nom devient "Angular".

La version 4 va paraître prochaînement (mais sera dans la continuité d'Angular 2).

# Presenter Notes

parler du sémantic versionning

--------------------------------------------------------------------------------

# Quel type de framework ?

- Spectre large
- Très structurant
- Fortement contraint

# Presenter Notes

expliquer les différences avec React

--------------------------------------------------------------------------------

# Les grands principes

- Composants
- TypeScript
- build

# Presenter Notes

--------------------------------------------------------------------------------

# 2 - Installation et tooling

# Presenter Notes

--------------------------------------------------------------------------------

# Installation

Installer NodeJS (6.9+) et NPM.

Installer Angular CLI:

    !console
    $ npm install -g @angular/cli

# Presenter Notes

--------------------------------------------------------------------------------

# Le CLI

Permet de générer un projet.

    !console
    $ ng new myproject
    $ cd myproject
    $ ng serve

Fournit des facilités pour le développement.

    !console
    $ ng serve
    
Permet d'y ajouter des composants.

    !console
    $ ng generate component MyComponent

# Presenter Notes

--------------------------------------------------------------------------------

# Exercice

- Installer NodeJS et Angular CLI
- Créer un projet
- Observer la structure de fichiers générée

--------------------------------------------------------------------------------

# 3 - Les concepts

- TypeScript
- Component
- Module
- Injection

--------------------------------------------------------------------------------

# Typescript

- TypeScript superset d'ES6 superset d'ES5
- Un "compilateur" fait la conversion
- Apporte :
    - le typage
    - les classes
    - les décorateurs

--------------------------------------------------------------------------------

# Component

Un composant est une classe avec un décorateur `@Component`.

Il correspond à un tag.

Il a un template HTML, éventuellement des fichiers de style.

--------------------------------------------------------------------------------

# Module

Le module est le point d'entrée de l'app Angular.

Il déclare les composants.

Il charge les modules tiers.

Il définit les injections disponibles.

--------------------------------------------------------------------------------

# Injections

Les composants ont besoin de services globaux (persistence des données, accès au backend, rouage, etc.).

Ils les obtiennent par injection de dépendances :
Angular va instancier les services dont on a besoin, et les fournir aux composants.

Les services injectables sont des classes ayant le décorateur `@Injectable`.

Ils sont déclarés dans le module (dans `providers`).

Ils sont fournis aux composants dans leur constructeur.

--------------------------------------------------------------------------------

# 4 - Créer une app simple

# Presenter Notes
utiliser le CLI
faire du debug
SCSS

--------------------------------------------------------------------------------

# 5 - Gérer le routage

# Presenter Notes

--------------------------------------------------------------------------------

# 6 - Appels au backend

# Presenter Notes

--------------------------------------------------------------------------------

# 7 - Gérer des formulaires

# Presenter Notes

--------------------------------------------------------------------------------

# 8 - Ajouter des dépendances externes

# Presenter Notes

--------------------------------------------------------------------------------

# 9 - Déployer en prod

# Presenter Notes

build de prod
vhost
Angular Universal

--------------------------------------------------------------------------------