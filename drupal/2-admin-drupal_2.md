
# Objectifs de la formation - Les fonctionnalités avancées

  * Administration (tâches d'administration, mises à jour, sauvegarde, multi-sites, performance)
  * Référencement (URL, meta-tags, sitemap.xml)
  * Multilinguisme
  * Autres contenus (vidéos, newsletters, formulaires)
  * Modules du cœur (aggregator, poll, search)

--------------------------------------------------------------------------------

# Administration

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

  * Rapport > Mises à jour disponibles (module _Update Status_)

__ATTENTION : Toujours faire une sauvegarde préalable des fichiers et de la base de données.__

![][1]

--------------------------------------------------------------------------------

## Mises à jour des modules

  * Télécharger la nouvelle version
  * Supprimer l'ancienne version
  * Ajouter la nouvelle version
  * Aller dans « Rapports > Tableau de bord »
  * Repérer la ligne « Mises à jour de la base de données »
  * Si une mise à jour est nécessaire suite aux modifications, un lien apparait
  * Cliquer sur le lien et suivre les instructions

--------------------------------------------------------------------------------

## Mises à jour du cœur

  * Télécharger la nouvelle version
  * Copier/coller sur l'ancienne version
  * Aller dans « Rapports > Tableau de bord »
  * Repérer la ligne « Mises à jour de la base de données »
  * Si une mise à jour est nécessaire suite aux modifications, un lien apparait
  * Cliquer sur le lien et suivre les instructions

--------------------------------------------------------------------------------

## DRUpal SHell

  * [https://github.com/drush-ops/drush][2]

  * Exécution d'installations et de mises à jour en ligne de commande
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

  * Traditionnelle - Partage des modules
    * Décompresser Drupal
    * Créer les répertoires correspondant à vos noms des domaines dans /sites
    * Copier le contenu de /sites/default dans ces nouveaux répertoires
    * Lancer l'installation classique via le navigateur

  * Module _Domain Access_ - Partage des données
    * Basé sur une unique instance (même base de données, même code)
    * Facilité d'administration
    * Partage de contenus, utilisateurs, blocs, etc.

--------------------------------------------------------------------------------

## Performance

  * Activer le cache
    * Fonctionne très bien pour les anonymes
  * Activer l'aggrégation
  * Modules avancés
    * _Views content cache_
    * _Memcache_
    * _Entity cache_
  * Intégration Varnish, Redis, CDN, etc.

--------------------------------------------------------------------------------

# Référencement

--------------------------------------------------------------------------------

## Ré-écriture des URL

  * Modules path (core) et pathauto
  * Recherche et métadonnées > Alias d'URL
  * Gestion de la ré-écriture automatique
    * Selon les types de contenu
    * Selon la taxonomie
  * Régénération d'URL en batch
  * Création à partir de tokens

--------------------------------------------------------------------------------

## Module Token

Sorte de « balises » permettant l'affichage de données variables en fonction
du contexte :

  * Global
    * Nom du site
    * Date actuelle
  * Node
    * Titre
    * Champs
    * Dates (création, modification)
  * Utilisateur
    * Nom d'utilisateur
    * Date de dernière connexion
  * ...

--------------------------------------------------------------------------------

## Module meta-tag

  * Métadonnées intégrées au code HTML des pages du site
  * À définir pour chaque contenu
  * Paramétrage spécifique pour la page d'accueil
  * Possibilité d'ajouter de nombreux tags

--------------------------------------------------------------------------------

## Module XMLsitemap

Génération d'un fichier sitemap.xml à la racine du site :

  * contient les URL du site à destination des robots de référencement
  * paramétrable afin de définir quelles pages sont à inclure ou exclure
  * reconstruit automatiquement au lancement du cron

![][5]

--------------------------------------------------------------------------------

## Autres modules

### Module Google Analytics

  * Code à renseigner
  * Script ajouté à toutes les pages

### Module Schema.org

  * Métadonnées pour l'affichage dans les résultats de recherche
  * Basé sur RDF

### Module SEO Checklist
### Module Search 404
### Redirect - Global Redirect

--------------------------------------------------------------------------------

# Multilinguisme

--------------------------------------------------------------------------------

## Introduction

  * Installation du module _I18n_ (_Internationalization_)
    * Activation du module et des sous-modules
    * Ajout d'une langue et configuration
    * Configuration > Régionalisation et langues > Langues

> Traduction au niveau du contenu

  * Autre possibilité : _Entity Translation_
    * Pratique pour les nœuds
    * Moins pour les menus, blocs, taxonomie, ...
    * Inclus dans Drupal 8

> Traduction au niveau des champs

--------------------------------------------------------------------------------

## Traduire les nœuds

  * Onglet « Traduire » pour chaque contenu
    * Tableau de synthèse du statut de traduction pour toutes les langues
  * Ajout d'une traduction :
    * par le lien « Ajouter » sur le tableau de synthèse
    * par la création d'un contenu en ajoutant sa référence dans la partie
      « Select translations for... »

![][6]

--------------------------------------------------------------------------------

## Traduire les blocs

  * Choix de la langue
  * Paramètres de visibilité : spécifier les chemins des contenus traduits où
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
    * Créer un item par langue dans le même menu

--------------------------------------------------------------------------------

## Traduire les variables

  * Nom du site
  * Slogan
  * Mails

--------------------------------------------------------------------------------

# Autres contenus

--------------------------------------------------------------------------------

## Media dans l'éditeur wysiwyg

  * Module _Media_
  * Gestion centralisée de tous les médias (images, vidéos, audio, flash)
  * Accès à la bibliothèque pour réutilisation
  * Facilité d'utilisation

![][11]

--------------------------------------------------------------------------------

## Autres modules de media

  * Alternatives à _Media_
    * _Scald_
    * _Asset_

  * Module _Video_
    * Permet de créer des champ de type vidéo dans les types de contenu

  * Module _MediaFront_
    * Champ vidéo et personnalisation du lecteur

--------------------------------------------------------------------------------

## Newsletter

  * Module _Simplenews_
    * Gestion des abonnements
    * Gestion des envois instantanés ou asynchrones
    * Gestion de plusieurs catégories de newsletter

  * Gestion des souscriptions seules
    * _Simple Subscription_
    * _Mailchimp_

--------------------------------------------------------------------------------

## Formulaires

  * Module _Webform_
  * Création/gestion intuitive des champs
  * Visualisation/export des soumissions

![][12]

![][13]

--------------------------------------------------------------------------------

# Modules du cœur

--------------------------------------------------------------------------------

## Modules du cœur de Drupal

  * _Aggregator_ (Flux RSS)
    * _Feeds_ pour aller plus loin

  * _Poll_ (Sondage)
    * _Webform_, _Advanced Poll_

  * _Search_
    * _Search API_, _Solr_, ...

--------------------------------------------------------------------------------

## Mise production d'un site Drupal

  * Transférer fichiers et données
  * Attention au fichier _settings.php_
  * Versionnement (Git approprié)
  * _Pathologic_ pour réparer les chemins cassés

Pendant le développement :

  * _Stage File Proxy_ pour récupérer les fichiers depuis le site de production
  * _Reroute Email_ pour désactiver les e-mails
  * _Masquerade_ pour se faire passer pour un autre utilisateur
  * _Administration menu_

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

