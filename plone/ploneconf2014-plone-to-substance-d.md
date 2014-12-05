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

# Good things in Substance D

All the good things from Pyramid

PLUS 

- stores data in a ZODB,
- provides a management interface (the SDI),
- "Substance D owes much of its spirit to the Zope application server" (sic)

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

DEMO!

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

# DEMO (the real one)

.fx: extra-large

--------------------------------------------------------------------------------

# How does that work

In core, only use components working in both Plone and Substance D.
 
.fx: extra-large

--------------------------------------------------------------------------------

# TTW scripting

TTW scripting is what Rapido is about.

(more globally, a rich TTW experience is vital to any CMS)

PythonScript ➜ zope.untrustedpython

.fx: extra-large

--------------------------------------------------------------------------------

# Catalog

Substance D has its own catalog, and Plone too...

➜ `repoze.catalog` is just fine.
 
.fx: extra-large

--------------------------------------------------------------------------------

# Content persistence

`souper`

<img src="img/Souper-64.png" width="33%" />
 
.fx: extra-large

--------------------------------------------------------------------------------

# Settings persistence

Sharing schemas between Plone and Substance D sounds scary.

➜ **Annotations!!**

Both Plone and Substance D contents can be `IAttributeAnnotatable`.
 
.fx: extra-large

--------------------------------------------------------------------------------

# Forms & widgets

Deform is not rich enough.

I did not considered running z3c.form on Substance D.

➜ **client-side rendering!!** with Angular Schema Form
 
.fx: extra-large

--------------------------------------------------------------------------------

# Access control

Both systems have a granular ACL service.

Probably possible to support them transparently from core, but for now:

**custom security implementation**
 
.fx: extra-large

--------------------------------------------------------------------------------

# My experience with Substance D

PROS:

- Fun!!
- Happy to find all the good ingredients.
 
.fx: extra-large

--------------------------------------------------------------------------------

# My experience with Substance D

CONS:

Not 100% ZCA-ready.

Need to call `config.hook_zca()`, it works fine, no problem.

Just not confortable with the "hook" term here.

We would probably need a local registry.
 
.fx: extra-large

--------------------------------------------------------------------------------

# Conclusion about Plone future

- **ZCA + buildout + ZODB** makes our **identity**, we must preserve it.
- We can find clever approaches to **avoid a full rewrite**.
 
.fx: extra-large

--------------------------------------------------------------------------------

# Conclusion about Plone future

Can we easily migrate to Substance D?
**No**

Should we migrate to something else?
**No**
 
.fx: extra-large

--------------------------------------------------------------------------------

# Thank you!