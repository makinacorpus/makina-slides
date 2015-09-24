# Happy hacking with Plone
## Éric Bréhault - PloneConf 2015

.fx: extra-large

--------------------------------------------------------------------------------

# We, Plone developers

- invest time in Plone,
- build something nice and attractive,
- feel pround of it.

.fx: extra-large

--------------------------------------------------------------------------------

# We, Plone developers

<video src="video/architect.mp4" poster="none.jpg" width="100%" controls="true"></video>
<p style="font-size: 16px">from "Les Vacances du Petit Nicolas" by Laurent Tirard</p>

--------------------------------------------------------------------------------

# The users

<img src="img/users.jpg" width="100%" />
<p style="font-size: 16px">from "Les Vacances du Petit Nicolas" by Laurent Tirard</p>

.fx: extra-large

--------------------------------------------------------------------------------

# The users play

<video src="video/users.mp4" poster="none.jpg" width="100%" controls="true"></video>
<p style="font-size: 16px">from "Les Vacances du Petit Nicolas" by Laurent Tirard</p>

.fx: extra-large

--------------------------------------------------------------------------------

# The conflict

- They loved it.
- We are desperate.

.fx: extra-large

--------------------------------------------------------------------------------

# We retaliate

<img src="img/nuclear-plant.jpg" width="100%" />

.fx: extra-large

--------------------------------------------------------------------------------

# Pharmakon

φάρμακον: medecine, drug, poison

**Any medecine is also a poison.**

.fx: extra-large

--------------------------------------------------------------------------------

# My solution

<img src="img/inflatable-castle.jpg" width="100%" />

.fx: extra-large

--------------------------------------------------------------------------------

# Hackability is a feature

It is **not** a flaw.

It must be **provided as a tool**.

.fx: extra-large

--------------------------------------------------------------------------------

# A hacking tool

- to change or add whatever we want in our Plone site
- through a modern and pleasant web interface

.fx: extra-large

--------------------------------------------------------------------------------

# ZMI?

<img src="img/zmi.png" width="100%" />

.fx: extra-large

--------------------------------------------------------------------------------

# The Plone Theming editor!!

Already a "hacking" tool:

**non-Plone experts can change the entire theme**.

.fx: extra-large

--------------------------------------------------------------------------------

# Diazo theory

**We Write XSLT, So You Don't Have To**

<img src="img/diazo-1.png" height="100%" />

.fx: extra-large

--------------------------------------------------------------------------------

# Diazo reality

**Guess what? I am writing tons of XSLT!!**

<img src="img/diazo-2.png" height="100%" />

.fx: extra-large

--------------------------------------------------------------------------------

# What we need

<img src="img/diazo-3.png" height="100%" />

.fx: extra-large

--------------------------------------------------------------------------------

# Content-to-content 

On-the-fly content changes with `<before/>` and `<after/>`.

    !xml
    <before css:content="#content-core">
        <a href="mailto:contact@diazo.org">
            Ask for help
        </a>
    </before>

.fx: extra-large

--------------------------------------------------------------------------------

# Content-to-content 

On-the-fly content insertion.

    !xml
    <before css:content-children="#main">
        <include css:content="#breadcrumbs" />
    </before>

.fx: extra-large

--------------------------------------------------------------------------------

# Content-to-content 

On-the-fly remote content insertion.

    !xml
    <before css:content-children="#main">
        <include href="/news"
            css:content="#breadcrumbs" />
    </before>

.fx: extra-large

--------------------------------------------------------------------------------

# We want more 

- create our own chuncks of content
- implement our own scripts

with basic knowledge of **HTML and Python**.

.fx: extra-large

--------------------------------------------------------------------------------

# Rapido 


.fx: extra-large

--------------------------------------------------------------------------------

Montrer un super chateau de sable.
Users want to play.
Montrer comment les enfants le cassent (Petit Nicolas)
montrer ce qu'on a fait: une centrale nucléaire
That's solid, but nobody wants to play with a nuclear plant (if some wants, they are most likely terrorists)
A solution is often its own poison.
montrer la solution: un chateau gonflable (solid, we can play with, does not attract terrorists). But that's a metaphor.
Hackability is not flaw, it is a feature.
It needs to be provided as a tool.
(Montrer la ZMI: it has frameset!! who ever developed an app involving frameset ? parler des digital native)
Montrer rapido avec diazo: assez cool (ref IEEE 589.2 cool-level official measurement)
(demo: un petit formualaire Do you want a Willy Waller 2006? How many Willy Waller  do you want ? + demo stupid captcha où on enlève l'ACTION du form avec diazo)
puis montrer rapido dans mosaic