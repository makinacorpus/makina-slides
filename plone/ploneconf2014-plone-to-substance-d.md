# Running a Plone product on Substance D
## Éric Bréhault - PloneConf 2014

.fx: extra-large

--------------------------------------------------------------------------------

# Let's be specific about it

"running" is not "migrating".

.fx: extra-large

--------------------------------------------------------------------------------

# Why would we do that?

No obvious reason.

.fx: extra-large

--------------------------------------------------------------------------------

# Why would I do that?

- <strike>I have free time</strike>.
- It sounds fun.
- It might be a good experiment for the future of Plone.

.fx: extra-large

--------------------------------------------------------------------------------

# Substance D

"Substance D owes much of its spirit to the Zope application server" (sic)

.fx: extra-large

--------------------------------------------------------------------------------

# Good things in Substance D

All the good things from Pyramid

PLUS 

- built on Pyramid,
- stores data in a ZODB,
- provides a management interface (the SDI).

.fx: extra-large

--------------------------------------------------------------------------------

# Good things in Substance D

<img src="img/monkey_d_luffy.jpg" class="float-right" />

The D initial!

"So it still lives... The will of D."

.fx: extra-large

--------------------------------------------------------------------------------

# First attempt to integrate Plone

    !console
    $ pcreate -s substanced ./plone

Make sure to load everything in `__init__.py`:

    !python
    config.load_zcml("plone-d.zcml")

.fx: extra-large

--------------------------------------------------------------------------------

# The real experiment case: Rapido

Rapido is the next Plomino version.

It is a complete rewrite.

.fx: extra-large

--------------------------------------------------------------------------------

# Plomino

It is an old Plone product (started in 2006).

Still based on Archetypes.

Stores data into CMF objects.

Uses *extensively* ZCatalog and PythonScript.

.fx: extra-large

--------------------------------------------------------------------------------

# Rapido

(Originally) it is a Plone 5 product.
 
Based on Dexterity.

.fx: extra-large

--------------------------------------------------------------------------------

# Rapido structure 

`rapido.core`

- totally independent on Plone
- provides adapters able to produce the expected behaviors
- requires a storage service

.fx: extra-large

--------------------------------------------------------------------------------

# Rapido structure 

`rapido.souper`

- provides a storage service based on Souper
- (Souper does work on Plone AND Pyramid)

.fx: extra-large

--------------------------------------------------------------------------------

# Rapido structure 

`rapido.plone`

- standard **Dexterity** contents
- adapts them using `rapido.core`
- (ideally) uses nothing but `plone.api`

.fx: extra-large


--------------------------------------------------------------------------------

# Rapido structure 

`rapido.substanced`

- standard <s>Dexterity</s> **substanced.content** classes
- adapts them using `rapido.core`
- uses nothing but <s>`plone.api`</s> **Substance D API**

.fx: extra-large

--------------------------------------------------------------------------------
# Thank you!