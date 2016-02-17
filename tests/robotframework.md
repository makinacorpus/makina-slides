# Les tests c'est bon, mangez-en !

.fx: extra-large

--------------------------------------------------------------------------------

# Tout le monde fait des tests

<img src="img/officier-des-transmissions-morse-1914.jpg" />

.fx: extra-large

--------------------------------------------------------------------------------

# Automatique c'est mieux

.fx: extra-large

--------------------------------------------------------------------------------

# Un chiffre qui fait réflechir

.fx: extra-large

--------------------------------------------------------------------------------

# On ne le fait pas car...

- c'est long
- c'est difficile
- des fois, c'est même **IMPOSSIBLE** !!
- j'ai pas de serveur de CI

.fx: extra-large

--------------------------------------------------------------------------------

# Oui, mais non

.fx: extra-large

--------------------------------------------------------------------------------

# Avoir juste 1 seul test

.fx: extra-large

--------------------------------------------------------------------------------

# C'est mieux que rien

.fx: extra-large

--------------------------------------------------------------------------------

# Avoir 1 test qui fait 1 seule assertion

.fx: extra-large

--------------------------------------------------------------------------------

# C'est mieux que rien

.fx: extra-large

--------------------------------------------------------------------------------

# Truander les interactions utilisateurs

.fx: extra-large

--------------------------------------------------------------------------------

# C'est mieux que rien

.fx: extra-large

--------------------------------------------------------------------------------

# Faire des tests sans serveur CI

.fx: extra-large

--------------------------------------------------------------------------------

# C'est mieux que rien

.fx: extra-large

--------------------------------------------------------------------------------

# La philosophie des tests

"Toujours commencer par le *mieux que rien* plutôt que rester à *rien* sous pretexte qu'on ne peut pas faire *tout*"

.fx: extra-large

--------------------------------------------------------------------------------

# Robotframework

.fx: extra-large

--------------------------------------------------------------------------------

# Installation

    !console
    $ easy_install pip
    $ pip install robotframework
    $ pip install robotframework-selenium2library
    $ pip install robotframework-debuglibrary

ChromeDriver à ajouter dans le dossier bin:
http://chromedriver.storage.googleapis.com
/index.html?path=2.19/

.fx: extra-large

--------------------------------------------------------------------------------

# Exemple de test

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

# La couche "technique" - resources.robot

    *** Settings ***
    Documentation     A resource file with reusable keywords and variables.

    Library           Selenium2Library

    *** Variables ***
    ${BROWSER}        Chrome
    ${DELAY}          0
    ${START_URL}      http://localhost:8100/

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

# Exécution

    !console
    $ pybot scenarios.robot

.fx: extra-large

--------------------------------------------------------------------------------

# Les compétences nécessaires

- sélecteurs CSS
- les keywords de base de `selenium2library`

.fx: extra-large

--------------------------------------------------------------------------------

# Factorisation

C'est ce qui en fait un outil génial même pour les développeurs.

.fx: extra-large

--------------------------------------------------------------------------------