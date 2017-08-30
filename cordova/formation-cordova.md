# Développer des applications mobiles avec Phonegap
## Éric Bréhault


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


--------------------------------------------------------------------------------

# App / WebApp / site mobile

- **app** : binaire éxécuté par l'OS du téléphone
- **web app** : application éxécutée dans le navigateur du téléphone
- **progressive web app** : site web qui est reconnu comme une app
- **site mobile** : site web adapté pour l'utilisation depuis un téléphone


--------------------------------------------------------------------------------

# Application hybride ou native

- **native** : compilée avec un SDK pour l'OS du téléphone
- **hybride** : développée avec des technologies web et packagée pour l'OS du téléphone


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


--------------------------------------------------------------------------------

# Le principe

- en plus des fonctionnalités de base, on a accès à des plugins,
- les plugins sont développés en natif pour chaque OS,
- on y accède en Javascript.


--------------------------------------------------------------------------------

# Les plugins officiels

- Battery Status : information sur l’état de la batterie
- Camera : gestion de l’appareil photo
- Console : surcharge du console.log JavaScript
- Contacts : gestion des contacts de l’appareil mobile
- Device : récupération d’informations sur l’appareil lui-même (système - d’exploitation, nom, etc.)


--------------------------------------------------------------------------------

# Les plugins officiels

- Device Motion : accès aux données de l’accéléromètre
- Device Orientation : accès à la boussole
- Dialogs : utilisation des fenêtres d’informations natives
- File : gestion de fichiers
- File Transfer : téléchargement et upload de fichiers


--------------------------------------------------------------------------------

# Les plugins officiels

- Geolocation : accès aux données de localisation géographique ;
- Globalization : gestion de la langue et des fuseaux horaires de l’appareil mobile
- In-App Browser : affichage de sites web directement dans l’application
- Media : lecture audio
- Media Capture : capture audio, vidéo et photo


--------------------------------------------------------------------------------

# Les plugins officiels

- Network Information : accès aux informations réseau de l’appareil mobile
- SplashScreen : gestion de l’écran de chargement
- Statusbar : gestion d’état en haut de l’écran
- Vibration : gestion du vibreur


--------------------------------------------------------------------------------

# Installation / premiers pas


--------------------------------------------------------------------------------

# Prérequis

- Java
- NodeJS
- Android SDK Manager


--------------------------------------------------------------------------------

# Installation

    !console
    $ npm install --global cordova
    $ npm install --global plugman


--------------------------------------------------------------------------------

# Générer une app

    !console
    $ cordova create monApp
        com.makinacorpus.maSuperApp MaSuperApp
    $ cordova platform add android


--------------------------------------------------------------------------------

# Coder le contenu de l'app

Faire un développement web frontend classique.
Mettre le code dans le dossier monApp/www.

Dans index.html, ajouter:

    !html
    <script src="cordova.js"></script>


--------------------------------------------------------------------------------

# Compiler ou éxécuter

    !console
    $ cordova build
    $ cordova run


--------------------------------------------------------------------------------

# Lancer sans terminal

- VM sous Android
- émulateurs


--------------------------------------------------------------------------------

# Ajouter un plugin

    !console
    $ plugman install --platform android
        --project .
        --plugin cordova-plugin-camera

ou

    !console
    $ cordova plugin add cordova-plugin-camera


--------------------------------------------------------------------------------

# Débugger

Débugging front: **inspecteur Chrome** chrome://inspect/#devices

Débugging système:

    !console
    $ adb logcat


--------------------------------------------------------------------------------

# Exercice

Créer une app Android avec une page d'accueil affichant un message de bienvenue.


--------------------------------------------------------------------------------

# JavaScript

Pas de `onload`, mais:

    !javascript
    document.addEventListener(
        "deviceready", callback, false);

Aucun plugin ne fonctionnera avant.


--------------------------------------------------------------------------------

# JavaScript, accès aux plugins

En général, les plugins sont exposés via l'objet global `navigator`:

    !javascript
    navigator.vibrate(1000);
    navigator.compass.getCurrentHeading(
        success, error);
    navigator.camera.getPicture(
        success, error, options);


--------------------------------------------------------------------------------

# Exercice

Créer une app Android avec un bouton qui fait vibrer l'appareil et qui affiche
le cap de la boussole.


--------------------------------------------------------------------------------

# Bonnes pratiques


--------------------------------------------------------------------------------

# Utiliser un framework JS

- Angular
- Backbone
- React


--------------------------------------------------------------------------------

# Utiliser un framework CSS

- Bootstrap
- Foundation


--------------------------------------------------------------------------------

# Utiliser un compilateur CSS

- LESS
- SASS


--------------------------------------------------------------------------------

# Utiliser un gestionnaire de dépendances

NPM


--------------------------------------------------------------------------------

# Utiliser un builder

- webpack
- scripts NPM


--------------------------------------------------------------------------------

# Utiliser un gestionnaire de sources

- Git


--------------------------------------------------------------------------------

# Avoir des tests automatiques

- Jasmine (ou autre),
- Protractor,
- RobotFramework


--------------------------------------------------------------------------------

# Crosswalk

Embarque Chrome dans l'app pour éviter le navigateur natif sur Android 4.0 à 4.3.


--------------------------------------------------------------------------------

# Ionic


--------------------------------------------------------------------------------

# Ionic

- un maximum de bonnes pratiques
- des optimisations
- Angular
- un framework CSS léger spécifique pour mobile


--------------------------------------------------------------------------------

# Ionic: installation

    !console
    $ npm install -g ionic


--------------------------------------------------------------------------------

# Ionic: créer une app

    !console
    $ ionic start myApp sidemenu
    $ ionic platform add android


--------------------------------------------------------------------------------

# Ionic: lancer en local

    !console
    $ ionic serve -l


--------------------------------------------------------------------------------

# Crosswalk sur ionic

    !console
    $ ionic browser add crosswalk


--------------------------------------------------------------------------------

# Les plugins


--------------------------------------------------------------------------------

# Capture d'image

- soumission directe: champ `<input type="file" capture="camera" />`
- obtention du fichier en local: plugin camera


--------------------------------------------------------------------------------

# Système de fichiers

- `cordova-plugin-file`,
- FileSystem HTML5,
- url en `cdvfile://`,
- `@ionic-native/file` fournit un service prêt à l'emploi.


    !console

    $ ionic plugin add --save cordova-plugin-file

    $ npm install --save @ionic-native/file

--------------------------------------------------------------------------------

# Système de fichiers

- dataDirectory: les fichiers gérés par l'app,
- externalDataDirectory: les fichiers partagés entre les différentes apps.

--------------------------------------------------------------------------------

# Système de fichiers

    !javascript
    import { File } from '@ionic-native/file';

    constructor(private file: File) { }

    ...

    this.file.checkDir(this.file.dataDirectory, 'mydir')
    .then(
        () => console.log('Directory exists')
    ).catch(
        err => console.log('Directory doesnt exist')
    );


--------------------------------------------------------------------------------

# Système de fichiers

    !console
    $ adb shell
    $ run-as com.mycompany.myapp
    $ cd files

--------------------------------------------------------------------------------

# Zip

    !console
    $ ionic plugin add --save cordova-plugin-zip
    $ npm install --save @ionic-native/zip
    !javascript
    import { Zip } from '@ionic-native/zip';

    constructor(private zip: Zip) { }

    ...

    this.zip.unzip('dossier/archive.zip', 'dossier/dest')
    .then((result) => {
        ...    
    })


--------------------------------------------------------------------------------

# SQLite

- WebSQL standard HTML5,
- pas de limite de taille, pas de soucis au nettoyage de cache.

    !console
    $ cordova plugin add cordova-sqlite-storage --save
    $ npm install --save @ionic/storage


--------------------------------------------------------------------------------

# Local notification

    !console
    $ ionic plugin add --save de.appplant.cordova.plugin.local-notification
    $ npm install --save @ionic-native/local-notifications


--------------------------------------------------------------------------------

# Notification

- PhoneGap (phonegap-plugin-push + @ionic-native/push)
- OneSignal (onesignal-cordova-plugin + @ionic-native/onesignal)

Le backend doit pousser les notifications vers l'API choisie (ou directement vers GCM et APN).


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


--------------------------------------------------------------------------------

# WhiteList

Autoriser l'accès à un backend

    !xml
    <access origin="*" />
    <allow-intent href="*" />
    <allow-navigation href="*" />
    <meta http-equiv="Content-Security-Policy" content="default-src *; style-src 'self' 'unsafe-inline'; script-src 'self' 'unsafe-inline' 'unsafe-eval'" />

--------------------------------------------------------------------------------

# Les tests


--------------------------------------------------------------------------------

# Tests unitaires

    !console
    $ npm install jasmine-core karma
        karma-chrome-launcher karma-jasmine
        --save-dev
    $ bower install angular-mocks


--------------------------------------------------------------------------------

# Tests unitaires - karma.conf.js

    !javascript
    module.exports = function(config){
      config.set({
        basePath : './',
        files : [
          'www/lib/ionic/js/ionic.bundle.js',
          'www/lib/angular-mocks/angular-mocks.js',
          'www/lib/DEPENDANCE_1',
          'www/lib/DEPENDANCE_2',
          'www/js/*.js'
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

# Tests unitaires - app_test.js

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

# Tests unitaires

    !console
    $ ./node_modules/karma/bin/karma start


--------------------------------------------------------------------------------

# Robotframework

    !console
    $ easy_install pip
    $ pip install robotframework
    $ pip install robotframework-selenium2library
    $ pip install robotframework-debuglibrary

ChromeDriver à ajouter dans le dossier bin:
http://chromedriver.storage.googleapis.com
/index.html?path=2.19/


--------------------------------------------------------------------------------

# Robotframework - resources.robot

    *** Settings ***
    Documentation     A resource file with reusable keywords and variables.

    Library           Selenium2Library

    *** Variables ***
    ${SERVER}         localhost:8100
    ${BROWSER}        Chrome
    ${DELAY}          0
    ${START_URL}      http://${SERVER}/

    *** Keywords ***

    Open Application
        Open Browser    ${START_URL}    ${BROWSER}
        Set Selenium Speed    ${DELAY}

    Page should be home
        Wait Until Page Contains Element    css=#home-page
        Page should contain element    css=#home-page

    Click '${title}' menu
        Click Element               css=a.menu-${title}

    Go back
        Sleep           200milliseconds
        Click Element                css=.back-button

--------------------------------------------------------------------------------

# Robotframework - scenarios.robot

    *** Settings ***
    Documentation     A test suite with basic tests
    Resource          Resources.robot

    *** Test Cases ***
    Read home page
        Open Application
        Page should be home
        Click 'search' menu
        Go back
        Page should be home
        [Teardown]    Close Browser

--------------------------------------------------------------------------------

# Robotframework

    !console
    $ pybot scenarios.robot


--------------------------------------------------------------------------------

# Cas métier


--------------------------------------------------------------------------------

# La publication


--------------------------------------------------------------------------------

# Les icons et splashcreens

    !console
    $ ionic resources


--------------------------------------------------------------------------------

# Signature Android

- créer un keystore (avec keytool ou le studio),
- ajouter un fichier `./release-signing.properties`:

    storeFile=/chemin/vers/monkeystore.keystore
    storeType=jks
    keyAlias=ma-clef
    // optionnel (evite de resaisir à chaque fois)
    keyPassword=your-key-password
    storePassword=your-store-password


--------------------------------------------------------------------------------

# Release

    !console
    $ cordova build --release


--------------------------------------------------------------------------------

# Publier l'app sur le PlayStore

- créer un compte Google developer,
- rédiger la fiche de l'app,
- uploader l'APK signé.


--------------------------------------------------------------------------------

# Préparer la fiche sur l'AppStore

- créer un compte Apple developer,
- déclarer l'app,
- obtenir les différents certificats,
- packager avec Xcode et uploader.


--------------------------------------------------------------------------------

# XCode

- importer le projet XCode généré dans `./platforms/ios`,
- saisir manuellement la target version (5.1.1 alors que la valeur minimale proposée est 6.0),
- puis Products / Archive pour produire l'archive.


--------------------------------------------------------------------------------

# Mises en garde pour XCode

On doit valider régulièrement les notifications sur le compte AppleDev, sinon la publication est bloquée.


--------------------------------------------------------------------------------

# Publier via des services tiers

- PhoneGap
- ionic.io
- Fastlane (pour iOS)


--------------------------------------------------------------------------------
