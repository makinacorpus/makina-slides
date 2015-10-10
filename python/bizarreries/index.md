# Pièges et bizarreries de (C)Python
## Alex Marandon
## PyConFr 2015

.fx: extra-large

--------------------------------------------------------------------------------

# Makina Corpus 
http://makina-corpus.com

.fx: extra-large

--------------------------------------------------------------------------------

    !pycon
    >>> def func(things=[]):
    ...     things.append("PyConFr")
    ...     return things
    ... 
    >>> func()
    ???

.fx: extra-large

--------------------------------------------------------------------------------

    !pycon
    >>> def func(things=[]):
    ...     things.append("PyConFr")
    ...     return things
    ... 
    >>> func()
    ['PyConFr']
    >>> func()
    ???

.fx: extra-large

--------------------------------------------------------------------------------

    !pycon
    >>> def func(things=[]):
    ...     things.append("PyConFr")
    ...     return things
    ... 
    >>> func()
    ['PyConFr']
    >>> func()
    ['PyConFr', 'PyConFr']
    >>> func()
    ['PyConFr', 'PyConFr', 'PyConFr']

.fx: extra-large

--------------------------------------------------------------------------------

    !pycon
    >>> func.__defaults__
    (['PyConFr', 'PyConFr', 'PyConFr'],)

.fx: extra-large

--------------------------------------------------------------------------------

    !pycon
    >>> func.__defaults__
    (['PyConFr', 'PyConFr', 'PyConFr'],)
    >>> del func.__defaults__[0][:]
    >>> func.__defaults__
    ([],)
    >>> func()
    ['PyConFr']

.fx: extra-large

--------------------------------------------------------------------------------

    !pycon
    >>> def func(things=[]):
    ...     print(id(things))
    ...     things.append("PyConFr")
    ...     return things
    ... 
    >>> func()
    140014883158640
    ['PyConFr']
    >>> func()
    140014883158640
    ['PyConFr', 'PyConFr']
    >>> func()
    140014883158640
    ['PyConFr', 'PyConFr', 'PyConFr']

.fx: extra-large

--------------------------------------------------------------------------------

Python Programming FAQ:

[Why are default values shared between objects?](https://docs.python.org/2/faq/programming.html#why-are-default-values-shared-between-objects)

.fx: extra-large

--------------------------------------------------------------------------------

    !pycon
    >>> functions = []
    >>> for i in range(5):
    ...     def func():
    ...         return i
    ...     functions.append(func)
    ... 
    >>> for func in functions:
    ...     func()
    ... 
    ?
    ?
    ?
    ?
    ?

.fx: extra-large

--------------------------------------------------------------------------------

    !pycon
    >>> functions = []
    >>> for i in range(5):
    ...     def func():
    ...         return i
    ...     functions.append(func)
    ... 
    >>> for func in functions:
    ...     func()
    ... 
    4
    4
    4
    4
    4

.fx: extra-large

--------------------------------------------------------------------------------

    !pycon
    >>> from dis import dis
    >>> dis(functions[0])
      3           0 LOAD_GLOBAL              0 (i)
                  3 RETURN_VALUE        
    >>> dis(functions[4])
      3           0 LOAD_GLOBAL              0 (i)
                  3 RETURN_VALUE        

Doc du module `dis`:

    LOAD_GLOBAL(namei)
        Loads the global named co_names[namei] onto the stack.


.fx: extra-large

--------------------------------------------------------------------------------

    !pycon
    >>> functions = []
    >>> for i in range(5):
    ...     def func(i=i):
    ...         return i
    ...     functions.append(func)
    ... 
    >>> for func in functions:
    ...     func()
    ... 
    0
    1
    2
    3
    4

.fx: extra-large

--------------------------------------------------------------------------------

    !pycon
    >>> dis(functions[0])
      3           0 LOAD_FAST                0 (i)
                  3 RETURN_VALUE        
    >>> dis(functions[4])
      3           0 LOAD_FAST                0 (i)
                  3 RETURN_VALUE        

Doc du module `dis`:

    LOAD_FAST(var_num)
        Pushes a reference to the local co_varnames[var_num] onto the stack.


  .fx: extra-large

--------------------------------------------------------------------------------

Python Programming FAQ:

[Why do lambdas defined in a loop with different values all return the same result?](https://docs.python.org/2/faq/programming.html#why-do-lambdas-defined-in-a-loop-with-different-values-all-return-the-same-result)

.fx: extra-large

--------------------------------------------------------------------------------

    !pycon
    >>> x = 10
    >>> def bar():
    ...     print(x)
    >>> bar()
    ??

.fx: extra-large

--------------------------------------------------------------------------------
    !pycon
    >>> x = 10
    >>> def bar():
    ...     print(x)
    >>> bar()
    10

.fx: extra-large

--------------------------------------------------------------------------------

    !pycon
    >>> x = 10
    >>> def foo():
    ...     print(x)
    ...     x += 1
    ... 
    >>> foo()
    ??

.fx: extra-large

--------------------------------------------------------------------------------

    !pycon
    >>> x = 10
    >>> def foo():
    ...     print(x)
    ...     x += 1
    ... 
    >>> foo()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<stdin>", line 2, in foo
    UnboundLocalError: local variable 'x' referenced before assignment


.fx: extra-large

--------------------------------------------------------------------------------

    !pycon
    >>> def bar():
    ...     print(x)
    ... 
    >>> dis(bar)
      2           0 LOAD_GLOBAL              0 (x)
                  3 PRINT_ITEM          
                  4 PRINT_NEWLINE       
                  5 LOAD_CONST               0 (None)
                  8 RETURN_VALUE        

.fx: extra-large

--------------------------------------------------------------------------------

    !pycon
    >>> def foo():
    ...     print(x)
    ...     x += 1
    ... 
    >>> dis(foo)
      2           0 LOAD_FAST                0 (x)
                  3 PRINT_ITEM          
                  4 PRINT_NEWLINE       

      3           5 LOAD_FAST                0 (x)
                  8 LOAD_CONST               1 (1)
                 11 INPLACE_ADD         
                 12 STORE_FAST               0 (x)
                 15 LOAD_CONST               0 (None)
                 18 RETURN_VALUE        


.fx: extra-large

--------------------------------------------------------------------------------

Python Programming FAQ: [Why am I getting an UnboundLocalError when the variable has a value?](https://docs.python.org/2/faq/programming.html#why-am-i-getting-an-unboundlocalerror-when-the-variable-has-a-value)

> when you make an assignment to a variable in a scope, that variable becomes local to that scope and shadows any similarly named variable in the outer scope


.fx: extra-large

--------------------------------------------------------------------------------

    !pycon
    >>> a = 256   
    >>> b = 256   
    >>> a is b     
    ???

.fx: extra-large

--------------------------------------------------------------------------------

    !pycon
    >>> a = 256   
    >>> b = 256   
    >>> a is b     
    True

.fx: extra-large

--------------------------------------------------------------------------------

    !pycon
    >>> a = 257   
    >>> b = 257   
    >>> a is b     
    ???

.fx: extra-large

--------------------------------------------------------------------------------

    !pycon
    >>> a = 257   
    >>> b = 257   
    >>> a is b     
    False

.fx: extra-large

--------------------------------------------------------------------------------

# CPython

[https://docs.python.org/2/c-api/int.html](https://docs.python.org/2/c-api/int.html)

> The current implementation keeps an array of integer objects for all integers
> between -5 and 256, when you create an int in that range you actually just get
> back a reference to the existing object.

--------------------------------------------------------------------------------

# PyPy

[http://pypy.readthedocs.org/en/latest/cpython_differences.html#object-identity-of-primitive-values-is-and-id](http://pypy.readthedocs.org/en/latest/cpython_differences.html#object-identity-of-primitive-values-is-and-id)

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
    >>> a = 257; b = 257;
    >>> a is b
    True

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

    !pycon
    >>> "100" > 1
    ???

.fx: extra-large

--------------------------------------------------------------------------------

    !pycon
    >>> "100" > 1
    True

.fx: extra-large

--------------------------------------------------------------------------------

    !pycon
    >>> "100" > 1000
    ???

.fx: extra-large

--------------------------------------------------------------------------------

    !pycon
    >>> "100" > 1000
    True

.fx: extra-large

--------------------------------------------------------------------------------

    !pycon
    >>> [1000] > [500]
    ???

.fx: extra-large

--------------------------------------------------------------------------------

    !pycon
    >>> [1000] > [500]
    True

.fx: extra-large

--------------------------------------------------------------------------------

    !pycon
    >>> [1000] > (500, )
    ???

.fx: extra-large

--------------------------------------------------------------------------------

    !pycon
    >>> [1000] > (500, )
    False

.fx: extra-large

--------------------------------------------------------------------------------

[Comparisons](https://docs.python.org/2/library/stdtypes.html#comparisons):

> Objects of different types except numbers are ordered by their type names

.fx: extra-large

--------------------------------------------------------------------------------

    !pycon
    >>> type([1000]).__name__
    'list'
    >>> type((500, )).__name__
    'tuple'
    >>> 'list' > 'tuple'
    False

.fx: extra-large

--------------------------------------------------------------------------------

# Python 3

    !pycon
    >>> [1000] > (500, )
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: unorderable types: list() > tuple()
    >>> "100" > 1000
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: unorderable types: str() > int()

.fx: extra-large

--------------------------------------------------------------------------------


# Inspiration

Une présentation en anglais de Amy Halton : [Investigating Python Wats](http://mathamy.com/pycon-recording-investigating-python-wats.html)

.fx: extra-large

--------------------------------------------------------------------------------
