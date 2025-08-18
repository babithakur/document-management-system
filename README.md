# 📄 Document Management System

A lightweight Document Management System to **upload, store, semantically search, and retrieve** PDF project reports. It extracts metadata like title, author, keywords, and summary using `PyMuPDF`, and supports **hybrid document search** using `SentenceTransformers`.

---

## 🚀 Features

- 📤 Upload and store PDF reports
- 🧠 Extract and store metadata (title, author, keywords, summary, created date)
- 🔍 **Hybrid Search**:
  - 🔡 Keyword-based search using SQL filters (title, author, summary, keywords)
  - 🧠 Semantic search using sentence embeddings (`SentenceTransformers`)
  - ⚖️ **Hybrid scoring** to rank documents by both relevance and meaning
- 📋 List all documents with metadata
- 🧽 Filter documents by author, date, or keyword
- 🛠️ REST API support to add/list/search documents

---

## 💡 How Hybrid Search Works

When a search query is submitted:

1. 📄 Documents are first filtered by keyword matches (title, author, summary, keywords).
2. 🧠 Each matching document's semantic similarity to the query is calculated using [all-MiniLM-L6-v2](https://www.sbert.net/docs/pretrained_models.html).
3. ⚖️ A **hybrid score** is computed combining:
   - `0.4 * keyword match score` (1 if query matches, else 0)
   - `0.6 * semantic similarity score` (cosine similarity between embeddings)
4. 🥇 Documents are ranked by this score, and only the **top-scoring document** is returned.

This allows the system to return accurate results even when the wording doesn’t exactly match — combining **precision** from keyword search and **meaningfulness** from semantic understanding.

---

## 🧰 Tech Stack

- 🐍 **Python 3.10+**
- ⚡ **FastAPI** – High-performance web framework
- 📄 **PyMuPDF** – PDF parsing and text extraction
- 🧠 **SentenceTransformers** – For semantic embeddings
- 🐘 **PostgreSQL** – Stores documents, metadata, and vector embeddings
- 🧵 **SQLAlchemy** – ORM for async DB access

---

## 📦 Installation & Setup

Follow these steps to run the project locally:

```bash
# 1️⃣ Clone the repository
git clone git@github.com:babithakur/document-management-system.git

# 2️⃣ Navigate into the project directory
cd document-management-system

# 3️⃣ Install required Python packages
pip install -r requirements.txt

# 4️⃣ Navigate out (optional, as uvicorn uses the module path)
cd ..

# 5️⃣ Database setup
psql -U your_user -d your_database -f document-management-system/documents_db.sql

# 6️⃣ Start the FastAPI server with uvicorn 🚀
uvicorn document-management-system.main:app --reload


