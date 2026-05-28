# Placement Intelligence RAG Assistant

AI-powered Placement Intelligence Retrieval-Augmented Generation (RAG) System built using Python, FAISS, Sentence Transformers, and Streamlit.

This project analyzes placement datasets and answers placement-related queries such as:

* Company package details
* CGPA cutoffs
* Interview rounds
* Placement trends
* Backlog eligibility
* Conflict detection
* Out-of-corpus query detection

---

# 🚀 Features

## Semantic Search & Retrieval

* Vector Embeddings
* FAISS Vector Database
* Semantic Search
* Retrieval-Augmented Generation (RAG)
* Context Reranking

## Placement Intelligence Features

* Company Package Analysis
* CGPA Eligibility Analysis
* Backlog Eligibility Queries
* Interview Round Information
* Trend Analysis
* Conflict Detection
* Out-of-Corpus Detection

## UI Features

* Streamlit Chatbot Interface
* Sidebar Query Suggestions
* Trend Visualization
* Retrieved Context Viewer
* Chat History Storage

---

# 🧠 Core RAG Pipeline

1. PDF Loading
2. Text Chunking
3. Deduplication
4. Embedding Generation
5. FAISS Vector Storage
6. Semantic Retrieval
7. Reranking
8. Reasoning
9. Response Generation

---

# 📌 Tech Stack

## Frontend

* Streamlit

## Backend

* Python

## AI / NLP

* Sentence Transformers
* FAISS

## PDF Processing

* PyMuPDF
* Camelot
* Pandas

---

# 📂 Folder Structure

```bash
placement-intelligence-rag/
│
├── ingestion/
│   ├── loader.py
│   ├── chunker.py
│   ├── deduplicator.py
│   ├── table_extractor.py
│   └── chart_processor.py
│
├── retrieval/
│   ├── vectorstore.py
│   ├── hybrid.py
│   ├── reranker.py
│   └── conflict_detector.py
│
├── tools/
│   ├── reasoner.py
│   ├── temporal.py
│   └── fallback.py
│
├── memory/
│   └── chat_memory.py
│
├── data/
│   └── Placement_RAG_Dataset_Enhanced.pdf
│
├── history.json
├── ui.py
├── app.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/Iswarya952/placement-intelligence-rag.git

cd placement-intelligence-rag
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Streamlit UI

```bash
streamlit run ui.py
```

---

# 💬 Sample Queries

## Package Queries

* Google package
* Amazon package
* Infosys package

## CGPA Queries

* Amazon CGPA
* TCS CGPA
* Companies with CGPA above 8.0

## Interview Queries

* Google interview rounds
* Amazon interview rounds
* TCS interview rounds

## Backlog Queries

* Which company allows 1 backlog
* Which company allows 2 backlogs
* Companies with zero backlogs

## Trend Queries

* Google trend
* Infosys trend
* Amazon trend

## Python Queries

* Which Python company gives highest package

## Fallback Queries

```text
Who won IPL 2025?
```

Expected Output:

```text
Out-of-corpus query detected.
```

---

# 📊 UML Diagrams

## Use Case Diagram

```text
+-------------------+
|       User        |
+-------------------+
          |
 ------------------------------------------------
 |                    |                         |
 v                    v                         v

+----------------+   +----------------+   +----------------+
|   Ask Query    |   |  View Trends   |   | Detect Conflict|
+----------------+   +----------------+   +----------------+

                    |
                    v

        +---------------------------+
        | Placement RAG Assistant   |
        +---------------------------+
```

---

## Sequence Diagram

```text
User
 |
 | Ask Query
 v
ui.py
 |
 | retrieve(query)
 v
hybrid.py
 |
 | search vectors
 v
FAISS Vector DB
 |
 | top chunks
 v
reranker.py
 |
 | reranked chunks
 v
reasoner.py
 |
 | generate answer
 v
ui.py
 |
 | display response
 v
User
```

---

## Activity Diagram

```text
Start
  |
  v
Load PDF
  |
  v
Chunk Text
  |
  v
Remove Duplicates
  |
  v
Create Embeddings
  |
  v
Build FAISS Index
  |
  v
User Query
  |
  v
Retrieve Chunks
  |
  v
Rerank Results
  |
  v
Generate Answer
  |
  v
Display Output
  |
  v
End
```

---

## Architecture Diagram

```text
PDF Dataset
     ↓
PDF Loader
     ↓
Chunking
     ↓
Deduplication
     ↓
Embeddings
     ↓
FAISS Vector Store
     ↓
Retriever
     ↓
Reranker
     ↓
Reasoning Engine
     ↓
Streamlit UI
```

---

# 📦 Modules Description

| Module          | Purpose                 |
| --------------- | ----------------------- |
| loader.py       | PDF loading             |
| chunker.py      | Text chunking           |
| deduplicator.py | Duplicate removal       |
| vectorstore.py  | FAISS vector creation   |
| hybrid.py       | Semantic retrieval      |
| reranker.py     | Retrieval filtering     |
| reasoner.py     | Answer generation       |
| temporal.py     | Trend analysis          |
| fallback.py     | Out-of-corpus detection |
| chat_memory.py  | Chat history storage    |

---

# ✅ Current Project Status

Completed Features:

* PDF Processing
* Chunking
* Deduplication
* FAISS Retrieval
* Semantic Search
* Streamlit UI
* Trend Analysis
* Conflict Detection
* Fallback Handling
* Chat Memory

---

# 🔮 Future Improvements

* LangChain Integration
* Gemini/OpenAI Integration
* Real LLM-based Reasoning
* Multi-PDF Upload
* Advanced Dashboard
* Better Table Retrieval
* Graph Understanding
* Deployment on Streamlit Cloud

---

# 🖼 Example Outputs

## Google Package Query

```text
Google offers 42.0 LPA package.
```

## Amazon CGPA Conflict

```text
Official : 6.4
Portal : 7.0
```

## Trend Analysis

```text
2021 : 38.0 LPA
2022 : 40.0 LPA
2023 : 41.0 LPA
2024 : 42.0 LPA
```

---

# 👨‍💻 Author

**Iswarya**

## GitHub

GitHub: Iswarya952

---

# 📜 License

This project is developed for educational and research purposes.
