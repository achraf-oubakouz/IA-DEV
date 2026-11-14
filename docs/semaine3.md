# Semaine 3 : l'API, notes du binôme

> Deux questions, quelques phrases chacune. Répondez avec ce que vous avez observé, pas avec le cours.

## 1. Pourquoi l'API refuse-t-elle de démarrer sans `models/sentiment.joblib`, plutôt que de démarrer et de répondre 503 ?

L'API charge le modèle dans le `lifespan`, avant d'accepter les requêtes, et `charger_modele()` lève immédiatement une erreur si le fichier est absent. Ce choix permet un démarrage en échec explicite plutôt qu'une API apparemment disponible mais incapable de prédire ; le statut 503 reste prévu pour le cas où l'application a démarré sans classifier chargé.

## 2. Un texte vide est refusé deux fois : par Pydantic, puis par `predict()`. Est-ce redondant ?

Ce n'est pas redondant : Pydantic protège la frontière HTTP et renvoie 422 avant d'appeler le modèle, tandis que `predict()` protège aussi les appels directs à la fonction. De plus, `predict()` utilise `strip()`, donc il refuse également un texte composé uniquement d'espaces, que la seule contrainte `min_length=1` accepterait.
