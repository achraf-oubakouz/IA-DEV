# Fiche de cadrage : Prévision des ruptures de stock dans une chaîne de supermarchés

> Remplir chaque rubrique en une à trois phrases. Les rubriques marquées (obligatoire) sont vérifiées par `pytest`.

## Besoin en une phrase (obligatoire)
Le besoin est de développer un système intelligent capable de prévoir quotidiennement la demande par produit et par magasin afin d'anticiper les ruptures de stock, d'éviter les surstocks et de minimiser les coûts associés.

## Utilisateur final (obligatoire)
Le responsable de la gestion des stocks.

## Approche retenue (obligatoire)

Cocher une seule case :

- [ ] Règles métier
- [x] Machine learning
- [ ] RAG
- [ ] Modèle génératif seul

## Justification (obligatoire, citer au moins deux critères de la grille : (a) données étiquetées, (b) vérifiabilité, (c) coût par requête, (d) conséquence d'une erreur)
Le Machine Learning permet d'analyser l'historique des ventes et les facteurs influençant la demande afin de prévoir les quantités nécessaires pour chaque produit dans chaque magasin. Les prévisions peuvent être comparées aux ventes réelles, ce qui facilite leur vérification (critère (b) : vérifiabilité), et le coût par requête reste faible une fois le modèle entraîné (critère (c) : coût par requête).

## Données nécessaires et leur origine (obligatoire)
-Historique des ventes : dates, quantités vendues, produits et magasins (base de données de la chaîne de supermarchés).
-Données des produits : catégories, prix et dates de péremption (catalogue des produits).
-Données des stocks : quantités disponibles et historiques des ruptures (système de gestion des stocks).
-Promotions : réductions et offres commerciales (service marketing).

## Métrique de succès et seuil d'acceptation (obligatoire)
-Métrique principale : WAPE (Weighted Absolute Percentage Error), pour mesurer l'erreur globale des prévisions.
-Seuil d'acceptation : WAPE inférieur ou égal à 20 %.

## Conséquence d'une erreur et validation humaine prévue (obligatoire)
Une sous-estimation peut entraîner des ruptures de stock et des pertes de ventes, tandis qu'une surestimation peut provoquer un surstock et des coûts supplémentaires.

Le responsable des stocks valide les recommandations de réapprovisionnement avant toute commande importante ou inhabituelle

## Risques éthiques ou de confidentialité (obligatoire)
-Protection des données commerciales sensibles (ventes, prix et stocks).
-Limitation de l'accès aux données aux personnes autorisées.
-Risque de biais dans les prévisions pour certains magasins ou produits.
-Sécurisation et anonymisation des données si des informations personnelles sont présentes.

## Approche écartée et pourquoi (facultatif)

-Règles métier : trop rigides pour prendre en compte les variations complexes de la demande.
-RAG : principalement conçu pour rechercher et exploiter des informations documentaires, pas pour prévoir des quantités de ventes.
-Modèle génératif seul : peu adapté aux prévisions numériques précises et répétitives sur des milliers de produits.