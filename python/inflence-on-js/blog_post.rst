# Motivation

In 2006, Brendan Eich, creator of JavaScript, wrote this `in the EcmaScript wiki <http://wiki.ecmascript.org/doku.php?id=discussion:iterators_and_generators#iterators_and_generators>`_:

> Given the years of development in Python and similarities to ECMAScript in
> application domains and programmer communities, we would rather follow than
> lead. By standing on Python’s shoulders we reuse developer knowledge as well as
> design and implementation experience. The trick then becomes not borrowing too
> much from Python, just enough to gain the essential benefits: **structured
> value-generating continuations** and a **general iteration protocol**.

By **structured value-generating continuations** he was referring to Python generators and by **general iteration protocol** he was
referring to the iterator and iterable protocols that Python already had.

He also posted `on his blog <https://brendaneich.com/2006/02/python-and-javascript/>`_ this sketch of what it might eventually look like, including array comprehensions:

.. sourcecode:: javascript

    js> function count(n) {
    for (var i = 0; i < n; i++)
    yield i;
    }
    js> g = count(10)
    [object Generator]
    js> g.next()
    0
    js> g.next()
    1
    js> two_to_nine = [i for i in g]
    2,3,4,5,6,7,8,9
    js> squares_to_20 = [i * i for i in count(20)]
    0,1,4,9,16,25,36,49,64,81,100,121,144,169,196,225,256,289,324,361

Array comprehensions actually never made it to the EcmaScript standard but as I
write this my version of Firefox does support [some form of it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Array_comprehensions):

.. sourcecode:: javascript

    let numbers = [1,2,3];
    undefined
    [for (i of numbers) i * 2]
    Array [ 2, 4, 6 ]

Iteration protocols and generators, on the other hand, did make it to the
standard. They ended up a bit different from what was planned but they still
captured the essence of what existed in Python. In this article we're going
to look at both Python and JavaScript incarnations while reviewing the
underlying concepts.


# Protocols

Python has the notion of protocol which can be described as an informal
interface, not enforced by the compiler but based on conventions and
documentation. Among the most well-known Python protocols we can mention
sequence, file, descriptor... Iterable and iterators are also two of those
protocols.

These protocols are often quite simple and we're perfectly allowed to
implement them only partially. By implementing them partially or completely,
we increase the chances that our objects will play well with Python built-in
functions and standard library modules, which often speak these protocols.

Creating objects that conform to these protocols is at the heart of writing
idiomatic Python and the iteration protocols are among the most important
ones.

# Python Iterable

In a project I work on, we have web services that take URL parameters with
multiple values. To save a bit of URL space, instead of using the standard
``name=value1&name=value2&name=value3`` query string convention, we represent
these parameters as comma-separated strings such as ``value1,value2,value3``.
Sometimes I need to use those parameters as string, for instance to construct
URLs, and sometimes I need to treat them as collections of values, for
instance to loop over them. In order to do that I'd like to avoid having to ``split`` and ``join`` on the comma all over the code. We're going to design a type that allows us to
treat these parameters as strings or to iterate on them, depending the
situation.

To conform to the iterable protocol, we need to define a class with an ``__iter__()`` method that returns an [iterator](https://docs.python.org/2/library/stdtypes.html#iterator-types). The ``iter`` function allows us to create an iterator on a list, so that's what we'll do first:


.. sourcecode:: python

    class ListParam:

        def __init__(self, csv_str):
            self.csv_str = csv_str
            self.params = self.csv_str.split(",")

        def __iter__(self):
            # Conforms to the iterable protocol
            return iter(self.params) # Lists are iterables

        def __str__(self):
						# Allows the object to be treated as a string
            return self.csv_str


Here is how we can use this class:

.. sourcecode:: pycon


    !pycon
    >>> from listparam import ListParam
    >>> 
    >>> params = ListParam("one,two,three")
    >>> 
    >>> print("My list param is {}.".format(params))
    My list param is one,two,three.
    >>> 
    >>> for param in params:
    ...     print("One of its params is {}.".format(param))
    ... 
    One of its params is one.
    One of its params is two.
    One of its params is three.

As you can see, we can use the object either in string formatting context or
in a ``for`` loop and it will do the right thing. That's because the ``for`` loop is aware of the iterable protocol. Behind the scene, it actually does the equivalent of the following while loop:

.. sourcecode:: pycon

    !pycon
    >>> it = iter(params)
    >>> while True:
    ...     try:
    ...         param = next(it)
    ...         print("One of its params is {}.".format(param))
    ...     except StopIteration:
    ...         break
    ... 
    One of its params is one.
    One of its params is two.
    One of its params is three.

First it calls the ``iter`` function on the object, which will trigger a call
to its ``__iter__`` method and return an iterator on the list of parameters.

It then repeatidely calls next on that iterator until a ``StopIteration`` is raised. That is iterator protocol, which will get back to in a bit. For now let's come back to JavaScript and see how we can create an object that supports the iterable protocol.

# JavaScript iterable

.. sourcecode:: javascript

Here is a function that returns an object literal implementing the iterable
protocol. In JavaScript an iterable must have a method with the computed name
``Symbol.iterator``. Here that method just delegates to the ``Symbol.iterator`` method of the ``Array`` object.


.. sourcecode:: javascript

    function listParam(csvStr) {
      var params = csvStr.split(",");
      return {
        csvStr: csvStr,
        [Symbol.iterator]: function() {  // Eq. to __iter__
          return params[Symbol.iterator]();  // Eq. to iter()
        },
        toString: function() { // Eq. to __str__
          return csvStr;
        }
      }
    }

In order to iterate over that object, we need to use the  JavaScript ``for-of`` loop:

.. sourcecode:: javascript

    > var params = listParam("one,two,three");
    > console.log("My list param is " + params + ".");
    My list param is one,two,three.
    > for (var param of params)
    ...     console.log("One of its params is " + param + ".")
    One of its params is one.
    One of its params is two.
    One of its params is three.


Please note that the ``for-of`` loop is a new kind of JavaScript ``for`` loop. It's equivalent to Python's ``for`` loop but different from JavaScript's original ``for (;;)`` and ``for-in`` loops.

---

# Iterator

Let's consider again how we provided an iterator to the for loop:


.. sourcecode:: python

    def __iter__(self):
        return iter(self.params)  # Returns an iterator

This works because Python lists are iterables :

.. sourcecode:: pycon

    >>> from collections.abc import Iterable
    >>> isinstance([], Iterable)
    True

Because Python lists are iterables, calling ``iter`` on them will return an iterator, so we can delegate to them to return an iterator from our own ``__iter__`` method.

Now what if we didn't have lists in Python? How can we build an iterator
object that can used by the ``for`` loop? You might have guessed the answer: we need to make an object that implements the iterator protocol!

# A custom iterator

An iterator is simply an object that has ``__next__`` method. That method returns a new value each time it's called, untill it raises ``StopIteration`` because it doesn't have any more values to return:

.. sourcecode:: python

    class ParamIterator:

        def __init__(self, csv_str):
            self.csv_str = csv_str
            self.position = 0
            self.done = False

        def __next__(self):
            if self.done:
                raise StopIteration
            comma_position = self.csv_str.find(",", self.position)
            if comma_position == -1:
                self.done = True
                return self.csv_str[self.position:]
            else:
                result = self.csv_str[self.position:comma_position]
                self.position = comma_position + 1
                return result

        # Something's actually missing to make it a proper iterator.
        # We'll come back to it.

## Using our custom iterator

Now instead of relying on Python lists to implement our iterable, we can use
our new iterator type:

.. sourcecode:: python

    from paramiterator import ParamIterator

    class ListParam:

        def __init__(self, csv_str):
            self.csv_str = csv_str

        def __str__(self):
            return self.csv_str

        def __iter__(self):
            return ParamIterator(self.csv_str)

## JavaScript custom iterator

The JavaScript way to make iterators is similar in essence but differs slightly in the details:

.. sourcecode:: javascript

     function paramIterator(csv_str) {
       var position = 0;
       var done = false;
       return {
         next: function() {
           if (done)
             return {done: true, value: undefined};
           var commaPosition = csv_str.indexOf(",", position);
           if (commaPosition === -1) {
             done = true;                          // No comma found
             var value = csv_str.slice(position);  // Return what's left
           } else {
             // Extract string from here to next comma
             var value = csv_str.slice(position, commaPosition);
             position = commaPosition + 1; // Advance to char after comma
           }
           return {done: false, value: value};
         }
       }
     }

The method to implement is called ``next`` instead of ``__next__`` but most
importantly it doesn't raise and exception when it has no more values to returni. Instead, each time it's called, it returns an object with a ``done``
property, indicating if it has returned all available values, and a
``value`` property holding the value itself:


.. sourcecode:: javascript

    > var it = paramIterator("one,two,three");
    > it.next()
    { done: false, value: 'one' }
    > it.next()
    { done: false, value: 'two' }
    > it.next()
    { done: false, value: 'three' }
    > it.next()
    { done: true, value: undefined }


## Using our JS iterator in an iterable

.. sourcecode:: javascript

    function listParam(csvStr) {
      var params = csvStr.split(",");
      return {
        csvStr: csvStr,
        [Symbol.iterator]: function() {
          return paramIterator(csvStr);
        },
        toString: function() {
          return csvStr;
        }
      }
    }

Let's try it:

.. sourcecode:: javascript

  	> var params = listParam("one,two,three");
  	> console.log("My list param is " + params + ".");
  	My list param is one,two,three.
  	> for (var param of params)
  	...     console.log("One of its params is " + param + ".")
  	One of its params is one.
  	One of its params is two.
  	One of its params is three.

---

# Iterators made easy: generators

    !py
    >>> def make_gen():
    ...    yield "one"
    ...    yield "two"
    ...    yield "three"
    ... 
    >>> gen = make_gen()
    >>> next(gen)
    'one'
    >>> next(gen)
    'two'
    >>> next(gen)
    'three'
    >>> next(gen)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration
    >>> from collections.abc import Iterator
    >>> isinstance(gen, Iterator)
    True


---

# Generator-based iterable

  	!py
    class ListParam:

        def __init__(self, csv_str):
            self.csv_str = csv_str

        def __str__(self):
            return self.csv_str

        def __iter__(self):
            position = 0
            comma_position = self.csv_str.find(",", position)
            while comma_position != -1:
                yield self.csv_str[position:comma_position]
                position = comma_position + 1
                comma_position = self.csv_str.find(",", position)
            yield self.csv_str[position:]


---

# Generators in JavaScript

    !js
    > function* make_gen() {
    ... yield "one";
    ... yield "two";
    ... yield "three";
    ... }
    > var gen = make_gen();
    > gen.next()
    { value: 'one', done: false }
    > gen.next()
    { value: 'two', done: false }
    > gen.next()
    { value: 'three', done: false }
    > gen.next()
    { value: undefined, done: true }

---

# Generator-based iterable in JS


  	!js
    function listParam(csvStr) {
      return {
        [Symbol.iterator]: function*() {
          var position = 0;
          var commaPosition = csvStr.indexOf(",", position);
          while (commaPosition != -1) {
            yield csvStr.slice(position, commaPosition);
            position = commaPosition + 1
            commaPosition = csvStr.indexOf(",", position);
          }
          yield csvStr.slice(position);
        },
        toString: function() {
          return csvStr;
        }
      }
    }

