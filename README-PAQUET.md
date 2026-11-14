# sentiment-app

`sentiment-app` est un paquet Python qui classe le sentiment d'un avis client en français
et renvoie une étiquette (`positive` ou `negative`) avec un score de confiance.

## Installation

Installez la roue distribuée avec le paquet :

```bash
python -m pip install sentiment_app-1.0.0-py3-none-any.whl
```

Le paquet embarque son modèle et installe la commande `sentiment`.

## Utilisation

```bash
sentiment "Livraison rapide, produit conforme, très satisfait"
sentiment --json "Produit cassé et service client injoignable"
```

La fonction Python est également disponible :

```python
from sentiment_app import predict

resultat = predict("Livraison rapide, produit conforme, très satisfait")
print(resultat)  # {'label': 'positive', 'score': 0.7087}
```

Un texte vide ou composé uniquement d'espaces lève `ValueError`.

## Limites

Le modèle est entraîné sur le petit jeu de démonstration du cours. Ses résultats ne sont
pas garantis pour d'autres domaines, les textes nuancés, l'ironie ou les négations. Le score
est une confiance du modèle, pas une probabilité calibrée ni une garantie de justesse.
La roue inclut le modèle entraîné et dépend de scikit-learn 1.5.
