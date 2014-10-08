
# Objectifs de la formation - Les fonctionnalités avancées

  * __Administration (Tâches d'administration, Mises à jour, sauvegarde, Multi-sites, performance)__
  * Référencement (urls, meta-tags, sitemap.xml)
  * Multilinguisme
  * Autres contenus (vidéos, newsletters, formulaires
  * Modules du coeur (aggregator, poll, search)

.fx: progress

--------------------------------------------------------------------------------

## Tâches d'administration

  * _Configurer > Personnes_ : Paramétrage/blocage de comptes
  * _Configurer > Système_ : Informations et Cron
  * _Configurer > Développement_ : Erreurs et Maintenance
  * _Rapports > Erreurs récentes_ : monitorer son site
  * _Rapports > Statistiques_ : Module _Statistics_ du cœur prend beaucoup de
  ressources, préférer _Google Analytics_

![][4]

--------------------------------------------------------------------------------

## Mises à jour

  * Rapport > Mises à jour disponibles (module _Update status_)

ATTENTION : Toujours faire une sauvegarde des fichiers et de la base de données de façon préalable.

![][1]


--------------------------------------------------------------------------------

## Mises à jour des modules

  * Télécharger la nouvelle version
  * Supprimer l'ancienne version
  * Ajouter la nouvelle version
  * Aller dans « Rapports > tableau de bord »
  * Repérer la ligne Mise à jour de la base de données
  * Si une mise à jour est nécessaire, suite aux modifications, un lien
apparait.

  * Cliquez sur le lien et suivre les instructions


--------------------------------------------------------------------------------

## Mises à jour du cœur

  * Télécharger la nouvelle version
  * Copier/coller sur l'ancienne version
  * Aller dans « Rapports > tableau de bord »
  * Repérer la ligne Mise à jour de la base de données
  * Si une mise à jour est nécessaire, suite aux modifications, un lien
apparaît.

  * Cliquez sur le lien et suivre les instructions


--------------------------------------------------------------------------------

## DRUpal SHell

  * [https://github.com/drush-ops/drush][2]

  * Exécution d'installation et de mise à jour en ligne de commande
    * gain de temps
    * administration simplifiée
    * nombreuses commandes et support par les modules

  * Liste des commandes : [http://drush.ws/][3]

  * Disponible sous Linux

  * Relativement supporté sur Windows


--------------------------------------------------------------------------------

## Sauvegardes

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

## Installation multi-sites

  * Traditionnel - Partage des modules
    * Décompresser Drupal
    * Créer les répertoires dans /sites/ avec les noms des domaines
    * Copier le contenu de /sites/default dans les sous-répertoires.
    * Lancer l'installation classique via le navigateur

  * Module Domain access - Partage des données
    * Basé sur 1 instance (même base de données,  même code)
    * Facilité d'administration
    * Partage de contenus, utilisateurs, blocks, etc.


--------------------------------------------------------------------------------

## Performance

  * Activer le cache - Activer l'aggrégation
    * Fonctionne très bien pour les anonymes

  * Modules avancés
    * Views cache content
    * Memcache
    * EntityCache

  * Intégration Varnish, Redis, CDN, etc.

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

## Ré-écriture des urls

  * Module path (core) et pathauto
  * Recherche et métadonnées > Alias d'urls
  * Gestion de la ré-écriture automatique
    * Selon les types de contenu
    * Selon la taxonomie
  * Régénération d'urls en batch
  * Création à partir de tokens

--------------------------------------------------------------------------------

## Module Token

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

## Module meta-tag

  * Méta-données intégrées dans le code HTML des pages du site
  * à définir pour chaque contenu
  * paramétrage pour la page d'accueil
  * possibilité d'ajouter de nombreux tag


## Module XMLsitemap

  * Génération d'un fichier sitemap.xml à la racine avec les urls du site (parsing par les robots de référencement)
  * dans les formulaires d'édition, paramètrage pour définir quelles pages sont à inclure / exclure
  * Reconstruction automatique au lancement du cron

![][5]

--------------------------------------------------------------------------------

## Module Google Analytics

  * Code à renseigner, script ajouté à toutes les pages

## Module Schema.org

  * Metadonnées pour l'affichage dans les résultats de recherche
  * Basé sur RDF

## Module SEO Checklist

## Module Search 404

## Redirect - Global Redirect

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

## Le multilinguisme

  * Installation du module I18n (Internationalization)
    * Activation du module et sous-modules
    * Ajout d'une langue et configuration
    * Configuration > Régionalisation et langues > Langues

> Traduction au niveau du contenu

  * Autre possibilité : Entity translation
    * Pratique pour les noeuds
    * Moins pour les menus, blocs, taxonomie, ...
    * Inclus dans D8

> Traduction au niveau des champs

--------------------------------------------------------------------------------

## Traduire les noeuds

  * Onglet Traduire pour chaque contenu
    * Tableau de synthèse du statut de traduction pour toutes les langues
  * Ajout d'une traduction :
    * par le lien ''ajouter une traduction''
    * par la création d'un contenu puis ajouter sa référence dans la partie
    ''Select translations for...''

![][6]

--------------------------------------------------------------------------------

## Traduire les blocs

  * Choix de la langue
  * Paramètres de visibilité : Spécifier les chemins des contenus traduits où
  le bloc doit apparaître.

![][7]

--------------------------------------------------------------------------------

## Traduire l'interface

  * Configuration > Régionalisation et langues > Traduction de l'interface
  * Traduction de l'interface différent de la traduction du contenu

![][8]

--------------------------------------------------------------------------------

## Traduire les menus

  * 2 possibilités :
    * Créer un menu par langue
    * Dans un menu, pour chaque item, ajouter un item par langue

## Traduire les variables

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

## Media dans l'éditeur wysiwyg

  * Module Media
  * Gestion centralisée de tous les médias (images, vidéos, audio, flash)
  * Accès à la bibliothèque pour ré-utilisation
  * Facilité d'utilisation


![][11]

--------------------------------------------------------------------------------

## Autres modules de media

  * Alternative à Media
    * Scald
    * Asset

  * Module Video
    * Fournit un champ vidéo à ajouter dans les types de contenu

  * Module MediaFront
    * Champ video et customisation du player.


--------------------------------------------------------------------------------

## Newsletter

  * Module Simplenews
    * Gestion des abonnements
    * Gestion des envois instantanés ou asynchrones
    * Gestion de plusieurs catégories de newsletters

  * Gestion des souscriptions seules
    * Simple Subscription
    * Mailchimp

--------------------------------------------------------------------------------

## Formulaires

  * Module Webform
  * Création/Gestion intuitive des champs
  * Visualisation/export des soumissions

![][12]

![][13]

--------------------------------------------------------------------------------

# Objectifs de la formation - Les fonctionnalités avancées

  * Administration (Mises à jour, Multi-sites, sauvegarde, cron, ldap,
performance, architecture)
  * Référencement (urls, meta-tags, sitemap.xml)
  * Multilinguisme
  * Autres contenus (vidéos, newsletters, formulaires)
  * __Modules du coeur (aggregator, poll, search)__

.fx: progress


--------------------------------------------------------------------------------

## Modules du coeur de Drupal

  * Aggregator (Flux RSS)
    * Feeds pour aller plus loin

  * Poll (Sondage)
      * Webform, Advanced Poll

  * Search
      * Search API, Solr, ...

--------------------------------------------------------------------------------

# Mise production d'un site Drupal

Transférer fichiers et données

Pour le passage en production

  * Attention au fichier settings.php
  * Versionnement (Git approprié)
  * Pathologic pour réparer les chemins cassés

Pour le développement

  * Stage File Proxy
  * Désactiver les mails _Reroute Email_
  * Se faire passer pour un utilisateur _Masquerade_
  * _Administration Menu_

--------------------------------------------------------------------------------

# Questions ?


   [1]: img/update.png

   [2]: https://github.com/drush-ops/drush

   [3]: http://drush.ws/

   [4]: img/reports.png

   [5]: img/sitemap.png

   [6]: img/traduction.png

   [7]: img/block_translation.png

   [8]: img/string_traduction.png

   [9]: img/panel.png

   [10]: img/panel2.png

   [11]: img/media.png

   [12]: img/webform.png

   [13]: img/export_webform.png

