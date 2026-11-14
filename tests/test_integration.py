"""Tests d'intégration : l'API telle qu'elle tourne vraiment (TP4, étape D).

Les tests du TP3 vérifient des réponses ; ceux-ci vérifient le démarrage de l'API
et son comportement quand le modèle manque ou tombe en panne.
"""
from pathlib import Path
from types import SimpleNamespace

import pytest

MODELE = Path(__file__).resolve().parents[1] / "models" / "sentiment.joblib"
pytestmark = pytest.mark.skipif(not MODELE.exists(), reason="modèle non produit : python src/train.py")


def test_demarrage_reel_charge_le_modele():
    """D.1 (donné en exemple) : un client ouvert par « with » exécute le lifespan."""
    from fastapi.testclient import TestClient

    from api.main import app

    with TestClient(app) as client:
        reponse = client.get("/health")
    assert reponse.status_code == 200
    assert "TP2" in reponse.json()["model"]


def test_demarrage_refuse_si_modele_absent(tmp_path, monkeypatch):
    import importlib

    from fastapi.testclient import TestClient

    from api import model as api_model
    from api.main import app

    prediction_module = importlib.import_module("predict")
    api_model.charger_modele.cache_clear()
    monkeypatch.setattr(prediction_module, "MODELE", tmp_path / "absent.joblib")
    try:
        with pytest.raises(FileNotFoundError, match="sentiment.joblib absent"):
            with TestClient(app):
                pass
    finally:
        api_model.charger_modele.cache_clear()


def test_modele_non_charge_repond_503(monkeypatch):
    from fastapi.testclient import TestClient

    from api.main import app

    with TestClient(app) as client:
        monkeypatch.delattr(app.state, "classifier")
        assert client.get("/health").status_code == 503
        assert client.post("/predict", json={"text": "Avis de test"}).status_code == 503


@pytest.mark.parametrize(
    "exception",
    [RuntimeError("panne du modèle"), ValueError("bug interne")],
    ids=["runtime-error", "value-error"],
)
def test_panne_modele_repond_500_sans_detail_interne(monkeypatch, exception):
    from fastapi.testclient import TestClient

    from api.main import app

    class BrokenClassifier:
        model_name = "modèle en panne"

        def predict(self, text: str) -> dict:
            raise exception

    with TestClient(app) as client:
        monkeypatch.setattr(app.state, "classifier", BrokenClassifier())
        reponse = client.post("/predict", json={"text": "Avis de test"})
    assert reponse.status_code == 500
    assert "bug interne" not in reponse.text
    assert "panne du modèle" not in reponse.text


def test_classes_modele_inattendues_refusees_au_demarrage(monkeypatch):
    from fastapi.testclient import TestClient

    from api import model as api_model
    from api.main import app

    monkeypatch.setattr(
        api_model,
        "charger_modele",
        lambda: SimpleNamespace(classes_=["negative", "neutral", "positive"]),
    )
    with pytest.raises(ValueError, match="Classes du modèle non prises en charge"):
        with TestClient(app):
            pass
