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

* Créé en 2003, basé sur le langage Python créé en 1990
* Rendu Open Source (BSD) en 2005
* Version actuelle : Django 1.6, sortie en novembre 2013
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

* Django 1.6
* Python : 2.6 / 2.7 / 3.2 / 3.3
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
    $ virtualenv --no-site-packages venv_todoproject
    $ source venv_todoproject/bin/activate

## Installation de Django

    !console
    $ pip install django==1.6

## Création du projet

    !console
    $ django-admin.py startproject todoproject

## Lancement du serveur de développement

    !console
    $ cd todoproject
    $ ./manage.py runserver

--------------------------------------------------------------------------------

# It worked !

![Page d'accueil par défaut Django](./it-worked.png)

.fx: imageslide

--------------------------------------------------------------------------------

# Le projet créé

    !console
    ├── todoproject
    │   ├── manage.py
    │   └── todoproject
    │       ├── __init__.py
    │       ├── settings.py
    │       ├── urls.py
    │       └── wsgi.py

* ``/todoproject`` : conteneur du projet (le nom est sans importance)
* ``/manage.py`` : utilitaire en ligne de commande permettant différentes actions sur le projet
* ``/todoproject/todoproject`` : paquet Python effectif du projet
* ``/todoproject/settings.py`` : réglages et configuration du projet
* ``/todoproject/urls.py`` : déclaration des URLs du projet
* ``/todoproject/wsgi.py`` : point d'entrée pour déployer le projet avec WSGI

--------------------------------------------------------------------------------

# Accès à la base de données
Django propose une configuration par défaut pour une base SQLite (cf : ``settings.py``).

Voici un exemple de configuration pour une base Postgresql :

    !python
    DATABASES = {
      'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'todoproject_db',
        'USER': 'todoproject_user',
        'PASSWORD': 'Cx12%a03oa',
        'HOST': 'localhost'
      }
    }

## Création de la structure de la base de données

    !console
    $ ./manage.py syncdb

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
    $ ./manage.py startapp todo

## L'application créée

    !console
     ├── todo
     │   ├── admin.py
     │   ├── __init__.py
     │   ├── models.py
     │   ├── tests.py
     │   └── views.py

* ``models.py`` : déclaration des modèles de l'application
* ``views.py`` : écriture des vues de l'application
* ``admin.py`` : comportement de l'application dans l'interface d'administration
* ``tests.py`` : Il. Faut. Tester.

--------------------------------------------------------------------------------

# Les modèles

--------------------------------------------------------------------------------

# Déclaration d'un modèle

    !python
    # models.py
    from django.db import models

    class Task(models.Model):
        name = models.CharField(max_length=100)
        deadline = models.DateField(blank=True, null=True)
        done = models.BooleanField(default=False)

        def __unicode__(self):
            return self.name

--------------------------------------------------------------------------------

# Quelques options pour les modèles

L'ajout de la classe ``Meta`` dans un modèle permet de déclarer des *options de métadonnées* sur le modèle. Exemple :

    !python
    class Task(models.Model):
        ...

        class Meta:
            db_table = 'task'
            verbose_name = 'Task'
            verbose_name_plural = 'Tasks'
            ordering = ('-deadline', )


D'autres options permettent par exemple de :

* rendre le modèle abstrait
* demander à Django de ne pas gérer ce modèle en base de données
* préciser des critères de tri
* déclarer des permissions relatives au modèle

--------------------------------------------------------------------------------

# Quelques options pour les champs

Chaque type de champ possède ses propres propriétés. Cependant, certaines sont communes et souvent utilisées comme : 

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
      'todo',
    )

## Création de la table en base de données

    !console
    $ ./manage.py syncdb

## Déclaration dans l'interface d'administration

    !python
    # admin.py
    from django.contrib import admin
    from todo.models import Task

    admin.site.register(Task)

--------------------------------------------------------------------------------

# L'interface d'administration Django

![L'interface d'administration Django](./admin.png)

.fx: imageslide

--------------------------------------------------------------------------------

# Tutoriel fil rouge : créer l'application *todo*, le modèle *tâche*, et activer l'application

.fx: alternate

--------------------------------------------------------------------------------

# Un exemple complet de vue : la liste des tâches

--------------------------------------------------------------------------------

# 1. Création de la vue

    !python
    # views.py
    from django.views.generic import ListView
    from todo.models import Task

    class TasKView(ListView):
        model = Task

--------------------------------------------------------------------------------

# 2. Création d'une template

    !html
    {# todo/templates/todo/task_list.html #}
    <h1>Liste des tâches</h1>
    {% if tasks %}
      <ul>
        {% for task in tasks %}
          <li>{{ task }}</li>
        {% endfor %}
      </ul>
    {% else %}
      <p>Aucune tâche !</p>
    {% endif %}


--------------------------------------------------------------------------------

# 3. Mapping de l'URL

## Déclaration d'une URL

    !python
    # todo/urls.py
    from django.conf.urls import patterns, include, url
    from todo.views import TaskView
    urlpatterns = patterns('',
        url(r'^task_list$', TaskView.as_view(), name='task_list'),
    )

## Inclusion des URLs de l'application au projet

    !python
    # todoproject/urls.py
    ...
    urlpatterns = patterns('',
        ...
        url(r'^todo/', include('todo.urls')),
    )
    
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

Une vue *basée sur une classe* Django permet de **structurer le code et de le réutiliser** en exploitant notamment l'héritage et les *mixins*.

Django fournit de multiples socles plus ou moins avancés pour construire ce type de vues.

Ces vues sont aussi généralement écrites dans le fichier ``views.py`` de l'application.

## Un exemple tiré de la documention Django

    !python
    # some_app/views.py
    from django.views.generic import TemplateView

    class AboutView(TemplateView):
        template_name = "about.html"

## Les classes fournies par Django

Un excellent site permettant d'avoir un aperçu complet : http://ccbv.co.uk/

--------------------------------------------------------------------------------

# Function-based vs. Class-based views

## Class-based views

Il faut probablement utiliser une vue basée sur une classe ... 

* si une des classes de vues génériques fournies par Django s'approche vraiment du besoin
* si la vue peut être créée par héritage d'une autre en surchargeant seulement des attributs
* si la vue à créer peut être réutilisée par héritage et avec peu de modifications par la suite

## Function-based views

Il faut probablement utiliser une vue basée sur une fonction ... 

* si une implémentation basée sur une classe semble complexe
* si la vue n'a pas vocation à être réutilisée

--------------------------------------------------------------------------------

# Le moteur de template

--------------------------------------------------------------------------------

# Qu'est-ce qu'une template Django ?

C'est un simple fichier texte qui peut générer n'importe quel format de texte (HTML, XML, CSV, ...).

Une template a accès à des **variables** qui lui auront été passées via un **contexte** par la vue.

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


### Cache de variable *with* :

    !python
    {% with total=list.count %} {{ total }} {% endwith %}

Django fournit aussi plusieurs tags nativement et il est possible d'écrire ses propres tags.

--------------------------------------------------------------------------------

# L'héritage de template

L'intérêt de l'héritage de template est par exemple de pouvoir créer un squelette HTML contenant tous les éléments communs du site et définir des blocs que chaque template pourra surcharger.

Dans une template *parent*, la balise ``{% block %}`` permet de définir les blocs surchargeables.

Dans une template *enfant*, la balise ``{% extends %}`` permet de préciser de quelle template celle-ci doit hériter.

--------------------------------------------------------------------------------

# Exemple de template *parent*

    !html
    {# base.html #}
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
    {# todo/templates/todo/task_list.html #}

    {% extends "base.html" %}

    {% block title %}
      Liste des tâches
    {% endblock %}

    {% block content %}
      {% if tasks %}
        <ul>
          {% for task in tasks %}
            <li>{{ task }}</li>
          {% endfor %}
        </ul>
      {% else %}
        <p>Aucune tâche !</p>
      {% endif %}
    {% endblock %}

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
    from myapp.views import MyView
    urlpatterns = patterns('',
        url(r'^myview$', MyView.as_view(), name='myview'),
        ...
    )

## Inclusion d'*URLconf*

Souvent, l'*URLconf* racine inclura les modules URLconf de chaque application :

    !python
    # urls.py
    from django.conf.urls import patterns, url
    urlpatterns = patterns('',
        url(r'^myapp/', include('myapp.urls')),
        ...
    )

--------------------------------------------------------------------------------

# Syntaxe de déclaration d'une URL

## URL sans paramètre
    
    !python
    url(r'^myview$',
        MyView.as_view(),
        name='myview')

La vue aura en argument seulement l'objet ``HttpRequest``.

# URL avec paramètres

    !python
    url(r'^myview_by_month/(?P<year>\d{4})/(?P<month>\d{2})/$',
        MyViewByMonth.as_view(),
        name='myview_by_month'),

La vue aura en argument l'objet ``HttpRequest``, puis les valeurs trouvées dans l'expression régulière (ex: ``year=2014, month=12``).

--------------------------------------------------------------------------------

# Syntaxe de déclaration d'une URL

## Mapping vers une *class-based view*

    !python
    # urls.py
    from django.conf.urls import patterns, url
    from myapp.views import MyView
    urlpatterns = patterns('',
        url(r'^myview$', MyView.as_view()),
        ...
    )

## Mapping vers une *function-based view*

    !python
    # urls.py
    from django.conf.urls import patterns, url
    urlpatterns = patterns('myapp.views',
        url(r'^myview$', 'myview'),
        ...
    )

--------------------------------------------------------------------------------

# Tutoriel fil rouge : créer la vue *listes des tâches* et "détail d'une tâche"

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

# Utilisation d'un formulaire dans une ``function-based view``

    !python
    from django.shortcuts import render
    from django.http import HttpResponseRedirect

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
        return render(request, 'contact.html', {
            'form': form,
        })

--------------------------------------------------------------------------------

# Utilisation d'un formulaire dans une ``class-based view``

    !python
    from myapp.forms import ContactForm
    from django.views.generic.edit import FormView

    class ContactView(FormView):
        template_name = 'contact.html'
        form_class = ContactForm
        success_url = '/thanks/'

        def form_valid(self, form):
            # Process the data in form.cleaned_data and redirect
            # This method is called when valid form data has been POSTed.
            # It should return an HttpResponse.
            # ...
            return super(ContactView, self).form_valid(form)

La classe ``FormView`` fournit d'autres méthodes pour personnaliser la gestion du formulaire dans la vue comme ``form_invalid``, ``get_initial``, ...

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
            exclude = ('borrowed', )

    # views.py
    def add_book(request):
        form = AddBookForm(request.POST or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/books/')
        return render(request, 'add_book.html', {'form': form})

--------------------------------------------------------------------------------

# Tutoriel : Créer les vues d'ajout / modification / détail d'une tâche

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
        barcode = models.ManyToManyField(BarCode,
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

# Tutoriel : Mettre en place un formulaire de filtrage de listes et de tâches

.fx: alternate

--------------------------------------------------------------------------------

# Pour finir ...

--------------------------------------------------------------------------------

# Quelques modules indispensables

## Gestion de la base de données
* ``south`` : migration de schéma et de données pour les évolutions de base de données

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

--------------------------------------------------------------------------------

# Où obtenir des informations ?

## Les sites
* http://www.djangoproject.com [EN]
* http://www.django-fr.org/ [FR]

## Les planètes
* http://www.planetdjango.org/ [EN]
* http://www.django-fr.org/planete/ [FR]

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

