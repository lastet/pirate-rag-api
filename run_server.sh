#!/usr/bin/env bash
set -e

export USE_MOCK_LLM=1

./venv/bin/python3 -m uvicorn app:app --reload
