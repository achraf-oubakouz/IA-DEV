# Fiche de cadrage : Ordonnances incomplètes en pharmacie

> Remplir chaque rubrique en une à trois phrases. Les rubriques marquées (obligatoire) sont vérifiées par `pytest`.

## Besoin en une phrase (obligatoire)
Automatiser la classification des avis clients des pharmacies en avis positifs ou négatifs afin d'identifier rapidement les problèmes liés à la qualité du service et à la satisfaction des clients.

## Utilisateur final (obligatoire)
Les propriétaires et gérants de pharmacies au Canada, qui souhaitent surveiller leur réputation en ligne et améliorer la qualité de leurs services.

## Approche retenue (obligatoire)

Cocher une seule case :

- [x] Règles métier
- [ ] Machine learning
- [ ] RAG
- [ ] Modèle génératif seul

## Justification (obligatoire, citer au moins deux critères de la grille : (a) données étiquetées, (b) vérifiabilité, (c) coût par requête, (d) conséquence d'une erreur)
L'approche supervisée est adaptée car nous disposons de 500 avis déjà étiquetés positifs ou négatifs (critère (a) : données étiquetées). Les prédictions sont facilement vérifiables par les propriétaires (critère (b) : vérifiabilité), et une erreur peut entraîner une mauvaise priorisation des problèmes de satisfaction client (critère (d) : conséquence d'une erreur).

## Données nécessaires et leur origine (obligatoire)
500 avis clients provenant de plateformes comme Google et Trustpilot, collectés sur une période de six mois et étiquetés par les propriétaires des pharmacies. Ils couvrent notamment la qualité du service, les délais d'attente, l'amabilité du personnel et la disponibilité des médicaments.

## Métrique de succès et seuil d'acceptation (obligatoire)
500 avis clients provenant de plateformes comme Google et Trustpilot, collectés sur une période de six mois et étiquetés par les propriétaires des pharmacies. Ils couvrent notamment la qualité du service, les délais d'attente, l'amabilité du personnel et la disponibilité des médicaments.


## Conséquence d'une erreur et validation humaine prévue (obligatoire)
Un faux négatif peut empêcher la détection d'un problème important, tandis qu'un faux positif peut entraîner une réaction inutile. Les propriétaires valideront les avis ambigus et les avis négatifs prioritaires avant toute action.

## Risques éthiques ou de confidentialité (obligatoire)
Les avis peuvent contenir des informations personnelles ou des données sensibles liées à la santé. Il faudra anonymiser les données, limiter leur accès et éviter de collecter ou d'exposer des informations permettant d'identifier les clients.

## Approche écartée et pourquoi (facultatif)
Le modèle génératif seul est écarté, car il serait plus coûteux par requête et inutilement complexe pour une classification binaire relativement simple.
