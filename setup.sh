#!/usr/bin/env bash
set -euo pipefail

echo "🔧  Setting up local development environment..."

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Upgrade pip & install deps
pip install --upgrade pip
pip install -r requirements.txt

echo "✅  Setup complete!"
