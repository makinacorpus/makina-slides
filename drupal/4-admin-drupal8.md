
# Formation Administration Drupal 8

--------------------------------------------------------------------------------

# Qui êtes-vous ?

# Que savez-vous de Drupal ?

# Comment vous sentez-vous ?

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

--------------------------------------------------------------------------------

# Installation

  * Pré-requis
    * Environnement Apache/Mysql/Php
      * Windows : Easyphp/Xampp/Wamp -> Acquia Dev Desktop plus intégré
      * Linux : LAMP
  * alternatives : Nginx (ou Microsoft IIS), PostgreSQL, SQLite (ou Oracle, MSSQL)
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

  * Dérouler le processus d'installation

![][22]

.fx: tp

--------------------------------------------------------------------------------

# Sélection de la langue

![][28]

--------------------------------------------------------------------------------

# Profil d'installation

![][29]

--------------------------------------------------------------------------------

# Configuration de la base de données

![][30]

--------------------------------------------------------------------------------

# Installation de modules

![][31]

--------------------------------------------------------------------------------

# Configuration du site

![][32]

--------------------------------------------------------------------------------

# Compte administateur

![][33]

--------------------------------------------------------------------------------

# Paramètres régionaux

![][34]

--------------------------------------------------------------------------------

# Vérification automatique des mises à jour

![][35]

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
<small>
Cœur de Drupal
<br>
Modules communs à tous les sites
<br>
Répertoire d'upload par défaut
<br><br>
Fichiers de configuration
<br><br><br>
Thèmes communs à tous les sites</small>

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
    * Utiliser la ligne de commande
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

  * Installer le module Pathauto

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

# Gérer les utilisateurs - Exercice

  * Créer un rôle 'Modérateur'
  * Créer un rôle 'Rédacteur'
  * Créer 2 utilisateurs (1 pour chaque rôle)
  * Paramètrer les droits d'accès pour ces rôles, de façon a ce que le 'rédacteur' puisse créer/éditer des 'articles' uniquement. Et que le modérateur puisse modérer ces articles.

.fx: tp larger

--------------------------------------------------------------------------------

# Workflow

  * Un workflow très simple dans le cœur (Brouillon / Publié)
    * MAIS pas de permission spécifique

  * Content moderation
    * Gestion de workflow complète

![][36]

--------------------------------------------------------------------------------

# Workflow

  * Content moderation
    * Création de nouveaux états et de nouvelles transitions

![][37]

--------------------------------------------------------------------------------

# Gérer les utilisateurs - Exercice 2

  * Refaites l'exercice précédent avec le module "Content Modération"
  * Vérifier que vous pouvez supprimer les droits d'aministration donnés
  précédemment

.fx: tp larger

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

  * Structure > Types de contenu

  * Gestion des champs
    * Paramètres d'affichage des champs

  * La gestion des images (Configuration > Styles d'images)

  * La gestion des commentaires (attention au type de commentaire)

  * Compléments :
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

  * Créer un type de contenu 'livre'
  * Permettre l'affichage de commentaires
  * Champs: Titre, résumé, référence (ISBN), auteur, couverture
  * Masquer la référence (ISBN) à l'affichage du nœud et de l'accroche
  * Afficher le label de l'auteur sur la même ligne que la valeur du champ
  * Créer au moins deux livres
  * Utiliser un style d'image pour uniformiser l'affichage

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
  * MAIS
    * Aucun moyen de les utiliser avec seulement le core
    * Voir le module
  [Form Mode Manager](https://www.drupal.org/project/form_mode_manager)

--------------------------------------------------------------------------------

# Mise en page des contenus (nouveauté Drupal 8)

  * Permettent d'organiser le contenu dans la page
  * _Uniquement_ pour la zone de contenu

<iframe width="560" height="315" src="https://www.youtube.com/embed/Hx4EEzI7aNE" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

--------------------------------------------------------------------------------

# Pour aller plus loin

  * [Layout Builder Restrictions](https://www.drupal.org/project/layout_builder_restrictions)
  * [Layout Builder Everywhere](https://www.drupal.org/project/lb_everywhere)
  * [Layout Builder UX](https://www.drupal.org/project/lb_ux)

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
  * Créer un type de bloc "Livre à la une", avec uniquement un champ
"Entity Référence" vers un livre, et afficher ce bloc uniquement sur la page
d'accueil dans la région de droite.

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
  * Création d'éléments sans lien -> Dans le cœur en 8.2 (novembre 2016)
  * Synchronisation entre une taxnomie et un menu -> _Taxonomy Menu_
  * Ajout d'attributs ('target', ...) : _Link Attributes widget_

<br><br><br><br>
> Les éléments de menus sont affichés à l'utilisateur seulement s'il a les
permissions d'accèder à sa cible

--------------------------------------------------------------------------------

# Les menus - Exercice

  * Mettre en place le menu principal du site avec des liens vers nos livres
  * Ajouter une page "Mentions légales" dans le pied de page
  * Ajouter un lien "Se connecter" dans le pied de page

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
  * Placer des blocs dans des régions
  * En Drupal 8, TOUT est bloc (logo, fil d'Ariane, ...)

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

  * Créer un bloc "Horaires" placer sur la barre de droite
    * Seulement pour la page d'accueil

  * Afficher qui est connecté pour les utilisateurs connectés dans le footer

  * Afficher le bloc RSS sur les contenus

.fx: tp

--------------------------------------------------------------------------------

# La gestion des blocs - Types de blocs

  * Comme les types de contenu, on peut créer des "types" de blocs
    * Blocs de publicité, bloc vidéo, ...
  * Attention, pour le moment, pas de permissions spécifiques
    
![][27]

--------------------------------------------------------------------------------

# La gestion des blocs - Exercice

  * Créer un nouveau type de bloc "à la une"
  * Ajouter un champ "Référence à un contenu"
  * Créer une instance de ce bloc en sélectionnant un livre créé précédemment
  * Positionner ce bloc en haut de la page de gauche de la page d'accueil

.fx: tp

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


  * En bonus
    * Installer le module _Better Exposed Filters_ pour masquer le bouton de
    soumission du formulaire de filtres exposés

.fx: tp

--------------------------------------------------------------------------------

# L'organisation du contenu - Exercice récapitulatif

  * Créer un type de contenu auteur : nom, biographie, photo (image)
  * Ajouter une référence vers l'auteur dans le type de contenu ''Livre''
  * Faire une vue qui affiche la bibliographie de l'auteur (bloc dans les
contenus ''auteur'')
    * Indice : utiliser les filtres contextuels
  * Faire une vue page qui affiche un slideshow (en installant le module
_views slideshow_) des 5 derniers livres publies. En en-tête, mettre un message
de bienvenue. Définir cette page comme page d'accueil.
  * Faire une vue de recherche des livres.

.fx: tp

--------------------------------------------------------------------------------

# Objectifs de la formation

  * Les CMS et Drupal
  * L'architecture de Drupal
  * Les contrôles d'accès
  * Gestion du contenu
  * L'organisation du contenu
  * __Les thèmes__
  * Les fonctionnalités avancées

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
    * Exemple: Zen, Bootstrap, Omega
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
  * Installer le thème Writer

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

   [21]: img/drupal-logo.png

   [22]: img/installed8.png

   [25]: img/taxonomy8.png

   [26]: img/taxonomy_field8.png

   [27]: img/block_types.png

   [28]: img/install_1_language_selection.png

   [29]: img/install_2_installation_profile.png

   [30]: img/install_3_database_configuration.png

   [31]: img/install_4_module_installation.png

   [32]: img/install_5_site_configuration.png

   [33]: img/install_6_admin_account.png

   [34]: img/install_7_regional_settings.png

   [35]: img/install_8_update_settings.png
   
   [36]: img/content_moderation_1.png
   
   [37]: img/content_moderation_2.png
   
   [39]: img/outside_in.png
