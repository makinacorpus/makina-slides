# Développer des applications mobiles avec Phonegap
## Éric Bréhault

.fx: extra-large

--------------------------------------------------------------------------------

# Plan

- Introduction
    - App, WebApp ou site mobile
    - Application hybride ou native
    - PhoneGap ou Cordova ?
    - Le principe
    - Les plugins officiels
- Installation / premiers pas
    - Prérequis
    - Installation
    - Générer une app simple
    - Débugger
- Bonnes pratiques
    - Les bonnes pratiques front-end
    - Gestionnaire de sources
    - Crosswalk
- Ionic
    - Installation
    - Utiliser les outils du client
    - La grille CSS et les composants
    - L'API
- Utilisation des plugins
    - camera
    - file
    - local notification
    - push notification
    - InAppBrowser
    - SQLite
- Tests
    - tests unitaires
    - tests d'acceptance
- Publication
    - Google PlayStore
    - AppStore

--------------------------------------------------------------------------------

# Introduction

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

# Installation / premiers pas

.fx: extra-large

--------------------------------------------------------------------------------

# Prérequis

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
    $ plugman install --platform android
        --project .
        --plugin cordova-plugin-camera

ou

    !console
    $ cordova plugin add cordova-plugin-camera

.fx: extra-large

--------------------------------------------------------------------------------

# Débugger

Débugging front: **inspecteur Chrome** chrome://inspect/#devices

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

.fx: extra-large

--------------------------------------------------------------------------------

# Utiliser un framework JS

- Angular
- Backbone
- React (avec ReactNative)

.fx: extra-large

--------------------------------------------------------------------------------

# Utiliser un framework CSS

- Bootstrap
- Foundation

.fx: extra-large

--------------------------------------------------------------------------------

# Utiliser un compilateur CSS

- LESS
- SASS

.fx: extra-large

--------------------------------------------------------------------------------

# Utiliser un gestionnaire de dépendances

- NPM
- NPM + Bower

.fx: extra-large

--------------------------------------------------------------------------------

# Utiliser un builder

- Grunt
- Gulp

.fx: extra-large

--------------------------------------------------------------------------------

# Utiliser un gestionnaire de sources

- Git

.fx: extra-large

--------------------------------------------------------------------------------

# Avoir des tests automatiques

- Jasmine (ou autre),
- CasperJS ou Selenium,
- RobotFramework

.fx: extra-large

--------------------------------------------------------------------------------

# Crosswalk

Embarque Chrome dans l'app pour éviter le navigateur natif sur Android 4.0 à 4.3.

.fx: extra-large

--------------------------------------------------------------------------------

# Ionic

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

# Les plugins

.fx: extra-large

--------------------------------------------------------------------------------

# Capture d'image

- soumission directe: champ `<input type="file" capture="camera" />`
- obtention du fichier en local: plugin camera

.fx: extra-large

--------------------------------------------------------------------------------

# Système de fichier

- `cordova-plugin-file`,
- FileSystem HTML5,
- url en `cdvfile://`,
- ngCordova fournit `$cordovaFile`.

.fx: extra-large

--------------------------------------------------------------------------------

# Système de fichier

    !javascript
    $cordovaFile.writeFile(
        cordova.file.dataDirectory,
        "file.txt", "text", true)
    .then(function (success) {
        // success
    }, function (error) {
        // error
    });

.fx: extra-large

--------------------------------------------------------------------------------

# Zip

https://github.com/MobileChromeApps/zip

    !javascript
    zip.unzip(zipLocalPath, toPath, callback)

.fx: extra-large

--------------------------------------------------------------------------------

# SQLite

- WebSQL standard HTML5,
- https://github.com/brodysoft/Cordova-SQLitePlugin : pas de limite de taille, pas de soucis au nettoyage de cache.

.fx: extra-large

--------------------------------------------------------------------------------

# Local notification

- `https://github.com/katzer/cordova-plugin-local-notifications.git`,
- ngCordova fournit `$cordovaLocalNotificationSource`.

.fx: extra-large

--------------------------------------------------------------------------------

# Notification

`https://github.com/Telerik-Verified-Plugins/PushNotification`

Le backend doit pousser les notifications vers GCM et APN.

.fx: extra-large

--------------------------------------------------------------------------------

# InAppBrowser

    !console
    $ cordova plugin add
        cordova-plugin-inappbrowser

et on peut ouvrir des pages externes avec:

    !javascript
    cordova.InAppBrowser.open(url, "_system");

ou:

    !html
    <a href="..." target="_system">

.fx: extra-large

--------------------------------------------------------------------------------

# Les tests

.fx: extra-large

--------------------------------------------------------------------------------

# Tests unitaires

    !console
    $ npm install jasmine-core karma
        karma-chrome-launcher karma-jasmine
        --save-dev

.fx: extra-large

--------------------------------------------------------------------------------

# Tests unitaires

    !javascript
    module.exports = function(config){
      config.set({
        basePath : './',
        files : [
          'www/lib/ionic/js/ionic.bundle.js',
          'www/lib/angular-mocks/angular-mocks.js',
          'www/js/app.js',
          'www/js/controllers.js',
          'www/js/app_test.js'
        ],
        autoWatch : true,
        frameworks: ['jasmine'],
        browsers : ['Chrome'],
        plugins : [
                'karma-chrome-launcher',
                'karma-jasmine'
                ],
      });
    };

--------------------------------------------------------------------------------

# Tests unitaires

    !javascript
    describe('MainCtrl', function() {
        var controller, scope;

        beforeEach(module('starter'));
        beforeEach(module('starter.controllers'));

        beforeEach(inject(function($controller, $rootScope) {
            scope = $rootScope.$new();
            controller = $controller('AppCtrl', {
                $scope: scope
            });
        }));

        it('should have scope to be defined', function() {
            expect(controller).toBeDefined();
        });

    });


--------------------------------------------------------------------------------

# Robotframework

    !console
    $ pip install robotframework
    $ pip install robotframework-selenium2library
    $ pip install robotframework-debuglibrary

ChromeDriver http://chromedriver.storage.googleapis.com/index.html?path=2.19/

.fx: extra-large

--------------------------------------------------------------------------------

# Cas métier

.fx: extra-large

--------------------------------------------------------------------------------

# La publication

.fx: extra-large

--------------------------------------------------------------------------------

# Les icons et splashcreens

    !console
    $ ionic resources

.fx: extra-large

--------------------------------------------------------------------------------

# Signature Android

- créer un keystore (avec keytool ou le studio),
- ajouter un fichier `./platforms/android/ant.properties`:

    key.store=/chemin/vers/le/keystore
    key.alias=la_clef

.fx: extra-large

--------------------------------------------------------------------------------

# Release

    !console:
    $ cordova build --release

.fx: extra-large

--------------------------------------------------------------------------------

# Publier l'app sur le PlayStore

- créer un compte Google developer,
- rédiger la fiche de l'app,
- uploader l'APK signé.

.fx: extra-large

--------------------------------------------------------------------------------

# Préparer la fiche sur l'AppStore

- créer un compte Apple developer,
- déclarer l'app,
- obtenir les différents certificats,
- packager avec Xcode et uploader.

.fx: extra-large

--------------------------------------------------------------------------------

# XCode

- importer le projet XCode généré dans `./platforms/ios`,
- saisir manuellement la target version (5.1.1 alors que la valeur minimale proposée est 6.0),
- puis Products / Archive pour produire l'archive.

.fx: extra-large

--------------------------------------------------------------------------------

# Mises en garde pour XCode

On doit valider régulièrement les notifications sur le compte AppleDev, sinon la publication est bloquée.

.fx: extra-large

--------------------------------------------------------------------------------

# Publier via des services tiers

- PhoneGap
- ionic.io
- Fastlane (pour iOS)

.fx: extra-large

--------------------------------------------------------------------------------
