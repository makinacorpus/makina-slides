# Développer des applications mobiles avec Phonegap
## Éric Bréhault

.fx: extra-large

--------------------------------------------------------------------------------

# PhoneGap ou Cordova ?

- à l'origine:
    - **PhoneGap** développé par Adobe,
    - cédé à l'Apache Foundation en 2011,
    - s'appelle **Cordova**.
- aujourd'hui:
    - le projet principal est Cordova,
    - PhoneGap existe toujours en tant que **distribution** Cordova

.fx: extra-large

--------------------------------------------------------------------------------

# Le principe

- on construit une app en HTML/JS,
- Cordova utilise le navigateur du mobile pour l'afficher,
- le même code marchera sur tous les OS.

.fx: extra-large

--------------------------------------------------------------------------------

# Le principe

- en plus des fonctionnalités de base, on a accès à des plugins,
- les plugins sont développés en natif pour chaque OS,
- on y accède en Javascript.

.fx: extra-large

--------------------------------------------------------------------------------

# Les plugins

- accès au système de fichiers,
- status réseau,
- GPS,
- caméra,
- contacts,
- etc.

.fx: extra-large

--------------------------------------------------------------------------------

# Les plugins

Attention à la liste des OS proposés par chaque plugin!

Vous pouvez développer vos propres plugins.

.fx: extra-large

--------------------------------------------------------------------------------

# Générer une app

    !console
    $ npm install cordova
    $ cordova create monApp
        com.makinacorpus.maSuperApp MaSuperApp

.fx: extra-large

--------------------------------------------------------------------------------

# Coder l'app

Faire un développement web frontend classique.
Mettre le code dans le dossier monApp/www.

.fx: extra-large

--------------------------------------------------------------------------------

# Compiler

    !console
    $ cordova platform add android
    $ cordova build

.fx: extra-large

--------------------------------------------------------------------------------

# DÉMO

.fx: extra-large

--------------------------------------------------------------------------------

# Outillage

- inspection du DOM avec Chrome/Safari,
- adb pour Android,
- XCode pour iOS.

.fx: extra-large

--------------------------------------------------------------------------------

# Bonnes pratiques

- adopter les méthodes front-end,
- utiliser un framework JS,
- utiliser une grid responsive,
- faire un maximum dans son navigateur.

.fx: extra-large

--------------------------------------------------------------------------------

# Frameworks et "distributions"

- ngCordova pour Angular,
- ionic,
- Steroids.

.fx: extra-large

--------------------------------------------------------------------------------

# DÉMO IONIC

    !console
    $ npm install ionic
    $ ionic monApp sidemenu

.fx: extra-large

--------------------------------------------------------------------------------

# Cas réels

.fx: extra-large

--------------------------------------------------------------------------------
# Merci !