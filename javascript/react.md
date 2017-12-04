---
title: Formation React
theme: theme/makina.css
verticalSeparator: <!--v-->
revealOptions:
    transition: 'slide'
---

<!-- .slide: class="title logo" data-background="./_assets/theme/images/bg-rocks.jpg" -->

# Formation React

---

<!-- .slide: class="title" data-background="./_assets/theme/images/bg-rocks.jpg" -->

# 1 - Introduction à React 

Et son écosystème

<!--v-->

## Historique

* *1995* : naissance de **Javascript**
* *2009* : Sortie de **l'iPhone 3GS**, **AngularJS**
* *2011* : Premier déployement de **React**, standard **ECMAScript 5**
* *2012* : **ELM**, **TypeScript**
* *2013* : **Ionic**, **React** est rendu open source
* *2014* : Premières implémantations de l'architecture **Flux**
* *2015* : **React Native**, **Redux**, **ECMAScript 6 (ES2015)** ([Support ECMAScript](http://kangax.github.io/compat-table/es6/))
* *2016* : **Angular 2**, **Ionic 2**

<!--v-->

### Sites basés sur React aujourd'hui

* AirBnB ([article](https://medium.com/airbnb-engineering/rearchitecting-airbnbs-frontend-5e213efc24d2))
* Instagram
* Netflix

<!--v-->

<!-- .slide: data-background="./_assets/images/framework-library.svg" data-background-size="90% auto" -->

<!--v-->

## Principes fondamentaux

* Composants
* One Way Data Flow
* **JSX** et **DOM virtuel**
* Evolutivitité
    * routing avec **react-router**
    * SSR (Server Side Rendering) avec **next.js**
    * gestion d'état avec **Redux** / flux / autre
    * se décline en natif avec **React Native**, en hybride et en **PWA** !

---

<!-- .slide: class="title" data-background="./_assets/theme/images/bg-rocks.jpg" -->

# 2 - Installation et tooling

<!--v-->

# Démarrer un projet React

## Pré-requis

Installer NodeJS (6.9+) et NPM.

https://nodejs.org/en/download/

<!--v-->

# Démarrer un projet React

## Avec le CLI

Installer Angular CLI:

```js
npm install -g create-react-app
``` 

**create-react-app** permet de générer un projet.

```js
create-react-app my-app
cd my-app
```

Démarrer le serveur de développement

```js
npm start
```

<!--v-->

# Démarrer un projet React

## "À la main"

On peut aussi créer nous-même la configuration, pour ça il faut :

* installer **react** et **react-dom**
* **un module bundler** : browserify ou webpack (on préférera utiliser webpack)
* **un transpileur** pour nous permettre d'écrire en ES6, **babel** est fait pour ça

<!--v-->

## Tooling spécifique à React

* Extension React et/ou JSX pour son éditeur de code
* **React DevTool** : extension Chrome / Firefox pour le debug d'applications React
* [**Jest**](https://facebook.github.io/jest/) : Outil de test (aussi conçu par Facebook, pour React)

<!--v-->
<!-- .slide: class="alternate" -->

# Exercice

* Installer create-react-app
* Créer un projet
* Lancer le serveur de dev avec `npm start` et ouvrir http://localhost:3000
* Observer la structure des fichiers générés

[Solution](https://github.com/makinacorpus/react-training/commit/0fc2b485b76a5f7e93ddac231113f5d848436c24)

---

<!-- .slide: class="title" data-background="./_assets/theme/images/bg-rocks.jpg" -->

# 3 - Les composants

simples ou à gestion d'état

<!--v-->

# state vs props

## state

Le state correspond à **l'état du composant**

Le state est un objet défini dans le constructeur

```js
class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      message = "Salut !"
    };
  }
}
```

<!--v-->

# state vs props

## props

Les props sont **les éléments fournis par le composant parent**

Les props se transmettent via des attributs :

```js
<App message="Bonjour">
```
<!--v-->

# state vs props

## props

On peut également passer des props entre crochet pour passer une variable

```js
const message = "Bonjour"
<App message={message}>
```

<!--v-->

# Composant simple

## Class component

```js
class HelloMessage extends React.Component {
  render() {
    return <div>Hello {this.props.name}</div>;
  }
}
```

Un composant peut être définit par **une classe JavaScript**
* qui hérite de la classe `Component` de React
* qui définit une méthode `render` renvoyant le code DOM du composant, avec un élément racine obligatoire
* qui peut accéder à `this.props`


<!--v-->

# Composant simple

## Functional component

```js
function HelloMessage(props) {
  return <div>Hello {props.name}</div>;
}
```

ou **une fonction** (functional component) 

* qui prend en paramètre les `props`
* et qui renvoie directement le code DOM du composant
* les **props sont en lecture seule**


<!--v-->

# Composant à gestion d'état

Un composant à gestion d'état a les mêmes propriétés qu'un composant simple de type class, mais qui en plus **des props**, peut accéder à un objet **state**.


<!--v-->

<!-- .slide: style="font-size: 80%" -->

# Composant à gestion d'état

```js
class Counter extends React.Component {
  state = { 
    clicksCount: 0
  };

  render() {
    return (
      <div>
        Counts: {this.state.clicksCount}
        <button onClick={() => this.setState(prevState => ({clicksCount: prevState.clicksCount + 1}))}>Click</button>
      </div>
    );
  }
}
```

* Le `state` est défini dans le constructeur de la class
* La modification du state se fait toujours avec la méthode `setState`

<!--v-->

<!-- .slide: data-background="./_assets/images/think-component-1.png" data-background-size="90% auto" -->

<!--v-->

# Cycle de vie du composant

La classe **Component** de React contient plusieurs méthodes pour gérer **le cycle de vie du composant** :

* `componentWillMount()`
* `componentDidMount()`
* ... [(cf. documentation officielle)](https://facebook.github.io/react/docs/react-component.html)

On peut différencier 3 types d'événements, selon qu'il soit émit :
  * au **mount** : quand le composant apparaît pour la première fois
  * à l'**update** : quand ses props ou son state est mis à jour
  * au **unmount** : quand le composant n'est plus présent

<!--v-->

<!-- .slide: data-background="./_assets/images/component-lifecycle.svg" data-background-size="90% auto" -->

<!--v-->

# Cycle de vie du composant

## La méthode setState

* La méthode `setState` effectue un **merge de l'objet passé en paramètre** avec le state. 
* Quand un composant modifie son state, il reçoit des événements d'update, ainsi que **tous ses enfants** qui sont mis à jour  par propagation (update).

<!--v-->

<!-- .slide: data-background="./_assets/images/lifecycle-component-react.png" -->

<!--v-->

# Résumé

* Une application est un ensemble de composants
* C'est aussi un composant
* Comme tout composant, elle nécessite **un noeud racine unique**
* Elle peut avoir **une gestion d'état** (`state`)
    * qui sera partagé au plus haut niveau
    * et donc avec l'ensemble de ses `children`
* **L'instanciation du composant dans le DOM** sera effectuée avec `ReactDOM.render`

<!--v-->

<!-- .slide: data-background="./_assets/images/think-component-2.png" data-background-size="80% auto" -->

<!--v-->

<!-- .slide: class="alternate" -->

# Exercice

On va commencer par [créer un nouveau composant simple](https://github.com/makinacorpus/react-training/commit/39c43020fa448c2606343ed912f454627b091307) qui contient une liste de pokémons.

Rendre ce composant dynamique en passant en props la liste des pokemons.

Notes : nous aurons besoin de la fonction [`map`](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Objets_globaux/Array/map) pour afficher les pokemon dans le JSX.

[Solution](https://github.com/makinacorpus/react-training/commit/9b2395e9ee6e308469f4694492cb3421910f58e1)

---

<!-- .slide: class="title" data-background="./_assets/theme/images/bg-rocks.jpg" -->

# 4 - Structurer son projet

<!--v-->

# Structure d'un projet React 

## (sans Redux)

<!-- .slide: style="font-size: 80%" -->

    |- node_modules         Modules npm
    |- build                Build
    |- public               Assets, index.html, et autres
    |- src                  Code source
       |- components        Composants
       |- [routes]          Routes de l'application, à discuter (car peut être intégré dans d'autres composants ?)
       |- services          Services s'interfaçant à une API par ex.
       |- helpers           Méthodes de gestion de données
       |- [styles]          Styles (peuvent aussi être avec le component correspondant)
    |- [test]               Ensemble des tests (ou collé à côté des components/containers/...)


<!--v-->

<!-- .slide: class="alternate" -->

# Exercice

## Restructurer notre application

* Créer un dossier components et y déplacer notre composant PokemonList
* On va mettre les données sur les pokémons dans un [fichier de configuration](https://github.com/makinacorpus/react-training/commit/b7305205f8224637007b3746abbe0b8b775e53d5) `config.js` et ajouter quelques infos (points de vie, taille, type) :

```
export const POKEMONS = [
  { id: 0, name: 'Pikachu', pv: 10, size: 100, type: 'electric' },
  { id: 1, name: 'Salamèche', pv: 7, size: 45, type: 'fire' },
  { id: 2, name: 'Bulbisar', pv: 6, size: 75, type: 'grass' }
]
```

<!--v-->

# Syntaxe JSX

Il est possible de définir des classes conditionnelles. Pour cela on va utiliser la librairie [classnames](https://www.npmjs.com/package/classnames).

```js
const sizeClass = classnames({
  big: pokemon.size > 80
})
```

classnames permet d'attribuer des class en fonction de critères définis. On pourra ensuite appliquer ces class à notre élément html :

```js
<span className={sizeClass}>{pokemon.type}</span>
```

<!--v-->

<!-- .slide: class="alternate" -->

# Exercice

## Page détail

* Créer un nouveau composant PokemonDetail. On affichera dans un premier temps le premier pokemon de la liste.
* On pourra ensuite appliquer des styles selon sa taille et/ou son type.

[Solution](https://github.com/makinacorpus/react-training/commit/e9e9715fdac1094c7615d48e9ac535dfbf0a20da)

---

<!-- .slide: class="title" data-background="./_assets/theme/images/bg-rocks.jpg" -->

# 5 - Le routing

<!--v-->

# React-router

* [**react-router**](https://reacttraining.com/react-router/web/guides/quick-start)
* **Attention : on en est à la v.4, les v.1, 2 et 3 s'implémentent différemment !**
* Permet de passer des paramètres en url
* Peut être synchronisation avec le store de redux
* Deux méthodes pour intégrer les routes : directement via le **composant**, ou via un objet de **config**

<!--v-->

# React-router

## Composant sans props

```js
const Home = () => (
  <div>
    <h2>Home</h2>
  </div>
)
<Route exact path="/" component={Home}/>
```

À noter : `exact` évite d'avoir une "imbrication" des routes.

<!--v-->

# React-router

## Composant avec props

Souvent, nous aurons besoin de passer des props à la route

```js
const Home = (props) => (
  <div>
    <h2>{props.title}</h2>
  </div>
)
```

Dans ce cas, on peut aussi fournir une fonction à l'attribut component.

De cette manière, on pourra fournir des props au composant.

```html
<Route exact path="/" component={() => <Home title="Home">}/>
```

<!--v-->

# Route config

Ce pattern permet une gestion plus complexe des routes

[https://reacttraining.com/react-router/web/example/route-config](https://reacttraining.com/react-router/web/example/route-config)

```js
const routes = [
    { 
        path: '/sandwiches', 
        component: Sandwiches 
    },
    { 
        path: '/tacos',
        component: Tacos,
        routes: [
            { path: '/tacos/bus', component: Bus },
            { path: '/tacos/cart', component: Cart }
        ]
    }
]
```

<!--v-->

<!-- .slide: class="alternate" -->

# Exercice

* Installer le package `react-router-dom` et l'importer dans le composant App
* Configurer le router afin d'optenir 
  * une route `/` qui affiche le détail d'un pokemon
  * une route `/pokemon` qui affiche la liste des pokemons

[Solution](https://github.com/makinacorpus/react-training/commit/91245ecb665b571a6434dc84dfddb23272499b9d)

<!--v-->

# Liens vers les routes

On peut très bien faire un lien normal vers une route :

```
<a href="/home">Home</a>
```

Mais cela va recharger la page en entier.

Si on veut rendre le routage dynamique, on utilise le composant `Link`:

```
<Link to="/home">Home</Link>
```

<!--v-->

# Routes paramétrées

On peut déclarer des routes contenant des paramètres :

```js
<Route path='/pokemon/:id' component={PokemonDetail}/>
```

<!--v-->

# Routes paramétrées

La librairie `react-router-dom` permet aux composants déclarés dans `Route` d'accéder à des infos concernant la route.

On peut notamment récupérer les paramètres via

```
this.props.match.params
```

<!--v-->

<!-- .slide: class="alternate" -->

# Exercice

## Routes paramétrées

* [Configurer le composant PokemonDetail](https://github.com/makinacorpus/react-training/commit/ccc7f587b70385bdbdaef71e2c6f7a3c73ff1f89) pour qu'il affiche le pokemon selon l'id en paramètre
* Ajouter des liens sur la liste des pokemons

[Solution](https://github.com/makinacorpus/react-training/commit/6ae071f01f09c9106c3452b204eec06e03895a18)


<!--v-->

## Syntaxe JSX

En JSX, on peut afficher des éléments de manière conditionnée avec l'opérateur ternaire :

```html
error ? <p>{error}</p> : <p>Mon pokemon...</p>
```

ou avec l'opérateur logique :

```html
<div>
  {error && <p>{error}</p>}
  {pokemon && <p>Mon pokemon...</p>}
</div>
```

<!--v-->

<!-- .slide: class="alternate" -->

# Exercice

## Afficher un message d'erreur

* Si l'id en paramètre ne correspond à aucun pokemon, on se retrouve avec un message d'erreur, il faut donc gérer ce cas et afficher un message si aucun pokemon n'a été trouvé.

[Solution](https://github.com/makinacorpus/react-training/commit/6ae071f01f09c9106c3452b204eec06e03895a18)

---

# 6 - Appel au backend

Plutôt que gérer des informations localement, on souhaite utiliser l'API publique [http://pokeapi.co/](http://pokeapi.co/).

Avec React, il n'y a pas de service `http` prêt-à-l'emploi comme ça peut être le cas avec Angular.

On va pour cela utiliser [fetch (+ polyfill)](https://github.com/github/fetch) ou [axios](https://github.com/axios/axios)

<!--v-->

## Où placer ces appels ?

Attention : la fonction render ne peut pas contenir d'appel asyncrone !

Pour afficher des données avec une promesse, nous aurons besoin d'utiliser `componentDidMount` et de stocker le résultat dans le state.

```js
state = {
  pokemons: []
}
componentDidMount() {
  fetch('http://pokeapi.co/api/v2/pokemon/')
    .then(response => response.json())
    .then((response) => {
      this.setState({pokemons: response.results})
    })
}
```

<!--v-->

<!-- .slide: class="alternate" -->

# Exercice

* Utiliser http://pokeapi.co/api/v2/pokemon/ pour avoir la liste des Pokémons.
* Utiliser http://pokeapi.co/api/v2/pokemon/:id pour avoir les informations d'un pokémon.

Notes : pour accéder à l'API, nous aurons besoin d'une [extension CORS](https://chrome.google.com/webstore/detail/allow-control-allow-origi/nlfbmbojpeacfghkpbjhddihlkkiljbi)

Solution

L'API est lente, il faut faire un spinner (ou un message de chargement).

Solution

<!--v-->

# Création de service

Un composant n'est pas censé faire d'appel à une API, c'est le rôle des services.

En générale, on place les services dans un dossier `/services` à la racine de `/src`.

<!--v-->

<!-- .slide: class="alternate" -->

# Exercice

Créer un fichier (`/src/services/api.js`) et y déplacer les fonction faisant appel à l'API.


---

<!-- .slide: class="title" data-background="./_assets/theme/images/bg-rocks.jpg" -->

# 7 - Les formulaires

* 2 méthodes :
    * les **formulaire controlé** (controlled components)
    * les **formulaires non controlé** (uncontrolled components)

<!--v-->

## Les formulaires controlés

[Documentation officielle](https://reactjs.org/docs/forms.html#controlled-components)

Comme son nom l'indique, permet de "controler" la valeur des champs. 

Dans le cas d'un input par exemple, on définira le champs value par une valeur contenue dans le state du composant.

```js
<input type="text" value={this.state.value} onChange={this.handleChange} />
```

* "Norme" dans les projets React
* De nombreuses librairies s'adaptent aux formulaire controllés
* **Attention** : Internet Explorer gère mal les formulaires controllés : problème de mémorisation d'identifiants

<!--v-->

## Les formulaires controlés

Pour changer la valeur de cet input, on utilisera une fonction qui va modifier le state

```js
handleChange(event) {
  this.setState({value: event.target.value});
}
```

<!--v-->

## Les formulaires non controlés

[Documentation officielle](https://reactjs.org/docs/uncontrolled-components.html)

```js
<input type="text" ref={(input) => this.input = input} />
```

* Les éléments non controlés sont de simples input HTML
* Ils **ne doivent pas** avoir de `onChange` ni de `value` défini
* `ref` permet de référencer l'objet correspondant à l'élément
* Préférable si IE est une cible importante

<!--v-->

## Les formulaires non controlés

```js
handleSubmit(event) {
  alert('A name was submitted: ' + this.input.value);
  event.preventDefault();
}
```

* On pourra récupérer la valeur de l'input au submit, en interrogeant l'objet référencé

<!--v-->

<!-- .slide: class="alternate" -->

# Exercice

* Créer une nouvelle route (=> nouveau composant) Contact.
* Faire un formulaire de type **controlé**.

[Solution](https://github.com/makinacorpus/react-training/commit/544e9b6dd3ce2fe5161f5a1fa80a62aa06d3bb30)

* Faire un second formulaire, mais cette fois-ci **non controlé**.

Note : comme on ne dispose pas d'un endpoint pour envoyer des mails, on va simplement écrire dans le log notre message.

[Solution](https://github.com/makinacorpus/react-training/commit/75e66275626ea433817c5377ebb7ed8525075136)


---

<!-- .slide: class="title" data-background="./_assets/theme/images/bg-rocks.jpg" -->

# 8 - Les styles

<!--v-->

# Les styles en React

La configuration de create-react-app permet, par default de charger des fichiers .css via le javascript.

```js
import './styles.css'
```

Attention : pour utiliser .scss il faudra extraire la configuration !

Il est aussi possible de charger des styles de manière "traditionnelle" (balise link dans le index.html) mais ce n'est pas très en accord avec le principe de composant.

<!--v-->

<!-- .slide: class="alternate" -->

# Exercice

Ajouter [Material-ui](https://material-ui-next.com/) à notre application (ou une bibliothèque de style de votre choix)

Attention : Material-ui existe en 2 versions : material-ui et material-ui@next. Leur implémentation est différente.

Pour les formulaires non controlés : la version 0.x de Material-ui ne permet pas de faire des formulaires non controlés. La nouvelle version le permet avec l'attribut `inputRef`.

[Solution](https://github.com/makinacorpus/react-training/commit/16fe681df475f6c3ad13e33fbac1c1f14e9cf271)


---

<!-- .slide: class="title" data-background="./_assets/theme/images/bg-rocks.jpg" -->

# 9 - Les test


<!--v-->

# Jest pour les tests

![](../assets/makina/images/bg-lenin.jpg)

.fx: title2 bg-image imageslide

<!--v-->

# Ce que fait Jest

* runner basé sur node permettant d'exécuter les tests dans un environnement node
* utilise [jsdom](https://github.com/tmpvar/jsdom) dans node

* [snapshot testing](http://facebook.github.io/jest/docs/en/snapshot-testing.html#content)
* tests 'classiques'
* mocking
* code coverage
* isolation et 'sandboxing' des tests
* marche avec d'autres bibliothèques de tests type [enzyme](http://airbnb.io/enzyme/index.html) / chai

<!--v-->

# Comment tester ?

* **quoi ?**
    * le rendu des composants (snapshot)
    * les services, helpers....
    * les différences de rendu selon le state
* **où ?**
    * fichiers juxtaposés
    * répertoire centralisant les tests
* **quand ?**
    * en permance dans le développement (extension code, console ouverte...)
    * dans les étapes de build
* **comment ?**
    * avec des [mocks](https://facebook.github.io/jest/docs/mock-functions.html#content) : `jest.fn`, ̀`jest.mock`
    * en atteignant une bonne couverture de code

<!--v-->

# L'immutabilité
* Découverte de immutable.js
* Comprendre l'intérêt de l'immutabilité pour les performances
https://facebook.github.io/immutable-js/docs/#/

---

# 10 - Redux

![](../assets/makina/images/bg-lenin.jpg)

<!--v-->

# Découvrir Flux et Redux

### Flux

* Flux est un pattern, un type d'architecture plus qu'une librairie
* Il existe une [implémantation "officielle"](https://github.com/facebook/flux) créee par Facebook, mais elle est très peu utilisée
* [Flux Cartoon](https://code-cartoons.com/a-cartoon-guide-to-flux-6157355ab207) : un blog illustré pour comprendre Flux

### Redux

* [Documentation Redux](http://redux.js.org/)
* Redux est une implémentation dérivée de Flux
* permet de créer un **store qui contient un état**
* réagit à des **actions dispatchées**
* modifie l'état du store grâce aux **reducers** 
* permet l'ajout de **middlewares**, qui peuvent en quelque sorte pre-processer les actions
* [Tester le store](http://redux.js.org/docs/recipes/WritingTests.html)
* [Redux Cartoon](https://code-cartoons.com/a-cartoon-intro-to-redux-3afb775501a6) : un blog illustré pour comprendre Redux

<!--v-->

# La vie d'un composant avec Redux

![Redux](assets/img/redux-component-lifecycle.gif)

<!--v-->

# Pourquoi utiliser Redux ?

![Redux](assets/img/redux.svg)

* **des données doivent transiter** entre plusieurs composants
* **trop de composants enfants imbriqués** doivent accéder et/ou modifier le state global

<!--v-->

# Structure d'un projet React avec Redux

    |- config               Instructions webpack
    |- node_modules         Modules npm
    |- build                Build déposé ici
    |- public               Assets, index.html, et autres
    |- src                  Code source
       |- components        Composants simples + stateful
       |- containers        Composants liés au store
       |- store             Store redux (plusieurs écoles)
          |- domainA        Contient les actions/reducers pour le domainA
          |- domainB        Contient les actions/reducers pour le domainB
       |- routes            Routes de l'application, à discuter (car peut être intégré dans d'autres composants ?)
       |- services          Services s'interfaçant à une API par ex.
       |- helpers           Méthodes de gestion de données
       |- selectors         Méthodes permettant de parser/extraire les données pour les fournir aux containers
    |- [test]               Ensemble des tests (ou collé à côté des components/containers/...)

* concernant le store, on peut aussi 
    * éclater les actions / reducers de chaque domaine
    * dans deux dossiers, un `actions`, l'autre `reducers`
    * contenant l'ensemble des actions et l'ensemble des reducers de tous les domaines

<!--v-->

![Redux](assets/img/redux-schema.svg)

* **le store** stocke les données. Il a un état initial définit et est ensuite dupliqué par les reducers pour changer son état (`state`).
* **les components** contiennent le JSX et affichent "bêtement" ce qu'ils reçoivent
* **les containers** fournissent aux composants :
    * des données (à partir du `state`) 
    * des events à **dispatcher aux actions**
* **les actions** sont des événements
* **les reducers** écoutent les événement et modifient en conséquence le store

.fx: wide smaller


<!--v-->

# Travaux pratiques (step-7)

### Étape 1 (step-7.1)

* Installer les dépendances de redux et ajouter un **store** au projet
* Configurer redux à l'aide `createStore` et `combineReducers`
* Créer les actions et les reducers pour nominatim et overpass
    * les **actions** mettent à jour `search` & `bbox`
    * les **reducers** doivent stocker les infos de nominatim et d'overpass

### Étape 2 (step-7.2)

* Installer l'extension **Redux Devtools** (Chrome ou Firefox) : [https://github.com/zalmoxisus/redux-devtools-extension](https://github.com/zalmoxisus/redux-devtools-extension)
* Implémanter un `enhancer` au niveau du store qui permet de lancer l'extension
* Ajouter une condition pour ne pas avoir accès à l'extension en mode prod
    * Utiliser la condition `process.env.NODE_ENV !== 'production'`

.fx: wide alternate

<!--v--> 

# Les middlewares Redux

On place en général dans le middleware tout ce qui n'a pas sa place, ni dans les composants/containers, ni dans les actions/reducers.

Un middleware peut par exemple servir à :

* **gérer le localstorage**
* **afficher des logs**
* permettre **l'asynchrone dans les actions**. Les plus connus :
    * [Redux Thunk](https://github.com/gaearon/redux-thunk)
    * [Redux Saga](https://github.com/redux-saga/redux-saga)
* effectuer des actions avec une **librairie tierce**, par exemple pour :
    * le **tracking**
    * l'**analytics**
* [Documentation](http://redux.js.org/docs/recipes/ReducingBoilerplate.html)

**Le middleware intervient lorsqu'une action est dispatchée**. Selon le middleware, on peut choisir d'intercepter uniquement certaines actions. L'action et le reducers continue ensuite sans se soucier du middleware.

.fx: wide small

<!--v-->

### Étape 3

* Installer **redux-thunk**
    * ajouter une **action asynchrone** pour lancer une recherche nominatim
    * et une autre pour une requête overpass (step-7.3)
    * **dispatcher les 2 actions**, observer le résultat
* Ajouter un bouton au niveau du HTML pour observer le store (step-7.4)

.fx: alternate

<!--v-->

### Étape 4

* Câbler le store à React :
    * la connection du store à un **composant** / **container** => smart component (avec `mapStateToProps`, `mapDispatchToProps`) (step-7.5)
    * la mise à jour du state depuis le composant (`this.state` => `this.props`) (step-7.6)
    * connecter la carte et les formulaires (step-7.7)
* Ajouter un **middleware** type logger (redux-logger + à la main) (step-7.8)
* Ajouter un **middleware** qui va appeler l'api nominatim / service (step-7.9)

**Attention à bien relancer les tests à chaque étape !**

Nous aurons besoin de [react-mock-store](http://arnaudbenard.com/redux-mock-store/) pour que les tests puissent fonctionner avec redux

.fx: alternate

<!--v-->

# Travaux pratiques (step-8)

* Ajouter une route `/home` (step-8.1)
* Ajouter une route `/search` ainsi qu'un menu permettant de naviguer entre ces 2 urls (step-8.2)
* Améliorer la route `/search` en autorisant un paramètre `/search/:address` (step-8.3)
* Améliorer la route `/search` en ajustant la **bounding box** d'affichage (step-8.4)

.fx: alternate

---

# Pour aller plus loin

Performance, i18n, ssr,...

![](../assets/makina/images/bg-lenin.jpg)

.fx: title2 bg-image imageslide

<!--v-->

# HOC

**Higher Order Components (HOC)** est un pattern qui permet de :

* factoriser du code
* manipuler des props
* faire abstraction du state 

<!--v-->

# Performance & packaging

* Mesurer la taille d'un bundle ([webpackBundleAnalyzer](https://www.npmjs.com/package/webpack-bundle-analyzer))
* Ajouter une dépendance type underscore ou lodash
* Prendre uniquement une fonction
* Charger uniquement les locales nécessaires (par exemple avec la lib *moment*) avec [ContextReplacementPlugin](https://webpack.js.org/plugins/context-replacement-plugin/)
* Mesurer les temps de rendu d'une application, initiation au devtool
* Les outils de monitoring applicatif React
* Quel est le package obtenu, et qu'en fait on ?

<!--v-->

# Le déployement

* Pour le dev : **surge.sh** : [http://surge.sh/](http://surge.sh/)
    * `npm i -g surge`
    * `surge -p build -d mondomaine.surge.sh`

<!--v-->

# L'internationalisation

* [**react-i18n**](https://react.i18next.com/)
* Issue du projet [i18next](https://www.i18next.com/#), "framework" de traduction
* Disponible pour plupart des technos front (Angular, Vue, Aurelia,...)
* => Compatibilité des fichiers de traduction

<!--v-->

# Travaux pratiques (step-9)

* Installer les paquets necéssaires à l'internationalisation `react-i18next`, `i18next` (+ les paquets optionnels comme `i18next-browser-languagedetector`)
* Ajouter le service i18n et traduire une chaîne de caractère dans un composant (step-9.1)

.fx: alternate

<!--v-->

# Le Server Side Rendering

### Pourquoi ?

* **le SEO**
* récupérer un token fourni par le serveur (NodeJS) sur un cookie
* Travailler en mode dev avec React + serveur autre que NodeJS => difficile à mettre en place, besoin d'adapter webpack et c'est très compliqué 

### Quelle solution ?

* [**next.js**](https://zeit.co/blog/next)
* next va "remplacer" react-script
* De nombreux éléments devront être adapté pour devenir s'adapter au SSR :
    * les styles (next n'accepte que les styles en inline dans le JSX)
    * les routes
    * le store
* Voir les exemples d'utilisation de next : [https://github.com/zeit/next.js/tree/master/examples](https://github.com/zeit/next.js/tree/master/examples)


<!--v-->

# Travaux pratiques (step-10)

* Installer `next-js` et ajouter le script de lancement dans `package.json` (step-10)
* Créer une page cablée au store, qui afficherait un élément du store par défaut
* Désactiver Javascript, vérifier si les infos du store sont toujours présentes (step-10.1)
* Charger la liste des résultats côté serveur et l'afficher (la page doit toujours fonctionner sans Javascript) (step-10.2)

.fx: alternate wide