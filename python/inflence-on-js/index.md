# How Python influenced JavaScript

by [Alex Marandon](http://alexmarandon.com)

.fx: extra-large

![](img/logo-black.png)

---

# Motivation

> Given the years of development in Python and similarities to ECMAScript in
> application domains and programmer communities, we would rather follow than
> lead. By standing on Python’s shoulders we reuse developer knowledge as well as
> design and implementation experience. The trick then becomes not borrowing too
> much from Python, just enough to gain the essential benefits: structured
> value-generating continuations and a general iteration protocol.

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
