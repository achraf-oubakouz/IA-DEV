"""Tests d'intégration : l'API telle qu'elle tourne vraiment (TP4, étape D). À COMPLÉTER.

Les tests du TP3 vérifient des réponses ; ceux-ci vérifient le démarrage de l'API
et son comportement quand le modèle manque ou tombe en panne.
"""
from pathlib import Path

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


def test_demarrage_refuse_modele_absent(monkeypatch):
    from fastapi.testclient import TestClient

    import predict
    from api.main import app
    from api.model import charger_modele

    monkeypatch.setattr(predict, "MODELE", MODELE.with_name("modele-inexistant.joblib"))
    charger_modele.cache_clear()
    try:
        with pytest.raises(FileNotFoundError, match="sentiment.joblib absent"):
            with TestClient(app):
                pass
    finally:
        charger_modele.cache_clear()


def test_modele_non_charge_renvoie_503():
    from fastapi.testclient import TestClient

    from api.main import app

    with TestClient(app) as client:
        app.state.classifier = None
        assert client.get("/health").status_code == 503
        assert client.post("/predict", json={"text": "Avis de test"}).status_code == 503


@pytest.mark.parametrize("exception", [RuntimeError("panne"), ValueError("bug interne")])
def test_modele_en_panne_renvoie_500_sans_detail_interne(exception):
    from fastapi.testclient import TestClient

    from api.main import app

    class BrokenClassifier:
        model_name = "test"

        def predict(self, text):
            raise exception

    with TestClient(app) as client:
        app.state.classifier = BrokenClassifier()
        response = client.post("/predict", json={"text": "Avis de test"})
    assert response.status_code == 500
    assert "bug interne" not in response.text
    assert "panne" not in response.text
