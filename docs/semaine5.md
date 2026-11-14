# Semaine 5 : l'interface, notes du binôme

> Trois questions, quelques phrases chacune. Répondez avec ce que vous avez observé.

## 1. Pourquoi l'interface n'importe-t-elle jamais `predict()` ni le fichier `.joblib` ?

L'interface envoie les textes à l'API avec `POST /predict`; seul le service API charge le modèle. Ainsi, réentraîner ou remplacer le modèle ne demande pas de modifier l'interface, et le fichier `.joblib` reste côté serveur.

## 2. Que montre l'interface quand le modèle hésite, et pourquoi est-ce mieux qu'un verdict forcé ?

Pour « xqzvb wlkptr grombu », elle affiche « Je ne sais pas : à faire vérifier par un humain », avec une confiance d'environ 52 % et un avertissement sur le seuil. L'abstention évite de présenter comme fiable une étiquette choisie avec une confiance insuffisante.

## 3. Que voit l'utilisateur quand l'API tombe ? Et le fichier `data/avis_exemple.csv` : combien d'avis partent vers un humain ?

Quand l'API est arrêtée, la page indique « API injoignable : lancez d'abord uvicorn api.main:app »; un texte refusé produit plutôt un avertissement de validation. Le CSV contient six avis : trois positifs, deux négatifs et un indéterminé; un avis, « xqzvb wlkptr grombu », part donc vers un humain.
