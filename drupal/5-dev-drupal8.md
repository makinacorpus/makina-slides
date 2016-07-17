
# Formation Développement Drupal

![][4]

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
  * Notions de HTML, CSS, JavaScript et requêtes SQL

--------------------------------------------------------------------------------

# 1er jour
  * Rappels PHP
  * Environnement de développement
  * Quelques outils utiles (Drush, Git, Devel)
  * Bonnes pratiques, standards de code, documentation
  * Architecture de Drupal & concepts de base
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

<br/>
<br/>
<br/>

<center>
# Slides disponibles en ligne

# <http://makinacorpus.github.io/makina-slides/drupal8-dev.html>
</center>

--------------------------------------------------------------------------------

# Rappels PHP

  * PHP 5.5.9 minimum (<http://www.phptherightway.com/>)
  * Programmation orientée Object (<http://lornajane.net/posts/2012/introduction-to-php-oop>)
  * Namespaces (<https://www.sitepoint.com/php-53-namespaces-basics/>)
  * Annotations
  * Injection de dépendances

.fx: alternate

--------------------------------------------------------------------------------

# Les normes PHP

  * Viennent du PHP Framework Interoperability Group (FIG)
  * Différentes normes
    * PSR-0 : autoloader standard
    * PSR-1 : normes de codage de base (Drupal les suit presque)
    * PSR-2 : normes de codage plus poussées (Drupal les suit presque)
    * PSR-3 : interface du logger (pas implémentée dans Drupal)
    * PSR-4 : autoloader amélioré (choisi par Drupal) : <https://www.drupal.org/node/2156625>

--------------------------------------------------------------------------------

# Symfony (<http://symfony.com/>)

  * Le plus populaire des frameworks PHP aujourd'hui (<http://symfony.com/doc/current/index.html>)
  * Ensemble de composants réutilisables
  * Certains sont réutilisés par Drupal

![][3]

--------------------------------------------------------------------------------

<h2>YAML</h2>

    !yaml
    key: 'value'
    tableau:
      - valeur 1
      - valeur 2

--------------------------------------------------------------------------------

# Composer (<https://getcomposer.org>)

  * Gestionnaire de dépendances utilisé par la communauté PHP
  * Installation uniquement locale au projet
  * composer.json
  * "composer install"
  * composer.lock
  * Contient un autoloader

<pre><code>
  curl -sS https://getcomposer.org/installer | php
  mv composer.phar /usr/local/bin/composer
</code></pre>

  <https://bojanz.wordpress.com/2015/09/18/d8-composer-definitive-intro/>

--------------------------------------------------------------------------------

# Environnement de développement

.fx: alternate

--------------------------------------------------------------------------------

# Le serveur Web

  * xAMP (Apache, MySQL, PHP) conseillé
  * D'autres possibilités : Nginx / IIS, PostgreSQL
  * Liste des languages utilisés :
    * SQL
    * PHP
    * Javascript
    * HTML
    * CSS

On utilisera dans cette formation Acquia Dev Desktop qui permet d'installer un
environnement de développement avec tous les pré-requis Drupal.

.notes: faire un tour de table des compétences et de l'expérience PHP, présenter Acquia, Dries et pourquoi AcquiaDevDesktop est pratique

--------------------------------------------------------------------------------

# TP: Installer Drupal 8

  * Choisir la distribution Drupal 8.x simple dans Acquia Dev Desktop
  * Installer le profil d'installation Standard
  * Paramètres
    * Nom du site : Formation
    * Adresse de courriel : formation@example.org
    * Utilisateur : admin
    * Mot de passe : admin

.fx: tp
.notes: présenter les distributions

--------------------------------------------------------------------------------

# L'éditeur de code

  * Le meilleur est celui que vous maitrisez
  * Différence IDE/Editeur simple :
    * Autocomplétion
    * XDebug
    * Refactoring
    * Erreurs de syntaxe
  * Possibilité de télécharger des configurations
  * Exemples : PHPStorm / Eclipse / Netbeans / Atom / Vim

--------------------------------------------------------------------------------

# Les standards de codage*

  * Indentation, espaces : lisibilité du code
  * Nommage, toujours commencer par le nom système : éviter les conflits
    * fonctions
    * constantes
    * variables persistantes
    * classes
    * fichiers
  * Tags `<?php` non fermés : éviter l'envoi du buffer

<strong>A connaître pour comprendre et être compris</strong>

<center>
# <https://drupal.org/coding-standards>
</center>

\* <small>basés sur le standard PEAR</small>

--------------------------------------------------------------------------------

# TP: Configuration de PHPStorm
  * Ouvrir le dossier Drupal dans PHPStorm
  * Afficher les messages de journal de PHPStorm
  * Cliquer sur "Enable Drupal support" et configurer le chemin
  * Cliquer sur "Fix extensions"

Avantages :

  * code style implémenté
  * navigation dans les hooks (appels et déclarations)
  * installation d'XDebug facile (<http://redcrackle.com/blog/drupal-8/phpstorm>)

.fx: tp

--------------------------------------------------------------------------------

# Les modules Drupal utiles au développement
  * _Features_: transférer la configuration dans le code
  * _Devel_ : debug et informations sur les données
  * _Drupal Console_ : générateur de code
  * _Drush_ : administration (DRUpal SHell) & téléchargement de modules et librairies
  * _Coder_ : revue de code
  * _Masquerade_ : changer d'utilisateur sans se déconnecter
  * _Examples for developpers_ : démonstrations de l'utilisation de l'API
  * Ne pas utiliser les caches durant le développement (<https://www.drupal.org/node/2598914>)

--------------------------------------------------------------------------------

# TP: Drush
  * Lancer Drush 
  * Regarder la liste des commandes 
  * Installer un module (features) 
  * Regarder à nouveau la liste des commandes 
  * Sauvegarder la base de données 
  * Installer les modules utiles au développement : devel, masquerade, examples
  * Desactiver le module help

.fx: tp

--------------------------------------------------------------------------------

#TP : Console
  * Intaller la console Drupal
  * Vérifier que c'est correctement installé
  * Regarder la liste des commandes (drupal list)

![][5]

.fx: tp

--------------------------------------------------------------------------------

# Git et la gestion de versions

  * Utilisé par beaucoup de développeurs dans le milieu du web

  * Très utile pour patcher des modules car utilisé par la communauté Drupal et
  sur drupal.org

  * Une connaissance basique de quelques commandes suffit

    * git clone
    * git add
    * git commit
    * git diff

  * Possibilité d'avoir une interface graphique : SourceTree, Gitg, GitLab, GitHub

--------------------------------------------------------------------------------

# L'architecture de Drupal

.fx: alternate

--------------------------------------------------------------------------------

# Présentation de l'arborescence

<img src="img/archi_fichiers8.png" style="float:left;padding:.5em 1em 0"/>
<div style="font-size: 0.95em;line-height: 1.25em;padding-top: 0.3em;">
Cœur de Drupal<br>
Modules de tous les sites<br>
Profils d'installations<br>
Répertoire spécifique au site<br>
Répertoire d'upload par défaut<br>
Fichiers de configuration<br>
-<br>
-<br>
-<br>
-<br>
-<br>
Thèmes de tous les sites<br>
</div>
<br><br>
Où travailler ? Dans un profil d'installation custom ou dans un
sous-repertoire `custom`

<center>
## <u>/!\</u> Le hack du core et l'avenir des chatons
</center>

--------------------------------------------------------------------------------

<img src="img/render_pipeline.png" class="single-image"/>

--------------------------------------------------------------------------------

<img src="img/render_pipeline_high_level.png" class="single-image"/>

--------------------------------------------------------------------------------

#TP: Jetons un œil à la base de données

  * se familiariser avec PhpMyAdmin
  * identifier les tables des modules actuellement activés
  * identifier les autres : cache, variable, registry
  * identifier la table contenant la configuration
  * <https://www.drupal.org/node/1785994>

.fx: tp

--------------------------------------------------------------------------------

# Qu'est ce qu'un module ?
  * `.info.yml` (<https://www.drupal.org/node/2000204>)
    * `name`
    * `core`
    * `description`
  * `.module` (souvent vide en D8)
  * `.install` facultatif (configuration désormais indépendante)
  * répertoire "config/install" pour la configuration
  * répertoire "src" pour les Plugins, Controller, Form, ...

--------------------------------------------------------------------------------

# Structure d'un module

![][2]

<center><https://www.drupal.org/node/2560405></center>

--------------------------------------------------------------------------------

# Fil rouge : le module Premium

  * Créer deux permissions pour les rôles, une pouvant affecter le status premium
  aux contenus et l'autre le voir
  * Créer un bloc affichant si l'utilisateur a la permission de voir les
  contenus premium
  * Administrer les types de contenus concernés par le statut premium
  * Altérer le formulaire d'édition de nœud pour ajouter le statut premium
  * Envoyer un mail aux utilisateurs ayant la permission de voir les contenus
  premium lorsque qu'un nouveau contenu premium apparait sur le site
  * Lister les contenus avec le statut premium
  * Créer un style d'image pour illustrer les contenus premium
  * Créer une fonction de theme pour afficher le statut premium d'un nœud
  * Créer des tests pour vérifier le bon fonctionnement du module

Créer ce module : il doit simplement apparaître dans la liste des modules.

.fx: tp

--------------------------------------------------------------------------------

# La création d'un module

.fx: alternate

--------------------------------------------------------------------------------

# Avant de commencer

## Votre bible : api.drupal.org

  Recense toutes les fonctions de Drupal, et leur documentation. Un IDE aura
  cette même documentation dans le code.

  Aborde certains topics en profondeur : form API, schema API, hooks, etc

  <https://api.drupal.org/api/drupal/core%21core.api.php/group/extending/8.1.x>

<br>
## Votre guide : modules `examples`

  Pour chaque concept de Drupal, des exemples concrets d'utilisation (ajax, form,
  blocks, cache, render, cron, dbtng, email, menu, node_access, theming, ...).

  Ils sont fonctionnels : on peut les activer et voir leur impact en terme
  d'interface.

  Très bien documentés, ne pas hésiter à lire, comprendre et reprendre le code
  de ces modules.

--------------------------------------------------------------------------------

# Les hooks 

  * Concept historique Drupal
  * Implémenter `hook_form_alter()` donnera `mon_module_form_alter()`
  * Poids des modules et altération
  * Répondent à des déclencheurs
  * Des hooks peuvent être déclarés par des modules contrib
  * Rappel: on ne « hack » JAMAIS le code <small>(sauf en cas de module bogué)</small>
  * Tend à disparaître avec Drupal 8 (Plugins, yml, events), mais existe encore...
  * Les implémentations sont mise en cache
  * Liste des hooks <https://api.drupal.org/api/drupal/core!core.api.php/group/hooks/8>

--------------------------------------------------------------------------------

# Les permissions

  * Créer un fichier `.permissions.yml`
  * Créer les deux permissions
  * Vider le cache
  * Créer un role contributeur pouvant affecter le statut premium
  * Créer un role premium pouvant voir le statut premium
  * Créer un utilisateur pour chaque rôle

.fx: tp

--------------------------------------------------------------------------------

# Les plugins & les annotations

  * Plugins : <https://www.drupal.org/node/2087839>
  * Annotations très utilisé dans le cœur : pour tous le plugins (block, entre autres)
  * <https://api.drupal.org/api/drupal/core%21core.api.php/group/annotation/8.1.x>

--------------------------------------------------------------------------------

# Les blocs

  * fichier src/Plugin/Block/TestBlock.php
  * Déclaration

<code><pre>
    namespace Drupal\mon_module\Plugin\Block;
    use Drupal\Core\Block\BlockBase;
    /**
     * Provides a 'Test' block.
     * 
     * @Block(
     *   id = "test_block",
     *   admin_label = @Translation("Test block"),
     * )
     */
    class TestBlock extends BlockBase {
      public function build() {
        return array('#markup' => '',);
      }
    }
</pre></code>

    // Altération
    function hook_block_build_BASE_BLOCK_ID_alter(&$build, $block) {}

--------------------------------------------------------------------------------

# TP: Notre premier bloc

Créer un bloc :

  - dont le titre côté administration est "Statut premium de l'utilisateur"
  - dont le delta (nom machine) est `premium-status`
  - qui affiche "Vous pouvez voir les contenus premium" ou "Vous ne pouvez pas
  voir les contenus premium"

Rappel: \Drupal::currentUser()->hasPermission(); pour vérifier les permissions

Attention au cache d'implementations

.fx: tp

--------------------------------------------------------------------------------

# Render Arrays

Les render arrays sont les blocs constituant une page Drupal. Ce sont des arrays
PHP qui définissent des données (c-a-d la structure) ; On est obligés de
produire des render arrays.
Ceci afin qu'ils puissent être modifiés via les hooks d'altérations ou par la
couche de theming.

Les propriétés sont toujours préfixées par un `#` et la propriété par défaut
est `#markup`, elle permet d'indiquer du balisage simple.
Un render array est converti en HTML avec la fonction `render();`

    !php
    // Un render array simple
    'ma_cle1' => array(
      '#markup' => "<h2>Du texte basique</h2>",
    ),

    // Des propriétés utiles
    'ma_cle2' => array(
      '#markup' => "Du texte basique",
      '#prefix' => '<h2>',
      '#suffix' => '</h2>',
    ),


--------------------------------------------------------------------------------

# Paramètres du render array et propriétés

Une fonction de `#theme` peut être renseignée ainsi que ses paramètres (<https://www.drupal.org/developing/api/8/render/arrays>)

    !php
    // Un render array qui produit un tableau HTML
    'ma_cle1' => array(
      '#theme' => 'table',
      '#header' => $header,
      '#rows' => $rows,
      '#empty' => "Aucune donnée pour ce tableau",
    ),

Des propriétés utiles :

  - `#type`: Le type d'élement
  - `#cache`: contexts, tags, ... /!\
  - `#markup`: Pour fournir directement de l'HTML
  - `#pre_render` / `#post_render`: agit sur le tableau
  - `#prefix` / `#suffix`, `#weight`, `#attached`, `#access`, ...

--------------------------------------------------------------------------------

# TP

Ajouter un '&lt;h3&gt;' autour du bloc précédent

.fx: tp

--------------------------------------------------------------------------------

# TP: Manipuler les render arrays

  Altérer le bloc dans un `hook_block_view_alter()` afin de changer le
  `<h3>` en `<h4>`

.fx: tp

--------------------------------------------------------------------------------

# Système de routage / menus

## Quelques définitions :
  * routage : faire pointer une route (`node/{node}`) à une action (afficher un noeud)
  * chemin (ou path) : route dont les arguments sont définis (ex: `node/123` est 
  un chemin, pointant vers la route `node/{node}` où l'argument est 123)
  * lien de menu : Texte (ou titre) pointant vers un chemin
  * alias : associe un chemin système (`node/123`) vers un chemin arbitraire 
  renseigné par le contributeur (`mon-noeud`)


## Les propriétés d'une route
  * _Permissions
  * Les arguments sont nommés (`{node}`) et peuvent être chargés dans le
  Controller (en les typant avec une classe)
  * Vous pouvez passer des paramètres fixes au controller en les indiquant
  dans la route

--------------------------------------------------------------------------------

# Les controllers

  * fichier src/Controller/ModuleController.php
  * Déclaration

<code><pre>
    namespace Drupal\mon_module\Controller;
    use Drupal\Core\Controller\ControllerBase;
    /**
     * Provides a 'Test' block.
     */
    class ModuleController extends ControllerBase {
      public function abc_view() {
        return array('#markup' => '',);
      }
    }
</pre></code>


--------------------------------------------------------------------------------

  * Type d'élément de menu
    * *.routing.yml -> définit une URL
    * *.links.menu.yml -> lien de menu dans l'arborescence
    * *.links.task.yml -> onglet
    * *.links.action.yml -> "action" (back-office)

  * Paramètres de routage : <https://www.drupal.org/node/2092643>

--------------------------------------------------------------------------------

# Exemples

    !yaml
    #.routing.yml
    mymodule.abc_view:
      path: '/abc/def'
      defaults:
        _title: "My ABC page"
        _controller: "\Drupal\module\Controller\ModuleController::abc_view"
      requirements:
        _permission: 'access my module'

    #.links.menu.yml
    mymodule.abc_view_tab:
      title: 'My ABC page'
      route_name: mymodule.abc_view
      description: 'Displays my ABC page'
      parent: mymodule.abc_view

    #.links.task.yml
    mymodule.abc_view_edit:
      title: 'Edit'
      route_name: mymodule.abc_view_edit
      base_route: mymodule.abc_view

--------------------------------------------------------------------------------

# TP: Création de page

Créer une page _Suis-je Premium ?_ reproduisant le comportement du bloc

  - url : suis-je-premium

Créer une page _Est-il Premium ?_ affichant la même chose, mais avec en
argument l'uid de l'utilisateur

  - url d'exemple : est-il-premium/2

Créer une page _Page Premium_ avec du contenu "Lorem Ipsum" et ne
s'affichant que si l'utilisateur courant à la permission de voir le contenu
premium

  - url : page-premium

.fx: tp

--------------------------------------------------------------------------------

# Gestion des nodes et des users

Quelques fonctions de l'API à connaitre :

  * `\Drupal::currentUser()` : utilisateur actuellement connecté
<small>(modifier avec prudence !)</small>
  * `Node::load()` et `Node::loadMultiple()` pour charger des nœuds
  * `User::load()` et `User::loadMultiple()` pour charger des utilisateurs
  * $entity->save() pour enregistrer un nœud, un utilisateur, ...

--------------------------------------------------------------------------------

# Gestion de la base de données /!\ en cours de modification /!\

## Requête en base de données

    !php
    $db = \Drupal::database();
    $result = db->select();
    $result = db->insert();
    $result = db->delete();
    $result = db->udpate();
    $result = db->merge();

## Requête sur le modèle objet

    !php
    $ids = \Drupal::entityQuery('user')->condition('name', 'test')->execute();
    $users = User::loadMultiple($ids);

[Documentation complète](https://api.drupal.org/api/drupal/core%21lib%21Drupal%21Core%21Database%21database.api.php/group/database/8.1.x)

--------------------------------------------------------------------------------

## DBTNG : DataBase The Next Generation (issu de Drupal 7)
    !php
    $results = $db->select('contact', 'c')
                  ->fields('c')
                  ->condition('created', REQUEST_TIME)
                  ->execute() // ->fetch*()
                  ;
    foreach ($results as $result) {
      // faire qqch
    }

Récupération de résultats :

  - fetchField() : la première colonne du premier résultat
  - fetchCol() : la première colonne sous forme d'array
  - fetchAssoc() : le premier résultat sous forme d'objet
  - fetchAllAssoc() : tous les résultats sous forme d'objet
  - fetchAllKeyed() : tous les résultats sous forme de tableau indexé par la
  1ere colonne avec pour valeur la 2e

--------------------------------------------------------------------------------

# Gestion des URLs et des paths

## Quelques fonctions

  * $this->redirect('contact.site_page'); -> redirection
  * `global $base_url` -> http://monsite.com
  * `base_path()` -> `/` ou `/mon-dossier-drupal`
  * `drupal_get_path()` (module, theme) -> chemin vers un module ou un thème (`drupal_get_path('module', 'devel')` donne _modules/devel_)

## L'objet URL
    !php
    use Drupal\Core\Url;
    $url = Url::fromRoute('contact.site_page', array())->toString();
    $url = Url::fromUserInput('/contact')->toString();
    $url = Url::fromUri('internal:/contact')->toString();
    $link = \Drupal::l(t('Contact'), $url);

--------------------------------------------------------------------------------

# TP: Création de page

Créer une page _Utilisateurs premium_ listant les utilisateurs du site ayant un
accès premium.

  * Créer une page

  * Récupérer les rôles ayant la permission de voir le contenu premium (dans la
  table `role_permission`)

  * Récupérer les utilisateurs ayant ces rôles (dans la table `users_roles`)

  * Les afficher d'abord dans une liste

  * Modifier pour les afficher dans un tableau avec _Identifiant_,
  _Nom_, _Lien vers son profil_

Attention au cache

.fx: tp

--------------------------------------------------------------------------------

# La Form API

<https://www.drupal.org/node/2117411>

.fx: alternate

--------------------------------------------------------------------------------

Un formulaire est une structure déclarative composée d'éléments de la form API.
La majeure partie des traitements est effectuée par celle-ci, rendant la
création ou la modification de formulaire rapide et sécurisée.


Référentiel des composants disponibles [sur api.drupal.org](
https://api.drupal.org/api/drupal/developer!topics!forms_api_reference.html/8)

    !php
    \Drupal::formBuilder()->getForm('Drupal\mymodule\MyModuleForm');

    // Déclaration
    public function getFormId() {
      return 'my_module_form';
    }
    public function build(array $form, FormStateInterface $form_state) {
      $form['submit'] = array(
        '#type' => 'submit',
        '#value' => t('Submit'),
      );
      return $form;
    }
    public function validate(array &$form, FormStateInterface $form_state) {
      // Logique de validation.
      $form_state->setErrorByName('form_field', 'message');
    }
    public function submit(array &$form, FormStateInterface $form_state) {
      // Traitement des données soumises.
    }

--------------------------------------------------------------------------------

# Traitement des données

Les données soumises et validées sont contenues dans `$form_state->getValue('key')`.

Après exécution du `_submit()`, l'utilisateur est redirigé vers le formulaire
vidé de ses valeurs, ou bien vers une route définie par `$form_state->setRedirectUrl($url)`

Chaque formulaire a un identifiant unique qui permet de l'altérer facilement par
les autres modules.

  * Validation par élément (`#element_validate`)
  * \#ajax (<https://api.drupal.org/api/drupal/core!core.api.php/group/ajax/8>)
  permet de faire de l'Ajax sans ecrire de JS
  * \#autocomplete_route_name

--------------------------------------------------------------------------------

# Appeler un formulaire directement depuis le routage
    !yaml
    example.form:
      path: '/example-form'
      defaults:
        _title: 'Example form'
        _form: '\Drupal\mymodule\Form\ExampleForm'

--------------------------------------------------------------------------------

# TP : Form API

But: définir pour quels types de contenu la fonctionnalité premium est activée.
C'est-à-dire, sur quels types on affichera l'option "Contenu premium" dans les
formulaires de création ou de modification de nœud.

  * Créer un formulaire listant les types de contenu avec pour chaque une
  checkbox

<p style="margin-left:2em"><code>
<label>Types de contenu pour lesquels activer la fonctionnalité Premium :</label><br/>
<input type="checkbox"> Article <br/>
<input type="checkbox"> Page de base <br/><br/>
<button>Enregistrer</button>
</code></p>

.fx: tp

--------------------------------------------------------------------------------

# TP : Form API

  * Valider le fait qu'on ne peut pas choisir le type de contenu _Page de base_

.fx: tp

--------------------------------------------------------------------------------

# Gestion de la configuration

  * <https://www.drupal.org/node/1905070>
  * $config = \Drupal::service('config.factory')->getEditable('monmodule.settings');
  * `$config->set('name', value)->save();` pour définir
  * $config = \Drupal::config('monmodule.settings');
  * `$config->get('name');` pour récupérer
  * $config = \Drupal::service('config.factory')->getEditable('monmodule.settings');
  * `$config->clear('name')->save();` pour supprimer une valeur
  * $config = \Drupal::service('config.factory')->getEditable('monmodule.settings')->delete();

Documentation de l'API sur <https://www.drupal.org/node/1809490>

--------------------------------------------------------------------------------

# Déclaration de la configuration

  * /config/install/mon_module.settings.yml -> initialisation à l'installation
  * /config/optionnal/module1.type1.name1.yml -> si module1 est activé
  * /config/schema/mon_module.schema.yml -> schéma de la configuration de votre module

## Exemple de fichier

    !yaml
    mon_module.settings:
      type: config_object
      mapping:
        settings_1:
          type: boolean
          label: 'Settings 1'
        settings_2:
          type: string
          label: 'Settings 2'

--------------------------------------------------------------------------------

# TP : Form API

  * A la soumission enregistrer les valeurs dans une variable persistante
  `'premium_types'`
  * Attention, il faut désinstaller et réinstaller votre module pour que Drupal connaisse votre configuration

.fx: tp

--------------------------------------------------------------------------------

# TP : Form API

  * Cocher les checkbox par défaut lorsque le type de contenu est activé
  (en lisant depuis la configuration)

.fx: tp

--------------------------------------------------------------------------------

# En bonus, Manipuler les "Form Modes"

    !php
    $this->entityFormBuilder()->getForm($form_id, 'form_mode');

--------------------------------------------------------------------------------

# Fournir un style par défaut

  Dans un fichier de configuration '/config/install/image.style.mon_style.yml'
  (l'exporter depuis l'interface)

    !yaml
    status: true
    dependencies: {  }
    name: mon_style
    label: 'mon style'
    effects:
      mon_style_desaturate:
        uuid: mon_style_desaturate
        id: image_desaturate
        weight: 1
        data: {  }

--------------------------------------------------------------------------------

# TP: Créer un style d'image pour nos contenus premium

Celui-ci nous servira pour les images qui seront sur les articles premium

.fx: tp

--------------------------------------------------------------------------------

# Le stockage

  * Ancienne méthode (D7) : on créé ses propres tables manuellement
  * Méthode Drupal 8 : on créé une _entité_ (2 types : configuration ou contenu)

--------------------------------------------------------------------------------

# Schema API (~ méthode Drupal 7)

  * Gère la base de données
  * Se situe dans le fichier .install
  * `hook_schema()` -> crée une ou plusieurs tables
  * `hook_schema_alter()` déclare une modification (mais ne la réalise pas)
  * API de la structure <https://drupal.org/node/146866>
  * Fonctions de l'API <https://drupal.org/node/150223>
  * Les `hook_update_N()` servent à réaliser des actions sur la structure ou
  les données
  * Très utile pour les mises à jour en production, et le test de celles-ci

--------------------------------------------------------------------------------

# Génération d'entité

  * Recommandation : utiliser la console pour générer l'entité
  * drupal generate:entity:content (ou drupal generate:entity:config)

--------------------------------------------------------------------------------

# TP: Enregistrer les statuts

## Déclarer une table premium

Via l'API, déclarer une table avec deux colonnes, nid et status.
Installer cette table via un `hook_update_N()` ou réinstaller le module.

## Altérer le formulaire de noeuds

  * Ajouter la checkbox au dessus du titre

  * Enregistrer la valeur dans notre table à l'enregistrement

  * La mettre à sa valeur par défaut à l'affichage du formulaire

Rappels 

  * `hook_form_alter(&$form, $form_state, $form_id)`
  * `hook_node_update()` et `hook_node_insert()`
  * Debug : `drupal_set_message('<pre>'.print_r($var, 1).'</pre>')`

.fx: tp

--------------------------------------------------------------------------------

# TP : Contrôler l'accès aux nœuds

Utiliser l'API Node Access ([documentation](https://api.drupal.org/api/drupal/modules!node!node.module/group/node_access/7))

Déclarer notre hook_node_access()` et ne retourner NODE_ACCESS_DENY que si les 4
conditions sont réunies :

  1. je suis en train de voir le nœud
  2. son type a la foncitonnalité premium activé
  3. c'est un contenu premium
  4.   je n'ai pas la permission de voir les contenu premium

<u>Attention:</u> ne fonctionnera pas pour les listes (dont la page d'accueil)
pour des raisons de performances, il faudrait declarer `hook_node_grants()`.
Rester simple et ne controler l'accès qu'à un nœud complet.

De même `hook_node_access()` n'est pas appelé pour le superadmin.

.fx: tp

--------------------------------------------------------------------------------

# Envoi de mails

    !php
    // Déclaration du contenu du mail avec hook_mail().
    function monmodule_mail($key, &$message, $params) {
      $account = $params['account'];
      $node = $params['node'];
      $message['subject'] = "Bonjour " . format_username($account);
      $message['body'][] = "Le noeud {$node->title} a été créé";
      $message['body'][] = "A bientot";
    }
    
    // Envoi du mail.
    drupal_mail('monmodule', 'maclé', 'toto@example.com', 'fr-FR', array(
      'node' => node_load(123),
      'user' => user_load_by_name('toto'),
    );

On peut utiliser la notion de tokens (jetons) ou la fonction strtr(). 
'`body`' est un tableau de lignes.

Envoi du mail avec `drupal_mail($module, $key,  $to, $language, $params = array())`;

La clé permet à un module de gérer plusieurs types de mail.

--------------------------------------------------------------------------------

# TP

## Notification par mail

Envoyer un mail à tous les utilisateurs premium :

<pre>
Sujet: Nouveau contenu premium

Bonjour _Nom d'utilisateur_,
Un nouveau _Type de contenu_ premium a été créé, il s'intitule _Titre_
Vous pouvez le consulter ici : _URL_
Cordialement,
L'équipe du site _Nom du site_
</pre>

## Affichage du statut premium sur le nœud

  - Trouver un hook qui permettrait d'ajouter un message `<strong>Contenu premium/strong>`
  sur chaque contenu premium
  - L'implementer avec #markup

.fx: tp

--------------------------------------------------------------------------------

# Le partie thème d'un module

Le module fournit **toujours** le markup par défaut.

Le `hook_theme()` définit des hooks/clés qui pourront ensuite être utilisés via
la propriété `#theme` des render arrays. Ces _theme hooks_   généreront ensuite
le markup HTML soit via une fonction, soit via un template.

On peut fournir des variables à ces _theme hooks_. Des fonctions preprocess et
process peuvent ajouter ou modifier des variables, et également ajouter des
suggestions de templates.

<https://www.drupal.org/files/theme_flow_6_1.pdf> (pour Drupal 6)

--------------------------------------------------------------------------------

## Déclaration et appel

    !php
    function forum_theme() {
    	return array(
    		'forums' => array(
    			'template' => 'forums',
    			'variables' => array(
    				'forums' => NULL,
    				'topics' => NULL,
    			),
    		),
    	);
    }

    $html_output = theme('forums', array(
      'forums' => $forums,
      'topics' => $topics,
    ));

    // Mais toujours privilégier les render arrays, car altérables
    $build['forums'] = array(
      '#theme' => 'forums',
      '#forums' => $forums,
      '#topics' => $topics,
    );

--------------------------------------------------------------------------------

# Fonctions de theme

Exemples d'utilisations de `theme()` :

  * table
  * item_list
  * pager
  * links
  * image

[Liste complete des implementation de theme du cœur](
https://api.drupal.org/api/drupal/core!lib!Drupal!Core!Render!theme.api.php/group/themeable/8)

    !php
    $table_element = array(
        '#theme'  => 'image',
        '#path' => drupal_get_path('module', 'monmodule') . '/monimage.png',
    );
    print drupal_render($table_element); // Quasi-automatiquement appelé
                                         // par les hooks

<https://www.drupal.org/developing/api/8/render/pipeline#html-main-content-renderer-pipeline>

--------------------------------------------------------------------------------

# Implémentation du hook_theme()

  * Fonction template_preprocess_forums
  * fichier forums.html.twig

--------------------------------------------------------------------------------

# Twig

  * Un template engine pour PHP
  * Créé par Fabien Potencier (Symfony)
  * [Documentation](http://twig.sensiolabs.org)
  * Très sécurisé
  * Extensible

--------------------------------------------------------------------------------

# Exemple de syntaxe

    !twig
    <!DOCTYPE html>
    <html lang="{{ language.language }}" dir="{{ language.dir }}">
      <head>
        <meta charset="utf-8">
        {{ head }}
        <title>{{ head_title }}</title>
        {{ styles }}
      </head>
      <body class="{{ classes }}" {{ attributes }}>
        {{ page_top }}
        {{ page }}
        {{ scripts }}
        {{ page_bottom }}
      </body>
    </html>

--------------------------------------------------------------------------------

# 3 syntaxes à connaître

  * {{ afficher }}
  * {# commenter #}
  * {% "programmer" %}

--------------------------------------------------------------------------------

# Afficher

![][1]

--------------------------------------------------------------------------------

# Programmer

  * {% if expr %} {% else %} {% endif %}
  * {% for item in items %} ({% else %}) {% endfor %}

--------------------------------------------------------------------------------

# Les filtres

  * {{ messages | join(', ') }}
  * {{ "now" | date('d/m/Y H:i') }}
  * {{ 'Home' | t }} (ajouté par Drupal)
  * {{ 'Home' | format_date('short') }} (ajouté par Drupal)
  * Voir core/lib/Drupal/Core/Template/TwigExtension.php pour la liste des rajouts Drupal
  * Sur toute une section : {% filter upper %} Texte {% endfilter %}

  * abs, batch, capitalize, convert_encoding, date, date_modify, default, escape, first, format, join, json_encode, keys, last, length, lower, merge, nl2br, number_format, raw, replace, reverse, round, slice, sort, split, striptags, title, trim, upper, url_encode

--------------------------------------------------------------------------------

# Les fonctions

  * dump(node)
  * {{ max(1, 3, 2) }}
  * {{ random(['pomme', 'orange', 'citron']) }}
  * + celles fournies par Drupal : <https://www.drupal.org/node/2486991>

--------------------------------------------------------------------------------

# Inclusion de template

  * {% include 'page.html.twig' with {'foo': 'bar', 'baz': 'bat'} %}

--------------------------------------------------------------------------------

# Héritage de template

    !twig
    {# Template A #}
    {% block foo %}
      <p>Mon premier paragraphe</p>
    {% endblock %}

    {# Template B #}
    {% extends 'TemplateA' %}
    {% block foo %}
      {{ parent() }}
        <p>Mon deuxième paragraphe</p>
    {% endblock %}

    {# Rendu Template B #}
    <p>Mon premier paragraphe</p>
    <p>Mon deuxième paragraphe</p>

--------------------------------------------------------------------------------

# Debug Twig dans Drupal

    !yaml
    parameters:
      twig.config:
        debug: true

dans sites/default/services.yml

--------------------------------------------------------------------------------

# TP: Créer un template pour premium

Convertir le render array utilisé dans `hook_node_view()` pour utiliser un
_theme hook_ qui se base sur un template.

Passer en paramètre le nœud et transformer "Contenu premium" en "_Titre du nœud_
est un contenu premium".

Ajouter une image de médaille dans ce template.

Créer un preprocess pour transformer cette image en variable.

Dans le preprocess, transformer l'image en render array, et utiliser la fonciton
render() dans le template.

Ajouter des suggestions pour ce template.

.fx: tp

--------------------------------------------------------------------------------

# Ajout de JS / CSS

    !yaml
    global-styling:
      css:
        theme:
          css/style.min.css
      js:
        js/theme.js
      dependencies:
        - core/jquery
        - core/drupal.ajax

  * Tout est sous forme de bibliothèque
  * \#attached[] -> au moment du rendering
  * drupal_add_library()

--------------------------------------------------------------------------------

# TP: Faire flotter l'image à droite

Ajouter une classe à l'image et créer un fichier CSS:

    !css
    img.premium-icon {
      float: right;
    }

L'ajouter lorsqu'un noœud premium est affiché.

.fx: tp

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

Voir les modules `example`

--------------------------------------------------------------------------------

# Les librairies JS fournies avec le cœur

  * jQuery
  * jQuery UI
  * Backbone
  * Underscore

--------------------------------------------------------------------------------

# Les services

  * <https://api.drupal.org/api/drupal/services/8.1.x>
  * Les services à connaître :
    * router.admin_context (->isAdminRoute())
    * path.matcher (->isFrontPage() / ->match())
    * plugin.manager.mail (->mail())
    * title_resolver (->getTitle())
    * entity_type.manager (->getStorage())
    * ...

--------------------------------------------------------------------------------

# Manipuler les fichiers

.fx: alternate

--------------------------------------------------------------------------------

# La File API

Un fichier n'est pas une entité ! (malheureusement)

Différence entre fichiers gérés et non gérés

Différence entre fichiers privés et fichiers publics

API complète <https://api.drupal.org/api/drupal/core!includes!file.inc/group/file/8>

## Les streams wrappers

Un stream est un chemin, une URI, vers un fichier interne ou externe :

  * public://
  * private://

--------------------------------------------------------------------------------

# La sécurité

## À retenir
  * "Valider les entrées, filtrer les sorties"

## Concrètement
  * URL : Html::escape(UrlHelper::stripDangerousProtocols($uri));
  * Texte brut : Html::escape($string);
  * Texte riche : check_markup($text, $format_id = NULL, $langcode = '', $filter_types_to_skip = array());
  * HTML : Xss::filter($string, array $html_tags = NULL);
  * Sinon, on considère que le texte est validé

--------------------------------------------------------------------------------

# Les migrations : le module Migrate

  * Depuis Drupal : TO DO
  * Depuis n'importe quoi : TO DO

--------------------------------------------------------------------------------

# Industrialistion

  * Les profils d'installation
  * L'outil drush make
  * La gestion de la configuration
  * Features

--------------------------------------------------------------------------------

# composer drupal project TO DO

--------------------------------------------------------------------------------

# Le cache TO DO

--------------------------------------------------------------------------------

# Merci

   [1]: img/twig_resolution.jpg

   [2]: img/module_structure.png

   [3]: img/symfony_components.png

   [4]: img/d8_learning_curve.jpg

   [5]: img/console.png

