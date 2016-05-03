# API REST - Évitez les pièges

.fx: extra-large

--------------------------------------------------------------------------------

# C'était pas mieux avant...

<img src="../tests/img/officier-des-transmissions-morse-1914.jpg" />

(avant) SOAP, (avant avant) CORBA

.fx: extra-large

--------------------------------------------------------------------------------

# API REST: une idée simple !

- juste HTTP,
- ses verbes,
- des URLs signifiantes,
- et un contenu hypermedia.

.fx: extra-large

--------------------------------------------------------------------------------

# Les verbes

GET: donne l'état d'une ressource (safe, idempotent)

POST: ajoute une ressource non nommée (non-safe, non-idempotent)

POST (2): modifie une ressource nommée (non-safe, idempotent)

.fx: extra-large

--------------------------------------------------------------------------------

# Les verbes

PUT: ajoute une ressource nommée (non-safe, idempotent)

DELETE: supprime une resource (non-safe, idempotent)

PATCH: modifie partiellement une ressource (non-safe, idempotent)

.fx: extra-large


--------------------------------------------------------------------------------

# Les URLs

    !console
    /des/urls/lisibles

.fx: extra-large

--------------------------------------------------------------------------------

# Les contenus

En général du JSON.

Avec des **liens** (hypermedia).

.fx: extra-large

--------------------------------------------------------------------------------

# Exemples

    !console
    GET /customers

    POST /orders
    {"id": 1234 , "customer": 8769, "weight": 100}

    PUT /orders/1234
    {"customer": 8769, "weight": 100}

    DELETE /customers/345

.fx: extra-large

--------------------------------------------------------------------------------

# Les pièges

<img src="img/boom.gif" />

.fx: extra-large

--------------------------------------------------------------------------------

# REST n'est PAS SQL

On expose des services, pas des tables.

    !console:
    GET /accounts?id=eric => TRES FAIBLE
    GET /accounts/eric => FAIBLE
    GET /myaccount => FORT

.fx: extra-large

--------------------------------------------------------------------------------

# Passer du full backend au frontend/backend

Normalement, rien ne change.

Mais...

.fx: extra-large

--------------------------------------------------------------------------------

# La désintoxication post-ORM


.fx: extra-large

--------------------------------------------------------------------------------

# La sécurité dans des couches trop hautes

.fx: extra-large

--------------------------------------------------------------------------------

# Des développeurs différents

Là où un seul pouvait tout faire, on va avoir 2 personnes.

L'API REST devient leur contrat mutuel. Il faut établir un consensus.

Il faut que ce soit documenté, testable, etc.

.fx: extra-large

--------------------------------------------------------------------------------

Avec l'avènement du développement front-end, exposer ses fonctionnalités métiers via une API REST est devenu un enjeu critique.

Trop souvent influencé par les architectures logicielles back-end traditionnelles ou par les bases de données relationnelles, les API REST sont parfois maladroites voire même contre-productives.

Vous souhaitez designer une API REST équilibrée et efficace et connaître les pièges à éviter ?