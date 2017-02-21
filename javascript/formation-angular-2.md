# Formation Angular
## Éric Bréhault

--------------------------------------------------------------------------------

# 1 - Présentation générale

--------------------------------------------------------------------------------

# La version 2 ?

AngularJS est la version 1.

À partir de la verison 2, le nom devient "Angular".

La version 4 va paraître prochaînement (mais sera dans la continuité d'Angular 2).

# Presenter Notes

parler du sémantic versionning

--------------------------------------------------------------------------------

# Quel type de framework ?

- Spectre large
- Très structurant
- Fortement contraint

# Presenter Notes

expliquer les différences avec React

--------------------------------------------------------------------------------

# Les grands principes

- Composants
- TypeScript
- build

# Presenter Notes

--------------------------------------------------------------------------------

# 2 - Installation et tooling

# Presenter Notes

--------------------------------------------------------------------------------

# Installation

Installer NodeJS (6.9+) et NPM.

Installer Angular CLI:

    !console
    $ npm install -g @angular/cli

# Presenter Notes

--------------------------------------------------------------------------------

# Le CLI

Permet de générer un projet.

    !console
    $ ng new myproject
    $ cd myproject
    $ ng serve

Fournit des facilités pour le développement.

    !console
    $ ng serve
    
Permet d'y ajouter des composants.

    !console
    $ ng generate component MyComponent

# Presenter Notes

--------------------------------------------------------------------------------

# Installation et premiers pas

- Installer NodeJS et Angular CLI
- Créer un projet
- Le lancer avec `ng serve` et ouvrir http://localhost:4200
- Observer la structure de fichiers générée

[Solution](https://github.com/makinacorpus/angular-training/commit/f865cbf4660be2087da7e6925db7ff931bd833b6)

--------------------------------------------------------------------------------

# 3 - Les concepts

- TypeScript
- Component
- Module
- Injection

--------------------------------------------------------------------------------

# Typescript

- TypeScript superset d'ES6 superset d'ES5
- Un "compilateur" fait la conversion
- Apporte :
    - le typage
    - les classes
    - les décorateurs

--------------------------------------------------------------------------------

# Component

Un composant est une classe avec un décorateur `@Component`.

Il correspond à un tag.

Il a un template HTML, éventuellement des fichiers de style.

--------------------------------------------------------------------------------

# Module

Le module est le point d'entrée de l'app Angular.

Il déclare les composants.

Il charge les modules tiers.

Il définit les injections disponibles.

--------------------------------------------------------------------------------

# Injections

Les composants ont besoin de services globaux (persistence des données, accès au backend, routage, etc.).

Ils les obtiennent par injection de dépendances :
Angular va instancier les services dont on a besoin, et les fournir aux composants.

Les services injectables sont des classes ayant le décorateur `@Injectable`.

Ils sont déclarés dans le module (dans `providers`).

Ils sont fournis aux composants dans leur constructeur.

--------------------------------------------------------------------------------

# 4 - Créer un composant simple

Le CLI permet de générer de nouveaux composants dans l'app.

Nous allons créer un composant pour la page d'accueil :

    !console
    $ ng generate component Home

--------------------------------------------------------------------------------

# Utiliser un composant

Le décorateur `@Component` associe un sélecteur (`selector`) au composant.

C'est sous ce nom qu'on peut utiliser le composant dans nos templates HTML.

Dans le cas présent : 

    !xml
    <app-home></app-home>

[Exemple](https://github.com/makinacorpus/angular-training/commit/3c42e93cf619d0efacc8581db4dbd212a4606902)

--------------------------------------------------------------------------------

# Créer un input

Le décorateur `@Input` permet de déclarer un nouvel attribut pour le composant :

    !javascript
    @Input() message: string;

déclare un attribut `message` qu'on peut utiliser de cette façon :

    !xml
    <app-home message="Bonjour !"></app-home>

[Exemple](https://github.com/makinacorpus/angular-training/commit/75741b6aeb7b9338ebf80cb98ce2e4855ec3259c)

--------------------------------------------------------------------------------

# Lier (i.e. binding) un input à une propriété

Plutôt qu'un message écrit en dur, nous souhaitons passer la valeur d'une propriété du composant `App` :

    !javascript
    welcomeMessage: string = 'Bienvenue ici';

Pour cela, on doit noter l'input entre crochet :

    !xml
    <app-home [message]="welcomeMessage"></app-home>

(sinon le message serait littéralement "welcomeMessage" et non pas "Bienvenue ici")

[Exemple](https://github.com/makinacorpus/angular-training/commit/963495ca67318867b8b8d3ce67f0ccf63805e88e)

--------------------------------------------------------------------------------

# Lier un événement à une méthode

Ajoutons au composant Hom une méthode qui modifie le message :

    !javascript
    changeMessage() {
       this.message = 'This is a new message';
    }

On souhaite appeler cette méthode lorsqu'on clique sur un bouton.
Pour cela, on note l'événement entre parenthèses:

    !xml
    <button (click)="changeMessage()">Change the message</button>

[Exemple](https://github.com/makinacorpus/angular-training/commit/6682d3ace9ad190878db075880e1d0745116c520)

--------------------------------------------------------------------------------

# Input et output

Les **inputs** sont les informations qui sont fournies en entrée au composant.

Ils sont notés entre crochets.

Les **outputs** sont les informations qui sont émises par le composant.

Ils sont notés entre parenthèses.

Pour les éléments pouvant être fournis en entrée et émis en sortie, on peut utiliser les 2 notations ensemble : `[()]`, par exemple pour un champ de formulaire. C'est le two-way data binding. En dehors de l'usage élémentaire pour des formulaires, on préfère l'éviter pour des raisons de performance.

--------------------------------------------------------------------------------

# Syntaxe des templates

Interpolation `{{ }}` : permet d'évaluer une expression.

Par exemple :

    !javascript
    {{ 1 + 2 }} // affiche 2
    {{ message }} // affiche la valeur de la propriété `message` du composant

--------------------------------------------------------------------------------

# Syntaxe des templates

Boucle avec `*ngFor`

Note : les directives structurelles (celles qui utilisent un template propre) sont préfixées par `*`.

Créons une propriété contenant une liste de pokémons et affichons-les dans une liste :

    !xml
    <ul>
      <li *ngFor="let pokemon of pokemons">{{pokemon.name}}</li>
    </ul>

[Exemple](https://github.com/makinacorpus/angular-training/commit/f3f629d4d5781dcaee95c43733e042f527766768)

--------------------------------------------------------------------------------

# Syntaxe des templates

Condition avec `*ngIf` ou `*ngSwitch`

On va créer une méthode qui indique si un pokémon est le plus fort :

    !javascript
    isStronger(pokemon:any) {
        let max_pv = Math.max(...this.pokemons.map(pok => pok.pv));
        return (pokemon.pv == max_pv)
    }

Et on utilise cette méthode dans un `*ngIf` pour afficher une mention à côté du plus fort :

    !xml
    <strong *ngIf="isStronger(pokemon)">Le plus fort !!</strong>

[Exemple](https://github.com/makinacorpus/angular-training/commit/c28624c8128f7fadba7e175958a963717e554e76)

--------------------------------------------------------------------------------

# Syntaxe des templates

Classes (et style) avec `ngClass`  (ou `ngStyle`)

On peut directement lier l'attribut normal `class` :

    !javascript
    private defaultClasses:string = 'btn btn-primary btn-special';

    !xml
    <div [class]="defaultClasses"></div>

On peut aussi conditionner une classe avec un booléen:

    !xml
    <div [class.alert]="isAlert"></div>

Mais la directive `ngClass` est souvent plus simple car elle permet de gérer plusieurs classes dans un dictionnaire :

    !javascript
    getClasses(pokemon:any) {
        return {
            grass: pokemon.type == 'grass',
            electric: pokemon.type == 'electric',
            fire: pokemon.type == 'fire',
            small: pokemon.size < 50,
            medium: pokemon.size < 100 && pokemon.size >= 50,
            big: pokemon.size >= 100
        }
    }

    !xml
    <li [ngClass]="getClasses(pokemon)">

[Exemple](https://github.com/makinacorpus/angular-training/commit/8431681ebd45a1de742b042259658fc9e32d8e43)

--------------------------------------------------------------------------------

# 5 - Gérer le routage

# Presenter Notes

--------------------------------------------------------------------------------

# 6 - Appels au backend

# Presenter Notes
API REST: http://pokeapi.co/

--------------------------------------------------------------------------------

# 7 - Gérer des formulaires

# Presenter Notes

--------------------------------------------------------------------------------

# 8 - Tester une app

# Presenter Notes

--------------------------------------------------------------------------------

# 9 - Ajouter des dépendances externes

# Presenter Notes

--------------------------------------------------------------------------------

# 10 - Déployer en prod

# Presenter Notes

build de prod
vhost
Angular Universal

--------------------------------------------------------------------------------