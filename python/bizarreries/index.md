# Pièges et bizarreries de (C)Python
## Alex Marandon
## PyConFr 2015

.fx: extra-large

--------------------------------------------------------------------------------

# Makina Corpus 
http://makina-corpus.com

.fx: extra-large

--------------------------------------------------------------------------------

# Source

Adapté d'une présentation en anglais de Amy Halton : [Investigating Python Wats](http://mathamy.com/pycon-recording-investigating-python-wats.html)

http://mathamy.com/pycon-recording-investigating-python-wats.html

.fx: extra-large

--------------------------------------------------------------------------------

* Identité
* Mutabilité
* Portée
* Typage

.fx: extra-large

--------------------------------------------------------------------------------

# Identité

--------------------------------------------------------------------------------

    !pycon
    >>> a = 256   
    >>> b = 256   
    >>> a is b     
    ???

.fx: extra-large

--------------------------------------------------------------------------------

    !pycon
    >>> a = 257   
    >>> b = 257   
    >>> a is b     
    ???

.fx: extra-large

--------------------------------------------------------------------------------

# CPython

https://docs.python.org/2/c-api/int.html

> The current implementation keeps an array of integer objects for all integers
> between -5 and 256, when you create an int in that range you actually just get
> back a reference to the existing object.

--------------------------------------------------------------------------------

# PyPy

http://pypy.readthedocs.org/en/latest/cpython_differences.html#object-identity-of-primitive-values-is-and-id

> Object identity of primitive values works by value equality, not by identity of
> the wrapper. This means that x + 1 is x + 1 is always true, for arbitrary
> integers x

--------------------------------------------------------------------------------

    !pycon
    >>> a = 257; b = 257;
    >>> a is b
    ???

.fx: extra-large

--------------------------------------------------------------------------------

    !pycon
    >>> a = 257   
    >>> b = 257   

est équivalent à :

    !pycon
    >>> code1 = compile("a = 257", filename="",
    ...                 mode="exec")
    >>> code2 = compile("b = 257", filename="",
    ...                 mode="exec")
    >>> code1.co_consts
    (257, None)
    >>> code2.co_consts
    (257, None)
    >>> code1.co_consts[0] is code2.co_consts[0]
    False

.fx: extra-large

--------------------------------------------------------------------------------

    !pycon
    >>> a = 257; b = 257;
    >>> a is b

est équivalent à :

    !pycon
    >>> code = compile("a = 257; b = 257",
                       filename="", mode="exec")
    >>> code.co_consts
    (257, None)

.fx: extra-large

--------------------------------------------------------------------------------

# Mutabilité

--------------------------------------------------------------------------------

On crée un fonction qui prends une liste vide comme paramètre par défaut :


    !pycon
    >>> def add_to_shopping_list(item, shopping_list=[]):
    ...     shopping_list.append(item)
    ...     return shopping_list
    ... 

On s'en sert pour créer une liste de livres à acheter :

    !pycon
    >>> reading_list = add_to_shopping_list("Python Cookbook")
    >>> add_to_shopping_list("Node.js pour les nuls", reading_list)
    ['Python Cookbook', 'Node.js pour les nuls']

--------------------------------------------------------------------------------

Puis pour nos courses d'alimentation :

    !pycon
    >>> alimentation = add_to_shopping_list("Camembert")
    >>> add_to_shopping_list("Pain", alimentation)
    ???

--------------------------------------------------------------------------------

    !pycon
    >>> alimentation
    ['Python Cookbook', 'Node.js pour les nuls', 'Camembert', 'Pain']


--------------------------------------------------------------------------------

    !pycon
    >>> def add_to_shopping_list(item, reading_list=[]):
    ...     reading_list.append(item)
    ...     return reading_list
    ... 
    >>> add_to_shopping_list.__defaults__
    ([],)
    >>> add_to_shopping_list.__defaults__[0].append('Java pour les nuls')

--------------------------------------------------------------------------------

    !pycon
    >>> add_to_shopping_list("Two Scoops of Django")
    ['Java pour les nuls', 'Two Scoops of Django']

--------------------------------------------------------------------------------

# Portée

--------------------------------------------------------------------------------

# Typage

--------------------------------------------------------------------------------
