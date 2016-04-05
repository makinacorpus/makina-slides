
# Objectifs de la formation - Les fonctionnalités avancées

  * __Administration (Tâches d'administration, Mises à jour, sauvegarde, Multi-sites, performance)__
  * Référencement (urls, meta-tags, sitemap.xml)
  * Multilinguisme
  * Autres contenus (vidéos, newsletters, formulaires)
  * Modules du coeur (aggregator, poll, search)

.fx: progress

--------------------------------------------------------------------------------

# Tâches d'administration

  * _Configurer > Personnes_ : Paramétrage/blocage de comptes (module _Ban_)
  * _Configurer > Système_ : Informations et Cron
  * _Configurer > Développement_ : Erreurs et Maintenance
  * _Rapports > Rapport d'état_ : monitorer son site
  * _Rapports > Erreurs récentes_ : monitorer son site
  * _Rapports > Statistiques_ : Module _Statistics_ du cœur prend beaucoup de
  ressources, préférer _Google Analytics_

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
  * Repérer la ligne Mise à jour de la base de données
  * Si une mise à jour est nécessaire, suite aux modifications, un lien
apparait.

  * Cliquez sur le lien et suivre les instructions

--------------------------------------------------------------------------------

# Mises à jour du cœur

  * Télécharger la nouvelle version
  * Copier/coller sur l'ancienne version
  * Aller dans « Rapports > tableau de bord »
  * Repérer la ligne Mise à jour de la base de données
  * Si une mise à jour est nécessaire, suite aux modifications, un lien
apparaît.

  * Cliquez sur le lien et suivre les instructions

--------------------------------------------------------------------------------

# DRUpal SHell (remplacer par console ?)

  * [https://github.com/drush-ops/drush][2]

  * Exécution d'installation et de mise à jour en ligne de commande
    * gain de temps
    * administration simplifiée
    * nombreuses commandes et support par les modules

  * Liste des commandes : [http://drush.ws/][3]

  * Disponible sous Linux

  * Relativement supporté sur Windows

--------------------------------------------------------------------------------

# Sauvegardes

  * Module _Backup & Migrate_
    * Sauvegarde de la base de données
    * Sauvegarde des fichiers

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

  * Module Domain access (pas encore prêt en D8) - Partage des données
    * Basé sur 1 instance (même base de données,  même code)
    * Facilité d'administration
    * Partage de contenus, utilisateurs, blocks, etc.

--------------------------------------------------------------------------------

# Performance

  * Cache activé par défaut
    * Fonctionne très bien pour les anonymes

  * Intégration Varnish, Redis (par Makina Corpus), Memcache, CDN, etc.

--------------------------------------------------------------------------------

# Objectifs de la formation - Les fonctionnalités avancées

  * Administration (Tâches d'administration, Mises à jour,  sauvegarde,
Multi-sites, ldap, performance)
  * __Référencement (urls, meta-tags, sitemap.xml)__
  * Multilinguisme
  * Autres contenus (vidéos, newsletters, formulaires
  * Modules du coeur (aggregator, poll, search)

.fx: progress

--------------------------------------------------------------------------------

# Ré-écriture des urls

  * Module path (core) et pathauto
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

## Module Simple sitemap

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

--------------------------------------------------------------------------------

# Objectifs de la formation - Les fonctionnalités avancées

  * Administration (Tâches d'administration, Mises à jour,  sauvegarde,
Multi-sites, ldap, performance)
  * Référencement (urls, meta-tags, sitemap.xml)
  * __Multilinguisme__
  * Autres contenus (vidéos, newsletters, formulaires
  * Modules du coeur (aggregator, poll, search)

.fx: progress

--------------------------------------------------------------------------------

# Le multilinguisme

  * Activation des 4 modules présents dans le coeur depuis la version 8
    * Configuration Translation (traduction de la configuration)
    * Content Translation (traduction du contenu)
    * Interface Translation (interface complète de traduction de tous champs)
    * Language (gestion des langues du site)
    
--------------------------------------------------------------------------------

# Traduire les noeuds

  * Onglet Traduire pour chaque contenu
    * Tableau de synthèse du statut de traduction pour toutes les langues
  * Ajout d'une traduction :
    * par le lien ''Ajouter''
    * par la création d'un contenu puis ajouter sa langue avec le champ
    ''Language''

![][6]

--------------------------------------------------------------------------------

# Traduire les blocs

  * Pour chaque bloc dans l'onglet ''Configurer le bloc''
  * Sélection de la langue
  * Pages : Spécifier les chemins des contenus traduits où
  le bloc doit apparaître.

![][7]

--------------------------------------------------------------------------------

# Traduire l'interface

  * Configuration > Régionalisation et langues > Traduction de l'interface utilisateur
  * Traduction de l'interface différent de la traduction du contenu
  * Traduction de l'interface aussi différent de la traduction de configuration

![][8]

--------------------------------------------------------------------------------

# Traduire les menus

  * 2 possibilités :
    * Créer un menu par langue
    * Dans un menu, pour chaque item, ajouter un item par langue

# Traduire les variables

  * Nom du site
  * Slogan
  * Mails

--------------------------------------------------------------------------------

# Objectifs de la formation - Les fonctionnalités avancées

  * Administration (Mises à jour, Multi-sites, sauvegarde, cron, ldap,
performance, architecture)
  * Référencement (urls, meta-tags, sitemap.xml)
  * Multilinguisme
  * __Autres contenus (vidéos, newsletters, formulaires)__
  * Modules du coeur (aggregator, poll, search)

.fx: progress

--------------------------------------------------------------------------------

# Gestion des médias 

  * Media Initiative
    * <http://www.drupalmedia.org>
    * Suite de modules (Entity Browser, Media entity, DropzoneJS ...)
    * Fichiers image, vidéo, audio, ...
    

![][11]

--------------------------------------------------------------------------------

# Newsletter

  * Module Simplenews
    * Gestion des abonnements
    * Gestion des envois instantanés ou asynchrones
    * Gestion de plusieurs catégories de newsletters

  * Gestion des souscriptions seules
    * Service externe : _Mailchimp_

--------------------------------------------------------------------------------

# Formulaires

  * Module Webform (pas encore prêt...)
  * Création/Gestion intuitive des champs
  * Visualisation/export des soumissions

![][12]

![][13]

--------------------------------------------------------------------------------

# Objectifs de la formation - Les fonctionnalités avancées

  * Multilinguisme
  * Administration (Mises à jour, Multi-sites, sauvegarde, cron, ldap,
performance, architecture)
  * Référencement (urls, meta-tags, sitemap.xml)
  * Autres contenus (vidéos, newsletters, formulaires)
  * __Recherche__

.fx: progress

--------------------------------------------------------------------------------

# La recherche

  * Search API
  * Apache Solr
    * module Apache Solr Search non porté sur Drupal 8
    * remplacé par Search API Solr Search
  * ElasticSearch
    * Elasticsearch Connector 
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

# Questions ?


   [1]: img/update.png

   [2]: https://github.com/drush-ops/drush

   [3]: http://drush.ws/

   [4]: img/reports8.png

   [5]: img/sitemap.png

   [6]: img/traduction.png

   [7]: img/block_translation.png

   [8]: img/string_traduction.png

   [9]: img/panel.png

   [10]: img/panel2.png

   [11]: img/media.png

   [12]: img/webform.png

   [13]: img/export_webform.png

