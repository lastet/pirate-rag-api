#!/usr/bin/env bash
set -e

# REAL LLM MODE — generation enabled
unset USE_MOCK_LLM

./venv/bin/python3 -m uvicorn app:app --reload
