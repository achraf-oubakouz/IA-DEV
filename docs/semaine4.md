# Semaine 4 : tests approfondis et qualité, notes du binôme

> Une à deux pages. Uniquement des chiffres issus de VOS exécutions.

## 1. Couverture

- Avant (étape A) : 91 %, avec six lignes jamais exécutées dans `api/main.py` :
  - ligne 49 : réponse 503 lorsque le modèle n'est pas chargé ;
  - lignes 77 à 79 : réponse 500 lorsque le modèle plante ;
  - lignes 85 à 87 : lancement direct de l'API, non exécuté sous pytest.
- Après (étape D) : … % ; lignes exclues de la mesure et pourquoi : …

## 2. Défauts trouvés

| Symptôme | Test qui l'a révélé | Correction |
| --- | --- | --- |
| … | … | … |

## 3. Seuil d'abstention

- Deux ou trois points de la courbe (`python src/courbe_seuil.py`) : …
- Seuil retenu : … ; part des avis envoyés à un humain : … ; justification : …

## 4. Jeu d'or

- Bilan (`python src/bilan_jeu_or.py`) : justes …, abstentions …, erreurs franches déclarées …
- Ce que ces chiffres disent du modèle : …

## 5. Outils statiques

- Au départ : 11 remarques de ruff — B904 deux fois dans `api/main.py`; I001 et F401 dans `api/model.py`; F401 et B905 dans `src/evaluate.py`; I001 dans `tests/test_api.py`; E741 trois fois dans deux tests du TP1. Mypy : `Success: no issues found in 4 source files`.
- Parmi les défauts de la partie 2, combien ruff et mypy avaient-ils signalés ? À compléter après l'étape B en comparant les défauts trouvés avec ces résultats de départ.
