# HTML5 / CSS3

 22-23 Septembre 2014
 CNFPT

----

# Jour 1 : HTML5 / CSS3

1. Introduction à HTML5 (nouveau Doctype, nouveaux éléments sémantiques, audio, video, canvas, géolocalisation, drag and drop, localstorage)
2. Introduction à CSS3 (propriétés, sélecteurs, préfixes, médias, transitions, transformations, Internet Explorer)
3. Syntaxe, préfixes et usages CSS3
4. Valeurs, fonctions et unités
5. La gestion des médias avec Media-Queries
6. Propriétés de texte et de contenu
7. Propriétés décoratives CSS3
8. Le positionnement en CSS3
9. La sélection d'éléments en CSS3
10. Les transformations
11. Les transitions et animations 

----

# Jour 2 : Bootstrap, LessCSS

## BOOTSTRAP 3

* installer Bootstrap
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

* URL
* HTML
* HTTP

## le W3C

**World Wide Web Consortium**, dirigé par *Tim Berners Lee*

* **389** membres (au 15 septembre 2014)
* Définit les spécifications (HTML, XML, accessibilité, mobile)
* Groupes de travail

[w3.org/Consortium](http://www.w3.org/Consortium/)

.fx: larger

----

## Historique

* 1989 : début des travaux de *Tim Berners Lee*, chercheur au CERN, et son équipe
* 1991 : *Tim Berners Lee* rend le projet **WorldWideWeb** public
* 1993 : création du navigateur **Mosaic**, qui intègre également les images
* 1994 : création du **W3C** par *Tim Berners Lee*
* 1996 : implémentation de **CSS1.0** par **IE**
* 1998 : publication des spécifications **CSS 2.0**
* 1999 : spécifications **HTML4.01**, et début des travaux sur **CSS3**
* 2000 : publication des spécifications pour **XHTML1**. 
* 2006 : publication des recommandations de **XHTML2.0**

Scission au sein du W3C : le **WhatWG** (Web Hypertext Application Technology Working Group) travaille sur un autre standard pour le **HTML**

* 2008 : "First Public Working Draft" du **HTML5** présentée par le **WHATWG**
* 2012 : **HTML5** passe en "Candidate Recommandation"

[fr.wikipedia.org/wiki/World_Wide_Web](http://fr.wikipedia.org/wiki/World_Wide_Web)

.fx: smaller

----

# Les outils de développement

* Éditeur de code : Notepad++, Sublime Text
* Navigateur : éviter IE !! Firefox ou Chrome, et leurs plugins d'inspection de code
* Test et validation [validator.w3.org](http://validator.w3.org/)
* Voir aussi [opquast.com](http://opquast.com/fr/) pour la qualité du code, l'accessibilité

.fx: larger

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
* localstorage

----

## Le HTML 5 est-il prêt ?

* En "Candidate Recommandation" depuis 2012
* Implémentation variable selon les navigateurs : voir [caniuse.com](http://caniuse.com/)
* Compatible avec IE9, du moins en partie, des outils permettent une "régression en douceur" (graceful regression)

## DocType

`<!DOCTYPE html>`

... tout simplement

----

# Sémantique

## Balises

* Section : `<article>`, `<aside>`, `<nav>`, `<section>`, `<header>`, `<footer>`
* Grouper : `<figure>`, `<figcaption>`

Voir [tinytypo.tetue.net](http://tinytypo.tetue.net/tinytypo.html)

## Microdatas

voir [schema.org](http://schema.org/docs/gs.html)

Autres implémentations : microformats, RDFa

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

----

# Éléments embarqués

## `<audio>` et `<video>`

    <audio id="musique" controls>
        <source src="donjon-episode31.ogg"></source>
        <source src="donjon-crom.mp3"></source>
    </audio>

Les limites : 

* format de fichiers différents selon les navigateurs

----

# CANVAS et SVG

* canvas vs. svg
* web gl
* flash n’est pas mort

----

# Application web en HTML5

## Stockage

* App Cache
* LOCALSTORAGE
* INDEXED DB
* Limites & USAGES


## File API


## Server-Sent Events

* Web Sockets

## Threads et requests

* WEB workers
* XMLHTTPREQUEST 2

----

# Partie 2 : CSS3

----

# Mise en forme

## Propriétés

* `background-size`, `border-radius`, `box-shadow`, `opacity`, 
* dégradés
* arrière-plan multiples
* transparence pour la couleur de fond

[css3generator.com](http://css3generator.com/)

----

## Sélecteurs

### Sélecteurs CSS2 maintenant implémentés :

par attribut

    a[attribut~="valeur"]

par élément fils direct

    a > b

par élément frère

    a + b

----

### Sélecteurs CSS3

par attribut

    a[attribut^="valeur"]

par fils premier, dernier ou tous les x éléments

    a:first-child
    a:last-child
    a:nth-child(expression)

négation

    a:not(.class)

première lettre, première ligne

    ::first-letter
    ::first-line

----

* Un tutoriel : [flukeout.github.io](http://flukeout.github.io/)
* La documentation officielle : [www.w3.org/TR/selectors](http://www.w3.org/TR/selectors/)

----

# Grid Layout

flexbox

----

## Font-Face

[fontsquirrel.com](http://www.fontsquirrel.com/)

----

# Media-queries

Le responsive webdesign en image
Orientation et Localisation
Device api

----

# CSS animé

## Transitions / Animations

## Transformations

## Extensions spécifiques des navigateurs

---- 

# Partie 3 : Bootstrap 3

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


# Partie 4 : LessCSS

----

## Sommaire

* variables
* imbrication de code
* mixins
* importation de fichier

## Installer LessCSS

* Dans windows : [winless.org](http://winless.org/)
* Pour utiliser plus de fonctionnalités de nodejs : [nodejs.org](http://nodejs.org/download/)

----

# Les bases

## variables

    @nice-blue: #5B83AD;
    @light-blue: @nice-blue + #111;

    #header {
      color: @light-blue;
    }

Résultat :

    #header {
      color: #6c94be;
    }

## imbrication de code

----

# mixins et fonctions


----

# importation de fichier

----

# TP : un thème avec LessCSS et Bootstrap

----

# Questions ?
