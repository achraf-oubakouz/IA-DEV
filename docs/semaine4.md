# Semaine 4 : tests approfondis et qualité, notes du binôme

> Une à deux pages. Uniquement des chiffres issus de VOS exécutions.

## 1. Couverture

- Avant (étape A) : 91 %, avec six lignes jamais exécutées dans `api/main.py` :
  - ligne 49 : réponse 503 lorsque le modèle n'est pas chargé ;
  - lignes 77 à 79 : réponse 500 lorsque le modèle plante ;
  - lignes 85 à 87 : lancement direct de l'API, non exécuté sous pytest.
- Après (étape D) : 97,78 % sans exclusion. Les lignes 83 à 85 de `api/main.py` (bloc `if __name__ == "__main__"`) restent non couvertes parce que les tests démarrent l'application avec `TestClient`, et non par le lancement direct du module.

## 2. Défauts trouvés

| Symptôme | Test qui l'a révélé | Correction |
| --- | --- | --- |
| Les espaces seuls recevaient un 422 avec `detail` sous forme de chaîne; Hypothesis a réduit le contre-exemple à `"\x85"`. | `test_frontieres_du_contrat` et `test_tout_texte_fait_de_blancs_est_refuse` | Un `field_validator` applique `strip()` dans `PredictRequest`, afin que Pydantic refuse les blancs avec sa forme d'erreur standard. |
| Une `ValueError` du modèle était renvoyée en 422 avec son message interne. | `test_panne_modele_repond_500_sans_detail_interne[value-error]` | Retrait du traitement spécial de `ValueError`; une panne du modèle est journalisée et renvoyée comme 500 générique. |
| Trois textes inventés étaient tous classés `NEGATIVE` avec une confiance de 0,5162, malgré une représentation TF-IDF nulle. | Essai manuel de trois textes inconnus; `test_predict_texte_inconnu_abstention` | Ajout du seuil `SEUIL_ABSTENTION = 0.60`; sous ce seuil, l'API renvoie `INDETERMINE`. |
| Le contrat des étiquettes ne garantissait pas les classes prises en charge. | `test_classes_modele_inattendues_refusees_au_demarrage` | Remplacement de `.upper()` par une correspondance typée et vérification des classes au démarrage. |

## 3. Seuil d'abstention

- Courbe observée : à 0,50, 58 réponses, 87,9 % d'exactitude et 7 erreurs; à 0,60, 42 réponses, 95,2 % et 2 erreurs; à 0,70, 37 réponses, 100 % et aucune erreur.
- Seuil retenu : 0,60 ; 16 avis sur 58 (28 %) sont envoyés à un humain. Par rapport à 0,50, ce seuil évite 5 erreurs en dirigeant ces 16 avis vers une validation humaine.

## 4. Jeu d'or

- Bilan (`python src/bilan_jeu_or.py`) : 4 justes, 13 abstentions, 3 erreurs franches déclarées sur 20 avis.
- Le modèle s'abstient souvent sur les formulations hors de son domaine ou peu couvertes par l'entraînement. Les trois erreurs déclarées montrent qu'il reste sensible aux avis mitigés, aux domaines différents et à la négation.
- `python -m pytest -q tests/test_jeu_or.py` : 18 passed, 3 xfailed; aucune erreur inattendue.

## 5. Outils statiques

- Au départ : 11 remarques de ruff — B904 deux fois dans `api/main.py`; I001 et F401 dans `api/model.py`; F401 et B905 dans `src/evaluate.py`; I001 dans `tests/test_api.py`; E741 trois fois dans deux tests du TP1. Mypy : `Success: no issues found in 4 source files`. Après correction, `ruff check .` et `mypy api` ne signalent plus de problème.
- Les deux défauts de comportement (validation des blancs et conversion de la panne en 422) n'ont été signalés ni par ruff ni par mypy; ce sont les tests qui les ont révélés.
