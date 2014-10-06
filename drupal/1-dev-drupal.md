
# Formation Développement Drupal

--------------------------------------------------------------------------------

# Qui suis-je ?

<center>
<h2>Sébastien Corbin</h2>

<h2>@SebCorbin sur le web</h2>

<h2>Développeur Drupal depuis 2009</h2>
</center>

.fx: larger

--------------------------------------------------------------------------------

# Objectifs de la formation
  * Appréhender l'environnement de développement Drupal
  * Comprendre les concepts et l'API Drupal 
  * Modifier le comportement d'un module existant 
  * Créer un module
  * Créer un profil d'installation
# Prérequis
  * Connaitre PHP et avoir développé quelques scripts
  * Avoir construit un site avec Drupal
  * Notions de HTML, CSS, JavaScript et requêtes SQL.

--------------------------------------------------------------------------------

# Planning

--------------------------------------------------------------------------------

# 1er jour
  * Environnement de développement
  * Quelques outils utiles (Drush, Git, Devel)
  * Bonnes pratiques, standards de code, documentation
  * Architecture de Drupal
  * Les concepts de base
  * Création du squelette d'un module
  * Les premiers hooks
# 2ème jour
  * Les différentes API
  * Les nœuds, le contenu et les droits d'accès
  * L'alteration des modules

--------------------------------------------------------------------------------

# 3ème jour
  * La form API
  * Les mails
  * Créer un thème basique
  * Les profils d'installation

--------------------------------------------------------------------------------

# Environnement de développement

.fx: alternate

--------------------------------------------------------------------------------

# Le serveur Web

  * xAMP (Apache, MySQL, PHP) conseillé
  * D'autres possibilités : Oracle, IIS, PostgreSQL

  * Liste des languages utilisés :
    * SQL
    * PHP
    * Javascript
    * HTML
    * CSS

.notes: faire un tour de table des compétences et de l'expérience PHP

--------------------------------------------------------------------------------

# TP: Installer Drupal 7

  * Télécharger la dernière version française depuis <http://drupalfr.org>
  * Installer le profil d'installation Standard
  * Paramètres
    * Nom du site : Formation
    * Adresse de courriel : formation@example.org
    * Utilisateur : admin
    * Mot de passe : admin
  * Désactiver les modules
    * update
    * overlay
    * shortcut
    * color

.fx: tp

--------------------------------------------------------------------------------

# L'éditeur de code

  * Le meilleur est celui que vous maitrisez

  * Différence IDE/Editeur

  * Possibilité de télécharger des configurations

  * Exemples
    * Eclipse
    * Netbeans
    * PHPStorm
    * SublimeText
    * Vim

.notes: Autocomplétion - XDebug - Refactoring - Erreurs de syntaxe

--------------------------------------------------------------------------------

# Les standards de codage

  * Indentation, espaces

  * Nommage des fonctions, constantes

  * Tags `<?php`

  * A connaître pour comprendre et être compris

<center><https://drupal.org/coding-standards></center>

--------------------------------------------------------------------------------

# TP: Configuration de Netbeans
  * General -> Content Types -> Text -> PHP Content type 
    * *.engine, *.theme, *.install, *.inc, *.module, *.test 
  * General -> Editors -> Text Editors 
    * « Insert Spaces for tabs » 
  * PHP -> Code Style -> Formatter 
    * « Tab policy » : spaces 
    * « Indentation size » : 2 
  * Properties 
    * « Text File Encoding » : UTF-8 
    * « New text file delimiter » : Unix 
  * XDebug 

.fx: tp

--------------------------------------------------------------------------------

# Les modules Drupal utiles au développement
  * _Features_: transférer la configuration dans le code
  * _Devel_ : debug et informations sur les données
  * _Drush_ : administration (DRUpal SHell)
  * _Drush Make_ : téléchargement de modules et librairies
  * _Coder_ : revue de code
  * _Entity_ : API sur les entités
  * _LESS_ : Le CSS en plus simple
  * _Admin Menu_ : flusher les caches rapidement
  * _Masquerade_ : changer d'utilisateur sans se déconnecter
  * _Example_ : démonstrations de l'utilisation de l'API

--------------------------------------------------------------------------------

# TP: Drush
  * Installer Drush 
  * Regarder la liste des commandes 
  * Installer un module (features) 
  * Regarder à nouveau la liste des commandes 
  * Sauvegarder la base de données 

.fx: tp

--------------------------------------------------------------------------------

# Git et la gestion de versions

  * Utilisé par beaucoup de développeurs dans le milieu du web

  * Très utile pour patcher des modules car utilisé pas la communauté Drupal et
  sur drupal.org

  * Une connaissance basique de quelques commandes suffit

    * git clone
    * git add
    * git commit
    * git reset
    * git diff

--------------------------------------------------------------------------------

# L'architecture de Drupal

.fx: alternate

--------------------------------------------------------------------------------

# Présentation de l'arborescence

  * profils d'installation
  * modules du core
  * sites
  * themes du core

Où travailler ?

Le hack du core et l'avenir des chatons

.fx:larger

--------------------------------------------------------------------------------

# Les modules du core
  * Les requis : _Node, User, Field_ (+storage), _System, Filter, Text_

  * Les quasi-requis : Block, Locale, Image, Menu, Path

  * Les utiles : Comment, Content translation, Contextual links,
  Field UI, Database Logging, File, List, Options, Number, Taxonomy, Update

  * Les autres

--------------------------------------------------------------------------------

# Les librairies JS

  * jQuery 1.4.4
  * jQuery UI 1.8.7
  * jQuery once (callback evenement unique)
  * jQuery form (envoi de form en ajax)
  * jQuery BBQ (hashchange)
  * jQuery Cookie (cookie JS)
  * Farbtastic (colorpicker)

Pour une version plus récente, utiliser le module jQuery Update

--------------------------------------------------------------------------------

#TP: Jetons un œil à la base de données

  * se familiariser avec PhpMyAdmin

  * identifier les tables des modules actuellement activés

  * identifier les autres : cache, variable, registry

  * identifier la table system et son utilité

.fx: tp

--------------------------------------------------------------------------------

# Qu'est ce qu'un module ?
  * `.info` (<https://drupal.org/node/542202>)
    * `name`
    * `core`
    * `description`
  * `.module`
  * `.install` facultatif
  * `.test` facultatif
  * les fichiers `.inc`


--------------------------------------------------------------------------------

# Fil rouge : le module gold

  * Administrer les types de contenus concernés par le statut gold
  * Affecter un statut gold à contenu
  * Lister les contenus avec le statut gold
  * Créer deux permissions pour les rôles, une pouvant affecter le status gold
  aux contenus et l'autre le voir
  * Créer un style d'image pour illustrer les contenus gold
  * Créer un bloc affichant si l'utilisateur a la permission de voir les
  contenus gold
  * Altérer le formulaire d'édition de nœud pour ajouter le statut gold
  * Envoyer un mail aux utilisateurs ayant la permission de voir les contenus
  gold lorsque qu'un nouveau contenu gold apparait sur le site
  * Créer une fonction de theme pour afficher le statut gold d'un nœud
  * Créer des tests pour vérifier le bon fonctionnement du module

Créer ce module : il doit apparaître dans la liste des modules.

.fx: tp

--------------------------------------------------------------------------------

# La création d'un module

.fx: alternate

--------------------------------------------------------------------------------

# Avant de commencer

## Votre bible : api.drupal.org

## Votre guide : modules `example`

# Les hooks 
  * Poids des modules et altération
  * Répondent à des déclencheurs
  * Implémenter `hook_form_alter()` donnera `mon_module_form_alter()`
  * Liste des hooks implémentés grâce à `Devel`
  * Les implémentations sont mise en cache
  * Des hooks peuvent être déclarés par des modules contrib
  * Rappel: on ne « hack » JAMAIS le code <small>(sauf en cas de module buggué)</small>

--------------------------------------------------------------------------------

# TP: Notre premier hook

  * Implémenter le `hook_permission()`

  * Créer les deux permissions

  * Vider le cache

  * Créer un role contributeur pouvant affecter le statut gold

  * Créer un role premium pouvant voir le statut gold

  * Créer un utilisateur pour chaque rôle

.fx: tp

--------------------------------------------------------------------------------

# Création d'un bloc
    !php
    function hook_block_info() {
      $blocks['syndicate'] = array(
        'info' => t('Syndicate'),
        'cache' => DRUPAL_NO_CACHE,
      );
      return $blocks;
    }
    function hook_block_view($delta = '') {
      if ($delta == 'syndicate') {
        return array(
          subject => '',
          content => '', // (Render array ou HTML) 
        );
      }
    }
    function hook_block_view_alter(&$data, $block) {}
    function hook_block_view_MODULE_DELTA_alter(&$data, $block) {}

--------------------------------------------------------------------------------

# Fonctions de theme et Render Arrays
  * Exemples de fonctions de `theme()` ([liste complete](
https://api.drupal.org/api/drupal/modules%21system%21theme.api.php/group/themeable/7))
    * table
    * item_list
    * pager
    * links
  * Render array: Association de données et d'une fonction de thème

        !php
        $table_element = array(
            '#theme'  => 'table', // Propriété préfixée par # sinon élément enfant
            '#header' => $header,
            '#rows'   => $rows,
            '#empty'  => t('Your table is empty'),
        );
        print drupal_render($table_element); // Quasi-automatiquement appelé
                                             // par les hooks
Documentation <http://drupal.org/node/930760> et le module `render_example`

--------------------------------------------------------------------------------

# Gestion des nodes et des users

Quelques globales et fonctions de l'API à connaitre :

  * `global $user` : utilisateur actuellement connecté
<small>(modifier avec prudence !)</small>
  * `node_load()` et `node_load_multiple()` pour charger des nœuds
  * `node_save()` pour enregistrer un nœud
  * `user_load()` et `user_load_multiple()` pour charger des utilisateurs
  * `user_save()` pour enregistrer un utilisateur
  * `REQUEST_TIME` : timestamp à l'appel de la page

--------------------------------------------------------------------------------

# TP: Création d'un bloc

  * Créer un bloc _Accès premium_ qui affiche le nom de l'utilisateur actuellement
  connecté ainsi que son accès au contenu gold

  * Faire une version sans render array, puis avec en l'entourant d'une balise
  `<h2>`

  * Le placer dans la sidebar pour tester

  * Attention au cache

.fx: tp

--------------------------------------------------------------------------------

# Système de menus
  * Différence path / alias 
  * Différence lien de menu / routage
  * Permissions 
  * Arguments pouvant être chargés à la volée
  * Type de menu 
    * `MENU_NORMAL_ITEM` (~ lien) 
    * `MENU_LOCAL_TASK` (~ onglet) 
    * `MENU_CALLBACK` (~ url)
  * Fichier d'emplacement

        !php
        function mymodule_menu() {
          $items['abc/def'] = array(
            'page callback' => 'mymodule_abc_view',
          );
          return $items;
        }

--------------------------------------------------------------------------------

# Gestion de la base de données
  * `db_query()` permet d'exécuter du SQL directement mais utiliser
    * `{table_name}`qui permet la gestion de prefixe
    * les placeholders pour les failles de sécurité
  * Utiliser `foreach()` pour parcourir les résultats

## DBTNG
    !php
    $results = db_select('contact', 'c')
                  ->fields('c')
                  ->condition('created', REQUEST_TIME)
                  ->execute()
                  ->fetchAssoc();
    foreach ($results as $result) {
      // faire qqch
    }
    // db_insert()
    // db_delete() 

--------------------------------------------------------------------------------

# Gestion des URLs et des paths

Quelques globales et fonctions de l'API à connaitre :

  * `global $base_url` et `base_path()`
  * `url()` et `l()`
  * `drupal_goto()`
  * `drupal_get_destination()`
  * `drupal_get_path()` (module, theme) 

--------------------------------------------------------------------------------

# TP: Création de page

Créer une page _Utilisateurs premium_ listant les utilisateurs du site ayant un
accès premium dans un tableau avec _Identifiant_, _Nom_, _Lien vers son profil_

  * Créer une page

  * Récupérer les roles ayant la permission de voir le contenu gold

  * Récupérer les utilisateurs ayant ces rôles

  * Les afficher dans un tableau

Les callback doivent être situées dans un autre fichier que le .module

Attention au cache

.fx: tp

--------------------------------------------------------------------------------

# La Form API

.fx: alternate

--------------------------------------------------------------------------------

Un formulaire est une structure déclarative composée d'éléments de la form API.
La majeure partie des traitements est effectuée par celle-ci, rendant la
création ou la modification de formulaire rapide et sécurisée.


Référentiel des composants disponibles [sur api.drupal.org](
http://api.drupal.org/api/drupal/developer!topics!forms_api_reference.html/7)

    !php
    $form = drupal_get_form('my_module_example_form'); // Appel

    // Déclaration
    function my_module_example_form($form, &$form_state) {
      $form['submit'] = array(
        '#type' => 'submit',
        '#value' => t('Submit'),
      );
      return $form;
    }
    function my_module_example_form_validate($form, &$form_state) {
      // Logique de validation.
    }
    function my_module_example_form_submit($form, &$form_state) {
      // Traitement des données soumises.
    }

--------------------------------------------------------------------------------

# Traitement des données

Les données soumises et validées sont contenues dans `$form_state['values']`.

Après exécution du `_submit()`, l'utilisateur est redirigé vers le formulaire
vidé de ses valeurs, ou bien vers une page définie par `$form_state['redirect']`

Chaque formulaire a un identifiant unique qui permet de l'altérer facilement par
les autres modules.

  * Possibilité de créer des formulaires multi-étapes.
  * Validation par élément
  * Possibilité de créer de nouveaux type d'éléments
  * \#ajax (<http://drupal.org/node/752056>) permet de faire de l'Ajax sans
  ecrire de JS
  * \#autocomplete_path 

Schéma de workflow complet : https://drupal.org/files/fapi_workflow_7.x_v1.1.png

--------------------------------------------------------------------------------

# Gestion de variables globales
  * `variable_set('name', value)` pour définir
  * `variable_get('name', default_value)` pour récupérer
  * `variable_del('name')` pour supprimer

--------------------------------------------------------------------------------

# TP : Form API

  * Créer un formulaire listant les types de contenu associés à une checkbox

  * Valider le fait qu'un contenu doit au moins être coché

  * A la soumission enregistrer les valeurs dans une variable globale et les
  réafficher

.fx: tp

--------------------------------------------------------------------------------

# Manipuler les fichiers et les images

.fx: alternate

--------------------------------------------------------------------------------

# La File API

Un fichier n'est pas une entité ! (malheureusement)

Différence entre fichiers gérés et non gérés

Différence entre fichiers privés et fichiers publics

API complète <https://api.drupal.org/api/drupal/includes%21file.inc/group/file/7>

## Les streams wrappers

Un stream est un chemin, une URI, vers un fichier interne ou externe :

  * public://
  * private://

--------------------------------------------------------------------------------

# Fournir un effet sur les images

    !php
    function hook_image_effect_info() {
      $effects['mymodule_resize'] = array(
        'label' => t('Resize'),
        'help' => t('Resize an image to an exact set of dimensions.'),
        'effect callback' => 'mymodule_resize_effect',
        'dimensions callback' => 'mymodule_resize_dimensions',
        'form callback' => 'mymodule_resize_form',
        'summary theme' => 'mymodule_resize_summary',
      );

      return $effects;
    }


--------------------------------------------------------------------------------

# Fournir un style par défaut

    !php
    function hook_image_default_styles() {
      $styles['mymodule_preview'] = array(
        'label' => 'My module preview',
        'effects' => array(
          array(
            'name' => 'image_scale',
            'data' => array(
              'width' => 400,
              'height' => 400,
              'upscale' => 1,
            ),
            'weight' => 0,
          ),
        ),
      );

      return $styles;
    }

--------------------------------------------------------------------------------

# TP: Créer un style d'image pour nos contenus gold

Celui-ci nous servira pour les images qui seront sur les articles gold

--------------------------------------------------------------------------------

# Schema API

  * Gère la base de données
  * Se situe dans le fichier .install
  * `hook_schema()` -> crée une base
  * `hook_schema_alter()` déclare une modification (mais ne la réalise pas)
  * API de la structure <https://drupal.org/node/146866>
  * Fonctions de l'API <https://drupal.org/node/150223>
  * Les `hook_update_N()` servent à réaliser des actions sur la structure ou
  les données
  * Très utile pour les mises à jour en production, et le test de celles-ci


--------------------------------------------------------------------------------

# TP: Créer une table gold

Via l'API

Deux colonnes :

  * nid
  * status

--------------------------------------------------------------------------------

# TP: Altérer le formulaire de noeuds
  * Ajouter la checkbox

  * Enregistrer la valeur dans notre table à l'enregistrement

  * Rappels 
    * `hook_form_alter(&$form, $form_state, $form_id)`
    * Debug : `drupal_set_message('<pre>'.print_r($var, 1).'</pre>')`

.fx: tp

--------------------------------------------------------------------------------

# TP : Accès aux nœuds

  * L'API Node Access

  * Déclarer notre hook_node_access()`


--------------------------------------------------------------------------------

# Envoi de mails

    !php
    function hook_mail($key, &$message, $params) {
      $account = $params['account'];
      $context = $params['context'];
      $node = $params['node'];
      $variables += array(
        '%uid' => $node->uid,
        '%node_url' => url('node/' . $node->nid, array('absolute' => TRUE)),
        '%node_type' => node_type_get_name($node),
        '%title' => $node->title,
        '%teaser' => $node->teaser,
        '%body' => $node->body,
      );
      $subject = strtr($context['subject'], $variables);
      $body = strtr($context['message'], $variables);
      $message['subject'] .= str_replace(array("\r", "\n"), '', $subject);
      $message['body'][] = drupal_html_to_text($body);
    }

Notion de tokens (jetons)

--------------------------------------------------------------------------------

# Le thème

  * hook_theme() 

  * Ajouter un fichier CSS / JS à votre module 

  * Le javascript dans Drupal 

  * Créer un thème

--------------------------------------------------------------------------------


# hook_theme()

    !php
    function forum_theme() {
    	return array(
    		'forums' => array(
    			'template' => 'forums',
    			'variables' => array(
    				'forums' => NULL,
    				'topics' => NULL,
    				'parents' => NULL,
    				'tid' => NULL,
  					'sortby' => NULL,
    				'forum_per_page' => NULL,
    			),
    		),
    	);
    }

    $output = theme('forums', $forums, $topics, $parents, 17, 'ASC', 25);

--------------------------------------------------------------------------------


# Ajout de JS / CSS

  * drupal_add_js() 
    * OU module.info (scripts[]) 
    * hook_js_alter() 
  * drupal_add_css() 
  * drupal_add_library
  * \#attached[]
  * Notion de groupes 
    * JS (JS_LIBRARY, JS_DEFAULT, JS_THEME)
    * CSS (CSS_SYSTEM, CSS_DEFAULT, CSS_THEME)


--------------------------------------------------------------------------------

# Le javascript

  * Bonnes pratiques 
  * Jquery (inclus dans Drupal) 
  * Le « Drupal way » 

## Bonnes pratiques JS

  * « Unobtrusive javascript » 
    * Surcouche 
    * Comportements dégradés 
    * Accessibilité 


--------------------------------------------------------------------------------

# Les profils d'installation

Quelques exemples

Une bonne pratique de développement

TP: créer un profil avec notre module gold

--------------------------------------------------------------------------------

# Aller plus loin

Drush make

Les performances

Features

--------------------------------------------------------------------------------

# Merci
