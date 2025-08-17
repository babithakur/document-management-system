# 📄 Document Management System

A lightweight Document Management System to **upload, store, search, and retrieve** PDF project reports. It extracts metadata like title, author, keywords, and summary using `PyMuPDF` and provides RESTful APIs built with `FastAPI`.

---

## 🚀 Features

- 📤 Upload and store PDF reports
- 🧠 Extract and store metadata (title, author, keywords, summary, date, etc.)
- 🔍 Keyword-based and full-text content search
- 📋 List all documents with metadata
- 🧽 Filter documents by author, date, keyword, or category
- 🛠️ REST API support to add/list/search documents

---

## 🧰 Tech Stack

- 🐍 **Python 3.10+**
- ⚡ **FastAPI** – For building high-performance APIs
- 📄 **PyMuPDF** – PDF parsing and text extraction
- 🐘 **PostgreSQL** – Relational database for metadata and content storage
- 🔍 **SQL** – Database setup via import script

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


