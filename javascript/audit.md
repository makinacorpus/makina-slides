# Stratégie JavaScript
## Éric Bréhault

.fx: extra-large

--------------------------------------------------------------------------------

# 1 - L'ère jQuery

.fx: extra-large

--------------------------------------------------------------------------------

# Le code JS autour du HTML

- éventuellement dedans (onclick, onload, etc.),
- en tout cas, le JS est un complément.

# Presenter Notes

En fait on fait du jQuery de ci de là pour manipuler le HTML.

.fx: extra-large

--------------------------------------------------------------------------------

# Gestion des dépendances

On télécharge puis on copie manuellement les fichiers dans le projet.

.fx: extra-large

--------------------------------------------------------------------------------

# Structuration du code

Aucune à priori.

.fx: extra-large

--------------------------------------------------------------------------------

# Packaging pour la production

- aucune,
- ou manuelle,
- ou gérée par le backend.

.fx: extra-large

--------------------------------------------------------------------------------

# 2 - L'ère MVC

.fx: extra-large

--------------------------------------------------------------------------------

# Le code au centre

- Le code est l'essentiel,
- le DOM est instrumentalisé pour faire le rendu.

.fx: extra-large

--------------------------------------------------------------------------------

# Gestion des dépendances

Bower

bower.json définit les versions.

.fx: extra-large

--------------------------------------------------------------------------------

# Structuration du code

.fx: extra-large

--------------------------------------------------------------------------------

# Framework MVC

Angular 1, Ember, Backbone

.fx: extra-large

--------------------------------------------------------------------------------

# Bonnes pratiques

- Développement objet
- Générateurs de projets
- Tests unitaires et d'acceptance

.fx: extra-large

--------------------------------------------------------------------------------

# Templating

mustache, underscore, handlebars, ...

.fx: extra-large

--------------------------------------------------------------------------------

# Grid et habillage

Bootstrap, Foundation

LESS, SASS

.fx: extra-large

--------------------------------------------------------------------------------

# Chargement des dépendances

AMD (RequireJS)

.fx: extra-large

--------------------------------------------------------------------------------

# Packaging pour la production

Bundling automatique.

.fx: extra-large

--------------------------------------------------------------------------------

# Tooling

Grunt, puis Gulp

.fx: extra-large

--------------------------------------------------------------------------------

# L'ère Composant

.fx: extra-large

--------------------------------------------------------------------------------

# Se débarasser des contingences

- programmation objet,
- languages plus évolués (ES6, TypeScript),
- création de nouveaux composants HTML.

.fx: extra-large

--------------------------------------------------------------------------------

# Gestion des dépendances

NPM

Tout est défini dans package.json.

.fx: extra-large

--------------------------------------------------------------------------------

# Structuration du code

.fx: extra-large

--------------------------------------------------------------------------------

# Framework Composants

Angular 2, React

.fx: extra-large

--------------------------------------------------------------------------------

# Templating

Directives, composants.

.fx: extra-large

--------------------------------------------------------------------------------

# Grid et habillage

Toujours Bootstrap.

Material design.

.fx: extra-large

--------------------------------------------------------------------------------

# Chargement des dépendances

Plus besoin.

.fx: extra-large

--------------------------------------------------------------------------------

# Tooling

Webpack (transpilation, bundling, etc.)

.fx: extra-large

--------------------------------------------------------------------------------

# Merci

# Presenter Notes

MVC Pas applicable

On préfère l'approche composant:

- le composant gère l'état de l'UI et les événements
- l'app gère l'état interne (le modèle) et la logique métier
