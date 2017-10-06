# Headless CMS
## Éric Bréhault

--------------------------------------------------------------------------------

# Why?

Just because frontend allows to create better websites.

--------------------------------------------------------------------------------

# "Drupal is a Burning Platform?"

https://drupal.sh/drupal-burning-platform

"PHP is increasingly not the first language that new web developers pick up. Instead JavaScript has become the dominant new language, and this is an area where Drupal is playing catch-up at best with it's aged front end architecture"

"Nowadays Drupal is seen by many as the Sharepoint of the JavaScript generation - a tool they don't want to use, but one that is pushed to them by the enterprise."

--------------------------------------------------------------------------------

# Is it the end of CMSes?

CMS features are still needed

(you know, it is not easy to implement a breadcrumb).

--------------------------------------------------------------------------------

# What is the current headless CMS offer?

- Firebase? Actually, that's more about creating applications.
- Contentful? That's just a CRUD implemented in PHP!!
- CosmicJS? Do we expect our customers to manage their content in a Django admin like UI?

--------------------------------------------------------------------------------

# Plone rocks

- excellent features (hierarchical content, flexible content-types, access control and workflow)
- secured
- opensource

--------------------------------------------------------------------------------

# What can we offer?

Now:

- Plone RESTAPI
- @plone/restapi-angular

Soon?

- plone.server
- @plone/ui-angular
- @plone/(...)-react

--------------------------------------------------------------------------------

# What is @plone/restapi-angular?

Simple Angular 4 API to use the Plone RESTAPI and build web sites easily.

https://github.com/plone/plone.restapi-angular

- traversing
- BrowserView-like view registration
- z3c.form-like form library


--------------------------------------------------------------------------------

# Real-life example

https://ddt65.terralego.com/

Backend:

- Vanilla Plone 5
- content-types created TTW

Frontend:

- declare the needed views
- overrides few @plone/restapi-angular templates
- PDF generation!!

Management:

- initial data import with Postman
- daily changes with WebDAV

--------------------------------------------------------------------------------

# But web sites can also be totally different

- new UI are possible
- mobile apps
- electron apps
- ...

--------------------------------------------------------------------------------

# Sprint objectives

- Promote Plone as a headless CMS.
- Promote our Angular tooling.

--------------------------------------------------------------------------------
