#!/usr/bin/env bash
set -euo pipefail

echo "🔧  Setting up local development environment..."

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Upgrade pip & install deps
pip install --upgrade pip
pip install -r requirements.txt

# Install pre‑commit hooks
pre-commit install

# Initial scan
echo "🧪  Running initial pre‑commit scan..."
pre-commit run --all-files

echo "✅  Setup complete!"
