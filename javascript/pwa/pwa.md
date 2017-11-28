# Progressive Web App
## Éric Bréhault

--------------------------------------------------------------------------------

# Le marché des apps

Seuls les jeux et les "grands classiques" (WhatsApp, Facebook, email, etc.) s'en sortent.



Mais les coûts de développement restent très supérieurs aux coûts habituels des développements web.

--------------------------------------------------------------------------------

# Principe

Une simple page web...

... avec un comportement d'application.

--------------------------------------------------------------------------------

# Comparaison

<table>
<tr><th></th><th>Natif</th><th>Hybride</th><th>PWA</th></tr>
<tr><td>Coût</td><td>N</td><td>N/2</td><td>N/4</td></tr>
<tr><td>Installation</td><td>via un store</td><td>via un store</td><td>en naviguant</td></tr>
<tr><td>Taille</td><td>plusieurs Mo</td><td>plusieurs Mo</td><td>juste le poids de la page web</td></tr>
<tr><td>Affichage</td><td>dans le mur d'app</td><td>dans le mur d'app</td><td>dans le mur d'app</td></tr>
<tr><td>Mode déconnecté</td><td>oui</td><td>oui</td><td>oui</td></tr>
<tr><td>Notifications</td><td>oui</td><td>oui</td><td>oui</td></tr>
<tr><td>Utilisation du GPS</td><td>oui</td><td>oui</td><td>oui</td></tr>
<tr><td>Utilisation de l'appareil photo</td><td>oui</td><td>oui</td><td>oui</td></tr>
<tr><td>Accès au système</td><td>oui</td><td>oui</td><td>non</td></tr>
</table>

--------------------------------------------------------------------------------

# Les gains

- pas de contrainte ni de coût pour la publication
- meilleure gestion des mises à jour logicielles
- distribution simplifiée
- technologie plus simple
- meilleure maintenabilité

--------------------------------------------------------------------------------

# Techniques de base

- un fichier manifest.json
- un service worker


--------------------------------------------------------------------------------

# Compatibilité

Manifest : quasiment tous les terminaux

Service workers :

- Android (à partir de 4.4, soit l'essentiel du marché)
- **PAS sur iPhone pour le moment**

--------------------------------------------------------------------------------

# Framework

Ionic 2 :

- Projet Angular normal
- Génération automatique d'une PWA

--------------------------------------------------------------------------------