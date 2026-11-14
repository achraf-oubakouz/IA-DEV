# Fiche de cadrage : Priorisation des avis négatifs

> Remplir chaque rubrique en une à trois phrases. Les rubriques marquées (obligatoire) sont vérifiées par `pytest`.

## Besoin en une phrase (obligatoire)
Détecter automatiquement et en temps réel les avis critiques contenant des accusations de fraude, d'abus ou de danger afin de les escalader dans un délai maximal de deux heures.

## Utilisateur final (obligatoire)
L'équipe Customer Success et les responsables de la gestion de crise et de la réputation de la marque e-commerce.

## Approche retenue (obligatoire)

Cocher une seule case :

- [ ] Règles métier
- [x] Machine learning
- [ ] RAG
- [ ] Modèle génératif seul

## Justification (obligatoire, citer au moins deux critères de la grille : (a) données étiquetées, (b) vérifiabilité, (c) coût par requête, (d) conséquence d'une erreur)
L'apprentissage supervisé est adapté car nous disposons de 500 avis étiquetés par l'équipe Customer Success (critère (a) : données étiquetées). La conséquence d'un faux négatif est particulièrement grave, car un avis critique non détecté peut entraîner des risques juridiques et réputationnels (critère (d) : conséquence d'une erreur). Les prédictions restent vérifiables par un humain (critère (b) : vérifiabilité).

## Données nécessaires et leur origine (obligatoire)
5 000 avis collectés sur les deux derniers mois depuis le site e-commerce et Amazon, dont 500 avis annotés manuellement par l'équipe Customer Success selon deux catégories : « NÉGATIF_CRITIQUE » et « AUTRE ». Les données doivent inclure le texte des avis et leurs métadonnées disponibles, comme la date et la note attribuée.

## Métrique de succès et seuil d'acceptation (obligatoire)
Atteindre un rappel d'au moins 98 % pour la classe « NÉGATIF_CRITIQUE », avec une précision d'au moins 80 % sur un jeu de test indépendant. L'objectif opérationnel est de détecter et signaler les avis critiques en moins de cinq minutes, afin de permettre leur escalade dans le délai de deux heures.

## Conséquence d'une erreur et validation humaine prévue (obligatoire)
Un faux négatif peut laisser passer un cas de fraude, d'abus ou de danger et provoquer une crise juridique ou réputationnelle. Un faux positif entraîne principalement une vérification supplémentaire. Chaque avis détecté comme critique sera immédiatement transmis à un membre de l'équipe pour validation et escalade humaine.

## Risques éthiques ou de confidentialité (obligatoire)
Les avis peuvent contenir des données personnelles, des accusations non vérifiées ou des informations sensibles sur les clients. Il faudra anonymiser les données, sécuriser leur stockage et éviter de considérer automatiquement une accusation comme un fait établi.

## Approche écartée et pourquoi (facultatif)
Les règles métier seules sont écartées car les formulations d'avis critiques peuvent être variées, implicites ou ironiques. Un modèle génératif seul serait plus coûteux et pourrait produire des interprétations incohérentes, ce qui est risqué dans un contexte de gestion de crise.
