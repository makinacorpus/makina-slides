
# Objectifs de la formation

  * __Les CMS et Drupal__
 * L'architecture Drupal
  * Les controles d'acces
 * Gestion du contenu
  * L'organisation du contenu
 * Les themes
  * Les fonctionnalites avancees

--------------------------------------------------------------------------------

## Définitions

  * Historique
  * Sites statiques en html, création page par page
    * fastidieux a maintenir
  * Sites dynamiques, Framework proposant des API
    * briques de base pour le code, standardisation
    * beaucoup de développement
  * CMS : Systeme de gestion de contenu
    * briques de fonctionnalites
    * pas/peu de développement

--------------------------------------------------------------------------------

## Définitions

  * Drupal : CMS + framework
    * environ 9500 modules disponibles pour Drupal 7
    * communauté active
      * [http://drupal.org][1]
      * [http://drupalfr.org/][2]
    * popularité et renommée grandissante

--------------------------------------------------------------------------------

## Installation

  * Pré-requis
    * Environnement Apache/Mysql/Php
      * Windows : Easyphp/Xampp/Wamp
      * Linux : LAMP
  * alternatives : Microsoft IIS , PostgreSQL, SQLite
  * versions :
      * Apache 1.3 ou 2.x,
      * MySQL > 4.1 (D6) ou > 5.0.15 (D7),
      * PHP > 5.2 (D6) ou > 5.3 (D7)
  * clean URL : mod_rewrite
    * [http://drupal.org/requirements][3]

--------------------------------------------------------------------------------

## Installation

  * Installation
    * Créer une base de données vide
    * Décompresser l'archive Drupal dans le répertoirerépertoire public du serveur
  * Accéder a l'application via un navigateur
  * Dérouler le processus d'installation :
      * Connexion a la BD
      * Parametrage du site et du compte admin
      * Creation et acces au site
      * Visiter Administrer > Rapports > Tableau de bord

--------------------------------------------------------------------------------

## Installation

  * Exercice
    * Via PhpMyAdmin, creer une base de données vide
    * Décompresser l'archive Drupal dans le répertoire pré-configuré du serveur
  * Accéder a l'application via un navigateur
  * Dérouler le processus d'installation

--------------------------------------------------------------------------------

## Objectifs de la formation

  * Les CMS et Drupal
  * L'architecture Drupal
  * Les contrôles d'accès
  * Gestion du contenu
  * L'organisation du contenu
  * Les thèmes
  * Les fonctionnalités avancées

--------------------------------------------------------------------------------

## Architecture fichiers

![][4]

## Modules integrés au coeur de Drupal

--------------------------------------------------------------------------------

## Choix des modules

  * Choisir le module : [http://drupal.org/project/modules][5]
  * Version courante (alpha, beta, dev, stable)
  * Utilisation
    * versions D4.7, D5, D6, D7
    * Module peu / très utilise
  * Intégration avec d'autres modules
    * Intégration future facilitée
  * Nombre de bugs ouverts
    * Vitesse de traitements des bugs
  * Incompatibilité avec des modules

--------------------------------------------------------------------------------

## Versions des modules

  * Exemple avec 7.x-2.1
    * 7.x-2.1 => Pour Drupal 7
    * 7.x-2.1 => Version majeure du module
      * Changement d'API par rapport a la 1.x
    * 7.x-2.1 => Version mineure du module
      * Bug fixing par rapport a la 2.0
  * 4 dénominations essentielles
    * Dev : module en développement
    * Alpha : module utilisable, API non figées
    * Beta : API en cours de gel
    * RC : tests finaux avant version stable

--------------------------------------------------------------------------------

## Installation de modules

  * Méthodes :
    * Décompresser dans /sites/all/modules
    * Utiliser l'interface d'installation
  * Lire le README.txt et le INSTALL.txt
  * Activer et Configurer
    * Paramètrer
    * Configurer les droits d'accès
![][6]

![][7]

--------------------------------------------------------------------------------

## Architecture interfaces

  * Structure du menu d'administration
  * Raccourcis
    * créer des raccourcis / user
![][8]

--------------------------------------------------------------------------------

## Ajout de modules

  * Exercice
  * Installer les modules Workbench modération, Views et WYSIWYG.
  * Configurer WYSIWYG.
    * librairie TinyMCE / FCK Editor / CKEditor
  * Module Media
  * Configuration > Formats de texte
  * Configuration > profils WYSIWYG

--------------------------------------------------------------------------------

## Objectifs de la formation

  * Les CMS et Drupal
  * L'architecture Drupal
  * Les contrôles d'accès
  * Gestion du contenu
  * L'organisation du contenu
  * Les thèmes
  * Les fonctionnalités avancées

--------------------------------------------------------------------------------

## Gérer les utilisateurs

  * Paramètrage de création de compte
    * Configuration > Personnes > Paramètres de compte

  * Liste des utilisateurs
    * Personnes

    * Filtres par roles/droits d'acces/statut
    * Actions en batch
  * Ajout de champs sur les utilisateurs

--------------------------------------------------------------------------------

## Droits d'accès

  * Ensemble de droits gérés par l'administrateur
    * Personnes > Droits
    * Personnes > Droits > Rôles

![][9]

--------------------------------------------------------------------------------

## Workflow

  * Workbench moderation
    * Parametrage des droits.
    * Gestion de la publication et des révisions.

![][10]

![][11]

--------------------------------------------------------------------------------

## Gérer les utilisateurs

  * Exercice
    * Créer un rôle 'Modérateur'
    * Créer un rôle 'Rédacteur'
  * Créer 2 utilisateurs et leur attribuer ces rôles
  * Parametrer les droits d'accès pour ces roles, de façon a ce que le
'redacteur' puisse creer/editer des 'pages' uniquement. Et que le moderateur
## puisse moderer ces pages.

--------------------------------------------------------------------------------

## Pour aller plus loin...

  * Content Access / ACL
    * Acces par role ou par utilisateur a 1 un contenu
  * Workbench Access
    * Acces par role ou par utilisateur a 1 rubrique

--------------------------------------------------------------------------------

## Objectifs de la formation

  * Les CMS et Drupal
  * L'architecture Drupal
  * Les controles d'acces
  * Gestion du contenu
  * L'organisation du contenu
  * Les themes
  * Les fonctionnalites avancees

--------------------------------------------------------------------------------

## Les types de contenu

  * Article / Page... Actualite / Partenaire...
  * Crees
    * Manuellement
    * Par des modules
  * Parametrages
    * Reglages des commentaires
    * Mode de publication
  * Libelle du titre
  * ...

--------------------------------------------------------------------------------

## Les types de contenu

  * Gestion des champs
    * Parametres d'affichage des champs
    * Gestion des droits
  * La gestion des images (definition de styles)
  * Modules complementaires :
    * Modules date, references...
    * Module WYSIWYG
  * Creation de noeuds (nodes)

--------------------------------------------------------------------------------

## Creation de contenu

  * > Contenu > Creer un contenu
  * Formulaire d'edition
    * Edition des champs
    * Parametrage du menu = Ajout d'un item de menu
    * Revisions
    * Informations/options de publication

--------------------------------------------------------------------------------

![][12]

## La gestion du contenu

  * Liste des contenus (noeuds)
  * > Contenu
    * Filtre par type de contenu / statut / langue
    * Actions batch
    * Filtrer la liste
  * Action en masse sur le contenu

--------------------------------------------------------------------------------

## La gestion du contenu

  * Exercice
    * Creer un type de contenu 'livre'.
    * Permettre l'affichage de commentaires

  * Champs: Titre, resume, reference, auteur.

  * Masquer la reference a l'affichage du noeud et de l'accroche.

  * Afficher le label auteur sur la meme ligne que la valeur du champ.

  * Creer au moins deux livres

--------------------------------------------------------------------------------

## Pour aller plus loin

  * Panels
  * Display suite

--------------------------------------------------------------------------------

## Objectifs de la formation

  * Les CMS et Drupal
  * L'architecture Drupal
  * Les controles d'acces
  * Gestion du contenu
  * L'organisation du contenu
  * Les themes
  * Les fonctionnalites avancees

--------------------------------------------------------------------------------

![][13]

## Les menus

  * Menus basiques
    * Menu principal
    * User menu
    * Navigation / Management
  * Creation d'un menu
    * Par l'administration
    * A la creation d'un noeud

--------------------------------------------------------------------------------

## La taxonomie

  * Categorise le contenu
    * vocabulaires (cree un champ supplementaire)
    * termes (liste des termes proposes par le champ)

  * A parametrer dans le type de contenu

  * A la creation d'un terme, creation d'une page associee
    * Affichage de la liste des contenus associes a un terme
> Structure > Taxonomie

--------------------------------------------------------------------------------

## La gestion des blocs

  * Les regions d'un theme
  * Creation de blocs :
    * Par des modules
    * Manuellement
    * Views
  * Parametres d'affichage:
    * Par role,
    * Type de contenu,
    * URL

--------------------------------------------------------------------------------

![][14]

## La gestion des blocs

  * Structure > Blocs
    * Choix du theme
    * Ordonner les blocs
  * Attribution a une region par la liste de selection
  * Modifier l'ordre par glisser/deposer

--------------------------------------------------------------------------------

## La gestion des blocs

  * Configuration d'un bloc :
    * Choix du positionnement pour chaque theme actif
    * Parametres d'affichage:
      * Par role,
      * Type de contenu,
      * URL

![][15]

![][16]

--------------------------------------------------------------------------------

## L'organisation du contenu

  * Exercice
    * Definir un vocabulaire ('Genre') et rajouter des termes ('Science
## Fiction', 'Policier'...)
  * L'appliquer au type de contenu 'livre' et categoriser les livres crees
## precedemment
  * Creer un item de menu (menu principal) pour chaque terme cree
  * Creer un bloc 'A la une' avec un texte decrivant un livre. Afficher
## uniquement sur la page d'accueil dans la region de droite.

--------------------------------------------------------------------------------

## Les vues (views)

  * Listing de contenu
  * 2 etapes :
    * Recuperation et filtrage des donnees
    * Choix du plug-in d'affichage

--------------------------------------------------------------------------------

## Les vues

  * Interface simplifiee
  
![][17]

--------------------------------------------------------------------------------

## Les vues

  * Champs
    * Donnees a afficher
  * Filtrer les donnees
    * Type de contenu, Taxonomie...
  * Filtre expose
  * Ordre de tri
    * date de publication, titre...
  * Relations
    * jointures sql
  * Filtres contextuels
    * Ajout d'un filtre dynamique dans l'URL

--------------------------------------------------------------------------------

## Les vues

  * Gestion de l'affichage
    * Style = mise en forme
  * Style de ligne = Donnees a afficher
  * Nombre d'element a afficher
  * pagination
  * messages d'en-tete / pied de page / texte de page vide
  * Mode d'affichage
    * Page
  * Bloc
  * Flux RSS
  * ''Fichier attache''

--------------------------------------------------------------------------------

## L'organisation du contenu

  * Exercice
    * Ajouter une case a cocher 'Mettre a la une' au type de contenu
'livre'.
  * Pour un des livres enregistres, cocher la case
  * Afficher un bloc qui affiche le livre dont la case 'Mettre a la une' est
## cochee sur toutes les pages du site.

--------------------------------------------------------------------------------

## L'organisation du contenu

  * Exercice
    * Creer une vue permettant de voir la liste des livres sous forme de
tableau
  * Affichage du titre, de l'auteur, du genre, d'un lien de visualisation,
d'edition et de suppression.
  * Tri sur le titre et filtre expose sur le genre
  * Creer un menu ''Tous les livres'' vers cette page

--------------------------------------------------------------------------------

## Objectifs de la formation

  * Les CMS et Drupal
  * L'architecture Drupal
  * Les controles d'acces
  * Gestion du contenu
  * L'organisation du contenu
  * Les themes
  * Les fonctionnalites avancees

--------------------------------------------------------------------------------

## Les themes

  * Habillage graphique front-office et back-office
    * [http://drupal.org/project/themes][18]
  * Dans sites/all/themes/
    * > Apparence
  * Parametrage

--------------------------------------------------------------------------------

## Les themes

  * Creation d'un theme
    * Utiliser un « starter » theme :
      * Zen (zenophile)
      * Blueprint
      * Genesis
      * Gain de temps
    * Classes CSS pre-existantes
    * Documentation
    * Reutilisabilite

--------------------------------------------------------------------------------

## Les themes

  * Templates
    * page.tpl.php, node.tpl.php, block.tpl.php
    * page-front.tpl.php, node-story.tpl.php, node-18.tpl.php
    * views-views--<nom de la vue>.tpl.php
    * views-view-field--<nom du champ>.tpl.php

## Exercice
    * Installer le theme rubik

--------------------------------------------------------------------------------

## L'organisation du contenu

  * Exercice recapitulatif
    * Creer un type de contenu auteur : nom, presentation, photo (image)
    * Ajouter une reference (references) vers l'auteur dans le type de contenu
''Livre''
  * Faire une vue qui affiche la bibliographie de l'auteur (bloc dans les
contenus ''auteur'')
  * Faire une vue page qui affiche un slideshow (views slideshow) des 5
derniers livres publies. En en-tete, mettre un message de bienvenue. Definir
cette page comme page d'accueil.
  * Faire une vue de recherche des livres.

--------------------------------------------------------------------------------

## Objectifs de la formation

  * Les CMS et Drupal
  * L'architecture Drupal
  * Les controles d'acces
  * Gestion du contenu
  * L'organisation du contenu
  * Les themes
  * Les fonctionnalites avancees
  *  Modules du coeur (aggregator, poll, search)
    * Autres contenus (videos, newsletters, formulaires)
    * Referencement (urls, meta-tags, sitemap.xml)
    * Fonctionnalites de contenu (multilinguisme, panels, display suite)
    * Administration (Mises a jour, Multi-sites, sauvegarde, cron, ldap,
performance, architecture)


   [1]: http://drupal.org/

   [2]: http://drupalfr.org/

   [3]: http://drupal.org/requirements

   [4]: img/archi_fichiers.png

   [5]: http://drupal.org/project/modules

   [6]: img/navigation.png

   [7]: img/modules.png

   [8]: img/raccourcis.png

   [9]: img/permissions.png

   [10]: img/workbench.png

   [11]: img/revisions.png

   [12]: img/contenu.png

   [13]: img/menu.png

   [14]: img/regions.png

   [15]: img/block.png

   [16]: img/visibilite.png

   [17]: img/views.png

   [18]: http://drupal.org/project/themes

