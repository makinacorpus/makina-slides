# HTML5 / CSS3

 28-29 avril 2015
 CNFPT

## Présentation

**Emmanuelle Helly**

* Intégratrice HTML/CSS depuis 2008
* Plone, Drupal
* emmanuelle.helly@makina-corpus.net

----

# Jour 1 : HTML5 / CSS3

## HTML5

* _Intro : le WorldWideWeb_
* Doctype
* Sémantique
* Formulaires
* Media (figure, audio, video)
* Canvas et SVG
* Drag & Drop
* Localstorage

----

## CSS3

* Mise en forme
* Sélecteurs
* Unités relatives et absolues
* Positionnement
* Mise en page (Grid layout)
* Media-queries
* Transformations
* Effets et animations

----

# Jour 2 : Bootstrap, LessCSS

## BOOTSTRAP 3

* Mise en forme du contenu : texte, tableaux, formulaires, boutons, images et la mise en page
* Mise en page avec la grille adaptative de Bootstrap : pour des sites Responsive Web Design
* Composants Bootstrap : barres de navigation, pagination, boutons, etc.

## LessCSS

* variables
* mixins
* heritages
* pseudo-classes
* importation de fichier

----

# Introduction : le World Wide Web

----

## Composants du WorldWideWeb

* URL (_Uniform Resource Locator_)
* HTML (_HyperText Markup Language_)
* HTTP (_HyperText Transfer Protocol_)

## le W3C

**World Wide Web Consortium**, dirigé par *Tim Berners Lee*

* **396** membres (au 27 avril 2015)
* Définit les spécifications (HTML, XML, accessibilité, mobile)
* Fonctionne par groupes de travail

[w3.org/Consortium](http://www.w3.org/Consortium/)

.fx: larger

----

## Historique

* 1989 : début des travaux de *Tim Berners Lee*, chercheur au CERN, et son équipe. Le principe, l'hypertexte
* 1991 : *Tim Berners Lee* rend le projet **WorldWideWeb** public
* 1993 : création du navigateur **Mosaic**
* 1994 : création du **W3C** par *Tim Berners Lee*
* 1996 : implémentation de **CSS1.0** par **IE**
* 1998 : publication des spécifications **CSS 2.0**
* 1999 : spécifications **HTML4.01**, et début des travaux sur **CSS3**
* 2000 : publication des spécifications pour **XHTML1**. 
* 2006 : publication des recommandations de **XHTML2.0**

Scission au sein du W3C : le **WHATWG** (Web Hypertext Application Technology Working Group) travaille sur un autre standard pour le **HTML**

* 2008 : "First Public Working Draft" du **HTML5** présentée par le **WHATWG**
* 2012 : **HTML5** passe en "Candidate Recommandation"
* fin 2014 : **HTML5** est un standard du W3C

[fr.wikipedia.org/wiki/World_Wide_Web](http://fr.wikipedia.org/wiki/World_Wide_Web)

.fx: smaller

----

# Les outils de développement

* Éditeur de code : [Notepad++](http://notepad-plus-plus.org/), Sublime Text, Geany, [Atom](https://atom.io/)
* Navigateur : **éviter IE** !! Firefox ou Chrome, et leurs plugins d'inspection de code (voir [Liste de puglins](http://makina-corpus.com/blog/metier/2013/extensions-firefox-pour-le-developpement-web))
* Test et validation
    * [validator.w3.org](http://validator.w3.org/) respect des standards
    * [opquast.com](http://opquast.com/fr/) pour la qualité du code, l'accessibilité
* Documentation
    * officielle [w3c.org/TR/html5](http://www.w3.org/TR/html5/)
    * compréhensible [developer.mozilla.org](https://developer.mozilla.org/fr/)

----

# Partie 1 : HTML5

----

## Sommaire

* Doctype
* Sémantique
* Formulaires
* Media (figure, audio, video)
* Canvas et SVG
* Drag & Drop
* Localstorage

----

## HTML5, standard depuis le 28 octobre 2014

* Implémentation variable selon les navigateurs : voir [caniuse.com](http://caniuse.com/)
* Compatible avec IE9, du moins en partie, des outils permettent une "régression en douceur" (graceful degradation)
* [Différences avec HTML4](http://www.w3.org/TR/html5-diff/)

## DocType

`<!DOCTYPE html>` ... tout simplement

## Encodage

Ajouter dans les entêtes `<meta charset="UTF-8">`

----

## Exemple 1 : Pour commencer

    !html
    <!doctype html>
    <html>
      <head>
        <meta charset="UTF-8">
        <title>Example document</title>
      </head>
      <body>
        <p>Example paragraph</p>
      </body>
    </html>

----

# Sémantique

## Balises

* Inline : `<mark>`, `<time>`, `<meter>`, `<progress>`
* [Section](https://developer.mozilla.org/fr/docs/Web/HTML/Sections_and_Outlines_of_an_HTML5_document) : `<section>`, `<article>`, `<main>`, `<aside>`, `<nav>`, `<header>`, `<footer>`
* Grouper : `<figure>`, `<figcaption>`

Code plus clair, page mieux structurée sémantiquement : un meilleur référencement.

<!-- Voir [tinytypo.tetue.net](http://tinytypo.tetue.net/tinytypo.html) -->

--- 

## Exemple 2 : Structure sémantique d'une page

    !html
    <body>
        <header>
            <nav data-role="menu">
                <ul>
                …
                </ul>
            </nav>
        </header>
        <main role="main">
            <article>
                <section>
                  <h1>éléphants de forêt</h1>
                  <p>Dans cette section, nous discutons des éléphants de forêt moins connus.
                       Ce paragraphe continue…</p>
                  <section>
                    <h2>Habitat</h2>
                    <p>Les éléphants de forêt ne vivent pas dans les arbres mais parmi eux.
                       Ce paragraphe continue…</p>
                    <figure><img src="__mon__url__" /></figure>
                    <p>Texte</p>
                  </section>
                </section>
            </article>
            <aside>
            … barre latérale …
            </aside>
        </main>
        <footer>
        …
        </footer>
    </body>

.fx: smaller

# presenter notes

`header` et `footer` désignent l'entête et le pied de page, mais ne sont pas forcément en haut ou en bas de la page.
Peuvent être à l'intérieur d'un article.

----

## Microdatas

Voir [schema.org](http://schema.org/docs/gs.html)

    !html
    <div itemscope itemtype="http://schema.org/Person">
        <div itemprop="name"><strong>Boris Vian</strong></div>
        <div itemscope 
            itemtype="http://schema.org/Organization">
        <a itemprop="url" href="www.letabou.com">
          <span itemprop="name">le Tabou</span></a>
        </div>
        <div itemprop="address" itemscope itemtype="http://schema.org/PostalAddress">
          <div itemprop="streetAddress">le Tabou<br>
                Saint Germain des Prés</div>
          <div>
            <span itemprop="postalCode">75006</span>
            <span itemprop="addressLocality">Paris</span>
          </div>
          <div itemprop="addressCountry">France</div>
        </div>
        <div itemprop="telephone">0149687368</div>
    </div>

Autres implémentations : microformats, RDFa

.fx: smaller

----

# Media et éléments embarqués

## `<embed>`

* Pour embarquer une application externe (un plugin par exemple). 
* Déjà existants en HTML4 : 

    * `<object>`
    * `<iframe>` : Peut embarquer un autre site, un éditeur de texte riche ou une carte par exemple.

----

## [`<audio>` et `<video>`](https://developer.mozilla.org/fr/docs/Web/HTML/Utilisation_d%27audio_et_video_en_HTML5)

    !html
    <audio src="./donjon-crom.mp3" controls></audio>
    <video src="video.ogg" controls 
        poster="video.jpg" width="640" height="480">

### Formats audio et vidéo / navigateurs

* ogg -> Chrome, Firefox, Opera
* webm -> Chrome, Firefox, Opera
* MPEG-4/H.264 -> Chrome, Firefox, Opera, Safari, IE

### Code

On peut inclure plusieurs formats de media

    !html
    <video controls poster="video.jpg" width="640" height="480">
        <source src="video.ogg" />
        <source src="video.avi" />
        <source src="video.mp4" />
    </video>

### Exercice

Essayer la balise `<video>` avec différentes sources, en ouvrant la page dans différents navigateurs.

----

## Image, nouveaux attributs `srcset` et `sizes`

`src` est ignoré pour les user-agent supportant srcset.

    !html
    <img src="img/eilean-donnan-castle-200.jpg" 
      alt="Clock" 
      srcset="img/eilean-donnan-castle-200.jpg 200w, img/eilean-donnan-castle-400.jpg 400w"
      sizes="(min-width: 800px) 400px, 50vw" />

Si (min-width: 600px) :

* alors image de largeur 200px
* sinon 50 % de la largeur viewport

Fonctionne avec Chrome, et firefox à partir de la version 38.

----

## Conteneur `<figure>`

Permet d'illustrer et ajouter une légende à une image, un schéma.

    !html
    <figure>
      <img src="image.jpg" alt="" />
      <figcaption>Légende de l'image</figcaption>
    </figure>

Peut contenir autre chose que des images : du code ou une vidéo par exemple.

----

# Formulaires

## Nouveaux contrôles

`<input>` de type text, mais aussi :

* tel, url, email, search
* date, time, number, range
* color

## Nouveaux attributs

* placeholder
* pattern
* autocomplete
* min, max, step (pour date, time, number et range)
* list

--- 

## Code

Url avec placeholder

    !html
    <input type="url" name="url" placeholder="Votre site Web" />

Range

    !html
    <input type="range" name="range" 
        min="10" max="100" step="5" value="15"/>

Pattern

    !html
    <input type="text" name="pattern" pattern="[a-z]{2}[0-9]{2}" />

Liste

    !html
    <input type="text" name="ville" list="villes"/>
    <datalist id="villes">
        <option value="Albi">
        <option value="Cahors">
    </datalist>

.fx: smaller

---

## Exercice

* Créez un formulaire avec les champs suivants : 
    * Nom complet, 
    * Téléphone, 
    * Date de naissance, 
    * Couleur préférée, 
    * Ville (parmi quelques villes)

[Exemple complet](https://github.com/numahell/html5-css3/blob/master/html/forms.html)

----


# Effets et 3D

## CANVAS

* surface de pixels contrôlés en JavaScript, API disponible
* Fonctionnement en "boite noire"

Le "Paint" du web

    !html
    <html>
     <head>
      <script type="application/x-javascript">
        function draw() {
         var canvas = document.getElementById("canvas");
         var ctx = canvas.getContext("2d");

         ctx.fillStyle = "rgb(200,0,0)";
         ctx.fillRect (10, 10, 55, 50);
        }
      </script>
     </head>
     <body onload="draw()">
       <canvas id="canvas" width="300" height="300"></canvas>
     </body>
    </html>

.fx: smaller

----

## SVG

Dessiner en 2D vectorielle via XML

* Accès aux éléments d'un SVG depuis le DOM
* CSS applicables
* Peut être chargé depuis un fichier externe ou en ligne dans un document HTML
* L’arbre des données est conservé en mémoire

### Example

    !html
    <svg>
      <circle id="circle1" cx="40" cy="40" r="24" />
    </svg>

Voir aussi [css-tricks.com/using-svg](http://css-tricks.com/using-svg/)

----

## WebGL

Un peu plus que bablutiant : de plus en plus de navigateurs le supportent, mais pas toujours les cartes vidéos.

Voir [Les interfaces de demain](http://fr.slideshare.net/makinacorpus/petit-djeuner-html5-et-css3-les-interfaces-de-demain) pour plus de détails.

## Flash ?

Flash n'est plus supporté par les Iphone et Ipad, GNU/Linux et Android depuis Jelly Bean. Oubliez-le.

----

# Application web en HTML5

## Drag&Drop

## Local Stockage

## File API

## Server-Sent Events

----

# Partie 2 : CSS3

----

## Sommaire

* Mise en forme
* Sélecteurs
* Unités relatives et absolues
* Positionnement
* Mise en page (Grid layout)
* Media-queries
* Transformations
* Effets et animations

----

# Mise en forme

## Propriétés

* `background-size`, `border-radius`, `box-shadow`, `opacity`, 
* dégradés
* arrière-plan multiples
* transparence pour la couleur de fond

[css3generator.com](http://css3generator.com/)

----

## Font-Face

    !css
    /* roboto bold */
    @font-face {
        font-family: 'roboto';
        src: url('roboto/Roboto-Bold-webfont.eot');
        src: url('roboto/Roboto-Bold-webfont.eot?#iefix') format('embedded-opentype'),
             url('roboto/Roboto-Bold-webfont.woff') format('woff'),
             url('roboto/Roboto-Bold-webfont.ttf') format('truetype'),
             url('roboto/Roboto-Bold-webfont.svg#robotobold') format('svg');
        font-weight: bold;
        font-style: normal;
    }

* Trouvez des fonts sur [fontsquirrel.com](http://www.fontsquirrel.com/)
* Possibilité de faire un import des fonts depuis [www.google.com/fonts](http://www.google.com/fonts/)

Attention à la qualité des glyphes, peuvent être mal positionnés sur la ligne de base.

----

## Extensions spécifiques des navigateurs

Les navigateurs principaux

<table border=1>
    <tbody>
        <tr>
            <td>Safari / Chrome</td>
            <td>-webkit-</td>
        </tr>
        <tr>
            <td>Firefox</td>
            <td>-moz-</td>
        </tr>
        <tr>
            <td>Opera</td>
            <td>-o-</td>
        </tr>
        <tr>
            <td>Internet Explorer</td>
            <td>-ms-</td>
        </tr>
    </tbody>
</table>

----

# Sélecteurs

## Sélecteurs CSS2

Sont maintenant implémentés par les navigateurs modernes

par attribut

    !css
    a[attribut~="valeur"]

par élément fils direct

    !css
    a > b

par élément frère

    !css
    a + b

----

## Sélecteurs CSS3

par attribut

    !css
    a[attribut^="valeur"]

par fils premier, dernier ou tous les x éléments

    !css
    a:first-child
    a:last-child
    a:nth-child(expression)

négation

    !css
    a:not(.class)

première lettre, première ligne

    !css
    ::first-letter
    ::first-line

* Un tutoriel : [flukeout.github.io](http://flukeout.github.io/)
* La documentation officielle : [www.w3.org/TR/selectors](http://www.w3.org/TR/selectors/)

.fx: smaller

----

# Unités

## Absolues

* px : pour les supports écran
* pt : pour les supports imprimés

## Relatives

* em, %
* rem (root em), relative à la taille attibuée au document (nouveau !)

----

# Positionnement

    !css
    position: absolute;
    top: 10%;
    left: 50px;

* L'élément sort du flux
* Position relatif au document ou à l'élément parent le plus proche positionné en relatif

----

# Mise en page

## Flexbox

    !css
    .flex { display: flex; }

    !html
    <div class="flex">
        <div>texte 1</div>
        <div>texte 2</div>
    </div>

Supporté par les navigateurs modernes, mais l'implémentation est parfois différente. Fonctionnel mais à utiliser à bon escient.

## Colonne

    !css
    div {
        column-count: 2;
        column-width: 12em;
    }

Supporté par les navigateurs actuels en utilisant les préfixes (voir caniuse.com)

.fx: smaller

----

# Media-queries

    @media (min-width: 700px) and (orientation: landscape) {…}

* Orientation (`portrait` ou `landscape`) et Localisation
* Device api (`screen`, `print`, `tv`, )

----

# CSS animé

## Transitions

    a:hover {
        transition color 200ms ease;
    }

Sur les propriété `height`, `width`, `color`, `background`

----

## Transformations

Rotation, translations

----

# TP Mise en page

* Créer une page structurée
* Ajouter un menu horizontal déroulant
* Ajouter une image de fond positionnée
* Responsive

---- 

# Partie 3 : Bootstrap 3

----

## Sommaire

* Mise en forme CSS
* La grille bootstrap
* Composants

[Des exemples](http://getbootstrap.com/getting-started/#examples)

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

----

## TP Bootstrap

(voir fichiers)

[Exemples de parallaxe](http://www.alsacreations.com/tuto/lire/1417-zoom-sur-effet-parallaxe.html)

[Générateur d'images](http://lorempixel.com/)

----


# Partie 4 : LessCSS

----

## Sommaire

* variables
* imbrication de code
* mixins
* importation de fichier

----

## Installer LessCSS

* Dans windows : [winless.org](http://winless.org/)
* Pour utiliser plus de fonctionnalités de nodejs : [nodejs.org](http://nodejs.org/download/)
* [Installer nodejs sous Ubuntu / debian](https://github.com/joyent/node/wiki/Installing-Node.js-via-package-manager#debian-and-ubuntu-based-linux-distributions)

Sur Ubuntu:

    curl -sL https://deb.nodesource.com/setup | sudo bash -

Installation du paquet:

    sudo apt-get install -y nodejs

Installer less

    sudo npm install -g less

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

# TP : un thème avec LessCSS et Bootstrap

----

## Intégrer un design simple

1. Créer l'arborescence du projet
1. Créer une structure de page d'accueil en utilisant les fonctionnalités de bootstrap. On doit retrouver les éléments suivants :

    * Logo et nom du site
    * Barre de navigation
    * Diaporama
    * Liste d'articles
    * Complément d'information sous forme d'accordéon

Voir [les exemples](http://getbootstrap.com/getting-started/#examples) pour l'inspiration.

----

## Arborescence type d'un thème

    !console
    mon_projet
    ├── base.html
    └── mon_theme
        ├── bootstrap -> /chemin/vers/dossier/bibliotheques/bootstrap/
        ├── css
        ├── fonts
        ├── img
        ├── js
        └── less
            ├── components/
            │   ├── search.less
            │   ├── nav.less
            │   ├── fonts.less
            │   └── forms.less
            ├── bootstrap.less
            ├── content.less
            ├── footer.less
            ├── header.less
            ├── style.less
            ├── mixins_project.less
            ├── variables_project.less
            └── variables.less

Compiler vos fichiers

    lessc less/style.less css/style.css

.fx: smaller

----

# Bonus

----

# Gulp, outil d'automatisation

Met en place des tâches qui peuvent remplir plusieurs fonctions

* automatiser la génération des fichiers css à partir des fichiers less,
* minifier les CSS et les JS
* ....

## Installation

Prérequis : installer nodejs

Installer `gulp` globalement
 
    !console
    npm install -g gulp

Installer les dépendances du projet et les ajouter au fichier `package.json`

    !console
    cd /dossier/de/montheme
    npm install --sav-dev gulp-less

Lancer l'installation des paquets indiqués dans `package.json` :

    !console
    npm install

.fx: smaller

----

## Initialisation

Copier `gulpfile.js` dans le dossier de thème

    !console
    var gulp = require('gulp');
    var less = require('gulp-less');
    var rename = require('gulp-rename');
    var notify = require('gulp-notify');
    var minifyCSS = require('gulp-minify-css');
    var dsource = "./src/";
    var ddest = "./www/";

    var lessfiles = [dsource+'less/styles.less'];
    var lessfiles_watch = [dsource+'less/**/*.less'];

    w = process.cwd();
    styles = gulp.task(
      'styles',
      function() {
        return gulp.src(lessfiles)
        .pipe(less())
        .pipe(rename("styles.css"))
        .pipe(gulp.dest(ddest+'css/'))
        .pipe(notify({message: 'Styles task complete'}))
        .pipe(rename({suffix: '.min'}))
        .pipe(minifyCSS())
        .pipe(gulp.dest(ddest+'css/'))
      });


.fx: smaller

----

## Usage

    !console
    gulp <nom_de_tache_définie>
    gulp styles # compile les fichiers less et minifie les CSS

## Resources

* Site officiel [gulpjs](http://gulpjs.com/)
* Tutoriel (en) sur [Site Point](http://www.sitepoint.com/introduction-gulp-js/)
* Erreur courante [Erreur ENOSPC](http://stackoverflow.com/questions/16748737/grunt-watch-error-waiting-fatal-error-watch-enospc)

----

# Autres ressources

## Outils

* [Yeoman](http://yeoman.io/)
* [HTML Shiv](https://github.com/aFarkas/html5shiv)
* [Polyfill](https://remysharp.com/2010/10/08/what-is-a-polyfill)

## Exemples de code

* [Codeopen](http://codepen.io)
* [Codedrops](http://tympanus.net/codrops/)


----

# Questions ?

