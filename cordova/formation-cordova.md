# Développer des applications mobiles avec Phonegap
## Éric Bréhault

.fx: extra-large

--------------------------------------------------------------------------------

# App / WebApp / site mobile

- **app** : binaire éxécuté par l'OS du téléphone
- **web app** : application éxécutée dans le navigateur du téléphone
- **site mobile** : site web adapté pour l'utilisation depuis un téléphone

.fx: extra-large

--------------------------------------------------------------------------------

# Application hybride ou native

- **native** : compilée avec un SDK pour l'OS du téléphone
- **hybride** : développée avec des technologies web et packagée pour l'OS du téléphone

.fx: extra-large

--------------------------------------------------------------------------------

# PhoneGap ou Cordova ?

- à l'origine:
    - **PhoneGap** développé par Nitobi,
    - racheté par Adobe,
    - cédé à l'Apache Foundation en 2011,
    - s'appelle **Cordova**.
- aujourd'hui:
    - le projet principal est Cordova,
    - PhoneGap existe toujours en tant que **distribution** Cordova d'Adobe

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

# Les plugins officiels

- Battery Status : information sur l’état de la batterie
- Camera : gestion de l’appareil photo
- Console : surcharge du console.log JavaScript
- Contacts : gestion des contacts de l’appareil mobile
- Device : récupération d’informations sur l’appareil lui-même (système - d’exploitation, nom, etc.)

.fx: extra-large

--------------------------------------------------------------------------------

# Les plugins officiels

- Device Motion : accès aux données de l’accéléromètre
- Device Orientation : accès à la boussole
- Dialogs : utilisation des fenêtres d’informations natives
- File : gestion de fichiers
- File Transfer : téléchargement et upload de fichiers

.fx: extra-large

--------------------------------------------------------------------------------

# Les plugins officiels

- Geolocation : accès aux données de localisation géographique ;
- Globalization : gestion de la langue et des fuseaux horaires de l’appareil mobile
- In-App Browser : affichage de sites web directement dans l’application
- Media : lecture audio
- Media Capture : capture audio, vidéo et photo

.fx: extra-large

--------------------------------------------------------------------------------

# Les plugins officiels

- Network Information : accès aux informations réseau de l’appareil mobile
- SplashScreen : gestion de l’écran de chargement
- Statusbar : gestion d’état en haut de l’écran
- Vibration : gestion du vibreur

.fx: extra-large

--------------------------------------------------------------------------------

# Installation

Prérequis:

- Java
- NodeJS
- Android SDK Manager

.fx: extra-large

--------------------------------------------------------------------------------

# Installation

    !console
    $ npm install --global cordova
    $ npm install --global plugman

.fx: extra-large

--------------------------------------------------------------------------------

# Générer une app

    !console
    $ cordova create monApp
        com.makinacorpus.maSuperApp MaSuperApp
    $ cordova platform add android

.fx: extra-large

--------------------------------------------------------------------------------

# Coder le contenu de l'app

Faire un développement web frontend classique.
Mettre le code dans le dossier monApp/www.

Dans index.html, ajouter:

    !html
    <script src="cordova.js"></script>

.fx: extra-large

--------------------------------------------------------------------------------

# Compiler ou éxécuter

    !console
    $ cordova build
    $ cordova run

.fx: extra-large

--------------------------------------------------------------------------------

# Lancer sans terminal

- VM sous Android
- émulateurs

.fx: extra-large

--------------------------------------------------------------------------------

# Ajouter un plugin

    !console
    $ plugman --platform android --project .
        --plugin cordova-plugin-camera

ou

    !console
    $ cordova plugin add cordova-plugin-camera

.fx: extra-large

--------------------------------------------------------------------------------

# Débugger

Débugging front: **inspecteur Chrome**.

Débugging système:

    !console
    $ adb logcat

.fx: extra-large

--------------------------------------------------------------------------------

# Exercice

Créer une app Android avec une page d'accueil affichant un message de bienvenue.

.fx: extra-large

--------------------------------------------------------------------------------

# JavaScript

Pas de `onload`, mais:

    !javascript
    document.addEventListener(
        "deviceready", callback, false);

Aucun plugin ne fonctionnera avant.

.fx: extra-large

--------------------------------------------------------------------------------

# JavaScript, accès aux plugins

En général, les plugins sont exposés via l'objet global `navigator`:

    !javascript
    navigator.vibrate(1000);
    navigator.compass.getCurrentHeading(
        success, error);
    navigator.camera.getPicture(
        success, error, options);

.fx: extra-large

--------------------------------------------------------------------------------

# Exercice

Créer une app Android avec un bouton qui fait vibrer l'appareil et qui affiche
le cap de la boussole.

.fx: extra-large

--------------------------------------------------------------------------------

# Bonnes pratiques

**Utiliser un framework JS**

- Angular
- Backbone
- React (avec ReactNative)

.fx: extra-large

--------------------------------------------------------------------------------

# Bonnes pratiques

**Utiliser un framework CSS**

- Bootstrap
- Foundation

.fx: extra-large

--------------------------------------------------------------------------------

# Bonnes pratiques

**Utiliser un compilateur CSS**

- LESS
- SASS

.fx: extra-large

--------------------------------------------------------------------------------

# Bonnes pratiques

**Utiliser un gestionnaire de dépendances**

- NPM
- NPM + Bower

.fx: extra-large

--------------------------------------------------------------------------------

# Bonnes pratiques

**Utiliser un builder**

- Grunt
- Gulp

.fx: extra-large

--------------------------------------------------------------------------------

# Bonnes pratiques

**Utiliser un gestionnaire de sources**

- Git

.fx: extra-large

--------------------------------------------------------------------------------

# Bonnes pratiques

**Avoir des tests automatiques**

- Jasmine (ou autre),
- CasperJS ou Selenium,
- RobotFramework

.fx: extra-large

--------------------------------------------------------------------------------

# Bonnes pratiques

**Crosswalk**

Embarque Chrome dans l'app pour éviter le navigateur natif sur Android 4.0 à 4.3.

.fx: extra-large

--------------------------------------------------------------------------------

# Ionic

- un maximum de bonnes pratiques
- des optimisations
- Angular
- un framework CSS léger spécifique pour mobile

.fx: extra-large

--------------------------------------------------------------------------------

# Ionic: installation

    !console
    $ npm install -g ionic

.fx: extra-large

--------------------------------------------------------------------------------

# Ionic: créer une app

    !console
    $ ionic start myApp sidemenu
    $ ionic platform add android

.fx: extra-large

--------------------------------------------------------------------------------

# Ionic: lancer en local

    !console
    $ ionic serve -l

.fx: extra-large

--------------------------------------------------------------------------------

# Crosswalk sur ionic

    !console
    $ ionic browser add crosswalk

.fx: extra-large

--------------------------------------------------------------------------------

1. Introduction générale

Différences entre application mobile, site web mobile et WebApp
Introduction aux cross plate-formes mobiles
Avantages du développement mobile multiplate-formes

2. PhoneGap

Présentation générale
Architecture
Langages de programmation
APIs PhoneGap
Installation de l'environnement de développement pour Android
Installation de l'environnement de développement pour iOS

3. HTML5, Responsive Web Design et expérience utilisateur

HTML5 / CSS3
RWD (Media-Queries...)
Expérience utilisateur

4. PhoneGap avancée

Application 1 : Utilisation de SQLite et Jquery mobile dans PhoneGap
Application 2 : Géolocalisation et affichage de la position de l'utilisateur sur Google Maps / OpenStreet Map (Leaflet JS)
Application 3 : Consommation d'un WS Service PHP REST / JSON

5. PhoneGap : une plate-forme extensible ?

À travers des bibliothèques JavaScript disponible
À travers des plugins en natif

--------------------------------------------------------------------------------