% Formation HTML5 / CSS3
% Emmanuelle Helly, intégratrice chez Makina Corpus

# HTML5 / CSS3

 6-8 octobre 2015


## Présentation

**Emmanuelle Helly**

* Intégratrice HTML/CSS depuis 2008
* Plone, Drupal, Django
* emmanuelle.helly@makina-corpus.net

----

# Partie 1 : HTML5

* Intro : le _WorldWideWeb_, les outils de développement web

## La structure

* Doctype
* Nouvelles balises sémantiques

## Les Media

* Media (figure, audio, video)
* Intégrer un SVG

## Les formulaires

* Types de champs
* Attributs

.fx: smaller

----

# Partie 2 : CSS3

## Rappels CSS

* Sélecteurs, hiérarchie des styles
* Comportement des éléments
* Modèle de boite
* Positionnement

## La forme

* Mise en forme CSS3
* Polices embarquées (font-face)

## Disposition et Grille

* Disposition du texte : Multicolonne
* Méthodes : float, inline-block, table-cell, flexbox
* Grid Flexbox

.fx: smaller

----

# Partie 3 : Responsive design

* Introduction
* Media-queries
* Grille responsive
* Outils de développement

----

# Partie 4 : Frameworks

* Découverte framework avec ou sans UI
* Étude de cas avec Bootstrap3

# _Bonus :_ SASS ou LessCSS

* Avantages d'un pre-compileur
* Variables et imbrications
* Fonctions et imports
* Installation et utilisation

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
    * [opquast.com](http://opquast.com/fr/) pour la qualité du code, l'accessibilité : module Firefox en cours de refonte
* Documentation
    * officielle [w3c.org/TR/html5](http://www.w3.org/TR/html5/)
    * compréhensible [developer.mozilla.org](https://developer.mozilla.org/fr/)

----

# Partie 1 : HTML5

----

# Sommaire

* Structure : Doctype et balises sémantiques
* Media (figure, audio, video, SVG)
* Formulaires

----

# Structure

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
                  <h1>Éléphants de forêt</h1>
                  <p>Dans cette section, nous discutons des éléphants de forêt moins connus.
                       Ce paragraphe continue…</p>
                  <section>
                    <h2>Habitat</h2>
                    <p>Les éléphants de forêt ne vivent pas dans les arbres mais parmi eux.
                       Ce paragraphe continue…</p>
                    <figure><img src="__mon__url__" /></figure>
                    <p>Texte</p>
                  </section>
                </section>2
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

On peut inclure plusieurs formats de media

    !html
    <video controls poster="video.jpg" width="640" height="480">
        <source src="video.ogg" />
        <source src="video.avi" />
        <source src="video.mp4" />
    </video>

### Formats audio et vidéo / navigateurs

* ogg -> Chrome, Firefox, Opera
* webm -> Chrome, Firefox, Opera
* MPEG-4/H.264 -> tous les navigateurs sauf IE8 et Opera mini
* MP3 reconnu par tous les navigateurs

Voir sur [CanIUse](http://caniuse.com/#search=video%20format)

----

## Image, nouveaux attributs `srcset` et `sizes`

`src` est ignoré pour les user-agent supportant srcset.

    !html
    <img src="small.jpg"
         srcset="large.jpg 1024w, medium.jpg 640w, small.jpg 320w"
         sizes="(min-width: 360px) 33.3vw, (min-width: 980px) 980px, 100vw"
         alt="A rad wolf">

`sizes`

* Si (min-width: 360px) alors image de largeur 33.3% de la taille de la fenêtre
* Si (min-width: 980px) alors l'image de largeur 980px de la taille de la fenêtre
* sinon 100% de la largeur de la fenêtre

`srcset` propose plusieurs fichiers correspondant à des largeurs différente.
Le navigateur choisit le fichier en fonction de la taille de l'emplacement de l'image'.

Fonctionne avec Chrome, et firefox à partir de la version 38.

Liens utiles : [Balise img sur la doc Mozilla](https://developer.mozilla.org/fr/docs/Web/HTML/Element/Img), [Responsive image community group](http://responsiveimages.org/)

.fx: smaller

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

## Exercice: bannière différente selon la définition d'écran

* Insérez une bannière de taille différente selon la définition d'écran en utilisant srcset.
* Insérez un logo en SVG

----

## CANVAS

* Surface de pixels contrôlés en JavaScript, API disponible
* Fonctionnement en "boite noire" : le **"Paint" du web**

## WebGL

Prend de l'ampleur, mais non encore complètement [supporté par tous les navigateurs](http://rando.ecrins-parcnational.fr/fr/boucle-du-pigeonnier-dans-le-cirque-du-gioberney) ni les drivers vidéos.

* De très belles expérimentations sur [Chrome Experience](https://www.chromeexperiments.com/webgl)
* Affichage 3D de randonnées dans l'application [Geotrek](http://geotrek.fr/), à voir sur [Rando Écrins](http://rando.ecrins-parcnational.fr/fr/boucle-du-pigeonnier-dans-le-cirque-du-gioberney)
* Voir aussi [Les interfaces de demain](http://fr.slideshare.net/makinacorpus/petit-djeuner-html5-et-css3-les-interfaces-de-demain) pour plus de détails

## Flash ?

Flash n'est plus supporté par les Iphone et Ipad, GNU/Linux et Android depuis Jelly Bean. Oubliez-le.

.fx: smaller

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

Créez un formulaire avec les champs suivants :

* Nom complet,
* Téléphone,
* Date de naissance,
* Couleur préférée,
* Ville (parmi quelques villes)

Utilisez Chrome (ou Chromium) et Firefox pour afficher ce formulaire.

[Exemple complet](https://github.com/numahell/html5-css3/blob/master/html/forms.html)

----

# Partie 2 : CSS3

----

# Sommaire

## Rappels CSS

* Sélecteurs, hiérarchie des styles
* Comportement des éléments
* Modèle de boite
* Positionnement

## La forme

* Mise en forme CSS3
* Polices embarquées (font-face)

----

# Compatibilité

## Préfixes des navigateurs

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

En général les frameworks implémentent les préfixes.

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

## Hiérarchie des styles

Vers le plus important

Implémentation du navigateur > Styles <link ...> > Styles définis dans <styles> dans la page HTML > style défini dans la balise

### Hiérarchie de sélecteurs

sélecteur de classe > Sélecteur de balise > Sélecteur d'id

----

## Exercice

Déroulez le tutoriel [flukeout.github.io](http://flukeout.github.io/)

----

# Unités

## Absolues

* `px` : pour les supports écran
* `pt` : pour les supports imprimés

## Relatives

* `em`, `%`
* `rem` (root em), relative à la taille attibuée au document (nouveau !)

## Bonne pratique

Définir la taille de référence pour le `<body>`, puis définir les autres tailles en `em` ou `rem`

----

# Positionnement

## Absolute

    !css
    position: absolute;
    top: 10%;
    left: 50px;

* L'élément sort du flux
* Position relatif au document ou à l'élément parent le plus proche positionné en relatif

## Fixed


    !css
    position: fixed;
    top: 10%;
    right: 20px;

* L'élément sort du flux
* Positionnement fixé par rapport à la partie visible du navigateur

.fx: smaller

----

# Mise en forme

## Propriétés

* `background-size`, `border-radius`, `opacity`,
* `box-shadow` : [exemples](http://codepen.io/ericbutler555/pen/ogJdMg) [sur codepen](http://codepen.io/thomasjwicker/pen/jzbHt)
* dégradés
* arrière-plan multiples
* transparence pour la couleur de fond

[css3generator.com](http://css3generator.com/)

----

# Disposition

## Flottant

    #sidebar {
        width: 33%;
        float: left;
    }
    #content {
        width: 76%;
        float: left;
    }

## Hybride inline et block

    #sidebar {
        width: 33%;
        display: inline-block;
    }
    #content {
        width: 76%;
        display: inline-block;
    }

.fx: smaller

----

## Comportement cellule de table

    #sidebar {
        width: 33%;
        display: table-cell;
    }
    #content {
        width: 76%;
        display: table-cell;

## Flexbox

Nouveauté en CSS3.

----

# Mise en page en CSS3

## Flexbox

    !css
    .flex {
        display: flex;
    }

    !html
    <div class="flex">
        <div>texte 1</div>
        <div>texte 2</div>
    </div>

Supporté par les navigateurs modernes, mais l'implémentation est parfois différente. Fonctionnel mais à utiliser à bon escient.

[Toutes les directives flex](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)

Exemples de code : [système de grille](http://codepen.io/uxc/pen/xwxZZg), [Justify-content](http://codepen.io/chrisnager/pen/wBoXLE)

Amusant : [Générateur de Mondrian](http://codepen.io/phantomesse/pen/KmxBI)

----

## Texte en colonne

Plutôt pour le contenu que pour la disposition

    !css
    div {
        column-count: 2;
        column-width: 12em;
    }

Supporté par les navigateurs actuels en utilisant les préfixes (voir caniuse.com)

.fx: smaller

----

## La grille en CSS

La grille, héritage du print (gouttière, colonnage)

* Les avantages et les limites (ex : design très élaborés ne rentrent pas toujours dans une grille)
* Comment penser son design en fonction d'une grille

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

# TP Mise en page

Mettre en page la page tp-mise-en-page.html qui contient

* un entête
* une barre latérale
* le contenu
* un pied de page

À faire:

1. Cherchez et corrigez les erreurs HTML
1. Disposez la barre latérale à droite du contenu- La partie aside doit occuper 1/4 de la page, la section content 3/4
1. Fixez la navigation en bas sur toute la largeur
1. Dans le menu pied de page, chaque bloc doivent être côte à côte
1. Changez la polices des titres avec google font.
1. Responsive : Ne laisser les blocs cote à cote qu’à partir de 900px.

.fx: smaller

----

# Partie 3 : Responsive design

----

# Sommaire

* Introduction
* Media-queries

----

# Introduction

Quantité de modèles de smartphones, de version de Android, IOS ou Windows Phone, de navigateurs et leurs versions, surchargés par les opérateurs ...
Impossible de tout couvrir.

## Responsive vs site dédié

Si le site web est une application métier, préférable de développer une application native, ou une version full mobile.

## Organisation et contenu responsive

* Organisation responsive : disposition varie en fonction de la définition d'écran
* Contenu responsive : certains contenus peuvent être affichés ou non selon la définition d'écran

----

# Media-queries

    @media (min-width: 700px) and (orientation: landscape) {…}

* Orientation (`portrait` ou `landscape`) et Localisation
* Device api (`screen`, `print`, `tv`, )

Importance de définir des points d'arrêt pertinents en fonction des terminaux les plus utilisés.

----

## Approche mobile first

    #sidebar {
        padding: 15px;
    }
    @media (min-width: 700px) {
        #sidebar {
            width: 33%;
            float: left;
        }
    }
    @media (min-width: 1040px) {
        #sidebar {
            width: 25%;
            float: left;
        }
    }

.fx: smaller

----

# Outils de développements

* Dimension des équipements (http://screensiz.es/phone)
* Afficher différentes définitions [Responsinator](http://www.responsinator.com/) et [Responsive.is](http://responsive.is/typecast.com)
* Mesurer le temps de chargement et poids des éléments
* Équipements virtualisés : service Browserstack
* Tester sur des équipements physiques

## Autres ressources

* [HTML Shiv](https://github.com/aFarkas/html5shiv) permet d'utiliser les balises HTML5 dans IE < 9
* [Modernizr](https://modernizr.com/)
* [Polyfill](https://remysharp.com/2010/10/08/what-is-a-polyfill)

----

# Partie 4 : Frameworks

----

# Sommaire

* Découverte framework avec ou sans UI
* Étude de cas avec Bootstrap3

----

# Frameworks

## Sans UI

* [SimpleGrid](http://getsimplegrid.com/)
* [KNACSS](http://knacss.com/) par Raphaël Goetter et AlsaCreations

## Avec UI et composants animés

* [Bootstrap](http://getbootstrap.com/)
* [Foundation](http://foundation.zurb.com/)

----

# Bootstrap 3

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

## TP Bootstrap : Intégrer un design simple

Reprendre le fichier `tp-mise-en-page.html`

1.  Utilisez les classe Bootstrap pour mettre en oeuvre la grille
2.  Utiliser le HTML de bootstrap pour les éléments media, rendre les
    vignettes arrondies
3.  Utiliser le HTML pour le formulaire, rendre le bouton “envoyer” vert
    et “reset” rouge.
4.  Créer un carousel

Voir [les exemples](http://getbootstrap.com/getting-started/#examples) pour l'inspiration.

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
* Pour utiliser plus de fonctionnalités de nodejs : [nodejs.org](http://nodejs.org/)
* [Installer nodejs sous Ubuntu / debian](https://nodejs.org/en/download/package-manager/#debian-and-ubuntu-based-linux-distributions)
* [Installer nodejs à l'aide de nvm](https://github.com/creationix/nvm#install-script)

Puis installer [LessCSS](http://lesscss.org/)

    npm install -g less

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

# Autres ressources

## Outils

* [Yeoman](http://yeoman.io/)
* [HTML Shiv](https://github.com/aFarkas/html5shiv)
* [Polyfill](https://remysharp.com/2010/10/08/what-is-a-polyfill)

## Exemples de code

* [Codeopen](http://codepen.io)
* [Codedrops](http://tympanus.net/codrops/)

## Autres

* [Font Awesome](http://fortawesome.github.io/Font-Awesome/icons/)


----

# Questions ?

----

# Merci !
