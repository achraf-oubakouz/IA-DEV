"""Raccord entre l'API et le modèle entraîné au TP2.

L'API n'entraîne rien et ne connaît pas scikit-learn : elle appelle la fonction
predict() de src/predict.py, qui charge models/sentiment.joblib une seule fois.
"""
import sys
from pathlib import Path
from typing import Literal, TypedDict

RACINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RACINE / "src"))
from predict import ModelLabel, charger_modele  # noqa: E402  (fonctions du TP2)
from predict import predict as _predict  # noqa: E402  (fonctions du TP2)

SEUIL_ABSTENTION = 0.60
ApiLabel = Literal["POSITIVE", "NEGATIVE", "INDETERMINE"]
ETIQUETTES: dict[ModelLabel, Literal["POSITIVE", "NEGATIVE"]] = {
    "positive": "POSITIVE",
    "negative": "NEGATIVE",
}


class SentimentPrediction(TypedDict):
    label: ApiLabel
    score: float
    text: str


class SentimentClassifier:
    """Enveloppe du modèle TP2 avec l'interface attendue par l'API."""

    model_name = "tfidf-logreg (TP2, models/sentiment.joblib)"

    def __init__(self) -> None:
        pipeline = charger_modele()
        classes = set(pipeline.classes_)
        if classes != set(ETIQUETTES):
            raise ValueError(f"Classes du modèle non prises en charge : {sorted(classes)}")

    def predict(self, text: str) -> SentimentPrediction:
        """Renvoie l'étiquette du contrat, le score et un aperçu du texte."""
        prediction = _predict(text)
        label: ApiLabel = ETIQUETTES[prediction["label"]]
        if prediction["score"] < SEUIL_ABSTENTION:
            label = "INDETERMINE"
        return {"label": label, "score": prediction["score"], "text": text[:100]}


def load_model() -> SentimentClassifier:
    """Construit le classifier (le cache de chargement est dans src/predict.py)."""
    return SentimentClassifier()
