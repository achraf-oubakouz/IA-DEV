# Semaine 4 : tests approfondis et qualité, notes du binôme

> Une à deux pages. Uniquement des chiffres issus de VOS exécutions.

## 1. Couverture

- Avant (étape A) : non mesurée dans les résultats disponibles ; les tests vérifiaient principalement l'environnement et le cadrage.
- Pour chacune, le comportement qu'aucun test ne vérifiait : le chargement du modèle au démarrage, les routes `/` et `/health`, les prédictions positives et négatives, les réponses 422 et la gestion des erreurs de prédiction.
- Après (étape D) : non mesurée dans les résultats disponibles ; les blocs de lancement en `__main__` et les chemins réservés aux erreurs inattendues sont à exclure si la couverture est calculée uniquement sur les appels HTTP testés.

## 2. Défauts trouvés

| Symptôme | Test qui l'a révélé | Correction |
| --- | --- | --- |
| Un avis contenant des éléments positifs et négatifs peut être classé selon le mauvais élément | Jeu d'or, avis difficile avec `erreur_connue` | Conserver l'erreur documentée, ajouter des exemples mixtes et envisager des caractéristiques tenant compte du contexte |

## 3. Seuil d'abstention

- Deux ou trois points de la courbe (`python src/courbe_seuil.py`) : non disponibles dans les résultats fournis ; la courbe doit être exécutée sur le jeu de test `demo` de 58 avis.
- Seuil retenu : non déterminé ; part des avis envoyés à un humain : non déterminée ; justification : il faut choisir ces valeurs après comparaison de l'exactitude et du nombre d'avis transmis à un humain.

## 4. Jeu d'or

- Bilan (`python src/bilan_jeu_or.py`) : non exécuté dans les résultats fournis ; le jeu contient 20 avis, dont 9 difficiles et 1 erreur connue déclarée.
- Ce que ces chiffres disent du modèle : le jeu d'or couvre des formulations hors entraînement et vérifie notamment les négations, l'ironie, les avis mitigés et un autre domaine ; l'erreur déclarée mesure une limite connue plutôt que de la masquer.

## 5. Outils statiques

- Remarques au départ : ruff et mypy ne sont pas déclarés dans `requirements.txt` et aucun résultat d'exécution n'est fourni.
- Parmi les défauts de la partie 2, combien ruff et mypy avaient-ils signalés ? Non déterminé sans exécuter ces outils ; l'absence de signalement ne permettrait pas de conclure que les défauts fonctionnels sont absents.
