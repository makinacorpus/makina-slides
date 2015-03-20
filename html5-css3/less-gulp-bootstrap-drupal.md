# Drupal Bootstrap / Less et Gulp

 23 mars 2015

## Présentation

**Emmanuelle Helly**

* Intégratrice HTML/CSS
* Plone, Drupal
* emmanuelle.helly@makina-corpus.net

----

# Programme

## Installer l'environnement

* Installation de nodejs
* Installation de Drupal et Bootstrap
* Installation des modules nécessaires pour Gulp
* Tâches de Gulp

## Bootstrap

* Mise en forme du contenu
* Mise en page avec la grille adaptative de Bootstrap : pour des sites Responsive Web Design
* Composants Bootstrap

---- 

## Less

* variables
* mixins
* heritages
* pseudo-classes
* importation de fichier

## Thème Drupal bootstrap

* Arborescence du thème

----

# Installer l'environnement

----

## À quoi sert gulp ?

Gulp sera utilisé pour :

* générer les fichiers css à partir de style.less et bootstrap.less, à chaque modification d'un fichier
* minifier les fichiers css et js (optionnel, dans ce cas on n'utilise pas les fonctions de minification de Drupal)

----

## Installer nodejs

Un outil pratique pour gérer les version de nodejs : [nvm](https://github.com/creationix/nvm)

    !console
    curl https://raw.githubusercontent.com/creationix/nvm/v0.24.0/install.sh | bash

Si nvm n'est pas dans le PATH:

    !console
    source ~/.nvm/nvm.sh

Installer et utiliser nodejs 0.10

    !console
    nvm install 0.10 # or stable
    nvm use 0.10 # or stable

----

# Créer un thème basé sur bootstrap pour un nouveau projet

* Installer Drupal et le thème bootstrap
* créer un sous-thème
* Installer les packages gulp

----

## Installer Drupal et les dépendences

Installer Drupal et le thème drupal Bootstrap

    !console
    drush dl bootstrap ; drush en -y bootstrap
    drush dl

Installer Bootstrap dans sites/all/libraries

    !console
    wget https://github.com/twbs/bootstrap/archive/v3.3.4.zip
    unzip v3.3.4.zip

On peut ajouter les lignes au fichier mon_profil.make

    !console
    ; Themes
    ; Base theme 
    ; Beware: Bootstrap 3.1 version will require PHP 5.3 and jQuery 1.9+
    projects[] = bootstrap
    libraries[bootstrap][download][type] = "get"
    libraries[bootstrap][download][url] = "https://github.com/twbs/bootstrap/archive/v3.3.4.zip"
    projects[] = views_bootstrap

----

## Créer un sous-thème

    !console
    cd sites/all/themes
    mv bootstrap/bootstrap_subtheme montheme
    cd montheme
    mv bootstrap_subtheme.info.starterkit montheme.info

Dans montheme.info, décommenter settings[cdn]

Créer un lien symbolique vers la librairie du framework bootstrap

    !console
    ln -s $PROJECT/sites/all/libraries/bootstrap \
        $PROJECT/sites/all/themes/montheme

----

## Installer les packages gulp et less

Copier package.json et gulpfile.js dans le dossier de thème

Activer l'environnement node

    !console
    nvm use 0.10

Lancer l'installation des paquets :

    !console
    cd /dossier/de/montheme
    npm install

Les paquets sont installés dans le dossier node_modules

----

# Utiliser l'environnement

Pour travailler sur le thème, activer l'environnement node et lancer la commande gulp watch

    !console
    nvm use 0.10
    ./node_modules/.bin/gulp watch

----

# Framework Bootstrap

----

## Sommaire

* Mise en forme CSS
* La grille bootstrap
* Composants

----

##  Mise en forme CSS

[getbootstrap.com/css](http://getbootstrap.com/css/)

* Typography (alignement, blockquotes, lists)
* Tables
* Formulaires
* Boutons
* Images

----

##  La grille bootstrap

[Grid option](http://getbootstrap.com/css/#grid-options)

* Le principe
* colonnes imbriquées
* offset
* ordre des colonnes

----

##  Composants

* Glyphicons
* Menus déroulants
* Navigation
* Breadcrumb, pagination, label, badges
* Media (groupe d'image + texte)
* Vignettes

---

# LessCSS

----

## Sommaire

* variables
* imbrication de code
* mixins
* importation de fichier

----

# Installer LessCSS

* Dans windows : [winless.org](http://winless.org/)
* Pour utiliser plus de fonctionnalités de nodejs : [nodejs.org](http://nodejs.org/download/)

----

# Les bases

## variables

    !css
    @nice-blue: #5B83AD;
    @light-blue: @nice-blue + #111;

    #header {
      color: @light-blue;
    }

Résultat :

    !css
    #header {
      color: #6c94be;
    }

Un gain de temps inestimable pour l'intégration front-end

----

## imbrication de code

    !css
    #header {
      color: black;
      .navigation {
        font-size: 12px;
      }
      .logo {
        width: 300px;
      }
    }

----

# Mixins et fonctions

[Documentation](http://lesscss.org/features/#mixins-feature)

    !css
    .a, #b {
      color: red;
    }
    .mixin-class {
      .a();
    }
    .mixin-id {
      #b();
    }

Résultat :

    !css
    .a, #b {
      color: red;
    }
    .mixin-class {
      color: red;
    }
    .mixin-id {
      color: red;
    }

----

# Import de fichier

    !css
    @import (option) "fichier";

Les options

* `reference`: importe en tant que fichier less sans l'inclure dans la sortie css. Très utilisé pour les fichiers de fonctions less.
* `inline`: inclue le fichier sans le compiler
* `less`: traite le fichier en tant que less, quelque soit l'extension
* `css`: traite le fichier en tant que css
* `once`: n'importe le fichier qu'une seule fois (comportement par défaut)
* `multiple`: importe le fichier plusieurs fois


----

# Drupal bootstrap

----

## Drupal Bootstrap

[Projet](https://www.drupal.org/project/bootstrap) ([Documentation](https://www.drupal.org/node/1976938))

## Arborescence dans le profil 

    !console
    mon_profil_drupal/
    ├── mon_profil_drupal.drush.inc
    ├── mon_profil_drupal.info
    ├── mon_profil_drupal.install
    ├── mon_profil_drupal.make
    ├── mon_profil_drupal.profile
    ├── modules
    ├── themes
    │   └── montheme
    └── translations


----

## Arborescence du thème

    !console
    montheme
    ├── bootstrap -> ../../../../sites/all/libraries/bootstrap/
    ├── css
    ├── fonts
    ├── img
    ├── js
    ├── less
    └── templates
        ├── block
        ├── bootstrap
        ├── node
        ├── system
        └── views

----

### Arborescence des fichiers less

    !console
    less
    ├── nodes
    │   ├── news.less
    │   └── event.less
    ├── objects
    │   ├── forms.less
    │   └── tables.less
    ├── pages
    │   └── register.less
    ├── views
    │   ├── recherche.less
    │   └── views.less
    ├── bootstrap.less
    ├── content.less
    ├── fonts.less
    ├── footer.less
    ├── header.less
    ├── mixins.less
    ├── overrides.less
    ├── style.less
    └── variables.less

----

## Les fichiers less

* `bootstrap.less` importe les feuilles de styles bootstrap
* `style.less` importe les feuilles de styles du projet
* `header.less`, `content.less` et `footer.less` pour gérer le layout
* Dans `objects/`, `forms.less` et `tables.less` pour gérer les formulaires ou les tableaux
* Dans `nodes/`, pour gérer ce qui est relatif aux types de contenus
* Dans `pages/`, pour gérer les pages telles que l'inscription
* `mixins.less` qui inclue les fonctions less du projet
* `variables.less` qui inclue les variables bootstrap et celles du projet

----

# Questions ?
