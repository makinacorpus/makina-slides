# Initiation à Django

---

# Faisons les présentations 

### Makina Corpus
Experts en logiciels libres, cartographie et analyse de données, nous concevons des applications métiers innovantes.

Nos valeurs :

* Les logiciels libres et les données ouvertes
* L'agilité
* Le développement durable

### Le formateur

`"%s : un•e expert•e, fort de %s ans d'expérience à votre écoute" % (name, xp)`

### Et vous ?

# Presenter notes

- quels sont les deux types d'arguments qu'on peut passer à une fonction ? args et kwargs
- comment déclarer une fonction ou une classe vide? pass
- quel opérateur utilise-t'on pour remplacer des variables dans une chaine ? %
- comment modifier la manière dont s'affiche un objet ? \_\_str\_\_
- comment récupérer l'avant dernier élément d'une liste ? liste[-2:1]
- quel mot-clé représente l'instance courante dans une classe ? self
- qu'est ce qu'une liste par compréhension ? une liste inline bouclant sur une autre
- sur quel protocole est basé le WWW ? HTTP
- quel est le type mime d'une page web ? text/html
- quels ports sont utilisés par HTTP(s) ? 80 et 443
- donner 2 méthodes HTTP ? GET POST PUT DELETE HEAD
- quelle entité html représente un espace insécable ? &amp;nbsp;
- autres questions : len(), type(); isinstance(), PyPi, URL, codes de statut HTTP


--------------------------------------------------------------------------------

# Programme

* Introduction
* Installation
* Structure
* Requêtes et réponses
* Modèles
* Vues, Templates et Urls
* Formulaires
* ORM
* Ressources

.fx: toc

--------------------------------------------------------------------------------

> La Plateforme de développement Web pour les perfectionnistes sous pression.

<cite> — www.django-fr.org</cite>

.fx: quoteslide

--------------------------------------------------------------------------------

# Qu'est-ce-que Django ?

* Django est un framework en Python pour le Web qui encourage le développement rapide et propre avec une conception pragmatique
* Django permet de construire des applications web rapidement et avec peu de code
* Malgré son haut niveau d'abstraction, il est toujours possible de descendre dans les couches

## Historique

* Créé en 2003 par le journal local de Lawrence (Kansas, USA), basé sur le langage Python créé en 1990
* Rendu Open Source (BSD) en 2005
* Django 1.x : compatible python 2 et 3
* Django 2.x : compatible python 3 uniquement
* Aujourd'hui utilisé par de très nombreuses entreprises/sites : Mozilla, Instagram, Pinterest, Disqus, Washington Times, ...

--------------------------------------------------------------------------------

## Philosophie

### KISS (*Keep It Simple, Stupid*)

> Simplicity should be a key goal in design and unnecessary complexity should be avoided.

### DRY (*Don't Repeat Yourself*)

> Every piece of knowledge must have a single, unambiguous, authoritative representation within a system.

### Conventions de codage

La documentation précise certaines conventions de codage spécifiques à Django. La PEP 8 fait référence pour le reste.

--------------------------------------------------------------------------------

## Philosophie

### Couplage faible
* Les différentes couches du framework sont indépendantes
* Le socle d'applications peut être réduit au strict minimum

### Peu de code à écrire
* Ecriture "automatique" de code
* Utilisation des possibilités d'introspection de Django

### Rapidité
* Dans le domaine du web, au 21e siècle, tout va très vite

--------------------------------------------------------------------------------

## 10 raisons d'utiliser Django

* Facile à installer
* Fonctionne *out of the box*
* Excellente documentation
* Modèles en Python et ORM efficace (peu de connaissances SQL requises)
* Interface d'administration auto-générée
* Architecture *pluggable*, nombreux modules existants
* Gestion de formulaires
* Serveur de développement *standalone*
* Déploiement facile
* Communauté autour du projet très active

--------------------------------------------------------------------------------

# Architecture MVC, ou plutôt MTV

L'architecture de Django s'inspire du principe MVC (*Model, View, Controller*) ou plutôt MTV (*Model, Template, View*) :

* **Model** : Les modèles sont écrits en Python et Django fournit un ORM (*Django ORM*) complet pour accéder à la base de données
* **Template** : Django possède son propre moteur de template (*Django Template Engine*)
* **View** : Les vues Django peuvent être de simples fonctions Python retournant des réponses HTTP ou être basées sur des classes

La fonction **controller** est gérée par l'*URL dispatcher* qui permet de faire correspondre des URLs sous forme d'expressions régulières à des vues.

--------------------------------------------------------------------------------

# Environnement

* Django 1.11+
* Python : 3.x
* Base de données : SQLite, PostgreSQL, MySQL

## Côté python

Python parcours sys.path pour chercher les modules à importer

* Par défaut ce path contient les répertoires systèmes tels que ``/usr/lib/python``, 
``/usr/local/lib/python``, ``~/.local/lib/python`` ainsi que le répertoire courant en général
* Comme tout module python, il faut que Django soit accessible dans le path pour pouvoir l'utiliser
* Virtualenv permet de créer un environnement python en isolation du système, 
c'est la méthode préférable pour développer avec python

---

## Introduction au virtualenv


    !shell
    $ virtualenv env  # crée l'environnement
    $ ./env/bin/python  # lance le python de l'environnement virtuel
    (env) $ source env/bin/activate  # ajoute ./env/bin en tête du PATH
    (env) $ python  # lance le python de l'environnement virtuel
    (env) $ deactivate  # rétablit le path
    $ python  # lance le python du système

Cela permet ainsi de créer plusieurs environnement avec différentes version de python, de Django, etc.

Quelques alternatives/extensions : _virtualenvwrapper_, _anaconda_, _pyenv_.


--------------------------------------------------------------------------------

# Tutoriel fil rouge 

Proposez vos idées pour un tutorial original !

Sur les slides, des exemples basés sur une bibliothèque seront utilisés

À défaut d'idées dans l'audience, nous créerons une application de gestion de *Todo lists* :

 - différentes listes de tâches
 - affectation à des utilisateurs
 - notifications par e-mail
 - catégorisation

.fx: alternate

--------------------------------------------------------------------------------

# Installer Django

.fx: titleslide

--------------------------------------------------------------------------------

## Création et activation du *virtualenv*

    !console
    $ virtualenv venv
    $ source venv/bin/activate

## Installation de Django

    !console
    (venv) $ pip install django

## Création du projet

    !console
    (venv) $ django-admin startproject library

## Lancement du serveur de développement

    !console
    (venv) $ cd library
    (venv) $ ./manage.py runserver


--------------------------------------------------------------------------------

![Page d'accueil par défaut Django](./it-worked.png)

.fx: bg-image

--------------------------------------------------------------------------------

## Développer avec le serveur de déveloopement Django

Django vient avec ce serveur HTTP de développement (à ne surtout pas utiliser en production pour des raisons de performances et de sécurité)

* Ce serveur se relance (presque toujours) automatiquement lorsqu'il détecte un changement de fichier
* Par défaut il écoute sur l'interface localhost sur le port 8000
* Le script manage.py fait la même chose que django-admin mais après avoir lu la configuration du projet (dans ``settings.py``)

--------------------------------------------------------------------------------

# Structure d'un projet Django

    !console
    └── library
        ├── library
        │   ├── __init__.py
        │   ├── settings.py
        │   ├── urls.py
        │   └── wsgi.py
        └── manage.py

* ``library`` : conteneur du projet (le nom est sans importance)
* ``library/manage.py`` : utilitaire en ligne de commande permettant différentes actions sur le projet
* ``library/library`` : paquet Python effectif du projet
* ``library/library/settings.py`` : réglages et configuration du projet
* ``library/library/urls.py`` : déclaration des URLs du projet
* ``library/library/wsgi.py`` : point d'entrée pour déployer le projet avec WSGI

--------------------------------------------------------------------------------

## Projet vs. Application

Il est important de différencier la notion de **projet** et d'**application**.

### Une application

> Une application est une application Web qui fait quelque chose – par exemple un système de blog, une base de données publique ou une application de sondage

### Un projet

> Un projet est un ensemble de réglages et d’applications pour un site Web particulier.

### Projets et applications

> Un projet peut contenir plusieurs applications. Une application peut apparaître dans plusieurs projets.

<cite> — docs.djangoproject.com</cite>


---

## Un projet est une combinaison d'applications

* Le projet peut être découpé en différentes apps
* Une même app peut être réutilisée dans plusieurs projets
* Django fourni par défaut des apps, par exemple pour gérer l'authentification
* De nombreuses autres apps sont mise à disposition par la communauté (installation via `pip`)
* Un projet django typique combine des apps de Django, d'autres provenant de la 
communauté, et enfin une ou des apps spécifiques au projet
* Ce sont des modules python
* La commande `manage.py startapp` crée automatiquement un patron d'app dans un nouveau
répertoire
* Les apps sont à déclarer dans les settings ( `INSTALLED_APPS = [...]` ) 

---

## Structure d'une application : chaque chose à sa place

Django "impose" une organisation du code (noms et emplacements des fichiers) 

  * C'est une contrainte mais c'est aussi très pratique pour retrouver son code, 
  quand c'est le sien ou quand c'est celui des autres : ce qui revient au même au bout d'un certain temps...
  * Par exemple les vues vont dans le  `views.py` dans le répertoire de l'app (ou dans le package `views` de l'app)
  * Et les urls vont dans le module urls (fichier `urls.py`)
  * On peut inclure une liste d'urls d'une app dans les urls du projet

<!-- -->

     !python
     from django.conf.urls import url, include
     urlpatterns = [
         # soit on définit des couples url-vue
         url(r'^$', une_vue),
         # ... ou on inclut les urls depuis une autre app
         url(r'', include('books.urls')),
     ]

--------------------------------------------------------------------------------

## Création d'une application

    !console
    $ ./manage.py startapp books

### L'application créée

    !console
      ├── books/
      │   ├── __init__.py
      │   ├── admin.py
      |   ├── apps.py
      │   ├── migrations/__init__.py
      │   ├── models.py
      │   ├── tests.py
      │   ├── views.py

* ``models.py`` : déclaration des modèles de l'application
* ``views.py`` : écriture des vues de l'application
* ``admin.py`` : comportement de l'application dans l'interface d'administration
* ``tests.py`` : Il. Faut. Tester.
* ``migrations``: modifications successives du schéma de la base de données

# Presenter notes

La commande devra être lancée avec le bon nom de module (todo).

---

## Activation de l'application

### Déclaration de l'application dans les *settings*

    !python
    # settings.py
    INSTALLED_APPS = (
      'django.contrib.admin',
      ...
      'books',
    )

--------------------------------------------------------------------------------

# Configuration de la BDD

Django propose une configuration par défaut pour une base SQLite (cf : ``settings.py``).

Voici un exemple de configuration pour une base Postgresql :

    !python
    DATABASES = {
      'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'library_db',
        'USER': 'library_user',
        'PASSWORD': 'Cx12%a03oa',
        'HOST': 'localhost'
      }
    }

## Création de la structure de la base de données

    !console
    $ ./manage.py migrate


--------------------------------------------------------------------------------

# Tutoriel fil rouge

Créer le projet (ex: *formation*) 

Puis une application (ex: *todo*)

Enfin activer l'application

.fx: alternate


--------------------------------------------------------------------------------

# Fonctionnement général

.fx: titleslide


--------------------------------------------------------------------------------

## Déroulement d'une requête HTTP

* Une vue est une fonction qui prend un objet `HttpRequest` et renvoie un objet `HttpResponse`
* Quand Django reçoit une requête HTTP, il crée l'objet `HttpRequest` correspondant à la requête du client
* Il cherche la fonction de vue associée à l'URL
* Il appelle cette fonction en lui passant l'objet `HttpRequest` en paramètre
* Il récupère un objet `HttpResponse` en retour de la fonction ou de la classe
* Il répond au client

---

## L'objet `HttpRequest`

Permet d'accéder à de nombreux attributs tels que

  * Le schéma (ex. http ou https), le domaine, et le chemin formant l'URL 
  * La méthode (ex. GET, POST, PUT, DELETE)
  * Les headers HTTP (ex. Content-Type)
  * Les paramètres et les fichiers uploadés
  * Les cookies

Peut être lu comme un flux 

  * request.read()
  * request.readline()
  * for line in request:

_cf._ <https://docs.djangoproject.com/fr/stable/ref/request-response/#httprequest-objects>

-----

## L'objet `HttpResponse`

Permet de régler de nombreux attributs tels que

* Le statut HTTP (ex. 200 OK, 404 Not Found)
* Le contenu de la réponse (ex. du code HTML, des données sérialisées en JSON) 
* Les headers HTTP (ex. Content-Type)
* Les cookies

Peut être instancié directement avec le contenu comme paramètre 

    !python
    response = HttpResponse("foobar")

Peut être écrit comme un flux 
    
    !python
    request.write()

Est dérivé en sous-classes (ex. HttpResponseRedirect)

_cf._ <https://docs.djangoproject.com/fr/stable/ref/request-response/#httpresponse-objects>

---

## Vue simple basée sur une chaîne

En somme, une vue se résume à déclarer une url :

    !python
    # books/urls.py
    from django.conf.urls import patterns, include, url
    import books.views
    urlpatterns = [
        url(r'^ma-vue$', book.views.ma_vue),
    ]

et retourner un contenu en fonction d'une requête

    !python
    # books/views.py
    from django.http import HttpResponse

    def ma_vue(request):
        return HttpResponse("mon contenu")

--------------------------------------------------------------------------------

# Exercice

Créer une vue affichant "Bienvenue dans la Todo List"

Ce sera notre page d'accueil, elle sera accessible sur `http://127.0.0.1:8000/`

.fx: alternate

--------------------------------------------------------------------------------

# Les modèles

.fx: titleslide

--------------------------------------------------------------------------------

## Déclaration d'un modèle

    !python
    # models.py
    from django.db import models

    class Book(models.Model):
        title = models.CharField(max_length=100)
        release = models.DateField(blank=True, null=True)
        borrowed = models.BooleanField(default=False)

        def __str__(self):
            return self.title

# Presenter notes

Ces 3 types de champs suffisent pour l'appli todo 

* title
* deadline
* done

Pour python2, utiliser `@python2_unicode_compatible`


--------------------------------------------------------------------------------

## Quelques options pour les modèles

L'ajout de la classe ``Meta`` dans un modèle permet de déclarer des *options de métadonnées* sur le modèle. Exemple :

    !python
    class Book(models.Model):
        ...

        class Meta:
            db_table = 'book'
            verbose_name = 'Book'
            verbose_name_plural = 'Books'
            ordering = ('-released', )


D'autres options permettent par exemple de :

* rendre le modèle abstrait
* demander à Django de ne pas gérer ce modèle en base de données
* préciser des critères de tri
* déclarer des permissions relatives au modèle

Documentation : <https://docs.djangoproject.com/fr/stable/ref/models/>

# Presenter notes

Ici on utilisera uniquement verbose_name et ordering

Mentionner le fait que les noms de modele sont declinés de leur nom système


--------------------------------------------------------------------------------

## Quelques types de champs de modèle

  * Les champs texte : 
    * `CharField` (une ligne avec longueur max)
    * `TextField` (multiligne)
    * `EmailField` (vérifie la syntaxe de l'adresse)
  * Les champs pour les nombres :
    * `IntegerField` et `PositiveIntegerField`
    * `FloatField`
    * `DecimalField` (précision fixe, non soumis aux arrondis) 
    * `AutoField` (`IntegerField` incrémenté automatiquement)
  * Les champs booléens :  `BooleanField` et `NullBooleandField`
  * Les champs pour la gestion des dates : 
    * `DateField`, `TimeField` et `DateTimeField`
    * `DurationField`
  * Les champs pour la gestion des fichiers : 
    * `FileField` et `ImageField`
    * `FilePathField`


---


## Quelques options pour les champs

Chaque type de champs possède ses propres propriétés. Cependant, certaines sont communes et souvent utilisées comme : 

* ``verbose_name``: label du champ
* ``null`` : valeur NULL autorisée ou non en base de données
* ``blank`` : valeur vide autorisée lors de la validation du champ dans un formulaire
* ``default`` : valeur par défaut pour une nouvelle instance
* ``editable`` : le champ doit-il apparaître automatiquement dans les formulaires
* `choices` permet d'expliciter la liste de valeurs possibles
* `primary_key` est la clé primaire (remplace *id*)
* `unique` ajoute une contrainte d'unicité
* `validators` permet d'ajouter des contraintes de validation au niveau du modèle

Documentation <https://docs.djangoproject.com/fr/stable/ref/models/fields/#field-options>

---

# Les migrations

* Django permet de faire évoluer les modèles sans devoir effacer les données en génèrant des « diffs » appelés migrations qu'il applique ensuite à la base de données
* Il compare la dernière des migrations existantes aux modèles déclarés en python (peu importe ce qui est dans la base de données)
* Puis il convertit en SQL et applique toutes les migrations qui n'ont pas déjà été faites (la liste des migrations déjà faites est stockée dans la base)
* Ces migrations sont numérotées et rangées dans les apps dans le sous-répertoire `migrations/`. Il est conseillé d'enregistrer les migrations avec le code

### Création d'une migration automatique

    !console
    (venv) $ ./manage.py makemigrations

### Application de la migration

    !console
    (venv) $ ./manage.py migrate


--------------------------------------------------------------------------------

## Déclaration dans l'interface d'administration

    !python
    # admin.py
    from django.contrib import admin
    from books.models import Book

    admin.site.register(Book)
    
L'interface d'administration est le "back-office" automatique" de Django qui 
liste les instances et par introspection des modèles, créer les formulaire de 
création/modification correspondants.

Elle est personnalisable et permet de modifier :

* les filtres et l'ordre des listes
* l'affichage des listes
* les formulaires et l'ordre des champs
* ajouter des actions en masse sur les listes

Documentation : <https://docs.djangoproject.com/fr/stable/ref/contrib/admin/>

--------------------------------------------------------------------------------

# L'interface d'administration Django

![L'interface d'administration Django](./admin.png)

.fx: bg-image

--------------------------------------------------------------------------------

# Exercice

Par défaut: Créer le modèle *tâche* ayant notamment les champs : 

- titre (texte)
- description (texte long)
- deadline (date et heure)
- réalisée (booléen)

Pour accèder à l'admin de Django, vous aurez besoin d'un superutilisateur :

    !console
    (venv) $ ./manage.py createsuperuser

But: Le modèle doit apparaitre dans l'interface d'administration avec les bons champs

.fx: alternate

--------------------------------------------------------------------------------

# Vue, template et URL

## Exemple complet : la liste des livres

.fx: titleslide

---

## Exemple : Création de la vue

    !python
    # book/views.py
    from django.shortcuts import render
    from books.models import Book

    def book_list(request):

        books = Book.objects.all()

        context = {
            'books': books
        }
    
        return render(request, 'books/book_list.html', context)

Ce style de vue est dit "Function-based" (par opposition à "Class-based").

--------------------------------------------------------------------------------

## Exemple : Création d'un template

    !html+django
    {# books/templates/books/book_list.html #}
    
    <h1>Liste des livres</h1>
    
    {% if books %}
        <ul>
            {% for book in books %}
            <li>{{ book }}</li>
            {% endfor %}
        </ul>
    {% else %}
        <p>Aucun livre !</p>
    {% endif %}

Documentation: <https://docs.djangoproject.com/fr/stable/topics/templates/>

--------------------------------------------------------------------------------

## Exemple : Mapping de l'URL

Routeur basé sur des regex, avec un préfixe par application. Ce préfixe n'est
pas obligatoire mais permet de classer les vues afin d'éviter les conflits, par exemple :

  * `book/list` et `book/add`
  * `movie/list` et `movie/add`

### Déclaration d'une URL

    !python
    # books/urls.py
    from django.conf.urls import patterns, include, url
    urlpatterns = [
        url(r'^book_list$', books.views.book_list, name='book_list'),
    ]

### Inclusion des URLs de l'application au projet

    !python
    # library/urls.py
    ...
    urlpatterns = [
        ...
        url(r'^books/', include('books.urls', namespace="books")),
    ]

--------------------------------------------------------------------------------

# Les vues

.fx: titleslide

--------------------------------------------------------------------------------

## Function-based views

Une vue *basée sur une fonction* Django est simplement une fonction Python qui prend en entrée une **requête HTTP** et retourne une **réponse HTTP**.

Cette réponse peut être une page HTML, un document XML, une redirection, une erreur 404, ...

Ces vues sont généralement écrites dans le fichier ``views.py`` de l'application.

### Un exemple tiré de la documention Django

    !python
    # some_app/views.py
    from django.http import HttpResponse
    import datetime

    def current_datetime(request):
        now = datetime.datetime.now()
        html = "<html><body>It is now %s.</body></html>" % now
        return HttpResponse(html)

--------------------------------------------------------------------------------

## Class-based views

Une vue *basée sur une classe* Django est simplement une classe Python préformatée qui prend en entrée une **requête HTTP** et retourne une **réponse HTTP**.


### Un exemple tiré de la documentation Django

    !python
    # some_app/views.py
    from django.http import HttpResponse
  	from django.views.generic import View

  	class CurrentDatetimeView(View):
  		def get(self, request, * args, ** kwargs):
  			now = datetime.datetime.now()
  			html = "<html><body>It is now %s.</body></html>" % now
  			return HttpResponse(html)

--------------------------------------------------------------------------------

# Le moteur de template

.fx: titleslide

--------------------------------------------------------------------------------

## Qu'est-ce qu'un template Django ?

C'est un simple fichier texte qui peut générer n'importe quel format de texte (HTML, XML, CSV, ...).

Un template a accès à des **variables** qui lui auront été passées via un **contexte** par la vue.

Par défaut, Django fournit sa propre syntaxe de template mais il est possible de la remplacer par un autre moteur comme Jinja2.

--------------------------------------------------------------------------------

## Où écrire ses templates ?

Pour retrouver les templates d'un projet, Django se base sur le réglage ``TEMPLATES``. Le plus souvent on stocke les templates :

* dans chaque application, en suivant l'arborescence ``<app>/templates/<app>``. 
  Ils seront retrouvés grâce au loader activé par défaut quand la clé ``APP_DIRS`` vaut `True`.
* dans un répertoire ``templates/`` à la racine du projet qu'il faudra déclarer dans la clé ``DIRS``.

Dans ce mécanisme de découverte, l'ordre importe : cela permet de surcharger les templates d'autres applications.

--------------------------------------------------------------------------------

## Syntaxe de Django template

### Affichage d'une variable

    !django
    {{ ma_variable }}

### Les filtres

Il est possible de modifier l'affichage d'une variable en appliquant des **filtres**. Un filtre peut prendre (ou non) un argument. Les filtres peuvent être appliqués en cascade. Quelques exemples :

    !django
    {{ name|lower }}
    {{ text|linebreaksbr }}
    {{ current_time|time:"H:i" }}
    {{ weight|floatformat:2|default_if_none:0 }}

Django fournit nativement une liste de filtres assez intéressante et il est possible d'écrire des filtres personnalisés facilement.

--------------------------------------------------------------------------------

## Syntaxe de Django template

### Les tags

Les **tags** sont plus complexes que les variables, ils peuvent créer du texte ou de la logique (boucle, condition, ...) dans la tempate.

### Une condition *if* :

    !django
    {% if condition %} .. {% else %} .. {% endif %}

### Une boucle *for* :

    !django
    {% for item in list %} .. {% endfor %}


### Un lien avec *url* :

    !html+django
    <a href="{% url 'books:book_detail' book.pk %}">Django book</a>

Django fournit aussi plusieurs tags nativement et il est possible d'écrire ses propres tags.

--------------------------------------------------------------------------------

## L'héritage de template

L'intérêt de l'héritage de template est par exemple de pouvoir créer un squelette HTML contenant tous les éléments communs du site et définir des blocs que chaque template pourra surcharger.

Dans une template *parent*, la balise ``{% block %}`` permet de définir les blocs surchargeables.

Dans une template *enfant*, la balise ``{% extends %}`` permet de préciser de quel template celui-ci doit hériter.

--------------------------------------------------------------------------------

## Exemple de template *parent*

    !html+django
    {# templates/base.html #}
    <html>
      <head>
        <title>
          {% block title %}
            ...
          {% endblock %}
        </title>
        <link href="styles.css" rel="stylesheet" />
      </head>
      <body>
        <header>Entête commune à tout le site</header>
        <section>
          {% block content %}
            ...
          {% endblock %}
        </section>
        <footer>Pied de page commun à tout le site</footer>
      </body>
    </html>

--------------------------------------------------------------------------------

## Exemple de template *enfant*

    !html+django
    {# books/templates/books/book_list.html #}

    {% extends "base.html" %}

    {% block title %}
      Liste des livres
    {% endblock %}

    {% block content %}
      {% if books %}
        <ul>
          {% for book in books %}
            <li>{{ book }}</li>
          {% endfor %}
        </ul>
      {% else %}
        <p>Aucun livre !</p>
      {% endif %}
    {% endblock %}

--------------------------------------------------------------------------------

## L'inclusion de template

L'intérêt de l'inclusion de template est de pouvoir factoriser du code de template :

* pour éviter d'avoir des fichiers de templates trop long
* pour le réutiliser facilement tout en évitant la duplication de code

Cela peut être utile dans différents cas :

* pour certains éléments communs de la page (menu, entête, pied de page, ...)
* pour certaines macros réutilisables (structure d'onglets, affichage en liste d'éléments, structure HTML d'une pop-in, ...)

--------------------------------------------------------------------------------

## Exemple de template *appelant*

    !html+django
    {# templates/base.html #}
    <html>
      <head>
        <title>
          {% block title %}
            ...
          {% endblock %}
        </title>
        <link href="styles.css" rel="stylesheet" />
      </head>
      <body>
        {% include 'templates/header.html' %}
        <section>
          {% block content %}
            ...
          {% endblock %}
        </section>
        {% include 'templates/footer.html' %}
      </body>
    </html>

--------------------------------------------------------------------------------

# L'URL dispatcher

.fx: titleslide

--------------------------------------------------------------------------------

## Processus de traitement des requêtes

1. Django identifie le module *URLconf* racine à utiliser (cf `ROOT_URLCONF` dans les *settings*), souvent `projet/urls.py`
2. Django charge ce module et cherche la variable ``urlpatterns``
3. Django parcourt chaque motif d’URL dans l’ordre et s’arrête dès la première
correspondance avec l’URL demandée. Il tient compte des _include_ d'autres `urls.py` de chaque application.
4. Une fois qu’une des regex correspond, Django appelle la vue correspondante
avec en paramètre la requête HTTP (objet Python ``HttpRequest``) puis toutes les valeurs capturées dans la regex.
5. Si aucune regex ne correspond, ou si une exception est levée durant ce
processus, Django appelle une vue d’erreur appropriée.

--------------------------------------------------------------------------------

## Écriture d'un module *URLconf*

Le module *URLconf* est un fichier ``urls.py`` contenant une variable ``urlpatterns`` :

    !python
    # library/urls.py
    from django.conf.urls import patterns, url
    urlpatterns = [
        url(r'^myview$', myapp.views.my_view, name='my_view'),
        ...
    ]

À chaque vue peut être associé un nom système qui pourra servir lors de l'inversion d'une url.

## Inclusion d'*URLconf*

Souvent, l'*URLconf* racine inclura les modules URLconf de chaque application :

    !python
    # urls.py
    from django.conf.urls import patterns, url
    urlpatterns = [
        url(r'^myapp/', include('myapp.urls', namespace='myapp')),
        ...
    ]
    
À chaque application peut être associé un namespace qui pourra servir lors de l'inversion d'une url.

--------------------------------------------------------------------------------

## Syntaxe de déclaration d'une URL

### URL sans paramètre
    
    !python
    url(r'^myview$', my_view, name='my_view')

La vue aura en argument seulement l'objet ``HttpRequest``.

### URL avec paramètres

    !python
    url(r'^myview_by_month/(?P<year>\d{4})/(?P<month>\d{2})/$',
        MyViewByMonth.as_view(),
        name='myview_by_month'),

La vue aura en argument l'objet ``HttpRequest``, puis les valeurs trouvées dans l'expression régulière (ex: ``request, year=2014, month=12``).

--------------------------------------------------------------------------------

## Résolution inversée d'une URL

La résolution d'une url consiste à partir d'une URL et trouver la regex correspondant ainsi que ses paramètres.<br/>
La résolution inversée part d'un nom système de vue et de paramètres pour arriver à une URL.

Ceci permet de modifier les motifs sans avoir à retoucher toutes les fois où
l'url est appelée (par exemple dans un `<a href>`).

    !python
    # project/urls.py
    urlpatterns = [
        url(r'^book/', include('book.urls', namespace='book')),
    ]

    # book/urls.py
    urlpatterns = [
        url(r'^list$', book.views.list, name='list'),
        url(r'^edit/(?P<pk>\d+)$', book.views.edit, name='edit'),
    ]

Dans un template:

    !html+django
    <a href="{% url 'book:list' %}">Liste des livres</a>

Dans du code python :

    !python
    from django.urls import reverse
    return HttpResponseRedirect(reverse('book:edit', pk=12))

.fx: wide

--------------------------------------------------------------------------------

# Tutoriel fil rouge

Créer la vue *liste des tâches* et *détail d'une tâche*

Créer auparavant quelques tâches via l'interface d'administration

Pour la liste de toutes les tâches : `Task.objects.all()` et pour le détail `Task.objects.get(pk=<pk>)`

.fx: alternate

--------------------------------------------------------------------------------

# Les formulaires

.fx: titleslide

--------------------------------------------------------------------------------

## La bibliothèque ``django.forms``

Django possède une bibliothèque assez complète de gestion de formulaires : ``django.forms``.

Les concepts principaux sont les suivants:

* La classe ``Widget`` : permet de gérer et faire le rendu d'un widget HTML (ex: un champ ``<input>``, ``<textarea>``, ...)
* La classe ``Field`` : permet de gérer l'initialisation et la validation d'un champ de formulaire
* La classe ``Form`` : permet de gérer un ensemble de champs de formulaires, ainsi que l'initialisation, le rendu et la validation du formulaire global
* La classe ``ModelForm`` : permet de gérer des formulaires basés sur des modèles (création / modification d'une instance du modèle)

--------------------------------------------------------------------------------

## Création d'un formulaire simple

### Un exemple tiré de la documentation Django

    !python
    # contact/forms.py
    from django import forms

    class ContactForm(forms.Form):
        subject = forms.CharField(max_length=100)
        message = forms.CharField() 
        sender = forms.EmailField()
        cc_myself = forms.BooleanField(required=False)

### Quelques méthodes souvent utilisées
* La méthode ``__init__`` : permet de personnaliser l'intialisation du formulaire (par exemple : pré-remplir le champ ``sender`` par l'email de l'utilisateur connecté)
* La méthode ``clean`` : permet de personnaliser la validation du formulaire (par exemple : vérifier que ``sender`` a bien été fourni si ``cc_myself`` a été coché)

--------------------------------------------------------------------------------

## Quelques champs de formulaire

La bibliothèque `django.forms` fournit plus de 20 types de champs différents, dont voici les principaux :

* Champs texte : `CharField`, `SlugField`, `RegexField`, `EmailField`, `UrlField`
* Champs pour les nombres : `FloatField`, `IntegerField`
* Champs booléens : `BooleanField`, `NullBooleandField`
* Champs de sélection : `ChoiceField`, `MultipleChoiceField`
* Champs pour les dates : `DateField`, `DateTimeField`, `TimeField`, `DurationField`
* Champs pour les fichiers : `FileField`, `FilePathField`, `ImageField`

Certains modules annexes fournissent leurs propres champs et il est possible d'écrire des champs personnalisés.

__Rappel__ : ces champs gérent les données, ce sont les widgets qui gèrent la manière
dont ils sont saisis. Par exemple, un `CharField` gérera du texte et aura par défaut
un widget `TextInput`, mais il est possible de spécifier un widget un widget `Textarea`.

--------------------------------------------------------------------------------

## Utilisation d'un formulaire dans une *Function-based view*

    !python
    from django.shortcuts import render
    from django.http import HttpResponseRedirect
    from myapp.forms import ContactForm

    def contact(request):
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                # Traite les données dans form.cleaned_data puis redirige
                # ...
                return HttpResponseRedirect('/thanks/')
        else:
            form = ContactForm()
        # Affiche le formulaire
        return render(request, 'contact.html', {'form': form})
        
### Méthode simplifiée

    !python
    def contact(request):
        form = ContactForm(request.POST or None)
        if form.is_valid():
            # ...
            return HttpResponseRedirect('/thanks/')
        return render(request, 'contact.html', {'form': form})

.fx: wide

--------------------------------------------------------------------------------

## Rendu du formulaire dans un template

    !html+django
    <form action="/contact/" method="post">
      {% csrf_token %}
      {{ form.as_p }}
      <input type="submit" value="Submit" />
    </form>

L'utilisation du tag ``{% csrf_token %}`` est importante car elle permet de protéger le formulaire des attaques de type CSRF (*Cross Site Request Forgeries*).

Un formulaire peut être rendu de différentes manières :

* _as\_p_: chaque champ est rendu dans un paragraphe
* _as\_ul_: chaque champ est rendu dans une ligne de liste
* _as\_table_: chaque champ est rendu dans une ligne de tableau

Des packages de la communauté (cripsy_forms, floppyforms, material) permettent d'afficher le bon markup pour un framework HTML/CSS.

--------------------------------------------------------------------------------

## Les formulaires de modèles

La classe ``ModelForm`` permet de créer automatiquement des formulaires basés sur des modèles.

Le fonctionnement est assez semblable à celui des formulaires classiques à quelques différences près :

* La déclaration d'une classe ``Meta`` est nécessaire pour préciser sur quel modèle doit se baser le formulaire
* La méthode ``__init__`` prend en argument l'instance du modèle à modifier (ou ``None`` dans le cas d'une création)
* Le formulaire fournit une méthode ``save`` qui permet d'enregistrer l'instance éditée via le formulaire
* Les champs sont automatiquement listés dès lors qu'ils n'ont pas la propriété ``editable=False``

--------------------------------------------------------------------------------

## Un exemple d'utilisation d'un ModelForm

    !python
    # book/models.py
    class Book(models.Model):
        title = models.CharField(max_length=100)
        release = models.DateField()
        borrowed = models.BooleanField(default=False)

    # book/forms.py
    class AddBookForm(forms.ModelForm):
        class Meta:
            model = Book
            fields = ('title', 'release')

    # book/views.py
    def add_book(request):
        form = AddBookForm(request.POST or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/books/')
        return render(request, 'add_book.html', {'form': form})

--------------------------------------------------------------------------------

# Tutoriel

Créer les vues d'ajout et modification d'une tâche

Afficher également des liens depuis la liste de tâches

.fx: alternate

--------------------------------------------------------------------------------

# Relations entre les modèles

.fx: titleslide

--------------------------------------------------------------------------------

## Relations entre les modèles - Les différents champs

La bibliothèque ``django.models`` fournit différents champs spécifiques pour représenter les relations entre modèles.

* ``models.ForeignKey`` : représente une relation de type 1-N
* ``models.ManyToManyField`` : représente une relation de type N-N
* ``models.OneToOneField`` : représente une relation de type 1-1

--------------------------------------------------------------------------------

## Le champ ForeignKey

Le champ ``ForeignKey`` doit être déclaré avec comme premier argument le modèle auquel il est lié par cette relation 1-N. L'argument optionnel ``related_name`` permet de nommer la relation inverse à partir de ce modèle lié.

La représentation de ce champ en base de données est une contrainte de type clé étrangère.

### Exemple

Un livre est associé à un auteur, un auteur peut avoir écrit plusieurs livres.

    !python
    # book/models.py
    class Author(models.Model):
        name = models.CharField(max_length=50)

    class Book(models.Model):
        title = models.CharField(max_length=100)
        author = models.ForeignKey(Author, related_name='books')

--------------------------------------------------------------------------------

## Le champ ManyToManyField

Le champ ``ManyToManyField`` doit être déclaré de la même manière que le champ ``ForeignKey``.

La représentation de ce champ en base de données est une table contenant deux clés étrangères vers les deux tables des modèles liés.

### Exemple

Un livre est associé à plusieurs catégories, plusieurs livres peuvent appartenir à une même catégorie.

    !python
    # book/models.py
    class Category(models.Model):
        label = models.CharField(max_length=50)

    class Book(models.Model):
        title = models.CharField(max_length=100)
        categories = models.ManyToManyField(Category, related_name='books')

--------------------------------------------------------------------------------

## Le champ OneToOneField

La déclaration du ``OneToOneField`` est similaire.

La représentation de ce champ en base de données est une clé étrangère possédant une contrainte d'unicité.

### Exemple

Un livre est associé à un seul code barre, un code barre correspond à un seul livre.

    !python
    # book/models.py
    class BarCode(models.Model):
        code = models.CharField(max_length=50)

    class Book(models.Model):
        title = models.CharField(max_length=100)
        barcode = models.OneToOneField(BarCode, related_name='book')

--------------------------------------------------------------------------------

# Tutoriel 

Mettre en place une modélisation gérant des listes de tâches partagées entre utilisateurs

.fx: alternate

# Presenter notes

Ici l'attendu est 

* un nouveau modèle pour les listes
* un ManyToManyField entre liste et utilisateurs

--------------------------------------------------------------------------------

# L'ORM

.fx: titleslide

-----------

## Les moteurs de base de donnée

  * 4 moteurs sont disponibles dans l'ORM de Django
    * PostgreSQL `django.db.backends.postgresql`
    * MySQL `django.db.backends.mysql`
    * Oracle `django.db.backends.oracle`
    * SQLite `django.db.backends.sqlite3`
  * SQLite n'est pas recommandé en production, il est d'abord pensé pour PostgreSQL (champs `DateRangeField`, `JSONField`, etc)
  * Possible de changer de moteur sans réécrire le code (mais il faut migrer les éventuelles données), sauf pour certaines spécificités
  * Recommandé de développer (ou au moins de tester) avec le moteur utilisé en production
  * Moteur spécifié dans `settings.py` (variable `DATABASES`), ainsi que la configuration du nom de la base, du serveur, et de l'authentification

Documentation <https://docs.djangoproject.com/fr/stable/ref/databases/>

-----------

## ORM (Object-relational mapping)

  * Fait correspondre une classe Python à une table SQL
  * Fait correspondre un objet python Python, instance de cette classe, à un enregistrement de cette table SQL
  * Il y a donc juste des classes et objets python à manipuler, aucun SQL à écrire, que ce soit : 
    * Pour créer et modiger les tables
    * Pour créer et modiger les données
    * Pour interroger la base
  * Facilite la gestion des relations entre modèles (jointures)
  * A sa propre "opinion", nécessite souvent des optimisations

--------------------------------------------------------------------------------

## Création / modification d'une instance

Pour créer une instance, il suffit de l'instancier en passant en argument les noms des attributs du modèle. L'instance dispose ensuite d'une méthode ``save`` qui permet de l'enregistrer en base de données.

    !python
    >>> b = Book(name='Two scoops of django',
                 release=date(2013, 08, 31))
    >>> b.save()

La même méthode ``save`` est utilisée pour enregistrer en base de données des modifications sur l'instance.

    !python
    >>> b.name ='Two scoops of django - Best practices'
    >>> b.save()

--------------------------------------------------------------------------------

## Suppression d'une instance

Pour supprimer une instance, il suffit d'appeler la méthode ``delete()`` qui permet de supprimer directement la ligne en base de données.

    !python
    >>> b = Book(name='Two scoops of django',
                 release=date(2013, 08, 31))
    # Création en BDD
    >>> b.save()
    # Suppression
    >>> b.delete()

--------------------------------------------------------------------------------

## Les concepts ``Manager`` & ``Queryset``

Pour récupérer une ou plusieurs instances, il faut construire un ``Queryset`` via un ``Manager`` associé au modèle.

### Qu'est ce qu'un ``Manager`` ?

Un ``Manager`` est l'interface à travers laquelle les opérations de requêtage en 
base de données sont mises à disposition d'un modèle Django. Chaque modèle 
possède un ``Manager`` par défaut accessible via la propriété ``objects``.

### Qu'est ce qu'un ``Queryset`` ?

Un ``Queryset`` représente une collection d'objets provenant de la base de 
données. Cette collection peut être filtrée, limitée, ordonnée, ... grâce à 
des méthodes qui correspondent à des clauses SQL.

A partir d'un queryset il est possible d'obtenir un autre queryset plus spécialisé.
Un queryset est paresseux (la requête SQL n'est faite que lorsqu'il n'est plus 
possible de la retarder).

--------------------------------------------------------------------------------

## Retrouver une liste d'instances

### Retrouver toutes les instances d'un modèle

    !python
    >>> Book.objects.all()

### Retrouver une liste filtrée d'instances
    
Les méthodes de filtrage principalement utilisées sont ``filter`` et ``exclude``. Il est possible de les chaîner.

    !python
    >>> Book.objects.filter(
            release__gte=date(2013, 01, 01)
          ).exclude(
            borrowed=True
          )

### Retrouver une liste ordonnée d'instances

    !python
    >>> Book.objects.exclude(borrowed=True).order_by('title')
    
---------

## ORM - Fitrage

  * Les paramètres nommés sont le nom du champ et la valeur
  * On peut ajouter derrière le nom du champ deux undescores et un lookup
    * `__iexact` pour une recherche insensible à la casse
    * `__contains` pour chercher à l'intérieur
    * `__lt`, `__lte`, ` __gt`,` __gte` pour les inégalités
  * Avec deux undescores on peut aussi suivre une relation
  * Il y a un **ET** logique entre les différentes conditions

Documentation : <https://docs.djangoproject.com/fr/stable/ref/models/lookups/>

    !python
    books = Book.objects.filter(title__startswith="Le")
    books = Book.objects.filter(release__year__lt=1950) \
                        .exclude(title__icontains="fleurs")

Pour l'opérateur **OU** ou des requêtes plus complexes, utiliser `django.db.models.F` 
et `django.db.models.Q`, qui permettent des combinaisons avant exécution.


--------------------------------------------------------------------------------

## Retrouver une instance en particulier

La méthode ``get`` permet de récupérer une instance particulière.

    !python
    >>> Book.objects.get(pk=12)

La méthode ne peut retourner qu'une instance précise, il faut donc que le filtre fourni ne soit pas ambigu. Il faut veiller à filtrer sur un champ ``unique`` (ou un ensemble de champs uniques ensemble).

### Exceptions potentielles

* Si l'instance n'est pas trouvée, une exception ``Book.DoesNotExist`` sera levée (de manière générique : ``<Model>.DoesNotExist``).
* Si plusieurs instances ont été trouvées, l'exception levée sera ``Book.MultipleObjectsReturned`` (``<Model>.MultipleObjectsReturned``).

--------------------------------------------------------------------------------

## Référence à des objets associés

Pour les relations entre instances (``ForeignKey``, ``ManyToManyField``), Django fournit un ``Manager`` spécifique nommé ``RelatedManager``. Il permet notamment de :

* retrouver les instances liées par une ``ForeignKey`` vers une instance donnée
* ajouter une liaison entre deux instances dans le cas d'un ``ManyToManyField``
* supprimer toutes les liaisons d'une instance vers d'autres

--------------------------------------------------------------------------------

## Référence à des objets associés - Quelques exemples

Retrouver les livres disponibles d'un auteur :

    !python
    >>> author = Author.objects.get(pk=25)
    >>> author.books.filter(borrowed=False)

Ajouter un livre à une catégorie :

    !python
    >>> category = Category.objects.get(pk=5)
    >>> book = Book.objects.get(pk=12)
    >>> category.books.add(book)

Supprimer l'association de livres à une catégorie :

    !python
    >>> category = Category.objects.get(pk=5)
    >>> category.books.clear()


--------------------------------------------------------------------------------

# Tutoriel

Mettre en place un formulaire de filtrage de tâches :

* entre deux dates
* sur le titre
* sur le fait qu'elles soient terminées ou non

.fx: alternate

--------------------------------------------------------------------------------

# Ressources

## Pour aller plus loin

.fx: titleslide

--------------------------------------------------------------------------------


# Quelques modules indispensables

## Outils
* ``django_extensions`` : plusieurs extensions et outils d'administration très pratiques
* ``django_debug_toolbar`` : une barre latérale permettant de faire du *debug* et du *profiling* page par page
* ``django_hijack``: permet de se connecter avec un autre utilisateur sans se déconnecter
* ``django_extra_views``: apporte d'autres CBV pour des formulaires et vues toujours plus rapides
* ``django_braces``: apporte des mixins pour vos CBV

## Tests
* ``factory_boy`` : création de grappes de données pour les tests
* ``django_jenkins`` : intégration à Jenkins

--------------------------------------------------------------------------------

# Quelques modules souvent utilisés

* ``django_compressor`` : compression des fichiers statiques
* ``django_pagination`` : affichage de listes paginées
* ``django_sorting`` : affichage de tableaux triables
* ``django_filters`` : création de liste filtrées
* ``django_crispy_forms`` : affichage de forms avec Bootstrap/Foundation/Uniform
* ``django_breadcrumbs`` : création de fil d'ariane
* ``django_xworkflows`` : gestion de workflows
* ``django_modeltranslation`` : gestion de modèles multilingues
* ``easy_thumbnails`` ou ``versatileimagefield`` : gestion de miniatures pour les images
* ``django_tinymce`` : intégration d'un *widget* TinyMCE
* ...

--------------------------------------------------------------------------------

# Où obtenir des informations ?

### Les sites
* http://www.djangoproject.com [EN]
* http://www.django-fr.org/ [FR]
* http://docs.djangoproject.com [EN]
* http://docs.djangoproject.com/fr [FR]
* http://stackoverflow.com/questions/tagged/django

### Les planètes
* http://www.planetdjango.org/ [EN]
* http://www.django-fr.org/planete/ [FR]

### Les outils de développement
* Le *bug tracker* : http://code.djangoproject.com
* Le Jenkins : http://ci.djangoproject.com/

--------------------------------------------------------------------------------

# La communauté Django

### Modules


* Un répertoire de modules : https://www.djangopackages.com/

### Contacts

* La *mailing list* Django : django@lists.afpy.org
* Les *channels* IRC : #django, #django-fr
* Le forum français : http://forum.django-fr.org

### Événements

* Djangocong : Conférence annuelle française
* Djangocon-eu : Conférence annuelle européenne
* D'autres Djangocon un peu partout dans le monde

--------------------------------------------------------------------------------

### Merci !

Des questions ? Des remarques ?

Gardons le contact : <https://makina-corpus.com>

