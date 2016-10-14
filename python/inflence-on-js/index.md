# How Python influences JavaScript

Iteration protocols and generators

by [Alex Marandon](http://alexmarandon.com)

.fx: extra-large

![](img/logo-black.png)

---

# Motivation

> Given the years of development in Python and similarities to ECMAScript in
> application domains and programmer communities, we would rather follow than
> lead. By standing on Python’s shoulders we reuse developer knowledge as well as
> design and implementation experience. The trick then becomes not borrowing too
> much from Python, just enough to gain the essential benefits: **structured
> value-generating continuations** and a **general iteration protocol**.

[Brendan Eich, 2006](http://wiki.ecmascript.org/doku.php?id=discussion:iterators_and_generators#iterators_and_generators)

---

> general iteration protocol

→ iterables and iterators

> structured value-generating continuations

→ generators

.fx: extra-large


---

# Initial plan

    !js
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

[Brendan Eich, 2006](https://brendaneich.com/2006/02/python-and-javascript/)

---

# Protocol

* Smalltalk already used the term *protocol*
* An informal interface
* Not enforced by compiler
* Defined by documentation and conventions
* Examples of protocols : iterable, iterator, sequence, file, descriptor, etc.

![](img/Smalltalk80book.jpg)

---

# Running example

URL parameters representing multiple values:

    !text
    http://example.com/path/one,two,three

We'll design a type to treat those parameters as strings:

    !pycon
    >>> params = ListParam("one,two,three")
    >>> print("My list param is {}.".format(params))
    My list param is one,two,three.

Or to iterate on them:

    !pycon
    >>> for param in params:
    ...     print("One of its params is {}.".format(param))
    ... 
    One of its params is one.
    One of its params is two.
    One of its params is three.

---

# Iterable

Object with an ``__iter__()`` method that returns an [iterator](https://docs.python.org/2/library/stdtypes.html#iterator-types)

    !py
    class ListParam:

        def __init__(self, csv_str):
            self.csv_str = csv_str
            self.params = self.csv_str.split(",")

        def __iter__(self):
            # Conforms to the iterable protocol
            return iter(self.params) # Lists are iterables

        def __str__(self):
            return self.csv_str

---

# Iterable example usage


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


---

# ``for`` loop behind the scene

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

---

# JavaScript iterable

    !js
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

---

# JavaScript ``for-of`` loop

    !js
    > var params = listParam("one,two,three");
    > console.log("My list param is " + params + ".");
    My list param is one,two,three.
    > for (var param of params)
    ...     console.log("One of its params is " + param + ".")
    One of its params is one.
    One of its params is two.
    One of its params is three.


Note: ``for-of`` is a new kind of for loop, equivalent to Python's for loop and different from JavaScript's original ``for (;;)`` and ``for-in`` loops.

---

# Iterator

Let's consider again how we provided an iterator to the for loop:

    !py
    def __iter__(self):
        return iter(self.params)  # Returns an iterator

This works because Python lists are iterables :

    !pycon
    >>> from collections.abc import Iterable
    >>> isinstance([], Iterable)
    True

What if we didn't have lists in Python ?

---

# A custom iterator

    !py
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

---

# Using our custom iterator


    !py
    from paramiterator import ParamIterator

    class ListParam:

        def __init__(self, csv_str):
            self.csv_str = csv_str

        def __str__(self):
            return self.csv_str

        def __iter__(self):
            return ParamIterator(self.csv_str)

---

# JavaScript custom iterator

     !js
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

---

# Playing with our JS iterator


    !js
    > var it = paramIterator("one,two,three");
    undefined
    > it.next()
    { done: false, value: 'one' }
    > it.next()
    { done: false, value: 'two' }
    > it.next()
    { done: false, value: 'three' }
    > it.next()
    { done: true, value: undefined }


---

# Using our JS iterator in an iterable

    !js
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

Try it:

    !js
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

---

# Other JavaScript features influenced by Python

- EcmaScript 2015 module system
- EcmaScript 2016 decorators

---

# Conclusion

- browsers don't support Python natively
- JavaScript borrows important concepts from Python
- let's write pythonic JavaScript!
