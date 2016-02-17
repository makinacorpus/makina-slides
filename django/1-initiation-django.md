# Initiation à Django

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
* Version actuelle : Django 1.9, sortie en décembre 2015
* Aujourd'hui utilisé par de très nombreuses entreprises : Mozilla, Instagram, Pinterest, Disqus, ...

--------------------------------------------------------------------------------

# Philosophie

## KISS (*Keep It Simple, Stupid*)

> Simplicity should be a key goal in design and unnecessary complexity should be avoided.

## DRY (*Don't Repeat Yourself*)

> Every piece of knowledge must have a single, unambiguous, authoritative representation within a system.

## Conventions de codage

La documentation précise certaines conventions de codage spécifiques à Django. La PEP 8 fait référence pour le reste.

--------------------------------------------------------------------------------

# 10 raisons d'utiliser Django

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

# Environnement

* Django 1.9
* Python : 2.7 / 3.x
* Base de données : SQLite, PostgreSQL, MySQL
* Il est préférable de travailler dans un environnement virtualisé (*virtualenv*)

--------------------------------------------------------------------------------

# Architecture MVC, ou plutôt MTV

L'architecture de Django s'inspire du principe MVC (*Model, View, Controller*) ou plutôt MTV (*Model, Template, View*) :

* **Model** : Les modèles sont écrits en Python et Django fournit un ORM (*Django ORM*) complet pour accéder à la base de données
* **Template** : Django possède son propre moteur de template (*Django Template Engine*)
* **View** : Les vues Django peuvent être de simples fonctions Python retournant des réponses HTTP ou être basées sur des classes

La fonction **controller** est gérée par l'*URL dispatcher* qui permet de faire correspondre des URLs sous forme d'expressions régulières à des vues.

--------------------------------------------------------------------------------

# Tutoriel fil rouge : une gestion de *Todo lists*

.fx: alternate

--------------------------------------------------------------------------------

# Installer Django

## Création et activation du *virtualenv*

    !console
    $ virtualenv venv
    $ source venv/bin/activate

## Installation de Django

    !console
    $ pip install django==1.9

## Création du projet

    !console
    $ django-admin.py startproject library

## Lancement du serveur de développement

    !console
    $ cd library
    $ ./manage.py runserver

--------------------------------------------------------------------------------

# It worked !

![Page d'accueil par défaut Django](./it-worked.png)

.fx: imageslide

--------------------------------------------------------------------------------

# Le projet créé

    !console
    ├── library/
    │   ├── manage.py
    │   └── library/
    │       ├── __init__.py
    │       ├── settings.py
    │       ├── urls.py
    │       └── wsgi.py

* ``/library`` : conteneur du projet (le nom est sans importance)
* ``/manage.py`` : utilitaire en ligne de commande permettant différentes actions sur le projet
* ``/library/library`` : paquet Python effectif du projet
* ``/library/settings.py`` : réglages et configuration du projet
* ``/library/urls.py`` : déclaration des URLs du projet
* ``/library/wsgi.py`` : point d'entrée pour déployer le projet avec WSGI

--------------------------------------------------------------------------------

# Accès à la base de données
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

# Projet vs. Application

Il est important de différencier la notion de **projet** et d'**application**.

## Une application

> Une application est une application Web qui fait quelque chose – par exemple un système de blog, une base de données publique ou une application de sondage

## Un projet

> Un projet est un ensemble de réglages et d’applications pour un site Web particulier.

## Projets et applications

> Un projet peut contenir plusieurs applications. Une application peut apparaître dans plusieurs projets.

<cite> — docs.djangoproject.com</cite>

--------------------------------------------------------------------------------

# Création d'une application

    !console
    $ ./manage.py startapp books

## L'application créée

    !console
    ├── library/
        ├── books/
        │   ├── __init__.py
        │   ├── admin.py
        |   ├── apps.py
        │   ├── migrations/
        │   ├── models.py
        │   ├── tests.py
        │   ├── views.py

* ``models.py`` : déclaration des modèles de l'application
* ``views.py`` : écriture des vues de l'application
* ``admin.py`` : comportement de l'application dans l'interface d'administration
* ``tests.py`` : Il. Faut. Tester.
* ``migrations``: modifications successives du schéma de la base de donnée

--------------------------------------------------------------------------------

# Les modèles

--------------------------------------------------------------------------------

# Déclaration d'un modèle

    !python
    # models.py
    from django.db import models

    class Book(models.Model):
        title = models.CharField(max_length=100)
        release = models.DateField(blank=True, null=True)
        borrowed = models.BooleanField(default=False)

        def __unicode__(self):  # ou __str__ en python 3
            return self.title

--------------------------------------------------------------------------------

# Quelques options pour les modèles

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

--------------------------------------------------------------------------------

# Quelques options pour les champs

Chaque type de champs possède ses propres propriétés. Cependant, certaines sont communes et souvent utilisées comme : 

* ``verbose_name``: label du champ
* ``null`` : valeur NULL autorisée ou non en base de données
* ``blank`` : valeur vide autorisée lors de la validation du champ dans un formulaire
* ``default`` : valeur par défaut pour une nouvelle instance
* ``editable`` : le champ doit-il apparaître automatiquement dans les formulaires
* ...

--------------------------------------------------------------------------------

# Activation de l'application

## Déclaration de l'application dans les *settings*

    !python
    # settings.py
    INSTALLED_APPS = (
      'django.contrib.admin',
      ...
      'books',
    )

## Création de la migration qui permet d'ajouter la table en base de données

    !console
    $ ./manage.py makemigrations

## Application de la migration

    !console
    $ ./manage.py migrate

--------------------------------------------------------------------------------

## Déclaration dans l'interface d'administration

    !python
    # admin.py
    from django.contrib import admin
    from books.models import Book

    admin.site.register(Book)

--------------------------------------------------------------------------------

# L'interface d'administration Django

![L'interface d'administration Django](./admin.png)

.fx: imageslide

--------------------------------------------------------------------------------

# Tutoriel fil rouge : créer l'application *todo*, le modèle *tâche*, et activer l'application

.fx: alternate

--------------------------------------------------------------------------------

# Un exemple complet de vue : la liste des livres

--------------------------------------------------------------------------------

# 1. Création de la vue

    !python
    # views.py
    from django.shortcuts import render_to_response
    from books.models import Book

    def book_list(request):

        books = Book.objects.all()

        context = {
            'books': books
        }
    
        return render_to_response(
            'books/book_list.html',
            context
        )

--------------------------------------------------------------------------------

# 2. Création d'une template

    !html
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


--------------------------------------------------------------------------------

# 3. Mapping de l'URL

## Déclaration d'une URL

    !python
    # books/urls.py
    from django.conf.urls import patterns, include, url
    urlpatterns = [
        url(r'^book_list$', 'books.views.book_list', name='book_list'),
    ]

## Inclusion des URLs de l'application au projet

    !python
    # library/urls.py
    ...
    urlpatterns = [
        ...
        url(r'^books/', include('books.urls', namespace="books")),
    ]
    
--------------------------------------------------------------------------------

# Plus en détail ...

--------------------------------------------------------------------------------

# Les vues

--------------------------------------------------------------------------------

# Function-based views

Une vue *basée sur une fonction* Django est simplement une fonction Python qui prend en entrée une **requête HTTP** et retourne une **réponse HTTP**.

Cette réponse peut être une page HTML, un document XML, une redirection, une erreur 404, ...

Ces vues sont généralement écrites dans le fichier ``views.py`` de l'application.

## Un exemple tiré de la documention Django

    !python
    # some_app/views.py
    from django.http import HttpResponse
    import datetime

    def current_datetime(request):
        now = datetime.datetime.now()
        html = "<html><body>It is now %s.</body></html>" % now
        return HttpResponse(html)

--------------------------------------------------------------------------------

# Class-based views

Une vue *basée sur une classe* Django est simplement une classe Python préformatée qui prend en entrée une **requête HTTP** et retourne une **réponse HTTP**.


## Un exemple tiré de la documention Django

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

--------------------------------------------------------------------------------

# Qu'est-ce qu'une template Django ?

C'est un simple fichier texte qui peut générer n'importe quel format de texte (HTML, XML, CSV, ...).

Une template a accès à des **variables** qui lui auront été passées via un **contexte** par la vue.

--------------------------------------------------------------------------------

# Où écrire ses templates ?

Django possède un mécanisme capable de retrouver les templates d'un projet, configurable via le réglage ``TEMPLATE_LOADERS``.

Le plus souvent on stocke les templates :
* dans chaque application, en suivant l'arborescence ``<application>/templates/<application>``. Ils seront retrouvés grâce au loader django.template.backends.django.DjangoTemplates, activé par défaut.
* dans un répertoire ``templates/`` à la racine du projet qu'il faudra déclarer dans la clé ``DIRS`` du réglage ``TEMPLATES``.

--------------------------------------------------------------------------------

# Base de la syntaxe de template

## Affichage d'une variable

    !python
    {{ ma_variable }}

## Les filtres

Il est possible de modifier l'affichage d'une variable en appliquant des **filtres**. Un filtre peut prendre (ou non) un argument. Les filtres peuvent être appliqués en cascade. Quelques exemples :

    !python
    {{ name|lower }}
    {{ text|linebreaksbr }}
    {{ current_time|time:"H:i" }}
    {{ weight|floatformat:2|default_if_none:0 }}

Django fournit nativement une liste de filtres assez intéressante et il est possible d'écrire des filtres personnalisés facilement.

--------------------------------------------------------------------------------

# Base de la syntaxe de template

## Les tags

Les **tags** sont plus complexes que les variables, ils peuvent créer du texte ou de la logique (boucle, condition, ...) dans la tempate.

### Une condition *if* :

    !python
    {% if condition %} .. {% else %} .. {% endif %}

### Une boucle *for* :

    !python
    {% for item in list %} .. {% endfor %}


### Un lien avec *url* :

    !html
    <a href="{% url 'books:book_detail' book.pk %}">Django book</a>

Django fournit aussi plusieurs tags nativement et il est possible d'écrire ses propres tags.

--------------------------------------------------------------------------------

# L'héritage de template

L'intérêt de l'héritage de template est par exemple de pouvoir créer un squelette HTML contenant tous les éléments communs du site et définir des blocs que chaque template pourra surcharger.

Dans une template *parent*, la balise ``{% block %}`` permet de définir les blocs surchargeables.

Dans une template *enfant*, la balise ``{% extends %}`` permet de préciser de quelle template celle-ci doit hériter.

--------------------------------------------------------------------------------

# Exemple de template *parent*

    !html
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

# Exemple de template *enfant*

    !html
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

# L'inclusion de template

L'intérêt de l'inclusion de template est de pouvoir factoriser du code de template :
* pour éviter d'avoir des fichiers de templates trop long
* pour le réutiliser facilement tout en évitant la duplication de code

Cela peut être utile dans différents cas :
* pour certains éléments communs de la page (menu, entête, pied de page, ...)
* pour certaines macros réutilisables (structure d'onglets, affichage en liste d'éléments, structure HTML d'une pop-in, ...)

--------------------------------------------------------------------------------

# Exemple de template *appelant*

    !html
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

--------------------------------------------------------------------------------

# Processus de traitement des requêtes par Django

1. Django identifie le module *URLconf* racine à utiliser (cf ROOT_URLCONF dans les *settings*).
2. Django charge ce module et cherche la variable ``urlpatterns``.
3. Django parcourt chaque motif d’URL (expression régulière) dans l’ordre et s’arrête dès la première correspondance avec l’URL demandée.
4. Une fois qu’une des expressions régulières correspond, Django importe et appelle la vue correspondante. La vue se voit passer une requête HTTP (objet Python ``HttpRequest``) en tant que premier paramètre puis toutes les valeurs capturées dans l’expression régulière.
5. Si aucune expression régulière ne correspond, ou si une exception est levée durant ce processus, Django appelle une vue d’erreur appropriée.

--------------------------------------------------------------------------------

# Écriture d'un module *URLconf*

Le module *URLconf* est un fichier ``urls.py`` contenant une variable ``urlpatterns`` :

    !python
    # urls.py
    from django.conf.urls import patterns, url
    urlpatterns = [,
        url(r'^myview$', 'myapp.views.my_view', name='my_view'),
        ...
      ]

## Inclusion d'*URLconf*

Souvent, l'*URLconf* racine inclura les modules URLconf de chaque application :

    !python
    # urls.py
    from django.conf.urls import patterns, url
    urlpatterns = [
        url(r'^myapp/', include('myapp.urls', namespace='myapp')),
        ...
    ]

--------------------------------------------------------------------------------

# Syntaxe de déclaration d'une URL

## URL sans paramètre
    
    !python
    url(r'^myview$', 'my_view', name='my_view')

La vue aura en argument seulement l'objet ``HttpRequest``.

# URL avec paramètres

    !python
    url(r'^myview_by_month/(?P<year>\d{4})/(?P<month>\d{2})/$',
        MyViewByMonth.as_view(),
        name='myview_by_month'),

La vue aura en argument l'objet ``HttpRequest``, puis les valeurs trouvées dans l'expression régulière (ex: ``request, year=2014, month=12``).

--------------------------------------------------------------------------------

# Tutoriel fil rouge : créer la vue *listes des tâches* et *détail d'une tâche*

.fx: alternate

--------------------------------------------------------------------------------

# Les formulaires

--------------------------------------------------------------------------------

# La bibliothèque ``django.forms``

Django possède une bibliothèque assez complète de gestion de formulaires : ``django.forms``.

Les concepts principaux sont les suivants:

* La classe ``Widget`` : permet de gérer et faire le rendu d'un widget HTML (ex: un champ ``<input>``, ``<textarea>``, ...)
* La classe ``Field`` : permet de gérer l'initialisation et la validation d'un champ de formulaire
* La classe ``Form`` : permet de gérer un ensemble de champs de formulaires, ainsi que l'initialisation, le rendu et la validation du formulaire global
* La classe ``ModelForm`` : permet de gérer des formulaires basés sur des modèles (création / modification d'une instance du modèle)

--------------------------------------------------------------------------------

# Création d'un formulaire simple

## Un exemple tiré de la documentation Django

    !python
    # forms.py
    from django import forms

    class ContactForm(forms.Form):
        subject = forms.CharField(max_length=100)
        message = forms.CharField() 
        sender = forms.EmailField()
        cc_myself = forms.BooleanField(required=False)

## Quelques méthodes souvent utilisées
* La méthode ``__init__`` : permet de personnaliser l'intialisation du formulaire (par exemple : pré-remplir le champ ``sender`` par l'email de l'utilisateur connecté)
* La méthode ``clean`` : permet de personnaliser la validation du formulaire (par exemple : vérifier que ``sender`` a bien été fourni si ``cc_myself`` a été coché)

--------------------------------------------------------------------------------

# Les champs de formulaire

La bibliothèque django.forms fournit plus de 20 types de champs différents, dont voici les principaux :
* Les champs pur texte : CharField , TextField
* Les champs pour les nombres : FloatField, IntegerField
* Les champs booléens : BooleanField, NullBooleandField
* Les champs de sélection : ChoiceField, MultipleChoiceField
* Les champs pour la gestion des dates : DateField, DateTimeField, TimeField
* Les champs pour la gestion des fichiers : FileField, FilePathField, ImageField

Certains modules annexes fournissent leurs propres champs et il est possible d'écrire des champs personnalisés.

--------------------------------------------------------------------------------

# Utilisation d'un formulaire dans une ``function-based view``

    !python
    from django.shortcuts import render_to_response
    from django.http import HttpResponseRedirect
    from myapp.forms import ContactForm

    def contact(request):
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                # Process the data in form.cleaned_data and redirect
                # ...
                return HttpResponseRedirect('/thanks/')
        else:
            form = ContactForm()
        # Render form
        return render_to_response(
            'contact.html',
            {'form': form,}
        )

--------------------------------------------------------------------------------

# Rendu du formulaire dans une template

    !python
    <form action="/contact/" method="post">
      {% csrf_token %}
      {{ form.as_p }}
      <input type="submit" value="Submit" />
    </form>

L'utilisation du tag ``{% csrf_token %}`` est importante car elle permet de protéger le formulaire des attaques de type CSRF (*Cross Site Request Forgeries*).

--------------------------------------------------------------------------------

# Les formulaires de modèles

La classe ``ModelForm`` permet de créer automatiquement des formulaires basés sur des modèles.

Le fonctionnement est assez semblable à celui des formulaires classiques à quelques différences près :

* La déclaration d'une classe ``Meta`` est nécessaire pour préciser sur quel modèle doit se baser le formulaire
* La méthode ``__init__`` prend en argument l'instance du modèle à modifier (ou ``None`` dans le cas d'une création)
* Le formulaire fournit une méthode ``save`` qui permet d'enregistrer l'instance éditée via le formulaire

--------------------------------------------------------------------------------

# Un exemple d'utilisation d'un ModelForm

    !python
    # models.py
    class Book(models.Model):
        title = models.CharField(max_length=100)
        release = models.DateField()
        borrowed = models.BooleanField(default=False)

    # forms.py
    class AddBookForm(forms.ModelForm):
        class Meta:
            model = Book
            fields = ('title', 'release')

    # views.py
    def add_book(request):
        form = AddBookForm(request.POST or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/books/')
        return render_to_response('add_book.html', {'form': form,})

--------------------------------------------------------------------------------

# Tutoriel : Créer les vues d'ajout et modification d'une tâche

.fx: alternate

--------------------------------------------------------------------------------

# Relations entre les modèles

--------------------------------------------------------------------------------

# Relations entre les modèles

La bibliothèque ``django.models`` fournit différents champs spécifiques pour représenter les relations entre modèles.

* ``models.ForeignKey`` : représente une relation de type 1-N
* ``models.ManyToManyField`` : représente une relation de type N-N
* ``models.OneToOneField`` : représente une relation de type 1-1

--------------------------------------------------------------------------------

# Le champ ForeignKey

Le champ ``ForeignKey`` doit être déclaré avec comme premier argument le modèle auquel il est lié par cette relation 1-N. L'argument optionnel ``related_name`` permet de nommer la relation inverse à partir de ce modèle lié.

La représentation de ce champ en base de données est une contrainte de type clé étrangère.

## Exemple

Un livre est associé à un auteur, un auteur peut avoir écrit plusieurs livres.

    !python
    # models.py
    class Author(models.Model):
        name = models.CharField(max_length=50)

    class Book(models.Model):
        title = models.CharField(max_length=100)
        author = models.ForeignKey(Author,
                                   related_name='books')

--------------------------------------------------------------------------------

# Le champ ManyToManyField

Le champ ``ManyToManyField`` doit être déclaré de la même manière que le champ ``ForeignKey``.

La représentation de ce champ en base de données est une table contenant deux clés étrangères vers les deux tables des modèles liés.

## Exemple

Un livre est associé à plusieurs catégories, plusieurs livres peuvent appartenir à une même catégorie.

    !python
    # models.py
    class Category(models.Model):
        label = models.CharField(max_length=50)

    class Book(models.Model):
        title = models.CharField(max_length=100)
        categories = models.ManyToManyField(Category,
                                            related_name='books')

--------------------------------------------------------------------------------

# Le champ OneToOneField

La déclaration du ``OneToOneField`` est similaire.

La représentation de ce champ en base de données est une clé étrangère possédant une contrainte d'unicité.

## Exemple

Un livre est associé à un seul code barre, un code barre correspond à un seul livre.

    !python
    # models.py
    class BarCode(models.Model):
        code = models.CharField(max_length=50)

    class Book(models.Model):
        title = models.CharField(max_length=100)
        barcode = models.OneToOneField(BarCode,
                                       related_name='book')

--------------------------------------------------------------------------------

# Tutoriel : Mettre en place une modélisation gérant des listes de tâches partagées entre utilisateurs

.fx: alternate

--------------------------------------------------------------------------------

# L'ORM : les requêtes

--------------------------------------------------------------------------------

# Création / modification d'une instance

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

# Suppression d'une instance

Pour supprimer une instance, il suffit d'appeler la méthode delete qui permet de supprimer directement la ligne en base de données.

    >>> b = Book(name='Two scoops of django',
                 release=date(2013, 08, 31))
    >>> b.save()
    >>> b.delete()

--------------------------------------------------------------------------------

# Les concepts ``Manager`` & ``Queryset``

Pour récupérer une ou plusieurs instances, il faut construire un ``Queryset`` via un ``Manager`` associé au modèle.

## Qu'est ce qu'un ``Manager`` ?

Un ``Manager`` est l'interface à travers laquelle les opérations de requêtage en base de données sont mises à disposition d'un modèle Django. Chaque modèle possède un ``Manager`` par défaut accessible via la propriété ``objects``.

## Qu'est ce qu'un ``Queryset`` ?

Un ``Queryset`` représente une collection d'objets provenant de la base de données. Cette collection peut être filtrée, limitée, ordonnée, ... grâce à des méthodes qui correspondent à des clauses SQL.

--------------------------------------------------------------------------------

# Retrouver une liste d'instances

## Retrouver toutes les instances d'un modèle

    !python
    >>> Book.objects.all()

## Retrouver une liste filtrée d'instances
    
Les méthodes de filtrage principalement utilisées sont ``filter`` et ``exclude``. Il est possible de les chaîner.

    !python
    >>> Book.objects.filter(
            release__gte=date(2013, 01, 01)
          ).exclude(
            borrowed=True
          )

## Retrouver une liste ordonnée d'instances

    !python
    >>> Book.objects.exclude(borrowed=True).order_by('title')

--------------------------------------------------------------------------------

# Retrouver une instance en particulier

La méthode ``get`` permet de récupérer une instance particulière.

    !python
    >>> Book.objects.get(pk=12)

La méthode ne peut retourner qu'une instance précise, il faut donc que le filtre fourni ne soit pas ambigu. Il faut veiller à filtrer sur un champ ``unique`` (ou un ensemble de champs uniques ensemble).

## Exceptions potentielles

* Si l'instance n'est pas trouvée, une exception ``Book.DoesNotExist`` sera levée (de manière générique : ``<Model>.DoesNotExist``).
* Si plusieurs instances ont été trouvées, l'exception levée sera ``Book.MultipleObjectsReturned`` (``<Model>.MultipleObjectsReturned``).

--------------------------------------------------------------------------------

# Référence à des objets associés

Pour les relations entre instances (``ForeignKey``, ``ManyToManyField``), Django fournit un ``Manager`` spécifique nommé ``RelatedManager``. Il permet notamment de :

* retrouver les instances liées par une ``ForeignKey`` vers une instance donnée
* ajouter une liaison entre deux instances dans le cas d'un ``ManyToManyField``
* supprimer toutes les liaisons d'une instance vers d'autres

--------------------------------------------------------------------------------

# Référence à des objets associés

## Quelques exemples

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

# Tutoriel : Mettre en place un formulaire de filtrage de tâches

.fx: alternate

--------------------------------------------------------------------------------

# Pour finir ...

--------------------------------------------------------------------------------

# Quelques modules indispensables

## Outils
* ``django_extensions`` : plusieurs extensions et outils d'administration très pratiques
* ``django_debug_toolbar`` : une barre latérale permettant de faire du *debug* et du *profiling* page par page

# Tests
* ``factory_boy`` : création de grappes de données pour les tests
* ``django_jenkins`` : intégration à Jenkins

--------------------------------------------------------------------------------

# Quelques modules souvent utilisés

* ``django_compressor`` : compression des fichiers statiques
* ``django_linaration_pagination`` : affichage de listes paginées
* ``django_sorting`` : affichage de tableaux triables
* ``django_breadcrumbs`` : création de fil d'ariane
* ``django_xworkflows`` : gestion de workflows
* ``django_modeltranslation`` : gestion de modèles multilingues
* ``easy_thumbnails`` : gestion de miniatures pour les images
* ``django_tinymce`` : intégration d'un *widget* TinyMCE
* ...

--------------------------------------------------------------------------------

# Où obtenir des informations ?

## Les sites
* http://www.djangoproject.com [EN]
* http://www.django-fr.org/ [FR]
* http://docs.djangoproject.com [EN]
* http://docs.djangoproject.com/fr [FR]
* http://stackoverflow.com/questions/tagged/django

## Les planètes
* http://www.planetdjango.org/ [EN]
* http://www.django-fr.org/planete/ [FR]

--------------------------------------------------------------------------------

## Les outils de développement
* Le *bug tracker* : http://code.djangoproject.com
* Le Jenkins : http://ci.djangoproject.com/

--------------------------------------------------------------------------------

# La communauté Django

## Modules
* Un répertoire de modules : https://www.djangopackages.com/

## Contacts

* La *mailing list* Django : django@lists.afpy.org
* Les *channels* IRC : #django, #django-fr
* Le forum français : http://forum.django-fr.org

## Événements

* Djangocong : Conférence annuelle française
* Djangocon-eu : Conférence annuelle européenne
* D'autres Djangocon un peu partout dans le monde

--------------------------------------------------------------------------------

# Merci !

