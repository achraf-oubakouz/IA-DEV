#!/usr/bin/env bash
# Mise en place complète du poste pour le TP1 (Linux / macOS / Git Bash).
# Usage : bash scripts/setup.sh
set -euo pipefail
cd "$(dirname "$0")/.."

echo "1/4 Vérification de Python 3.11"
PY=$(command -v python3.11 || command -v python3 || command -v python)
PY_VERSION=$("$PY" -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
if [ "$PY_VERSION" != "3.11" ]; then
    echo "Python 3.11 est requis (version trouvée : $PY_VERSION)." >&2
    exit 1
fi
"$PY" --version

echo "2/4 Création de l'environnement virtuel"
if [ -x .venv/bin/python ]; then
    VENV_VERSION=$(.venv/bin/python -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
    if [ "$VENV_VERSION" != "3.11" ]; then
        echo "Environnement existant en Python $VENV_VERSION : recréation en Python 3.11"
        rm -rf .venv
    fi
elif [ -x .venv/Scripts/python.exe ]; then
    VENV_VERSION=$(.venv/Scripts/python.exe -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
    if [ "$VENV_VERSION" != "3.11" ]; then
        echo "Environnement existant en Python $VENV_VERSION : recréation en Python 3.11"
        rm -rf .venv
    fi
fi
[ -d .venv ] || "$PY" -m venv .venv
# shellcheck disable=SC1091
source .venv/bin/activate 2>/dev/null || source .venv/Scripts/activate

echo "3/4 Installation des dépendances"
python -m pip install --upgrade pip
pip install -r requirements.txt
pip freeze > requirements.lock

echo "4/4 Diagnostic"
python scripts/check_setup.py
