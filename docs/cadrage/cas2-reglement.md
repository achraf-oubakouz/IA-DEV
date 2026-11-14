# Fiche de cadrage : Questions sur le règlement intérieur

> Remplir chaque rubrique en une à trois phrases. Les rubriques marquées (obligatoire) sont vérifiées par `pytest`.

## Besoin en une phrase (obligatoire)
Automatiser la classification des commentaires des résidents afin d'identifier les problèmes liés à l'application du règlement de copropriété et de faciliter leur traitement par le syndic.

## Utilisateur final (obligatoire)
Le syndic et le comité d'administration d'une grande copropriété souhaitant réduire le temps consacré à l'analyse des commentaires des résidents.

## Approche retenue (obligatoire)

Cocher une seule case :

- [ ] Règles métier
- [x] Machine learning
- [ ] RAG
- [ ] Modèle génératif seul

## Justification (obligatoire, citer au moins deux critères de la grille : (a) données étiquetées, (b) vérifiabilité, (c) coût par requête, (d) conséquence d'une erreur)
L'apprentissage supervisé est pertinent car nous disposons de 1 200 commentaires déjà étiquetés par le comité d'administration (critère (a) : données étiquetées). Les résultats sont facilement vérifiables par le syndic en relisant les commentaires (critère (b) : vérifiabilité), et le coût de classification après entraînement est faible (critère (c) : coût par requête).

## Données nécessaires et leur origine (obligatoire)
1 200 commentaires de résidents collectés sur deux ans via l'application de la copropriété et classés positifs ou négatifs par le comité d'administration. Ils concernent le stationnement, le bruit, les espaces communs, l'entreposage et les frais de copropriété.

## Métrique de succès et seuil d'acceptation (obligatoire)
Atteindre un F1-score d'au moins 85 % sur un jeu de test indépendant, avec un rappel d'au moins 85 % pour la classe négative. Réduire d'au moins 70 % le temps consacré au tri des commentaires, soit passer de quatre heures à environ une heure et vingt minutes par semaine.

## Conséquence d'une erreur et validation humaine prévue (obligatoire)
Un faux négatif peut faire passer inaperçu un problème réel concernant l'application du règlement, tandis qu'un faux positif peut mobiliser inutilement le syndic. Le syndic vérifiera les commentaires signalés comme problématiques avant de prendre une décision ou d'engager une action.

## Risques éthiques ou de confidentialité (obligatoire)
Les commentaires peuvent révéler des informations personnelles sur les résidents, leurs habitudes ou leurs conflits avec leurs voisins. Il faudra anonymiser les données, restreindre les accès et garantir que les classifications ne soient pas utilisées pour discriminer ou pénaliser injustement un résident.

## Approche écartée et pourquoi (facultatif)
Les règles métier sont écartées car les commentaires peuvent être formulés de nombreuses manières et nécessitent une compréhension du contexte. Un modèle génératif seul serait également plus coûteux qu'un classificateur supervisé pour cette tâche.
