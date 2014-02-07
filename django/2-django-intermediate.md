# Django perfectionnement

--------------------------------------------------------------------------------

# Gestion des utilisateurs 

--------------------------------------------------------------------------------

# Principaux concepts

La gestion des utilisateurs Django est principalement gérée par le module
``django.contrib.auth``. Ce module introduit plusieurs concepts :

* ``User`` : classe représentant un utilisateur Django ;
* ``Permission`` : classe d'assigner à un utilisateur le droit de faire une certaine action ou non (booléen);
* ``Group`` : classe permettant d'associer plusieurs permissions à un sous-ensemble d'utilisateurs ;
* des vues spécifiques (connexion, déconnexion, ...) ;
* des formulaires (CRUD, connexion, changement de mot de passe, ...) ;
* un *backend* d'authentification souple et personnalisable.

Pour disposer de cette fonctionnalité, le module ``django.contrib.auth`` doit
être présent dans les ``INSTALLED_APPS`` du projet (cf ``settings.py``).

--------------------------------------------------------------------------------

# Les utilisateurs

La classe ``User`` est le coeur du système d'authentification Django. Une instance
de ``User`` représente un utilisateur, une personne qui interagit avec le site. Elle
permet plusieurs choses comme :

* gérer des restriction d'accès ;
* personnaliser des profils utilisateurs ;
* associer des contenus à leur créateur.

## Quelques propriétés

La classe ``User`` fournit quelques propriétés de base comme ``first_name``, ``last_name``,
``username``, ``password``, ``email``. D'autres propriétés, plus *fonctionnelles*,
sont à connaitre :

* ``is_active`` : booléen précisant si le compte est actif ;
* ``is_active`` : booléen précisant si l'utilisateur peut accéder à l'interface d'administration ;
* ``is_superuser`` : booleén spécifiant si l'utilisateur est un super-utilisateur.

--------------------------------------------------------------------------------

# Les permissions

Django fournit un système de permissions assez simple. Il consiste à assigner des
permissions particulières à des utilisateurs ou/et à des groupes.

L'interface d'administration peut notamment utiliser les permissions génériques
``add``, ``change`` et ``delete`` sur chaque modèle existant dans le projet Django.

Pour le modèle ``my_model`` de l'application ``my_app``, les permissions suivantes
pourront être créées par un ``./manage.py syncdb`` :

* 'my_app.add_my_model'
* 'my_app.change_my_model'
* 'my_app.delete_my_model'

Il est aussi possible de créer ses propres permissions.

Quelques fonctions de la classe ``User`` permettent de travailler avec ces permissions,
notamment :

* ``user.get_all_permissions()``
* ``user.has_perm(perm)``

--------------------------------------------------------------------------------

# Les groupes

L'objectif des groupes et de catégoriser des sous-ensembles d'utilisateurs
afin de leur assigner une liste commune de permissions. Exemple :

* *Rédacteur* : permissions d'ajout/modification/suppression d'articles
* *Administrateur* : permissions d'ajout/modification/suppression d'utilisateurs
* ...

--------------------------------------------------------------------------------

# Les vues

Django apporte nativement quelques vues facilitant l'authentification et la gestion
du mot de passe des utilisateurs, principalement :

* ``login``
* ``logout``
* ``logout_then_login``
* ``password_change``
* ``password_reset``
* ...

Quelques settings permettent aussi de simplifier cette gestion :

* ``LOGIN_URL`` : URL vers la vue de connexion
* ``LOGIN_REDIRECT_URL`` : URL de redirection après l'authentification de l'utilisateur
* ``LOGOUT_URL`` : URL de la vue de déconnexion

--------------------------------------------------------------------------------

# Les formulaires

Sans utiliser directement les vues prêtes à l'emploi, il est aussi possible de baser
des vues personnalisées sur des formulaires présents dans la bibliothèque
``django.contrib.auth.forms``.

Ces formulaires réalisent de base certaines vérifications très utiles (unicité du nom 
d'utilisateur, vérification de la ressaisie du mot de passe, ...).

* ``AuthenticationForm`` : formulaire d'authentification
* ``UserChangeForm`` : formulaire d'édition du compte utilisateur
* ``PasswordChangeForm`` : formulaire de changement de mot de passe
* ``PasswordResetForm`` : formulaire de réinitialisation de mot de passe
* ``SetPasswordForm`` : formulaire de création de mot de passe

--------------------------------------------------------------------------------

# Backend d'authentification

La bibliothèque ``django.contrib.auth.backends`` apporte un système de *backend*
d'authentification relativement simple et très souple.

Deux *backends* par défaut sont disponibles:

* ``ModelBackend`` : *backend* d'authentification par défaut utilisant le nom d'utilisateur / mot de passe de l'utilisateur
* ``RemoteUserBackend`` : permet de gérer une authentification depuis une source externe via les entête HTTP

## Écrire un backend personnalisé

Il est assez facile d'écrire son propre *backend* pour personnaliser l'authentification
des utilisateurs en écrivant une simple classe qui implémente certaines fonctions comme :

* ``authenticate``
* ``get_user``
* ...

--------------------------------------------------------------------------------

# Tutoriel : Mettre en place la connexion/déconnexion des utilisateurs et créer un groupe possédant les droits d'administrer les tâches

.fx: alternate

--------------------------------------------------------------------------------

# Aller plus loin avec les modèles

--------------------------------------------------------------------------------

# Le concept ``Queryset``

## Rappel

Un ``Queryset`` représente une collection d'objets provenant de la base de données. Cette collection peut être filtrée, limitée, ordonnée, ... grâce à des méthodes qui correspondent à des clauses SQL.

Il est donc possible de construire des requêtes en base de données via ce QuerySet.

## Exemple

    !python
    >>> Book.objects.filter(title__icontains='django') \
                    .excldue(relase__lte=date('2014-01-01')) \
                    .order_by('price')

--------------------------------------------------------------------------------

# Aller plus loin avec les ``QuerySet``

## La méthode ``values()``

Cette méthode retourne un ``ValuesQuerySet`` qui liste des dictionnaires plutôt que des instances du modèle. Chaque dictionnaire représente une instance ; ses clés correspondent aux attributs de l'instance. Il est possible de spécifier les clés que l'on souhaite récupérer.

    !python
    >>> Book.objects.filter(name__icontais='django') \
                    .values('title' , 'release')

    [{'title': 'Two scoops of django', 'release': date(2013, 08, 31)}, ]


Un ``ValuesQuerySet`` peut être très intéressant quand le nombre d'attributs dont on a besoin est faible, car on évite de charger les instances sous forme de modèles python.

Attention, dans le cas d'un attribut de type ``ForeignKey``, la clé et la valeur retournées seront le nom de le colonne et la valeur trouvée en base de données (ex: ``'author_id': 12``)

--------------------------------------------------------------------------------

# Aller plus loin avec les ``QuerySet``

## La méthode ``values_list()``

Cette méthode est semblable à la précédente mais elle retourne une liste de tuples plutôt qu'une liste de dictionnaires.

    !python
    >>> Book.objects.filter(name__icontais='django') \
                    .values_list('title' , 'release')

    [('Two scoops of django', date(2013, 08, 31)),
     ('Django avancé', date(2013, 05, 15))]

Si un seul attribut est précisé, il est possible d'ajouter le paramètre ``flat=True``
pour obtenir une liste non imbriquée.

    !python
    >>> Book.objects.filter(name__icontais='django') \
                    .values_list('title', flat=True)

    ['Two scoops of django', 'Django avancé']

--------------------------------------------------------------------------------

# Aller plus loin avec les ``QuerySet``

La méthode basique pour créer une instance est d'instancier le modèle puis de faire appel à la méthode ``save()`` de cette instance, mais une autre solution très pratique existe.

## Les méthodes ``create() et get_or_create()``

La méthode ``create()`` permet de réaliser l'opération ci-dessus en une seule instruction :

    !python
    book = Book.objects.create(title="New django book", price="42€")

La méthode ``get_or_create()`` permet de tenter de récupérer un objet (via ``get()``), et de le créer si il n'existe pas. Elle retourne un tuple comprenant un booléen qui précise si l'instance vient d'être créée, et l'instance elle-même :

    !python
    book, created = Book.objects.get_or_create(
        title="New django book", date(2013, 05, 15),
        defaults={'price': '42€'})

Les valeurs passées directement en paramètres sont utilisées lors de l'appel de le méthode ``get()``, les valeurs passées dans ``defaults`` sont utilisées lors de la création éventuelle de l'instance pour initialiser la valeur des propriétés correspondantes.

--------------------------------------------------------------------------------

# Le concept ``Manager``

## Rappel

Un ``Manager`` est l'interface à travers laquelle les opérations de requêtage en base de données sont mises à disposition d'un modèle Django. Chaque modèle possède un ``Manager`` par défaut accessible via la propriété ``objects``.

    !python

    from django.db import models

    class Book(models.Model):
        #...
        objects = models.Manager()

Ce ``Manager`` par défaut fournit nativement quelques méthodes très souvent utilisées, comme :

    !python
    >>> Book.objects.get(pk=12)
    >>> Book.objects.all()
    >>> Book.objects.filter(title__icontains='django')
    >>> Book.objects.exclude(date__lt=date(2013, 01, 01))

--------------------------------------------------------------------------------

# Manager personnalisé

## Objectif

Il peut cependant être utile d'écrire son propre ``Manager`` pour principalement
deux raisons :

* ajouter des méthodes supplémentaires ;
* modifier le ``QuerySet`` initial retourné par le ``Manager``.

## Méthode

Un ``Manager`` personnalisé est une classe héritant de ``Manager`` que l'on instancie dans un attribut du modèle.


    !python
    from django.db import models

    class CustomBookManager(models.Manager):
        # ...

    class Book(models.Model):
        #...
        custom_books = models.Manager()

--------------------------------------------------------------------------------

# Ajouter des méthodes supplémentaires

Écrire un ``Manager`` personnalisé est la bonne solution pour ajouter des méthodes de niveau *table* (qui renvoit des informations sur un ensemble d'instances) contrairement aux méthodes du modèle dites de niveau *ligne* (qui renvoit des informations sur une instance).

    !python
    from django.db import models

    class AuthorManager(models.Manager):
        def with_nb_books(self):
            self.get_query_set() \
                .annotate(nb_books=Count('books')) \
                .order_by('nb_books')

    class Author(models.Model):
        #...
        objects = models.AuthorManager()

&nbsp;

    !python
    >>> authors_with_nb_books = Author.objects.with_nb_books()
    >>> authors_with_nb_books[0]
    <Author : John Doe>
    >>> authors_with_nb_books[0].nb_books
    42

--------------------------------------------------------------------------------

# Modifier le ``QuerySet`` initial

La méthode ``Manager.get_query_set()`` renvoit un ``QuerySet`` par défaut qui correspond à ``Model.objects.all()``. 

Il peut être intéressant de créer un ``Manager`` pour surcharger cette méthode et retourner un ``QuerySet`` personnalisé.

    !python
    from django.db import models

    class EnglishBookManager(models.Manager):
        def get_query_set(self):
             return Manager.get_queryset(self).filter(lang='EN')

    class FrenchBookManager(models.Manager):
        def get_query_set(self):
             return Manager.get_queryset(self).filter(lang='FR')

    class Book(models.Model):
        #...
        objects = models.Manager()
        english_books = models.EnglishBookManager()
        french_books = models.FrenchBookManager()

--------------------------------------------------------------------------------

# Modifier le ``QuerySet`` initial

## Attention !

Quand on surcharge le ``QuerySet`` initial, il est souvent préférable de ne pas remplacer l'attribut ``objects`` par le ``Manager`` personnalisé. 

En effet, ``objects`` est le ``Manager`` utilisé par défaut (dans l'administration par exemple). Il est donc très risqué d'altérer son comportement.

En revanche, remplacer ``objects`` par un ``Manager`` personnalisé qui ne fait qu'ajouter des méthodes personnalisées ne pose pas de problème, puisque le comportement naturel n'est pas altéré.

--------------------------------------------------------------------------------

# Tutoriel : Écrire un ``Manager`` personnalisé permettant de lister les tâches urgentes et non réalisées

.fx: alternate

--------------------------------------------------------------------------------

# L'héritage de modèles

--------------------------------------------------------------------------------

# L'héritage par classe abstraite

Ce type d'héritage est souvent utilisé pour mettre en commun un certain nombre d'informations et/ou de comportements entre plusieurs modèles. Cette classe abstraite ne sera pas utilisé de manière autonome.

## Caractéristiques

* La classe abstraite ne donnera pas lieu a une création de table en base de données ;
* Chaque champ de classe abstraite est présente dans chaque modèle qui en hérite ;
* Il n'est pas possible de faire des requêtes sur la classe abstraite.


--------------------------------------------------------------------------------

# L'héritage par classe abstraite

## Exemple

    !python
    # models.py

    class CommonInfo(models.Model):
        creation_date = models.DateField()
        modification_date = models.DateField()

        class Meta:
            abstract = True

    class Book(CommonInfo):
        title = models.CharField(max_length=100)
        # ...

    class Author(CommonInfo):
        name = models.CharField(max_length=100)
        # ...


--------------------------------------------------------------------------------

# L'héritage traditionnel (multi-tables)

Pour spécialiser un modèle déjà existant (éventuellement d'une application externe) ou/et si on souhaite que les modèles aient des tables séparées, il faut utiliser l'héritabe multi-tables.

## Caractéristiques

* Chaque modèle a sa propre table en base de données ;
* Il est possible de requêter chaque modèle indépendamment ;
* La relation est représentée par un champ ``OneToOneField``


--------------------------------------------------------------------------------

# L'héritage traditionnel (multi-tables)

## Exemple

    !python
    # models.py

    class Book(models.Model):
        title = models.CharField(max_length=100)
        author = models.ForeignKey(Author)

    class Comic(Book):
        illustrator = models.CharField(max_length=100)
        # ...

    class Biography(Book):
        personage = models.CharField(max_length=100)
        # ...

--------------------------------------------------------------------------------

# L'héritage "proxy"

Grâce aux modèles *proxy*, il est possible de modifier le comportement d'un objet (``Manager`` personnalisé, ajout d'une méthode, ...) sans toucher aux données (champs) et donc sans créer une nouvelle table pour ce modèle dérivé.

## Caractéristiques

* Le modèle *proxy* n'engendre pas de nouvelle table en base de données ;
* Le modèle *proxy* et son modèle parent travaille sur la même table ;
* Il est possible de le requêter de manière indépendante.

--------------------------------------------------------------------------------

# L'héritage "proxy"

## Exemple

    !python
    # models.py

    class Book(models.Model):
        title = models.CharField(max_length=100)
        author = models.ForeignKey(Author)

    class OrderedByAuthorBook(Book):

        class Meta:
            proxy = True
            ordering = ['author']

--------------------------------------------------------------------------------

# Tutoriel : Stocker les dates de création/modification pour les listes et les tâches. 

.fx: alternate

--------------------------------------------------------------------------------

# Aller plus loin avec les vues

--------------------------------------------------------------------------------

# Les vues basées sur des classes

Les vues basées sur des classes possèdent des avantages sur les vues classiques :

* possibilité d'organiser le code dans différentes méthodes (notamment selon la méthode HTTP entrante) ;
* possibilité d'utiliser l'héritage et les *mixins* pour factoriser et réutiliser le code.


Django propose une biobliothèque riche permettant de travailler avec des vues basées sur des classes, dont la classe ``View`` est le point central

## Worfklow de base

* La méthode ``as_view()`` est appelée par l'``URLDispatcher`` ;
* Cette méthode instancie la classe et appelle la méthode ``dispatch()`` de l'instance créée ;
* Celle-ci appelle la méthode ``get()``, ``post()``, ... en fonction de la méthode HTTP entrante (GET, POST, ...) ;
* Le traitement qui suit dépend du cas d'utilisation, puis une ``HttpResponse`` est relayée par ``dispatch()``.

--------------------------------------------------------------------------------

# Passage aux vues basées sur des classes

## Vue simple basée sur une fonction

    !python
    from django.http import HttpResponse

    def my_view(request):
        if request.method == 'GET':
            # traitements
            return HttpResponse('result')

## Vue simple basée sur une classe

    !python
    from django.http import HttpResponse
    from django.views.generic.base import View

    class MyView(View):
        def get(self, request):
            # traitements
            return HttpResponse('result')

--------------------------------------------------------------------------------

# Quelques classes de base

## Les vues basiques

Dans ``django.views.generic.base`` :

* ``View`` est la classe *mère* et fourni le workflow vu précédemment.
* ``TemplateView`` est une classe permettant très simplement de faire le rendu d'une template.

## Les vues permettant de traiter un formulaire

Dans ``django.views.generic.edit`` :

* ``FormView`` facilite la gestion d'un formulaire en permettant une bonne organisation du code et en limitant l'indentation.

--------------------------------------------------------------------------------

# Quelques classes de base

## Les vues permettant d'afficher des instances

Dans ``django.views.generic`` :

* ``ListView`` permet de lister très simplement des instances d'un modèle.
* ``DetailView`` permet d'afficher le détail d'une instance d'un modèle.

## Les vues permettant d'afficher des instances

Dans ``django.views.generic.edit`` :

* ``CreateView`` et ``UpdateView`` sont très utiles pour la création/modification d'instance, de l'affichage du formulaire jusqu'à l'enregistrement de l'instance.
* ``DeleteView`` facilite l'implémentation de vues pour la suppression d'intance.

--------------------------------------------------------------------------------

# Protéger une vue

## Les décorateurs

Les décorateurs sont des fonctions Python dont le rôle est de modifier le comportement par défaut d'autres fonctions ou classes. 

Il est par exemple possible de protéger une vue avec un ou plusieurs décorateurs.

## Quelques décorateurs utiles

* ``require_http_methods`` permet de limiter l'accès à une vue sur certaines méthodes HTTP précises ;
* ``login_required`` permet de limiter l'accès à une vue aux utilisateurs connectés ;
* ``permission_required`` permet de limiter l'accès à une vue aux utilisateurs possédant la permission précisée.

--------------------------------------------------------------------------------

# Protéger une vue basée sur une fonction

## Exemple avec ``login_required``

    !python
    from django.contrib.auth.decorators import login_required

    @login_required()
    def my_view(request):
        # Seul un utilisateur connecté peut accéder à cette vue
        # ...

## Exemple avec ``require_http_methods``

    !python
    from django.contrib.auth.decorators import login_required

    @require_http_methods(["GET", "POST"])
    def my_view(request):
        # On ne peut pas accéder à cette vue qu'en GET ou POST
        # ...

--------------------------------------------------------------------------------

# Protéger une vue basée sur une classe

## Dans la vue

    !python
    # views.py
    from django.contrib.auth.decorators import login_required
    from django.utils.decorators import method_decorator

    class MyProtectedView(TemplateView):
        template_name = 'my_protected_view.html'

        @method_decorator(login_required)
        def dispatch(self, *args, **kwargs):
            return super(MyProtectedView, self).dispatch(*args, **kwargs)

## Dans l'``URLConf``

    !python
    # urls.py
    from django.contrib.auth.decorators import login_required
    from my_app.views import MyProtectedView

    urlpatterns = patterns('',
        (r'^secret/', login_required(MyProtectedView.as_view())),
    )

--------------------------------------------------------------------------------

# Tutoriel : Limiter l'accès aux vues aux utilisateurs connectés

.fx: alternate

--------------------------------------------------------------------------------

# Gérer les erreurs

--------------------------------------------------------------------------------

# Retourner une erreur 404

Il est important de gérer les erreurs selon les concepts du protocole HTTP. Une ressource non trouvée sur un site doit donc retourner une erreur de type 404. On utilise pour cela une exception de type ``Http404``.

    !python
    from django.http import Http404

    def book_detail(request, book_id):
        
        try:
            b = Book.objects.get(pk=book_id)
        except Book.DoesNotExist:
            raise Http404
        
        return render('books/detail.html', {'book': b})


--------------------------------------------------------------------------------

# Retourner une erreur 403

Comme pour l'erreur 404, Il est important de gérer les erreurs en accord avec le protocole HTTP. Un problème de permission doit donc engendrer une erreur de type 403. On utilise pour cela une exception de type ``PermissionDenied``.

    !python
    from django.core.exceptions import PermissionDenied

    def book_detail(request, book_id):
        
        if not library.is_registered(user):
            raise PermissionDenied
        
        b = Book.objects.get(pk=book_id)
        
        return render('books/detail.html', {'book': b})

--------------------------------------------------------------------------------

# Affichage par défaut d'une erreur

Plusieurs types d'erreurs peuvent être générées manuellement ou automatiquement par Django, principalement : 400, 403, 404 et 500.

Par défaut, chaque erreur correspond à une vue dont Django fait le rendu quand l'exception est levée :

* Erreur 400 : ``django.views.defaults.bad_request``
* Erreur 403 : ``django.views.defaults.permission_denied``
* Erreur 404 : ``django.views.defaults.page_not_found``
* Erreur 500 : ``django.views.defaults.server_error``

## Mode ``debug``

Le réglage ``TEMPLATE_DEBUG`` (dans ``settings.py``) permet d'activer ou non 
l'affichage de la page de débogage pedant le développement. Cette page vient en
remplacement des vues d'erreurs listées ci-dessus. Il est donc important de
la désactiver en production.

--------------------------------------------------------------------------------

# Personnaliser l'affichage d'une erreur

## Avec une template personnalisée

Pour personnaliser simplement l'affichage, il suffit de nommer la template
403.html, 404.html, ... et Django fera le rendu de cette template automatiquement.

## Avec une vue personnalisée

Si on souhaite que le traitement de l'erreur soit plus complexe, il est possible
de créer une vue dont il faudra préciser le nom dans l'``URLConf`` :

    !python
    # views.py
    def my_403_view(request):
        send_mail_to_admin()
        # ...
        return render('403.html')

    # urls.py
    urlpatterns = patterns('',
        # ...
    )
    handler403 = 'my_app.views.my_403_view'

--------------------------------------------------------------------------------

# Tutoriel : Personnaliser la page d'erreur 404

.fx: alternate

--------------------------------------------------------------------------------

# Aller plus loin avec les templates

--------------------------------------------------------------------------------

# Chaînes de caractères sécurisées et échappement

##  Chaîne de caractère sécurisée

Une chaîne est dite sécurisée quand elle a été marquée comme n'ayant pas besoin
d'échappement lors d'un rendu HTML, c'est à dire que les caractères qui ne
doivent pas être interprétés par le moteur HTML ont déjà été transformés en leurs 
entités appropriées.
Une chaîne sécurisée est représentée par un objet ``SafeString``.

## Échappement

Plusieurs filtres et tag permettent de gérer l'échappement des chaînes :

* ``escape`` : transforme les caractères HTML d'une chaîne en entités (ex: "<" en "``&lt;``")
* ``safe`` : marque la chaîne comme n'ayant pas besoin d'échappement
* ``{% autoescape on|off %}`` : précise si les chaînes doivent être ou non échappées systématiquement à l'intérieur de ce bloc

--------------------------------------------------------------------------------

# Écrire un filtre personnalisé

--------------------------------------------------------------------------------

# Arborescence des fichiers

Les filtres personnalisés doivent être écrits dans une module ``templatetags``
de l'application.


    !console
    ├── todo
    │   ├── admin.py
    │   ├── forms.py
    │   ├── __init__.py
    │   ├── models.py
    │   ├── templatetags
    │   │   ├── __init__.py
    │   │   └── my_todo_app_filters.py


Le nom du fichier en lui-même n'a pas d'importance, mais il sera utilisé pour
charger les filtres au niveau des templates.

--------------------------------------------------------------------------------

# Structure d'un filtre

Un filtre personnalisé est une simple fonctions python qui prend un ou deux arguments :

* la valeur de la variable dont on veut modifier l'affichage (pas nécessairement
une chaîne de caractère)
* un argument optionnel (qui peut avoir une valeur par défaut ou non)

Un filtre sera sans argument supplémentaire sera appelé de la manière suivante :

    !python
    {{ variable|my_simple_filter }}

et un filtre avec argument sera utilisé ainsi :

    !python
    {{ variable|my_filter:"foo" }}

--------------------------------------------------------------------------------

# Quelques exemples

## Exemple d'un filtre avec un seul argument

    !python
    # filters.py
    def lower(value):
        """Converts a string into all lowercase"""
        return value.lower()

    {# template #}
    {{ variable|lower }}

## Exemple d'un filtre avec deux arguments

    !python
    # filters.py
    def cut(value, arg):
        """Removes all values of arg from the given string"""
        return value.replace(arg, '')

    {# template #}
    {{ variable|cut:'0' }}

--------------------------------------------------------------------------------

# Enregistrement du filtre personnalisé

La class ``Library`` permet d'ajouter les filtres personnalisés à la bibliothèque
de filtres Django pour pouvoir ensuite les charger et les utiliser dans les
templates. Deux solutions :

## Via un appel de fonction classique

    !python
    from django import template
    register = template.Library()

    def my_filter(value):
        # code du filtre

    register.filter('my_filter', my_filter)

## Via un décorateur

    !python
    from django import template
    register = template.Library()

    register.filter()
    def my_filter(value):
        # code du filtre

--------------------------------------------------------------------------------

# Filtres et échappement

L'échappement (ou non) de la chaîne retournée en sortie du filtre doit être
contrôlé.

Si le filtre n'introduit pas de caractère HTML (comme "&" ou "<"), il peut être
marqué comme sécurisé au moment de l'enregistrement grâce à l'équipement ``is_safe``.

    !python
    register.filter(is_safe=True)
    def my_filter(value):
        # code du filtre

Django traîtera alors l'échappement de la chaîne en entrée en sachant que le
filtre personnalisé n'aura pas d'impact.


Il est aussi possible de marqué la chaîne comme sécurisée manuellement en sortie du 
filter (nécessaire si le filtre introduit du HTML).

    !python
    from django.utils.safestring import mark_safe

    register.filter(is_safe=True)
    def my_filter(value):
        # code du filtre
        return mark_safe(output)

--------------------------------------------------------------------------------

# Tutoriel : Écrire un filtre personnalisé qui transforme la date d'une tâche en  temps restant pour la réaliser

.fx: alternate

--------------------------------------------------------------------------------

# Gestion des fichiers

* Upload
* Media
* Static

--------------------------------------------------------------------------------

# Internationalisation et localisation

--------------------------------------------------------------------------------

# Quelques réglages

Plusieurs réglages dans ``settings.py`` permettent d'activer ou non certaines
fonctionnalités liés à l'internationalisation et la localisation :

* ``USE_I18N`` : active ou non le module de traduction
* ``USE_L10N`` : active ou non l'affichages des dates et des nombres selon la langue
* ``USE_TZ`` : active ou non la gestion des fuseaux horaires
* ``LANGUAGE_CODE`` : langue par défaut
* ``LANGUAGES`` : liste des langues connues par l'application


--------------------------------------------------------------------------------

# Traduire l'interface (fichiers python)

## Utilisation de la bibliothèque ``gettext``

Pour traduire les différents textes de l'interface, on utilise les fonctions ``ugetttext``,
ou plus souvent ``ugettext_lazy``. Pour la simplicité de l'écriture, on importe
généralement cette fonction avec l'alias '_'.

    !python
    from django.utils.translation import ugettext_lazy as _

## Exemple d'utilisation dans un modèle

    !python
    # models.py
    from django.utils.translation import ugettext_lazy as _

    class Book(models.Model):
        name = models.CharField(max_length=100,
                                verbose_name=_('Title'))

        class Meta:
            db_table = 'task'
            verbose_name = _('Book')
            verbose_name_plural = _('Books')

--------------------------------------------------------------------------------

# Traduire l'interface (fichiers python)

## Exemple d'utilisation dans un formulaire

    !python
    # forms.py
    from django.utils.translation import ugettext_lazy as _

    class BookSearchForm(models.Model):
        search_text = models.CharField(label=_('Search text'))

## Exemple d'utilisation dans une vue

    !python
    # views.py
    from django.utils.translation import ugettext_lazy as _
    
    def confirmation(request, result):
        if result == 'OK':
            confirmation = _('Verification succeeded')
        else:
            confirmation = _('Verification failed')
        # Render form
        return render(request, 'confirmation.html', {
            'confirmation': confirmation,
        })

--------------------------------------------------------------------------------

# Traduire l'interface (templates)

Deux tags permettent de traduire l'interface directement dans les templates
sont utilisés :

## Le tag {% trans %}

Il permet de traduire une chaine de caractère ou le contenu d'une variable.

    !html
    <title>{% trans "List of books" %}</title>
    <title>{% trans page_title %}</title>

## Le tag {% blocktrans %}

Il permet de mixer chaînes de caractères et variables pour traduire des chaînes complexes.

    !html
    {% blocktrans with book_t=book|title author_t=author|title %}
    <p>This is {{ book_t }} by {{ author_t }}</p>
    {% endblocktrans %}

--------------------------------------------------------------------------------

# Gérer les fichiers de traduction

## Créer / mettre à jour le fichier de traduction

La commande ``makemessages`` permet de créer le fichier traduction pour une langue
donnée (fichier texte avec l'extension ".po" contenant les identifiants de messages
et les traductions correspondantes). Elle doit être lancée depuis la racine
de l'application ou du projet pour lequel le fichier doit être créé car la commande
génère une arborescence de dossiers ``locale/LANG/LC_MESSAGES``.

    !console
     $ django-admin.py makemessages -l fr


## Compiler le fichier de traduction

La commande ``compilemessages`` permet de compiler le fichier de traduction
pour qu'il soit utilisable dans le code Python.

    !console
     $ django-admin.py compilemessages -l fr

--------------------------------------------------------------------------------

# Scripting

Ecrire une commande manage.py

--------------------------------------------------------------------------------

# Administration

Customisation basique

--------------------------------------------------------------------------------

# Introduction aux tests

Quoi mettre ?

--------------------------------------------------------------------------------

# Merci !