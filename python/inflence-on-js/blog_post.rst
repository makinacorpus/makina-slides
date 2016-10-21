Background
==========

In 2006, Brendan Eich, creator of JavaScript, wrote this `in the ECMAScript wiki <http://wiki.ecmascript.org/doku.php?id=discussion:iterators_and_generators#iterators_and_generators>`_:

  Given the years of development in Python and similarities to ECMAScript in
  application domains and programmer communities, we would rather follow than
  lead. By standing on Python’s shoulders we reuse developer knowledge as well as
  design and implementation experience. The trick then becomes not borrowing too
  much from Python, just enough to gain the essential benefits: **structured
  value-generating continuations** and a **general iteration protocol**.

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

Array comprehensions actually never made it to the ECMAScript standard but as I
write this, my version of Firefox does support `some form of it <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Array_comprehensions>`_:

.. sourcecode:: javascript

    > let numbers = [1,2,3];
    > [for (i of numbers) i * 2]
    Array [ 2, 4, 6 ]

Iteration protocols and generators, on the other hand, did make it to the
standard. They ended up a bit different from what was initially sketched but
they still captured the essence of what existed in Python. In this article
we're going to look at both Python and JavaScript incarnations while reviewing
the underlying concepts.


Protocols
---------

Python has the notion of protocol which can be described as an informal
interface, not enforced by the compiler but based on conventions and
documentation. Among the most well-known Python protocols we can mention
`descriptor <https://docs.python.org/3.6/howto/descriptor.html>`_, `sequence <https://docs.python.org/3.6/glossary.html#term-sequence>`_ or `file-like objects <https://docs.python.org/3.6/glossary.html#term-file-object>`_. `Iterable <https://docs.python.org/3.6/glossary.html#term-iterable>`_ and `iterators <https://docs.python.org/3.6/glossary.html#term-iterator>`_ are also two of these
protocols.

These protocols are often quite simple and we're perfectly allowed to
implement them only partially. By implementing them partially or completely,
we increase the chances that our objects will play well with Python built-in
functions and standard library modules, which often speak these protocols.

Creating objects that conform to these protocols is at the heart of writing
idiomatic Python and the iteration protocols are among the most important ones.

Iterable
========

In a project I work on, we have web services that take URL parameters with
multiple values. To save a bit of URL space, instead of using the usual convention
``name=value1&name=value2&name=value3``, we represent
these parameters as comma-separated strings such as ``value1,value2,value3``.
Sometimes I need to use these parameters as strings, for instance to construct
URLs, and sometimes I need to treat them as collections of values, for
instance to loop through them. In order to do that, I'd like to avoid using ``split`` and ``join`` all over the code to convert between strings and lists. We're going to design a type that allows us to
treat these parameters as strings or to iterate on them, depending on the
situation.

To conform to the iterable protocol, we need to define a class with a
``__iter__()`` method that returns an
`iterator <https://docs.python.org/2/library/stdtypes.html#iterator-types>`_. The
``iter`` function allows us to create an iterator on a list, so we'll delegate to it:

.. sourcecode:: python

    class ListParam:

        def __init__(self, csv_str):
            self.csv_str = csv_str
            self.params = self.csv_str.split(",")

        # Conform to the iterable protocol
        def __iter__(self):
            # Lists are iterables
            # Calling iter on them returns an iterator
            return iter(self.params)

        def __str__(self):
            # Allows the object to be used to format strings
            return self.csv_str


Here is how we can use this class:

.. sourcecode:: pycon


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

As you can see, we can use the object either in string formatting context or in
a ``for`` loop and it will do the right thing. That's because the ``for`` loop
is aware of the iterable protocol. Behind the scene, it actually does the
equivalent of the following while loop:

.. sourcecode:: pycon

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

It then repeatedly calls ``next`` on that iterator until a ``StopIteration`` exception is
raised. That is the iterator protocol, which will get back to in a bit. For now
let's come back to JavaScript and see how we can create an object that supports
the iterable protocol.

JavaScript iterable
-------------------

Here is a function that returns an object literal implementing the iterable
protocol. In JavaScript an iterable must have a method with the computed name
``Symbol.iterator``. Here that method just delegates to the ``Symbol.iterator`` method of the ``Array`` object.

.. sourcecode:: javascript

    function listParam(csvStr) {
      var params = csvStr.split(",");
      return {
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


Please note that the ``for-of`` loop is a new kind of JavaScript ``for`` loop.
It's equivalent to Python's ``for`` loop but different from JavaScript's
original ``for (;;)`` and ``for-in`` loops. The point of the ``for-of`` loop is that it speaks the iterable and iterator protocols.

Iterator
========

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

A custom iterator
-----------------

An iterator is simply an object that has a ``__next__`` method. That method returns a new value each time it's called, until it raises ``StopIteration`` because it doesn't have any more values to return:

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

        def __iter__(self):
            return self # An iterator should also be iterable


Using our custom iterator
-------------------------

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

JavaScript custom iterator
--------------------------

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
importantly it doesn't raise and exception when it has no more values to return. Instead, each time it's called, it returns an object with a ``done``
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


Using our JS iterator in an iterable
------------------------------------

We can now get rid of the array and use our iterator in our iterable:

.. sourcecode:: javascript

    function listParam(csvStr) {
      return {
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

Iterators made easy: generators
===============================

This is all working fine but manually coding an iterator is a bit verbose. To simplify the process of creating iterators, we can use generator objects which are also iterators. Playing with a simple generator shows that it implements the iterator protocol:

.. sourcecode:: pycon

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

And checking it against the Iterator `abstract base class <https://docs.python.org/dev/library/collections.abc.html>`_ confirms this observation:

.. sourcecode:: pycon

    >>> from collections.abc import Iterator
    >>> isinstance(gen, Iterator)
    True


Generator-based iterable
------------------------

So instead instead of explicitly returning an iterator from our ``__iter__`` method, we can turn that method into a generator method:

.. sourcecode:: python

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


Generators in JavaScript
------------------------

In JavaScript, generator functions are similar to Python, although we `need to mark them with a star character <http://stackoverflow.com/questions/27778105/what-purpose-of-asterisk-in-es6-generator-functions/27787527#27787527>`_.

.. sourcecode:: javascript

    > function* make_gen() {
    ... yield "one";
    ... yield "two";
    ... yield "three";
    ... }


They also return an object conforming to the JavaScript iterator protocol:

.. sourcecode:: javascript

    > var gen = make_gen();
    > gen.next()
    { value: 'one', done: false }
    > gen.next()
    { value: 'two', done: false }
    > gen.next()
    { value: 'three', done: false }
    > gen.next()
    { value: undefined, done: true }


Generator-based iterable in JS
------------------------------

So we can convert our ``Symbol.iterator`` method into a generator method:

.. sourcecode:: javascript


    function listParam(csvStr) {
      return {
        [Symbol.iterator]: function*() {
          var position = 0;
          var commaPosition = csvStr.indexOf(",", position);
          while (commaPosition != -1) {
            // Yield from current position to next comma
            yield csvStr.slice(position, commaPosition);
            // Advance to char after next comma
            position = commaPosition + 1
            // Find next comma position
            commaPosition = csvStr.indexOf(",", position);
          }
          // No comma left, yielding what's left
          yield csvStr.slice(position);
        },
        toString: function() {
          return csvStr;
        }
      }
    }

Usage notes
-----------

So far we've seen how we can use iteration protocols and generators to
create data types that can be iterated over. Keep in mind that those types
don't necessary need to represent flat sequences, you may want to allow
easy iteration on the elements of tree structures or on randomly nested collections
by exposing the iterable interface.

`Generators are great <http://www.dabeaz.com/generators/>`_ to transform collections of items in successive
steps without creating intermediate lists. This can save a lot of memory
when we need to transform large data sets.

But they can also be used in more ordinary code to refactor loops into separate
functions. Say for instance you have a function that iterates over a collection
and processes each item before passing it to another function:

.. sourcecode:: python

    def some_function(a, b, collection):
        data = a + b
        for item in collection:
            new_item = copy_item(item)
            # ...
            # Do more stuff with the new item
            # ...
            do_something_with(data, new_item)

As the transformation process becomes more complex, or is shared between different parts of the code, you'll likely want to factor it out to a separate transformation function like this:

.. sourcecode:: python

    def some_function(a, b, collection):
        data = a + b
        new_collection = transform_collection(collection)
        for new_item in new_collection:
            do_something_with(data, new_item)

    def transform_collection(collection):
        result = []
        for item in collection:
            new_item = copy_item(item)
            # ...
            # Do more stuff with the new item
            # ...
            result.append(new_item)
        return result


This kind of function can easily be simplified by converting it to a generator:

.. sourcecode:: python

    def transform_collection(collection):
        for item in collection:
            new_item = copy_item(item)
            # ...
            # Do more stuff with the new item
            # ...
            yield new_item

On top of reducing boilerplate code, this new version uses less memory by
avoiding the creation of a new list, which can be useful with large data
sets.

More generator features
-----------------------

There are more advanced generator features that I didn't mention and that are supported by both languages: generator delegation and sending values to generators. 

Generator delegation allows to delegate to another iterable, similarly to how a function call allows to delegate to another function. Because generator objects are iterable this can also be used to delegate to another generator.

Since version 3.3, Python has the ``yield from`` statement:

.. sourcecode:: python

    yield from [1, 2, 3]
    yield from another_gen()

JavaScript uses ``yield*``:

.. sourcecode:: javascript

    yield* [1, 2, 3]
    yield* another_gen()

It's also possible to send values to a generator, which is useful to implement coroutines. In Python you use the ``send`` method:

.. sourcecode:: python

    gen_obj.send(value)

And you receive the value from within the generator like this:

.. sourcecode:: python

    value = yield

In JavaScript you can send a value by passing an argument to the ``next`` method:

.. sourcecode:: javascript

    gen_obj.next(value)

And you recieve from within a generator exactly like in Python:

.. sourcecode:: javascript

    value = yield

I won't go into too much details about those more advanced features, but
you can see that JavaScript kept following Python's lead even for more
recent features.

Conclusion
==========

I hope this article helped you understand or review iteration protocols
and generators in both Python and JavaScript. If you use both languages
these protocols are worth mastering because except for minor details
they're similar in both languages and the patterns you'll come up with in
one language will apply equally well to the other.
