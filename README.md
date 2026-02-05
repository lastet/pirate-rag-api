# 🏴‍☠️ pirate-rag-api

A production-oriented **Retrieval-Augmented Generation (RAG) API** built with FastAPI, ChromaDB, and a local LLM via Ollama.

This project demonstrates how to design, test, containerize, and continuously validate an AI-powered API **without relying on non-deterministic LLM output in CI**.

---

## ✨ What This Project Does

`pirate-rag-api` answers user questions **only** based on provided documents.
The system:

1. Retrieves relevant context from a vector database
2. Augments the prompt with that context
3. Generates an answer using a local LLM

The result is a controllable, testable, and production-friendly RAG service.

---

## 🧠 Architecture Overview

**Flow:**

User → FastAPI `/query` → ChromaDB semantic search → context retrieval → LLM → response

**Core layers:**

* **API layer**: FastAPI + Uvicorn
* **Retrieval layer**: ChromaDB (vector embeddings)
* **Generation layer**: Ollama with TinyLlama


---

## 🔧 Tech Stack

* **FastAPI** — API framework with automatic Swagger UI
* **Uvicorn** — ASGI web server
* **ChromaDB** — vector database for semantic search
* **Ollama** — local LLM runtime
* **TinyLlama** — lightweight generation model
* **Docker** — containerization
* **GitHub Actions** — CI/CD pipeline

---

## 🧪 Testing Strategy (Key Design Decision)

LLM outputs are **non-deterministic**, which makes them unsuitable for CI testing.

To solve this, the project introduces a **Mock LLM Mode**:

* During CI runs, the API returns **retrieved context directly**
* Tests validate **retrieval quality**, not generated text
* Same input → same output → reliable CI

### Benefits

* Deterministic tests
* Faster CI runs
* No Ollama dependency in CI
* Data quality protection

This approach ensures that degraded knowledge updates are caught **before deployment**.

---

## 🚀 Running the Project Locally

mock mode: ./run_server.sh
real LLM: ./run_server_real.sh
tests: ./run_tests.sh

### 1. Prerequisites

* Python 3.12+
* Ollama installed and running
* Docker (optional, for containerized run)

---

### 2. Clone and Setup

```bash
git clone https://github.com/your-username/pirate-rag-api.git
cd pirate-rag-api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

### 3. Start Ollama

```bash
ollama run tinyllama
```

---

### 4. Run the API

```bash
uvicorn app:app --reload
```

Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## 🔍 Example Query

```bash
curl -X POST "http://127.0.0.1:8000/query" \
  -G --data-urlencode "q=How to make pancakes?"
```

---

## ➕ Adding Knowledge Dynamically

Use the `/add` endpoint to update the knowledge base **without restarting the API**.

This allows live updates and immediate availability of new data.

---

## 🐳 Docker Support

Build and run the container:

```bash
docker build -t pirate-rag-api .
docker run -p 8000:8000 pirate-rag-api
```

The container includes precomputed embeddings for faster startup.

---

## 🔄 CI/CD with GitHub Actions

On every push, the pipeline:

* Installs dependencies
* Rebuilds embeddings
* Runs semantic tests in mock LLM mode
* Blocks degraded data changes

This ensures consistent API behavior and protects knowledge quality.

---

## 🗺️ Project Structure

```text
pirate-rag-api/
├── app.py              # FastAPI application
├── embed.py            # Embedding generation
├── semantic_test.py    # Deterministic semantic tests
├── docs/             # Knowledge base document
├── Dockerfile
├── requirements.txt
└── .github/workflows/
    └── ci.yml
```

---

## 🎯 Why This Project Matters

This project focuses on **engineering AI systems**, not just calling an LLM.

Key takeaways:

* LLMs must be treated as unreliable components
* Retrieval quality is testable and critical
* CI/CD applies to AI systems just like traditional services

---

## 🧭 Next Steps

* Add UI for live demo 
* Add more pirate documentation
* Expand semantic test coverage 
* Add monitoring & observability

---

Built with curiosity, discipline, and a slight pirate attitude ☠️
