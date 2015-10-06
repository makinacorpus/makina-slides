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

# Portée

--------------------------------------------------------------------------------

# Typage

--------------------------------------------------------------------------------
