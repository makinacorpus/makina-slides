
# Objectifs de la formation - Les fonctionnalités avancées

  * __Administration (Tâches d'administration, Mises à jour, sauvegarde, Multi-sites, performance)__
  * Référencement (urls, meta-tags, sitemap.xml)
  * Multilinguisme
  * Autres contenus (médias, newsletters, formulaires)
  * Recherche

.fx: progress

--------------------------------------------------------------------------------

# Tâches d'administration

  * _Configurer > Personnes_ : Paramétrage/blocage de comptes (module _Ban_)
  * _Configurer > Système_ : Informations et Cron
  * _Configurer > Développement_ : Erreurs et Maintenance
  * _Rapports > Rapport d'état_ : monitorer son site
  * _Rapports > Erreurs récentes_ : monitorer son site
  * _Rapports > Statistiques_ : Module _Statistics_ du cœur (mais il ne couvre pas
  ce qu'attendent les gens, préférer _Google Analytics_)

![][4]

--------------------------------------------------------------------------------

# Mises à jour

  * Rapport > Mises à jour disponibles (module _Update manager_)

# ATTENTION : Toujours faire une sauvegarde des fichiers et de la base de données de façon préalable.

![][1]

--------------------------------------------------------------------------------

# Mises à jour des modules

  * Télécharger la nouvelle version
  * Supprimer l'ancienne version
  * Ajouter la nouvelle version
  * Aller dans « Rapports > tableau de bord »
  * Repérer la ligne "Mise à jour de la base de données"
  * Si une mise à jour est nécessaire suite aux modifications, un lien
apparait.
  * Cliquez sur le lien et suivre les instructions

--------------------------------------------------------------------------------

# Mises à jour du cœur

  * Télécharger la nouvelle version
  * Copier/coller sur l'ancienne version
  * Aller dans « Rapports > tableau de bord » et repérer la ligne "Mise à jour de la base de données"
  * Si une mise à jour est nécessaire suite aux modifications, un lien
apparaît. Cliquez sur le lien et suivre les instructions

![][24]

--------------------------------------------------------------------------------

# DRUpal SHell

  * [https://github.com/drush-ops/drush][2]

  * Exécution d'installation et de mise à jour en ligne de commande
    * gain de temps
    * administration simplifiée
    * nombreuses commandes et support par les modules

  * Liste des commandes : [http://drush.ws/][3]

  * Disponible sous Linux

  * Relativement supporté sur Windows (pour Drupal 8, installer avec Composer)

--------------------------------------------------------------------------------

# Sauvegardes

  * Module _Backup & Migrate_
    * Sauvegarde de la base de données
    * Sauvegarde des fichiers
    * Pas encore stable pour D8

  * Script shell maison

  * Commandes drush
    * drush archive-dump
    * drush archive-restore
    * drush sql-dump
    * drush sql-client

--------------------------------------------------------------------------------

# Installation multi-sites

  * Traditionnel - Partage des modules
    * Décompresser Drupal
    * Créer les répertoires dans /sites/ avec les noms des domaines
    * Copier le contenu de /sites/default dans les sous-répertoires.
    * Lancer l'installation classique via le navigateur

  * Module Domain access (en cours de port D8) - Partage des données
    * Basé sur 1 instance (même base de données,  même code)
    * Facilité d'administration
    * Partage de contenus, utilisateurs, blocks, etc.

  * [https://www.palantir.net/blog/multi-headed-drupal][23]

--------------------------------------------------------------------------------

# Performance

  * Cache activé par défaut
    * Fonctionne très bien pour les anonymes

  * Intégration Varnish, Redis, Memcache, CDN, etc.

  * Passez à PHP7 et MySQL 5.6 !

--------------------------------------------------------------------------------

# Objectifs de la formation - Les fonctionnalités avancées

  * Administration (Tâches d'administration, Mises à jour,  sauvegarde,
Multi-sites, performance)
  * __Référencement (urls, meta-tags, sitemap.xml)__
  * Multilinguisme
  * Autres contenus (médias, newsletters, formulaires)
  * Recherche

.fx: progress

--------------------------------------------------------------------------------

# Ré-écriture des urls

  * Module path (core) et __Pathauto__
  * Recherche et métadonnées > Alias d'urls
  * Gestion de la ré-écriture automatique
    * Selon les types de contenu
    * Selon la taxonomie
  * Régénération d'urls en batch
  * Création à partir de tokens

--------------------------------------------------------------------------------

# Module Token

  * Sorte de variables affichant certaines données en fonction d'un contexte
  * Global
    * nom du site
    * date actuelle
  * Node
    * titre
    * champs
    * date
  * Utilisateur
    * nom d'utilisateur
    * date de dernière connexion

Et bien d'autres

--------------------------------------------------------------------------------

## Module Metatag

  * Méta-données intégrées dans le code HTML des pages du site
  * à définir pour chaque contenu
  * paramétrage pour la page d'accueil
  * possibilité d'ajouter de nombreux tag

--------------------------------------------------------------------------------

## Module XMLSitemap

  * Génération d'un fichier sitemap.xml à la racine avec les urls du site (parsing par les robots de référencement)
  * Paramétrage pour définir quelles pages sont à inclure / exclure
  * Reconstruction automatique au lancement du cron

![][5]

--------------------------------------------------------------------------------

## Module Google Analytics

  * Code à renseigner, script ajouté à toutes les pages

## Sémantique

  * Metadonnées pour l'affichage dans les résultats de recherche
  * Inclus dans le cœur de Drupal (module RDF)

## Redirect

  * Gestion des redirections

--------------------------------------------------------------------------------

# Objectifs de la formation - Les fonctionnalités avancées

  * Administration (Tâches d'administration, Mises à jour,  sauvegarde,
Multi-sites, performance)
  * Référencement (urls, meta-tags, sitemap.xml)
  * __Multilinguisme__
  * Autres contenus (médias, newsletters, formulaires)
  * Recherche

.fx: progress

--------------------------------------------------------------------------------

# Le multilinguisme

  * 4 modules présents dans le coeur
    * Language (gestion des langues du site)
    * Interface Translation (interface de traduction, administration du site en FR)
    * Configuration Translation (traduction de la configuration)
    * Content Translation (traduction du contenu)

![][14]
    
--------------------------------------------------------------------------------

# La langue

  * Ajout de langage
  * Gère également si la langue s'écrit de gauche à droite

![][15]
    
--------------------------------------------------------------------------------

# La langue

  * Activé automatiquement si on choisit l'installation dans une autre langue
  * Permet de combiner différentes méthodes de détection de langue

![][16]
    
--------------------------------------------------------------------------------

# Traduction de l'interface

  * Interface de traduction du back-office

![][17]
 
![][18]

--------------------------------------------------------------------------------

# Traduction du contenu

  * Module "Content Translation"
  * "Contenu" = 
    * Nœuds
    * Blocs
    * Menus
    * Taxonomie
    * Utilisateurs
 
![][19]

--------------------------------------------------------------------------------

# Traduction du contenu

  * Activation du multilinguisme sur le type de contenu
    * (ou utilisateur, vocabulaire, ...)
  * Stratégie de langage par défaut (selon les profils, droits, ...)

![][20]

--------------------------------------------------------------------------------

# Traduction du contenu

  * Onglet "Traduire" pour chaque contenu
    * Tableau de synthèse du statut de traduction pour toutes les langues
    * Ajout d'une traduction par langue

![][6]

--------------------------------------------------------------------------------

# Traduction du contenu

  * Attention, il faut paramétrer les champs qui peuvent se traduire !
  * Administration > Configuration > Langue et région > Langue du contenu et traduction

![][21]

--------------------------------------------------------------------------------

# Traduire les blocs

  * Pour chaque bloc dans l'onglet ''Configurer le bloc''
    * Restriction du bloc à certains langages

![][7]

--------------------------------------------------------------------------------

# Traduire la configuration

![][8]

  * Tout le reste du site...
  * Page d'accueil, 404, ...
  * Administration > Configuration > Langue et région > Traduction de la configuration

![][22]

--------------------------------------------------------------------------------

# Traduire les menus

  * 2 stratégies :
    * Créer un menu par langue
    * Traduire un menu, qui comprendra alors des éléments de chaque langue (pas tous affichés)

--------------------------------------------------------------------------------

# Objectifs de la formation - Les fonctionnalités avancées

  * Administration (Mises à jour, Multi-sites, sauvegarde, cron,
performance, architecture)
  * Référencement (urls, meta-tags, sitemap.xml)
  * Multilinguisme
  * __Autres contenus (médias, newsletters, formulaires)__
  * Recherche

.fx: progress

--------------------------------------------------------------------------------

# Gestion des médias 

  * Media Initiative
    * <http://www.drupalmedia.org>
    * Suite de modules (Entity Browser, Media entity, DropzoneJS ...)
    * Fichiers image, vidéo, audio, ...
  * Pas complètement stable !
    * Mais en développement actif, sera bientôt prêt


--------------------------------------------------------------------------------

# Newsletter

  * Module Simplenews
    * Gestion des abonnements
    * Gestion des envois instantanés ou asynchrones
    * Gestion de plusieurs catégories de newsletters
    * Pas tout à fait finalisé pour Drupal 8

  * Gestion des souscriptions seules
    * Service externe : _Mailchimp_ (ou d'autres, Mailjet, ...)
    * Solution recommandée aujourd'hui

--------------------------------------------------------------------------------

# Formulaires

  * Référence Drupal : module Webform
    * Mais pas prêt du tout pour Drupal 8
    * Création/Gestion intuitive des champs
    * Visualisation/export des soumissions
  * Utilisation du module __Contact__
    * Avec Contact Storage
    * et d'autres éventuellement (pour l'export CSV)

--------------------------------------------------------------------------------

# Objectifs de la formation - Les fonctionnalités avancées

  * Multilinguisme
  * Administration (Mises à jour, Multi-sites, sauvegarde, cron,
performance, architecture)
  * Référencement (urls, meta-tags, sitemap.xml)
  * Autres contenus (médias, newsletters, formulaires)
  * __Recherche__

.fx: progress

--------------------------------------------------------------------------------

# La recherche

  * Search API
    * Lien Apache Solr (module __Search API Solr Search__)
    * Lien ElasticSearch (module __Elasticsearch Connector__)
  * ...

--------------------------------------------------------------------------------

# Mise production d'un site Drupal

Transférer fichiers et données

Pour le passage en production

  * Attention au fichier settings.php, services.yml
  * Et surtout la configuration (dans /files)
  * Versionnement (Git approprié)
  * Pathologic pour réparer les chemins cassés

Pour le développement

  * Stage File Proxy
  * Désactiver les mails _Reroute Email_
  * Se faire passer pour un utilisateur _Masquerade_

--------------------------------------------------------------------------------

# Procédure de construction d'un site

   * Configuration initiale (multilinguisme, workflow, metatag, ...)
   * Formats d'images, directement à partir des maquettes
   * Types de contenu
   * Views
   * Mise en page (blocs, panels ou display suite ou ...)
   * Intégration graphique
   * Développements spécifiques ou modules additionnels (flags, rules, ...)

   * __Problème__ : aucune intégration graphique avant la fin => incompatible avec une livraison régulière...

![][25]

--------------------------------------------------------------------------------

# Procédure de construction d'un site

   * Configuration initiale => style guide, charte graphique par défaut
   * Formats d'images
   * Types de contenu => templates de contenu
   * Views => templates de Views
   * Mise en page => finition du template
   * Développements spécifiques ou modules additionnels (flags, rules, ...)
   * Intégration graphique des derniers modules

--------------------------------------------------------------------------------

# Questions ?


   [1]: img/update.png

   [2]: https://github.com/drush-ops/drush

   [3]: http://drush.ws/

   [4]: img/reports8.png

   [5]: img/sitemap.png

   [6]: img/traduction.png

   [7]: img/block_translation.png

   [8]: img/configuration_translation.png

   [9]: img/panel.png

   [10]: img/panel2.png

   [11]: img/media.png

   [12]: img/webform.png

   [13]: img/export_webform.png

   [14]: img/multilinguisme.png

   [15]: img/add_language.png

   [16]: img/language_detection.png

   [17]: img/interface_translation.png

   [18]: img/user_interface_translation.png

   [19]: img/content_translation.png

   [20]: img/content_type_translation.png

   [21]: img/language_field_translation.png

   [22]: img/system_information_translation.png

   [23]: https://www.palantir.net/blog/multi-headed-drupal

   [24]: img/original_release_schedule.png

   [25]: https://makina-corpus.com/blog/metier/2016/comment-creer-un-site-web-avec-drupal

