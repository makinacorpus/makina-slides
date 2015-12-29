
# Formation Administration Drupal 8

--------------------------------------------------------------------------------

# Objectifs de la formation

  * __Les CMS et Drupal__
  * L'architecture de Drupal
  * Les contrôles d'accès
  * Gestion du contenu
  * L'organisation du contenu
  * Les thèmes
  * Les fonctionnalités avancées

.fx: progress

--------------------------------------------------------------------------------

# Historique

  * Sites statiques en HTML, création page par page
    * fastidieux à maintenir
  * Sites dynamiques, Framework proposant des API
    * briques de base pour le code, standardisation
    * beaucoup de développement
  * CMS : Système de gestion de contenu
    * briques de fonctionnalités
    * pas/peu de développement

--------------------------------------------------------------------------------

# Quelques autres CMS

  * Wordpress
    * grande communauté
    * nombreux plugins et thèmes
    * qualité/sécurité du code laisse à désirer hors du cœur
    * pratique pour les projets statiques/légers

![][19]

--------------------------------------------------------------------------------

# Quelques autres CMS

  * Joomla
    * plugins nombreux mais peu maintenus / payants
    * communauté moindre

![][20]

--------------------------------------------------------------------------------

# Définitions

> Content Management Framework

## Drupal = CMS + framework

  * de très nombreux modules disponibles
  * communauté active ([http://drupal.org][1] & [http://drupalfr.org][2])
  * popularité et renommée grandissante
  * une version 8 entièrement réécrite

![][21]

--------------------------------------------------------------------------------

# Quelques références mondiales

  * Whitehouse.gov
  * Tesla
  * Washington Post
  * Twitter, LinkedIn, Nvidia developer Documentation
  * Economist.com
  * Harvard community
  * Stanford school
  * Grammy.com
  * Amnesty.org
  * Danone

--------------------------------------------------------------------------------

# Quelques références françaises

  * Guerlain
  * McDonalds
  * Cartier
  * Gouvernement.fr / Senat.fr / Sites des ministères
  * SNCF
  * Eurostar
  * Orange Business Services
  * Rue89
  * Le Figaro

--------------------------------------------------------------------------------

# Installation

  * Pré-requis
    * Environnement Apache/Mysql/Php
      * Windows : Easyphp/Xampp/Wamp
      * Linux : LAMP
  * alternatives : Nginx, Microsoft IIS, PostgreSQL, SQLite
  * versions :
      * Apache 2.x (avec mod_rewrite)
      * MySQL > 5.5.3
      * PHP > 5.5.9
  * [http://drupal.org/requirements][3]

--------------------------------------------------------------------------------

# Installation

  * Créer une base de données vide
  * Décompresser l'archive Drupal dans le répertoire serveur
  * Accéder à l'application via un navigateur
  * Dérouler le processus d'installation :
    * Connexion à la BD
    * Paramètrage du site et du compte admin
    * Création et accès au site
    * Visiter Administrer > Rapports > Tableau de bord

--------------------------------------------------------------------------------

# Installation - Exercice

  * Via PhpMyAdmin, créer une base de données vide
  * Décompresser l'archive Drupal dans le répertoire pré-configuré du serveur
  * Accéder à l'application via un navigateur
  * Dérouler le processus d'installation

![][22]

.fx: tp

--------------------------------------------------------------------------------

# Objectifs de la formation

  * Les CMS et Drupal
  * __L'architecture de Drupal__
  * Les contrôles d'accès
  * Gestion du contenu
  * L'organisation du contenu
  * Les thèmes
  * Les fonctionnalités avancées

.fx: progress

--------------------------------------------------------------------------------

# Architecture fichiers

<img src="img/archi_fichiers8.png" style="float:left;padding:0 1em"/>

Cœur de Drupal
<br>
Modules communs à tous les sites
<br><br><br>
Répertoire d'upload par défaut
<br>
Fichiers de configuration
<br><br><br><br><br><br><br>
Thèmes communs à tous les sites

--------------------------------------------------------------------------------

# Principales fonctionnalités - Modules du core

  * _System, User_ -> prérequis
  * _Node, cKEditor, Field, Comment_ -> création de contenu
  * _Menu, Block, Taxonomy_ -> structuration
  * _Toolbar, Shortcut, Color, Contextual, Quick Edit_ -> interface
  * _Book, Forum_ -> Types de contenus avancés
  * _Contact, Aggregator, Activity Tracker, Update_ -> fonctions spécifiques
  * _Path, RDF_ -> SEO
  * _Migrate_ -> gestion de migration d'autres systèmes (nouveauté D8)
  * _Views_ -> listes de données (nouveauté D8)
  * Section _Field types_ -> types de champs
  * Section _Multilingual_ -> traduction (nouveauté D8)
  * Section _Web services_ -> services web (nouveauté D8)

> Drupal sans ses modules contrib ne permet que de faire des sites simples.

--------------------------------------------------------------------------------

# Choix des modules

  * Choisir le module : [http://drupal.org/project/modules][5]
  * Version courante (alpha, beta, dev, stable)
  * Utilisation
    * versions D5, D6, D7, D8
    * Module peu / très utilisé
  * Intégration avec d'autres modules
    * Intégration future facilitée
  * Nombre de bugs ouverts
    * Vitesse de traitements des bugs
  * Incompatibilité avec des modules

> [http://simplytest.me](http://simplytest.me) pour tester le core ou ses modules rapidement

--------------------------------------------------------------------------------

# Versions des modules

  * Exemple avec 8.x-2.1
    * 8.x-2.1 => Pour Drupal 8
    * 8.x-2.1 => Version majeure du module
      * Changement d'API par rapport à la 1.x
    * 8.x-2.1 => Version mineure du module
      * Bug fixing par rapport à la 2.0
  * 4 dénominations essentielles
    * Dev : module en développement
    * Alpha : module utilisable, API non figées
    * Beta : API en cours de gel
    * RC : tests finaux avant version stable

--------------------------------------------------------------------------------

# Installation de modules

  * Méthodes : ![][6]
    * Décompresser dans /modules
    * Utiliser l'interface d'installation
  * Lire le README.txt et le INSTALL.txt
  * Activer et Configurer
    * Paramètrer
    * Configurer les droits d'accès

![][7]

--------------------------------------------------------------------------------

# Architecture des interfaces

  * Structure du menu d'administration
  * Raccourcis
    * créer des raccourcis /user

![][8]

--------------------------------------------------------------------------------

# Exercice

  * Installer le module Devel

.fx: tp

--------------------------------------------------------------------------------

# Objectifs de la formation

  * Les CMS et Drupal
  * L'architecture de Drupal
  * __Les contrôles d'accès__
  * Gestion du contenu
  * L'organisation du contenu
  * Les thèmes
  * Les fonctionnalités avancées

.fx: progress

--------------------------------------------------------------------------------

# Gérer les utilisateurs

  * Paramètrage de création de compte
    * Configuration > Personnes > Paramètres de compte
  * Liste des utilisateurs
    * Personnes
    * Filtres par rôles/droits d'accès/statut
    * Actions en batch
  * Ajout de champs sur les utilisateurs

--------------------------------------------------------------------------------

# Droits d'accès

  * Ensemble de droits gérés par l'administrateur
    * Personnes > Droits
    * Personnes > Rôles

![][9]

--------------------------------------------------------------------------------

# Workflow

  * Prévu pour la 8.1 (via le module Drafty)
  * Plusieurs modules disponibles en attendant
    * Workflow (-beta)
    * Workbench moderation (-dev)
    * Multiversion ?

--------------------------------------------------------------------------------

# Gérer les utilisateurs - Exercice

  * Créer un rôle 'Modérateur'
  * Créer un rôle 'Rédacteur'
  * Créer 2 utilisateurs et leur attribuer ces rôles
  * Paramètrer les droits d'accès pour ces rôles, de façon a ce que le
'rédacteur' puisse créer/éditer des 'pages' uniquement. Et que le modérateur
puisse modérer ces pages.

.fx: tp larger

--------------------------------------------------------------------------------

# Pour aller plus loin...

  * Modules de la communauté
    * Content Access

  * Reconstruction des droits d'accès

--------------------------------------------------------------------------------

# Objectifs de la formation

  * Les CMS et Drupal
  * L'architecture de Drupal
  * Les contrôles d'accès
  * __Gestion du contenu__
  * L'organisation du contenu
  * Les thèmes
  * Les fonctionnalités avancées

.fx: progress

--------------------------------------------------------------------------------

# Les types de contenu

  * Article / Page... Actualité / Partenaire...
  * Créés
    * Manuellement
    * Par des modules
  * Paramètres
    * Options de publication (Publié, Épinglé, Promu en page d'accueil)
  * Libellé du titre

--------------------------------------------------------------------------------

# Les types de contenu

  * Gestion des champs
    * Paramètres d'affichage des champs
    * Gestion des droits

  * La gestion des images (définition de styles)

  * La gestion des commentaires

  * Compléments :
    * Installer de nouveaux champs : date, références...
    * Voir la configuration de cKEditor

  * Création de nœuds (nodes)

--------------------------------------------------------------------------------

# Création de contenu

  * Contenu > Créer un contenu

  * Formulaire d'édition
    * Edition des champs
    * Paramètrage du menu = Ajout d'un item de menu
    * Révisions
    * Informations/options de publication

--------------------------------------------------------------------------------

# La gestion du contenu

  * Liste des contenus (nœuds)
    * Filtre par type de contenu / statut / langue
    * Actions batch
    * Filtrer la liste

  * Action en masse sur le contenu

--------------------------------------------------------------------------------

# La gestion du contenu - Exercice

  * Créer un type de contenu 'livre'.
  * Permettre l'affichage de commentaires
  * Champs: Titre, résumé, référence, auteur.
  * Masquer la référence à l'affichage du nœud et de l'accroche.
  * Afficher le label auteur sur la même ligne que la valeur du champ.
  * Créer au moins deux livres

.fx: tp

--------------------------------------------------------------------------------

# Les modes d'affichage

  * Définissent si un champ doit apparaitre et comment il doit apparaitre
  (via un de ses formatter)
  * Les modes d'affichages sont fournis par les modules
  * Drupal Core
    * _Par défaut_
    * Full
    * Teaser
    * RSS
    * Résultat de recherche
  * Créer de nouveaux modes

> Si le mode d'affichage n'est pas défini pour un type de contenu, celui par défaut sera pris en compte

--------------------------------------------------------------------------------

# Les modes de formulaire (nouveauté Drupal 8)

  * Définissent si un champ doit apparaitre
  * Fonctionnent comme pour l'affichage

--------------------------------------------------------------------------------

# Panels (pas encore prêt)

  * Permet de structurer les nœuds et les contenus entre eux
  * En fonction de condition
  * Interface complexe
  * Peut vite devenir une "usine à gaz"
  * Préférable de ne pas penser à Panels tout de suite

![][23]

--------------------------------------------------------------------------------

# Display suite

  * structurer les champs dans un nœud

![][24]

--------------------------------------------------------------------------------

# Exercices Display Suite

  * Créer plusieurs displays pour le livre
    * 2 colonnes (image seule à gauche & tout à droite)
    * 2 colonnes (tout à gauche & body à droite)

.fx: tp

--------------------------------------------------------------------------------

# Objectifs de la formation

  * Les CMS et Drupal
  * L'architecture de Drupal
  * Les contrôles d'accès
  * Gestion du contenu
  * __L'organisation du contenu__
  * Les thèmes
  * Les fonctionnalités avancées

.fx: progress

--------------------------------------------------------------------------------

# La taxonomie

  * Catégorise le contenu
    * notion de vocabulaire
    * termes de taxonomie
  * Possibilité de créer plusieurs vocabulaires, qui peuvent être partagés par
  plusieurs types de contenu

![][25]

--------------------------------------------------------------------------------

# La taxonomie

  * Attacher un ou plusieurs vocabulaires via un champ à paramètrer dans
  le type de contenu
  * À la création d'un terme, création d'une page associée qui affiche la
  liste des contenus associes à un terme
  * Possibilité de créer des termes à la volée (tagging)
  * Ou de choisir parmi un liste définie (selection)

![][26]

--------------------------------------------------------------------------------

# L'organisation du contenu - Exercice

  * Définir un vocabulaire ('Genre') et rajouter des termes ('Science
Fiction', 'Policier'...)
  * L'appliquer au type de contenu 'livre' et catégoriser les livres crées
précédemment
  * Créer un item de menu (menu principal) pour chaque terme crée
  * Créer un bloc 'À la une' avec un texte décrivant un livre. Afficher
uniquement sur la page d'accueil dans la région de droite.

.fx: tp

--------------------------------------------------------------------------------

# Les menus

  * Menus basiques
    * Menu principal
    * User menu
    * Tools / Administration
    * Footer
  * Possibilité de créer des menus personnalisés
  * Chaque menu crée un bloc correspondant

![][13]

--------------------------------------------------------------------------------

# Les menus

  * Création d'un élément de menu
    * Par l'administration
    * À la création d'un nœud
  * Possibilité de désactiver les éléments de menu
  * Possibilité de hierarchiser les éléments de menu
  * Création de séparateurs ou d'éléments sans lien -> _Special Menu Items_ (pas encore en D8)
  * Synchronisation entre une taxnomie et un menu -> _Taxonomy Menu_ (pas encore en D8)

<br><br><br><br>
> Les éléments de menus sont affichés à l'utilisateur seulement s'il a les
permissions d'accèder à sa cible

--------------------------------------------------------------------------------

# Les menus - Exercice

  * Installer le module _Nice menus_
  * Ajouter quelques liens externes et internes
  * Organiser entre parents et enfants

_La suite après les blocs_

.fx: tp

--------------------------------------------------------------------------------

# La gestion des blocs

  * Les régions d'un thème
  * Création de blocs :
    * Par des modules
    * Manuellement
    * Views
  * Paramètres d'affichage:
    * Par rôle,
    * Type de contenu,
    * URL

--------------------------------------------------------------------------------

# La gestion des blocs

  * Structure > Blocs
    * Choix du thème
    * Ordonner les blocs
  * Attribution a une région par la liste de sélection
  * Modifier l'ordre par glisser/déposer

![][14]

--------------------------------------------------------------------------------

# La gestion des blocs - Configuration

  * Choix du positionnement pour chaque thème actif
  * Paramètres d'affichage:
    * Par rôle,
    * Type de contenu,
    * URL

![][16]

--------------------------------------------------------------------------------

# La gestion des blocs - Exercice

  * Placer notre Nice menu principal en sidebar
    * Seulement pour autres pages que la page d'accueil

  * Afficher qui est connecté pour les utilisateurs connectés dans le footer

  * Afficher le bloc RSS sur les contenus

.fx: tp

--------------------------------------------------------------------------------

# La gestion des blocs - Types de blocs

  * Comme les types de contenu, il y a des types de blocs
    * Blocs de publicité, bloc vidéo, ...

--------------------------------------------------------------------------------

# Les vues (views)

  * Listing de contenu

  * 2 étapes :
    * Récupération et filtrage des données
    * Choix du plug-in d'affichage

  * Permet de créer bloc, pages, RSS, excel, JSON, cartes, etc.

  * Les modules peuvent fournir des vues par défaut (ex: _Le cœur_)

--------------------------------------------------------------------------------

# Les vues

  * Interface simplifiée
  
![][17]

--------------------------------------------------------------------------------

# Les vues

  * Champs
    * Données a afficher
  * Filtrer les données
    * Type de contenu, Taxonomie...
  * Filtre exposé
  * Ordre de tri
    * date de publication, titre...
  * Relations
    * jointures sql
  * Filtres contextuels
    * Ajout d'un filtre dynamique dans l'URL

--------------------------------------------------------------------------------

# Les vues

  * Gestion de l'affichage
    * Style = mise en forme
  * Style de ligne = Données a afficher
  * Nombre d'élément a afficher
  * pagination
  * messages d'en-tête / pied de page / texte de page vide
  * Mode d'affichage
    * Page
    * Bloc
    * Flux RSS
    * ''Fichier attaché''

--------------------------------------------------------------------------------

# L'organisation du contenu - Exercice

  * Bloc
    * Pour un des livres enregistrés, cocher la case 'Promu en page d'accueil'
    * Afficher un bloc qui affiche le livre dont la case 'Promu en page 
d'accueil' est cochée sur toutes les pages du site


  * Page
    * Créer une vue permettant de voir la liste des livres sous forme de
  tableau
    * Affichage du titre, de l'auteur, du genre, d'un lien de visualisation,
  d'édition et de suppression.
    * Tri sur le titre et filtre expose sur le genre
    * Créer un menu ''Tous les livres'' vers cette page

.fx: tp

--------------------------------------------------------------------------------

# Objectifs de la formation

  * Les CMS et Drupal
  * L'architecture de Drupal
  * Les contrôles d'accès
  * Gestion du contenu
  * L'organisation du contenu
  * __Les thèmes__
  * Créer une vue permettant de voir la liste des livres sous forme de

.fx: progress

--------------------------------------------------------------------------------

# Les thèmes

  * Habillage graphique front-office et back-office
    * [http://drupal.org/project/themes][18]
  * Dans /themes
  * Paramètrage différent selon le thème
  * Possible intégration avec le module color
  * Chaque thème ajoute son propre CSS avec celui des modules et surcharge les
  templates par défaut des modules grâce aux suggestions

--------------------------------------------------------------------------------

# Les thèmes

  * Création d'un thème
  * Utiliser un « starter » thème
    * Aucun existant en D8 pour le moment
    * Gain de temps
    * Classes CSS préexistantes
    * Documentation
    * Réutilisabilité

--------------------------------------------------------------------------------

# Les thèmes

  * Templates
    * html.html.twig, page.html.twig, node.html.twig, block.html.twig
    * page-front.html.twig, node-blog.html.twig, node-18.html.twig
    * views-views--{nom de la vue}.html.twig
    * views-view-field--{nom du champ}.html.twig

# Exercice

  * Installer le thème Adminimal

--------------------------------------------------------------------------------

# L'organisation du contenu - Exercice récapitulatif

  * Créer un type de contenu auteur : nom, présentation, photo (image)
  * Ajouter une référence (references) vers l'auteur dans le type de contenu
''Livre''
  * Faire une vue qui affiche la bibliographie de l'auteur (bloc dans les
contenus ''auteur'')
  * Faire une vue page qui affiche un slideshow (views slideshow) des 5
derniers livres publies. En en-tête, mettre un message de bienvenue. Définir
cette page comme page d'accueil.
  * Faire une vue de recherche des livres.

.fx: tp

--------------------------------------------------------------------------------

# Objectifs de la formation

  * Les CMS et Drupal
  * L'architecture de Drupal
  * Les contrôles d'accès
  * Gestion du contenu
  * L'organisation du contenu
  * Les thèmes
  * __Les fonctionnalités avancées__


.fx: progress


   [1]: http://drupal.org/

   [2]: http://drupalfr.org/

   [3]: http://drupal.org/requirements

   [5]: http://drupal.org/project/modules

   [6]: img/navigation8.png

   [7]: img/modules8.png

   [8]: img/raccourcis8.png

   [9]: img/permissions8.png

   [13]: img/menu8.png

   [14]: img/regions8.png

   [16]: img/visibilite8.png

   [17]: img/views8.png

   [18]: http://drupal.org/project/themes

   [19]: img/wordpress-logo.png

   [20]: img/joomla-logo.png

   [21]: img/druplicon-logo.png

   [22]: img/installed8.png

   [23]: img/panels.png

   [24]: img/ds.jpg

   [25]: img/taxonomy8.png

   [26]: img/taxonomy_field8.png


