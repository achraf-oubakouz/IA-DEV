# Semaine 3 : l'API, notes du binôme

> Deux questions, quelques phrases chacune. Répondez avec ce que vous avez observé, pas avec le cours.

## 1. Pourquoi l'API refuse-t-elle de démarrer sans `models/sentiment.joblib`, plutôt que de démarrer et de répondre 503 ?

Le modèle est chargé dans le `lifespan` avant que l'application accepte des requêtes; sans le fichier, `load_model()` lève une `FileNotFoundError` et le démarrage échoue. C'est un choix « fail fast » : l'API ne se déclare pas prête si elle ne peut pas prédire, tandis que le 503 de `_classifier()` couvre le cas où l'API fonctionne mais où aucun classifieur n'est disponible.

## 2. Un texte vide est refusé deux fois : par Pydantic, puis par `predict()`. Est-ce redondant ?

La validation Pydantic et celle de `predict()` ne vérifient pas exactement la même chose : `min_length=1` rejette `""`, alors que `"   "` passe ce contrôle mais est rejeté par `predict()` après suppression des espaces. La vérification du modèle protège aussi les appels faits en dehors de l'API; dans une requête HTTP, Pydantic arrête `""` avant l'appel à `predict()`.
