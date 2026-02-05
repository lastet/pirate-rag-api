#!/usr/bin/env bash
set -e

echo "🏴‍☠️ Activating pirate test run..."

export USE_MOCK_LLM=1

./venv/bin/python3 semantic_test.py
