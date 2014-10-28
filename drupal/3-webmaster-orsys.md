
# Formation Webmaster Drupal

--------------------------------------------------------------------------------

Plan

  * __Les tâches de l'administrateur__
    * Administrer le serveur
    * Administrer un site de gestion de contenu
    * Administrer les contenus
    * Administrer les utilisateurs (droits, rôles...)
    * Paramétrer et déployer les distributions

  * Les outils de l'administrateur
  * Installer Drupal
  * Rapports et tableaux de bord de l'administrateur
  * Définir la configuration système
  * Définir la configuration des utilisateurs
  * Configurer les contenus
  * Déployer le site

.fx: progress

--------------------------------------------------------------------------------

# Introduction - Les tâches de l'administrateur

--------------------------------------------------------------------------------

## Administrer le serveur

  * Serveur : Apache, IIS
  * Language : PHP
  * Base de données : MySQL, SQLite, PostgreSQL, Oracle

>> Stack xAMP : (*, Apache, MySQL, PHP)

Exemples sous Windows :

  * WampServer
  * Xampp
  * Acquia Dev Desktop

--------------------------------------------------------------------------------

## Administrer un site de gestion de contenu

<dl>
    <dt>CMS</dt>
    <dd>Content Management System</dd>
</dl>

>> Un système de gestion de contenu modulaire

<dl>
    <dt>CMF</dt>
    <dd>Content Management Framework</dd>
</dl>

>> Une API sécurisée et structurée

>> Des modules de qualité

Autres exemples de CMS :

  * WordPress
  * Joomla
  * Typo3

--------------------------------------------------------------------------------

### Quelques autres CMS

  * Wordpress
    * grande communauté
    * nombreux plugins et thèmes
    * qualité/sécurité du code laisse à désirer hors du cœur
    * pratique pour les projets statiques/légers

![][19]

--------------------------------------------------------------------------------

### Quelques autres CMS

  * Joomla
    * plugins nombreux mais peu maintenus
    * communauté moindre

![][20]

--------------------------------------------------------------------------------

## Administrer les contenus

### Historique

  * Sites statiques en HTML, création page par page
    * fastidieux à maintenir
  * Sites dynamiques, Framework proposant des API
    * briques de base pour le code, standardisation
    * beaucoup de développement
  * CMS : Système de gestion de contenu
    * briques de fonctionnalités
    * pas/peu de développement

### Le nœud, structure centrale de Drupal

Le module `Node` est requis dès que l'on installe Drupal, il stocke quelques
métadonnées de base comme la date de création, l'auteur.
Chaque contenu a un type, de base : _article_, _page_.

--------------------------------------------------------------------------------

## Administrer les utilisateurs (droits, rôles...)

De même, le module `User` est requis dès l'installation et fournit les
fonctionnalités liées à la gestion de compte et aux droits d'accès.

Chaque module fournit une liste de permissions disponibles.

Un rôle est un ensemble de permissions.

Un utilisateur peut avoir plusieurs rôles, ses droits d'accès seront donc
définis par la somme des permissions de chacun de ses rôles.

Des modules peuvent ajouter ou affiner les permissions d'autres modules.

--------------------------------------------------------------------------------

## Paramétrer et déployer les distributions

### Qu'est qu'une distribution ?

C'est un profil d'installation Drupal qui installe et pré-configure une liste
de modules. On obtient après l'installation de ce profil un site prêt à
l'emploi.

### Une liste de quelques distributions Drupal

  * _Commerce Kickstart_ : distribution e-commerce
  * _Open Atrium_ : intranet et collaboration
  * _Drupal Commons_ : organisation de communautés, social business
  * _OpenPublish_ : site media, éditorial
  * _OpenPublic_ : administrations publiques (mairies, ...)
  * _Spark_ : production de contenu, experience utilisateur
  * _Opigno LMS_ : éducation
  * _OpenHotel_, _Rooms_, _Restaurant_ : hotellerie
  * _ERPal_ : ERP

--------------------------------------------------------------------------------

### Paramètrage de la distribution

La majorité des distributions proposent une liste de paramètres à configurer
pendant le processus d'installation. La totalité des module communautaires
(ou _"contirb"_) utilisés reste configurable post-installation

### Déploiement d'une distribution

Une distribution se déploie de la même manière qu'un Drupal construit à la main.
L'avantage étant qu'elle peut être plus rapide à configurer si elle correspond
exactement à nos besoins.

--------------------------------------------------------------------------------

Plan

  * Les tâches de l'administrateur
  * __Les outils de l'administrateur__
    * Comprendre la licence de Drupal
    * Obtenir une assistance de la communauté Drupal
    * Accéder à la documentation disponible
    * Trouver les téléchargements et les extensions

  * Installer Drupal
  * Rapports et tableaux de bord de l'administrateur
  * Définir la configuration système
  * Définir la configuration des utilisateurs
  * Configurer les contenus
  * Déployer le site

.fx: progress

--------------------------------------------------------------------------------

# Les outils de l'administrateur

--------------------------------------------------------------------------------

## Comprendre la licence Drupal

Drupal, un logiciel open-source :
La totalité des sources de Drupal sont disponibles au public sous licence GNU
GPL v2 (License générale publique). Cela veut dire qu'on :

  * est libre d'exécuter le logiciel, pour n'importe quel usage
  * est libre d'étudier le fonctionnement d'un programme et de l'adapter à ses
  besoins, ce qui passe par l'accès aux codes sources
  * est libre de redistribuer des copies
  * a l'obligation de faire bénéficier à la communauté des versions modifiées

Les sources sont donc redistribuées sur Drupal.org. Si on distribue une version
modifiée de Drupal, on a l'obligation de rendre son code source public. En
revanche, ce n'est pas le cas pour une utilisation personnelle.

--------------------------------------------------------------------------------

## Obtenir une assistance de la communauté Drupal

### La communauté internationale

La communauté internationale est présente sur les canaux suivants :

  * Forum : [groups.drupal.org](https://groups.drupal.org), [forum.drupal.org](https://forum.drupal.org)
  * Bugtracker : [drupal.org](https://www.drupal.org)
  * Q & A : [drupal.stackexchange.com](https://drupal.stackexchange.com)
  * Meetups : [meetup.com](http://www.meetup.com)
  * Evenements : [drupical.com](http://drupical.com)
  * IRC : [chat.freenode.net #drupal](irc://chat.freenode.net/#drupal),
  [chat.freenode.net #drupal-support](irc://chat.freenode.net/#drupal-support)

--------------------------------------------------------------------------------

### La communauté française

La communauté française est présente sur les canaux suivants :

  * Forum : [drupalfr.org](http://www.drupalfr.org)
  * Traduction : [localize.drupal.org](https://localize.drupal.org/translate/languages/fr),
   [traduction.drupalfr.org](http://traduction.drupalfr.org)
  * Meetups : [meetup.com](http://www.meetup.com/drupal-france-francophonie)
  * IRC : [chat.freenode.net #drupal](irc://chat.freenode.net/#drupal-fr)

À noter, Google recense des milliers d'articles en anglais et en français pour
débuter avec Drupal, parmi lesquels :

  * [kolossaldrupal.org](http://kolossaldrupal.org/)
  * [drupalfacile.org](http://www.drupalfacile.org/) (podcasts vidéos)
  * [documentation DrupalFR](http://drupalfr.org/documentation)

--------------------------------------------------------------------------------

## Trouver les téléchargements et les extensions

Tout est sur Drupal.org :

  * Drupal core : [drupal.org/project/drupal](https://www.drupal.org/project/drupal)
  ou sur [drupalfr.org](http://drupalfr.org) pour la version française
  * [Recherche de modules](https://www.drupal.org/project/project_module) : https://drupal.org/project/modules
  * [Recherche de themes](https://www.drupal.org/project/project_theme) : https://drupal.org/project/themes
  * [Recherche de distributions](https://www.drupal.org/project/project_distribution) : https://drupal.org/project/distributions

<img style="float:left;padding-right:2em" src="img/recherche_module.png"/>

Permet de filtrer pour ne garder que :

  * la version dont on a besoin
  * des modules encore supportés
  * les plus utilisés
  * les plus téléchargés
  * les plus récents

--------------------------------------------------------------------------------

Plan

  * Les tâches de l'administrateur
  * Les outils de l'administrateur
  * __Installer Drupal__
    * Installer Drupal en mode interactif
    * Installer Drupal en mode commande
    * Les modules du Core
    * Les modules complémentaires
    * Travaux pratiques

  * Rapports et tableaux de bord de l'administrateur
  * Définir la configuration système
  * Définir la configuration des utilisateurs
  * Configurer les contenus
  * Déployer le site

.fx: progress

--------------------------------------------------------------------------------

# Installer Drupal

--------------------------------------------------------------------------------

## Installer Drupal en mode interactif

_cf Chapitre `I`, 1.3.2_

### Plusieurs méthodes pour récupérer les sources

  * Sur drupal.org (version anglaise)
  * Sur drupalfr.org (avec traduction)
  * directement dans Acquia Dev Desktop (modules Acquia®©™ inclus)

--------------------------------------------------------------------------------

## Installer Drupal en mode commande

### Drush

  * __DRU__pal __SH__ell: outil en ligne de commande pour Drupal
  * Site officiel: [drush.ws](http://drush.ws)
  * Initialement pour Linux mais version Windows maintenue (mais peu testée)
  * Très utilisé par les professionnels de Drupal, utile dès le profil webmaster

### Exemples d'utilisation

  * Installation
  * Installation/activation/désactivation de modules
  * Mise à jour du code et de la BDD
  * Vidage des caches
  * Sauvegarde/Restauration
  * Développement de fonctionnalités

--------------------------------------------------------------------------------

### Installation de Drupal avec Drush

    !bash
    drush dl drupal  # télécharge la dernière version de Drupal
    mv drupal-7.* monsite  # renomme le dossier contenant Drupal
    cd monsite  # se place dans ledit dossier

    # Installe Drupal dans la base 'mabase'
    drush site-install --db-url=mysql://user:mdp@localhost/mabase

    drush en l10n_update  # Télécharge et installe le module l10n update
    drush l10n-update  # Vérifie et télécharge les traductions

    drush cc all  # Vide les caches

    drush ard  # Crée une sauvegarde du site

--------------------------------------------------------------------------------

## Les modules du Cœur

_cf Chapitre `II` et `IV`_

### Liste des modules du cœur

  * _System, User_ -> prérequis
  * _Node, Field, Comment, File, Image_ -> création de contenu
  * _Text, List, Options, Number_ -> types de champs
  * _Menu, Block, Taxonomie_ -> structuration
  * _Toolbar, Shortcut, Dashboard, Color, Overlay, Contextual_ -> interface
  * _Book, Blog, Forum, Poll_ -> structuration avancée
  * _Contact, Aggregator, Tracker, Update, OpenID_ -> fonctions spécifiques
  * _Path, RDF_ -> SEO
  * _Locale, Content Translation_ -> traduction

--------------------------------------------------------------------------------

et bien d'autres

### La gestion de contenu

_cf Chapitre `II`, 3 et 4_

### L'organisation du site

_cf Chapitre `II`, 2_

<br><br><br><br>

> Drupal sans ses modules contrib ne permet que de faire des sites
_très_ simples.

--------------------------------------------------------------------------------

## Les modules complémentaires

Communément appelés modules _contrib_ car réalisés par la communauté et
les contributeurs Drupal (_cf Chapitre `IV`_).

Modules les plus utilisés :

  * Views (création de liste de contenu)
  * Pathauto (avec Token)
  * CKEditor (WYSIWYG)
  * IMCE (gestion d'upload de fichiers)
  * Administration Menu
  * Google Analytics
  * Date, Link, E-mail (types de champs)
  * Webform (sondages et enquêtes)
  * Backup & Migrate
  * Rules (règles et actions automatiques)

--------------------------------------------------------------------------------

## Travaux pratiques

  * Installer Drupal
  * Activer le module Administration Menu
  * Ajouter la langue française
  * Activer le module de mise à jour automatique de traductions
  * Mettre à jour les traductions
  * Ajouter le module Google Analytics
  * Configurer le code Google Analytics
  * Activer le module Module Filter

> En ligne de commande !

.fx: tp

--------------------------------------------------------------------------------

Plan

  * Les tâches de l'administrateur
  * Les outils de l'administrateur
  * Installer Drupal
  * __Rapports et tableaux de bord de l'administrateur__
    * Le tableau de bord d'administration
    * Etre alerté des mises à jour disponibles
    * Consulter le journal des événements
    * Détecter les tentatives d'intrusion (erreurs 403) et les URL obsolètes (erreurs 404)

  * Définir la configuration système
  * Définir la configuration des utilisateurs
  * Configurer les contenus
  * Déployer le site

.fx: progress

--------------------------------------------------------------------------------

# Rapports et tableaux de bord de l'administrateur

--------------------------------------------------------------------------------

<span></span>

## Le tableau de bord d'administration

_cf Chapitre `I`, 1.6_

## Etre alerté des mises à jour disponibles

_cf Chapitre `III`, 3.2_

## Consulter le journal des événements

La section _Rapports > Entrées récentes du journal_ contient tous les événements
de votre site. Le nombre d'entrées stockées est configurable.

Les événements peuvent être filtrés par type (généralement le module ayant
enregistré l'événement) et par criticité.

## Détecter les erreurs 403 et 404

Des rapports spécifiques aux pages 403 et 404 permettent de connaître les
erreurs de navigation, les pages obsolètes ou les tentatives d'intrusion.

Préférer les statistiques d'exploration de Google Webmaster Tools.

--------------------------------------------------------------------------------

Plan

  * Les tâches de l'administrateur
  * Les outils de l'administrateur
  * Installer Drupal
  * Rapports et tableaux de bord de l'administrateur
  * __Définir la configuration système__
    * Changer le nom du site, l'adresse de courriel, le slogan, la page d'accueil par défaut. Gérer le cache
    * Configurer les migrations, les sauvegardes et les restaurations de la base de données
    * Gérer les tâches de maintenance automatique (cron)
    * Paramétrer la journalisation des événements système
    * Configurer les options du système

  * Définir la configuration des utilisateurs
  * Configurer les contenus
  * Déployer le site

.fx: progress

--------------------------------------------------------------------------------

# Définir la configuration système

--------------------------------------------------------------------------------

Chaque module fournit sa propre configuration, un lien pour chaque module est
généralement indiqué dans la liste des modules. Les options de configuration
sont réparties dans différentes sections.

## Changer le nom du site, l'adresse de courriel, le slogan, la page d'accueil par défaut. Gérer le cache

_cf Chapitre `II`, 1.2_
_cf Chapitre `III`, 3.1_

## Configurer les migrations, les sauvegardes et les restaurations de la base de données

_cf Chapitre `III`, 2_

## Gérer les tâches de maintenance automatique (cron)

_cf Chapitre `III`, 3.3_

## Paramétrer la journalisation des événements système

_Configuration > Développement > Journalisation & Erreurs_ (Requiert le cron)


--------------------------------------------------------------------------------

Plan

  * Les tâches de l'administrateur
  * Les outils de l'administrateur
  * Installer Drupal
  * Rapports et tableaux de bord de l'administrateur
  * Définir la configuration système
  * __Définir la configuration des utilisateurs__
    * Configurer le comportement par défaut des utilisateurs, le thème par défaut et les paramètres de localisation
    * Définir les rôles et les droits d'accès
    * Créer les comptes utilisateurs
    * Définir des profils utilisateurs

  * Configurer les contenus
  * Déployer le site

.fx: progress

--------------------------------------------------------------------------------

# Définir la configuration des utilisateurs

--------------------------------------------------------------------------------

## Configurer le comportement par défaut des utilisateurs, le thème par défaut et les paramètres de localisation

### Comportement par défaut

_cf Chapitre `II`, 2.3_

### Thème par défaut

_cf Chapitre `V`, 1_

### Paramètres de de localisation

_Configuration > Régionalisation & Langues > Paramètres régionaux_

--------------------------------------------------------------------------------

## Définir les rôles et les droits d'accès

_cf Chapitre `I`, 2.4_
_cf Chapitre `II`, 2.3_

--------------------------------------------------------------------------------

## Créer les comptes utilisateurs

_cf Chapitre `II`, 2.3_

--------------------------------------------------------------------------------

## Définir des profils utilisateurs

Le module Field UI permet d'ajouter des champs aux utilisateurs, pour par exemple
stocker leur :

  * nom
  * prénom
  * adresse postale
  * date de naissance
  * etc.

Si plusieurs types de profils doivent être créés (_i.e._ : plusieurs ensembles
de champs), préférer le module Profile2. Il permet également de définir des
champs privés non affichés aux autres utilisateurs.

--------------------------------------------------------------------------------

Plan

  * Les tâches de l'administrateur
  * Les outils de l'administrateur
  * Installer Drupal
  * Rapports et tableaux de bord de l'administrateur
  * Définir la configuration système
  * Définir la configuration des utilisateurs
  * __Configurer les contenus__
    * Configurer les langues (contenu, interface utilisateur)
    * Configurer les formats de texte et les éditeurs de texte
    * Paramétrer les options de recherche et d'indexation
    * Définir les alias d'URL et les URL simplifiées

  * Déployer le site

.fx: progress

--------------------------------------------------------------------------------

# Configurer les contenus

--------------------------------------------------------------------------------

<span></span>

## Configurer les langues (contenu, interface utilisateur)

_cf Chapitre `IV`, 2_


## Configurer les formats de texte et les éditeurs de texte

_cf Chapitre `II`, 3.2, 3.3, 3.4_
_cf Chapitre `IV`, 4.1_

## Paramétrer les options de recherche et d'indexation

_cf Chapitre `IV`, 4.4_

## Définir les alias d'URL et les URL simplifiées

_cf Chapitre `II`, 2.4_
_cf Chapitre `IV`, 4.3_


--------------------------------------------------------------------------------

Plan

  * Les tâches de l'administrateur
  * Les outils de l'administrateur
  * Installer Drupal
  * Rapports et tableaux de bord de l'administrateur
  * Définir la configuration système
  * Définir la configuration des utilisateurs
  * Configurer les contenus
  * __Déployer le site__
    * Préparer le serveur de production
    * Créer une distribution. Déployer le site
    * Suivre l'activité du site

.fx: progress

--------------------------------------------------------------------------------

# Déployer le site

--------------------------------------------------------------------------------

## Préparer le serveur de production

_cf Chapitre `III`, 1_

--------------------------------------------------------------------------------

## Créer une distribution. Déployer le site

### Créer des Features

_cf Chapitre `III`, 1_

### Créer son profil d'installation

  * Créer un nouveau dossier dans `/profiles`
  * Créer son fichier .info
  * Ajouter les modules et les thèmes
  * Ajouter les dépendances

### Déployer le site

Installer le profil d'installation correspondant ou transférer les fichiers et
la base de données.

Possibilité de développement plus professionel avec Features, le versionnement
de fichiers et Drush.

--------------------------------------------------------------------------------

## Suivre l'activité du site

<dl>
    <dt>Google Analytics</dt>
    <dd>Statistiques sur les visites du sites</dd>
    <br><br>
    <dt>Google Webmaster Tools</dt>
    <dd>
    Statistiques sur l'exploration par Google et le référencement du site
    </dd>
    <br><br>
    <dt>Modules Statistics</dt>
    <dd>
    Enregistre les visites en base de données, peu performant, affecte les
    performances du site
    </dd>
    <br><br>
    <dt>Monitoring côté serveur</dt>
    <dd>
    Certains hebergeurs comme OVH propose un monitoring du serveur Apache et
    MySQL afin de détecter les pages les plus lentes, ou les problèmes de
    performance généraux.
    </dd>
</dl>

--------------------------------------------------------------------------------




# Questions ?


   [19]: img/wordpress-logo.png

   [20]: img/joomla-logo.png
