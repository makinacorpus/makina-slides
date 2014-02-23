# Gestion et maintenance d'un parc d'équipements industriels

--------------------------------------------------------------------------------

> La gestion de maintenance assistée par ordinateur est une méthode de gestion assistée d'un logiciel destiné aux services de maintenance d'une entreprise afin de l'aider dans ses activités.

<cite> — http://fr.wikipedia.org/wiki/GMAO</cite>

.fx: quoteslide

--------------------------------------------------------------------------------

# Introduction à la GMAO JOB

.fx: alternate

--------------------------------------------------------------------------------

# La GMAO JOB en quelques mots

* Référencer ses équipements en entrant dans le détail de leur architecture technique.
* Assurer le suivi et la maintenance de ces équipements.
* Piloter l'activité de maintenance via des tableaux de bords.
* Accessible en mode web 24h/24 depuis n'importe quel PC, tablette ou smartphone équipé d'un navigateur Google Chrome ou Firefox de dernière génération.
* Interconnexion avec les applications du SI.
* Utilisée par tous les services de l'entreprise : responsables d’opération et administratif, commerciaux, techniciens.
* Mais aussi par les clients et partenaires.
* Accès sécurisé : identifiant/mot de passe, HTTPS, LDAP.

--------------------------------------------------------------------------------

# Une GMAO développée pour la société ALMA Services

.fx: alternate

--------------------------------------------------------------------------------

# La société ALMA Services > Le métier

* Société positionnée dans le secteur des équipements, installations et services pour la distribution des produits pétroliers en aval des raffineries.
* Maintenance des camions citernes et dépôts pétroliers.
* 10 établissements répartis sur le territoire français, 90 personnes.

![ALMA Services - Camions et dépôts](images/alma-depot-camion.jpg)

![ALMA Services](images/alma-logo.png)

--------------------------------------------------------------------------------

# La société ALMA Services > Le besoin initial

* Automatiser son processus métier de gestion des interventions sur son parc d'équipements.
* Modéliser dans le détail l'architecture techniques de ses équipements.
* Assurer la traçabilité de toutes les interventions techniques.
* Impliquer tous les services de la société.
* Offrir à ses clients un accès sécurisé à leurs données.
* Produire des tableaux de bord et bilans pour suivi et piloter l'activité.
* Connecter l'outil aux autres applications du SI : gestion clients, gestion des stocks, facturation, planification, ...
* Une application web accessible 24h/24 en mobilité, réactive, ergonomique et évolutive.

![Marketing et Statégie](images/marketing-strategy.jpg)

# Presenter Notes

* Cycle de vie d'une intervention : revue de contrat, préparation et planification de la mission, exécution de la mission par le technicien, clôture administrative et financière.
* Services impliqués : techniciens, responsables d’opération et administratifs, partenaires, clients, commerciaux, ...
* Mobilité : tablette, PC tactiles équipés de connexion 3G

--------------------------------------------------------------------------------

# La société ALMA Services > Les contraintes

*   Importance de l'ergomie, notamment pour la saisie des rapports d'intervention par des techniciens non habitués à l'outil informatique.
*   Récupération de l'historique des données des anciennes GMAO de la société (constitution technique et historique des interventions) :
    * Une GMAO dépôts écrite en PHP
    * 7 GMAO "quasi" identiques écrites en Access

![ALMA Services](images/contraintes.jpg)

# Presenter Notes

* Historique : assurer une continuité dans la traçabilité de toutes les interventions réalisées depuis les 10 dernières années

--------------------------------------------------------------------------------

# Un développement utilisant uniquement des outils et logiciels libres

.fx: alternate

--------------------------------------------------------------------------------

# Quels avantages par rapports aux logiciels propriétaires existants ?

*   Pas de coût d'acquisition de licence mais coût de développement initial.
*   Une indépendance totale vis à vis de l'éditeur/prestataire
    * Accès au code source
    * Changer de prestataire si nécessaire
    * L'internalisation du développement des évolutions et de la maintenance est possible
* Des communautés d'utilisateurs et de développeurs apportent leur aide et assurent la perrenité des outils utilisés.
*   Et peut-être le principal : permet d'adapter la solutions aux besoins du client !

## Adapter le logiciel à ses besoins, et non pas adapter ses besoins au logiciel.

# Presenter Notes

* Il existe des outils spécialisés au métier d'ALMA Services mais aucun ne répondait intégralement au besoin et étaient rétissant à s'adapter aux besoins d'ALMA.
* Coût d'acquisition : peut être la contrainte la moins importante
* Accès au code source : pouvoir vérifier la qualité de l'application. Le logiciel n'est pas une boîte noire.
* Internaliser les développement : on trouve de plus en plus facilement des formations pour développeurs
* Communautés : Ex en cas de bug : Ayant accès au code source des briques utilisées ils nous est possible d’investiguer, de résoudre le problème ou de le reporter efficacement pour aider d’autres développeurs à le corriger. Nous avons eu le cas avec un bug de fonctionnement des menus Twitter Bootstrap sur les tablettes Androïd.

* Les outils de développement Open Source ont permis de répondre à l’intégralité des besoins, du développement du logiciel jusqu’à sa mise en production et son hébergement.

--------------------------------------------------------------------------------

# Des outils de développement Open Source de plus en plus utilisés

* Il existe des outils Open Source permettant de répondre à quasiment tous les besoins : de la conception du logiciel à sa mise en production et son hébergement.
* Des projets d'envergure les adoptent. Exemples pour le framework Django :

![Autolib](images/autolib-logo.png)

![Oscaro](images/oscaro-logo.png)

mais aussi : La Nasa, le Washington Times, Google App Engine, ...

--------------------------------------------------------------------------------

# GMAO, les principales fonctionnalités

.fx: alternate

--------------------------------------------------------------------------------

# GMAO > Connexion sécurisée à l'application

![GMAO : Écran de connexion](images/screenshots/00-ecran-de-connexion.png)
<div class="img_legend">Écran de connexion</div>

.fx: gmao_image

--------------------------------------------------------------------------------

# GMAO > Tableau de bord métier : piloter l'activité

Vue d'ensemble des interventions et des missions ; alertes sur les équipements et les contrats.

![GMAO : Tableau de bord](images/screenshots/01-tableau-de-bord-1.png)
<div class="img_legend">Tableau de bord</div>

.fx: gmao_image

# Presenter Notes

* Interventions : en cours, planifiées, en préparation, clôturées
* Le tableau bord est personnalisé en fonction du profil. Un technicien y retourve son planning et la liste des rapports d'intervention qu'il doit remplir.

--------------------------------------------------------------------------------

# GMAO > Tableau de bord métier : piloter l'activité

![GMAO : Tableau de bord](images/screenshots/01-tableau-de-bord-2.png)
<div class="img_legend">Suite du tableau de bord</div>

.fx: gmao_image

--------------------------------------------------------------------------------

# GMAO > Constitution technique des équipements

Décrire finement les équipements faisant l'objet d'interventions de maintenance (ex : camion, dépôt pétrolier, station service).

![GMAO : Camion](images/screenshots/02-equipement-camion.png)
<div class="img_legend">Fiche d'un camion citerne</div>

.fx: gmao_image

--------------------------------------------------------------------------------

# GMAO > Constitution technique des équipements

L'application est conçue de manière à ce qu'il soit possible de développer de nouveaux types d'équipements (ex : éolienne, pipeline, station de mesure, téléphérique, ascenseur, ...).

![GMAO : Dépôt](images/screenshots/03-equipement-depot.png)
<div class="img_legend">Fiche d'un dépôt pétrolier</div>

.fx: gmao_image

--------------------------------------------------------------------------------

# GMAO > Les clients

La base de données Clients est synchronisée sur la base de données fournie par votre ERP/CRM (ex : Ciel Quantum, Sage, ERP maison, SugarCRM...).

![GMAO : Gestion des clients](images/screenshots/04-client-1.png)
<div class="img_legend">Fiche client</div>

.fx: gmao_image

--------------------------------------------------------------------------------

# GMAO > Les clients

L'application de gestion des interventions permet d'enrichir cette base de données avec des informations utiles pour les interventions de maintenance (adresses, instruction particulières, documentation, ...).

![GMAO : Gestion des clients](images/screenshots/04-client-2.png)
<div class="img_legend">Suite de la fiche client</div>

.fx: gmao_image

--------------------------------------------------------------------------------

# GMAO > Les contrats

Les contrats sont en lien avec les clients, les équipements et les interventions. Ils alimentent des alertes (ex : contrat arrivant à échéance) et des bilans graphiques.

![GMAO : Gestion des contrats](images/screenshots/05-contrat.png)
<div class="img_legend">Gestion de contrat</div>

.fx: gmao_image

--------------------------------------------------------------------------------

# GMAO > Organisation mono ou multi-agences

Organisation des responsables et des techniciens par agence.

![GMAO : Gestion des agences](images/screenshots/06-agence-1.png)
<div class="img_legend">Liste des agences</div>

.fx: gmao_image

--------------------------------------------------------------------------------

# GMAO > Organisation mono ou multi-agences

Tableau de bord, planning et bilans par agence.

![GMAO : Fiche agence](images/screenshots/06-agence-2.png)
<div class="img_legend">Détail d'une fiche agence</div>

.fx: gmao_image

--------------------------------------------------------------------------------

# GMAO > Les intervenants

Liste des intervenants (nom, rattachement à une agence ou non, coordonnées...) réalisant les opérations de maintenance.

![GMAO : Liste des intervenants](images/screenshots/07-intervenant-1.png)
<div class="img_legend">Liste des intervenants</div>

.fx: gmao_image

--------------------------------------------------------------------------------

# GMAO > Les intervenants

Les intervenants sont responsables de saisir leurs rapports d'intervention dans l'outil.

![GMAO : Fiche intervenant](images/screenshots/07-intervenant-2.png)
<div class="img_legend">Détail d'une fiche intervenant</div>

.fx: gmao_image

--------------------------------------------------------------------------------

# GMAO > Les pièces détachées

Le module « Articles » permet de gérer toute la base de données des articles (pièces détachées) sur la base des informations fournies par votre ERP.

![GMAO : Gestion des agences](images/screenshots/08-article.png)
<div class="img_legend">Détail d'une fiche article</div>

.fx: gmao_image

--------------------------------------------------------------------------------

# GMAO > Les stocks de pièces détachées

Le module « Stocks » permet de visualiser le contenu des stocks sur la base des informations fournies par votre ERP.

![GMAO : Consultation des stocks](images/screenshots/09-stocks-1.png)
<div class="img_legend">Consultation des stocks de pièces détachées</div>

.fx: gmao_image img_w75percent

--------------------------------------------------------------------------------

# GMAO > Aide à la feuille de temps

Outil d'aide offrant aux intervenants le suivi des heures réalisées en intervention.

![GMAO : Aide à la feuille](images/screenshots/10-aide-a-la-feuille-de-temps.png)
<div class="img_legend">Consulter ses heures réalisées en intervention</div>

.fx: gmao_image

# Presenter Notes

Cela peut aider par exemple à la saisie des feuilles de temps par les employés.

--------------------------------------------------------------------------------

# GMAO > Aide à la planification

Outil permettant de planifier en avance des interventions récurrentes sur des équipements.

![GMAO : Aide à la planification](images/screenshots/11-aide-a-la-planification-1.png)
<div class="img_legend">Planifications d'interventions récurrentes</div>

.fx: gmao_image img_w85percent

# Presenter Notes

* Plus qu'une aide à la saisie, ce module permet de préparer en avance son planning avec toutes les interventions à venir connues.

* Des alertes informent en temps voulu les planificateurs de la nécessité de planifier une intervention.

--------------------------------------------------------------------------------

# GMAO > Aide à la planification

Planification d'une intervention et choix de la date pour la prochaine occurrence.

![GMAO : Aide à la planification](images/screenshots/11-aide-a-la-planification-2.png)
<div class="img_legend">Planification d'une intervention récurrente</div>

.fx: gmao_image img_w75percent

--------------------------------------------------------------------------------

# GMAO > Planning

Le planning permet de suivre les interventions par agence ou par équipe et par intervenant.

![GMAO : Planning](images/screenshots/12-planning-1.png)
<div class="img_legend">Interventions planifiées à venir</div>

.fx: gmao_image img_w90percent

--------------------------------------------------------------------------------

# GMAO > Planning

![GMAO : Planning](images/screenshots/12-planning-2.png)
<div class="img_legend">Consultation du résumé d'une ntervention à venir</div>

.fx: gmao_image img_w95percent

--------------------------------------------------------------------------------

# GMAO > Planning

Le planning des intervenants est synchronisable avec Google Agenda.

![GMAO : Google Agenda](images/screenshots/17-google-agenda-planning.png)
<div class="img_legend">Google Agenda</div>

.fx: gmao_image img_w90percent

# Presenter Notes

* Agenda comprenant un calendrier par intervenant.
* Cela offre une solution simple pour partager facilement des calendriers, et permet d' y accéder depuis son smartphone.

--------------------------------------------------------------------------------

# GMAO > Le rapport d'intervention

Automatisation complète du processus métier de gestion d'une intervention : de la revue de contrat jusqu'à l'envoi du rapport PDF au client ainsi qu'un document de pré-facturation à l'ERP.

![GMAO : Rapport d'intervention](images/screenshots/13-intervention-1.png)
<div class="img_legend">Rapport d'intervention : iniation de la mission et revue de contrat</div>

.fx: gmao_image img_w65percent

# Presenter Notes

* Les interventions de maintenance sont réalisées par les intervenants sur les équipements.
* Les étapes du cycle de vie sont organisées ainsi : Initiation mission, Revue de contrat, Préparation intervention, Exécution intervention (rapport de l'intervenant en mobilité), Clôture intervention, Intervention clôturée et mission pré-facturée.

--------------------------------------------------------------------------------

# GMAO > Le rapport d'intervention

![GMAO : Rapport d'intervention](images/screenshots/13-intervention-2.png)
<div class="img_legend">Rapport d'intervention : prépration et planification de l'intervention</div>

.fx: gmao_image img_w95percent

--------------------------------------------------------------------------------

# GMAO > Le rapport d'intervention

![GMAO : Rapport d'intervention](images/screenshots/13-intervention-3.png)
<div class="img_legend">Rapport d'intervention : rapport du technicien</div>

.fx: gmao_image img_w90percent

# Presenter Notes

* Il y a également un module activant la géolocalisation du lieu au moment de l'envoi du rapport PDF au client.

--------------------------------------------------------------------------------

# GMAO > Préparation de facture

Préparation de facture imprimable en PDF : rappel de la mission, du client, des temps passés, des déplacements et articles consommées. Envoi à l'ERP pour facturation.

![GMAO : Préparation de facture](images/screenshots/14-preparation-de-facture-1.png)
<div class="img_legend">Préparation de facture</div>

.fx: gmao_image img_w75percent

--------------------------------------------------------------------------------

# GMAO > Bilans et statistiques

De nombreux graphiques, statistiques, bilans peuvent être générés.

![GMAO : Bilans et indicateurs par agences](images/screenshots/15-bilans-1.png)
<div class="img_legend">Bilans et indicateurs par agences</div>

.fx: gmao_image img_w70percent

--------------------------------------------------------------------------------

# GMAO > Bilans et statistiques

![GMAO : Bilans par profil d'intervention](images/screenshots/15-bilans-2.png)
<div class="img_legend">Bilans par profil d'intervention</div>

.fx: gmao_image

--------------------------------------------------------------------------------

# GMAO > Bilans et statistiques

![GMAO : Bilans par mois et par profil d'intervention ; Importance du curatif](images/screenshots/15-bilans-3.png)
<div class="img_legend">Bilans par mois et par profil d'intervention ; Importance du curatif</div>

.fx: gmao_image img_w75percent

--------------------------------------------------------------------------------

# GMAO > Bilans et statistiques

![GMAO : Bilans par type d'équipement ; Consommatino d'articles](images/screenshots/15-bilans-4.png)
<div class="img_legend">Bilans par type d'équipement ; Consommation d'articles</div>

.fx: gmao_image img_w80percent

--------------------------------------------------------------------------------

# GMAO > Bilans et statistiques

![GMAO : Taux de disponibilité](images/screenshots/15-bilans-5-taux-de-disponibilite.png)
<div class="img_legend">Taux de disponibilité</div>

.fx: gmao_image img_w85percent

--------------------------------------------------------------------------------

# GMAO > Bilans et statistiques

![GMAO : Carte des équipements et des agences](images/screenshots/15-bilans-6-carte.png)
<div class="img_legend">Carte des équipements et des agences</div>

.fx: gmao_image img_w85percent

--------------------------------------------------------------------------------

# GMAO > Accès clients

Donner accès à ses clients à la constitution technique de leurs équipements et à l'historique des interventions de maintenance associées.

![GMAO : Liste des accès clients](images/screenshots/16-acces-clients-1.png)
<div class="img_legend">Liste des accès clients</div>

.fx: gmao_image img_w85percent

--------------------------------------------------------------------------------

# GMAO > Accès clients

![GMAO : Détail d'un accès client](images/screenshots/16-acces-clients-2.png)
<div class="img_legend">Détail d'un accès client</div>

.fx: gmao_image

# Presenter Notes

* On peut également avoir une photo d'accueil personnalisée.

--------------------------------------------------------------------------------

# GMAO > Utilisation en mobilité

L’application peut être utilisée dans le navigateur d'un smartphone ou d'une tablette connectée à Internet.

![GMAO : Utilisation depuis une tablette](images/screenshots/18-mobilite-tablette.jpg)
<div class="img_legend">Utilisation depuis une tablette</div>

.fx: gmao_image img_w80percent

--------------------------------------------------------------------------------

# GMAO > Utilisation en mobilité

![GMAO : Utilisation depuis un smartphone](images/screenshots/18-mobilite-smartphone.jpg)
<div class="img_legend">Utilisation depuis une smartphone</div>

.fx: gmao_image img_w90percent


--------------------------------------------------------------------------------

# Merci !

