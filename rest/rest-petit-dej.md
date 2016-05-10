# API REST - Évitez les pièges

.fx: extra-large

--------------------------------------------------------------------------------

# C'était pas mieux avant...

<img src="../tests/img/officier-des-transmissions-morse-1914.jpg" />

(avant) SOAP et (avant avant) CORBA

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

.fx: extra-large

--------------------------------------------------------------------------------

# Les verbes

PUT: modifie une ressource nommée (non-safe, idempotent)

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

Avec des **<u>liens</u>** (hypermedia).

Un endpoint c'est une page web !!

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

# Exemples

    !console
    {
        "id": 1234 ,
        "customers": [
            {"id": 8769, "weight": 100},
            {"id": 3877, "weight": 52},
            ... TROP LONG ...
            {"id": 85, "weight": 56},
            {"id": 64, "weight": 112}
        ]
    }

devient ...

.fx: extra-large

--------------------------------------------------------------------------------

# Exemples

    !console
    {
        "id": 1234 ,
        "customers": "/customers/1234"
    }

.fx: extra-large

--------------------------------------------------------------------------------

# Les pièges

<img src="img/boom.gif" />

.fx: extra-large

--------------------------------------------------------------------------------

# Les pièges

- API incompréhensible,
- API non-communiquable,
- failles de sécurité,
- inadéquation avec les attentes front.

.fx: extra-large

--------------------------------------------------------------------------------

# REST n'est PAS SQL

On expose des services, pas des tables.

    !console
    GET /accounts?id=eric => TRÈS FAIBLE
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

Évitons le ORM-over-IP

.fx: extra-large

--------------------------------------------------------------------------------

# Penser ressources

Les objets métiers du fullback deviennent des ressources REST.

Donc pas de:

    !console
    POST /store
    {"type": "order", id": 56, "customer": 98}

En général, les URLs contiennent **des noms**, pas des verbes.

.fx: extra-large

--------------------------------------------------------------------------------

# La sécurité dans des couches trop hautes

En fullback, pas de contrainte (fondamentale) pour gérer la sécurité sur la couche qu'on souhaite.

.fx: extra-large

--------------------------------------------------------------------------------

# Des développeurs différents

Là où un seul pouvait tout faire, on va avoir 2 personnes.

L'API REST devient leur contrat mutuel :

- établir un consensus,
- API documentée,
- testée et testable.

.fx: extra-large

--------------------------------------------------------------------------------

# Conclusion

Rien ne change, on garde les bonnes pratiques d'hier.

Mais maintenant elles ne sont plus optionnelles.

Donc tout change.

.fx: extra-large

--------------------------------------------------------------------------------