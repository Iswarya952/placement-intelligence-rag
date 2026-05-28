Placement Intelligence RAG Assistant

AI-powered Placement Intelligence Retrieval-Augmented Generation (RAG) System built using Python, FAISS, Sentence Transformers, and Streamlit.

This project analyses placement datasets and answers placement-related queries such as:

Company package details
CGPA cutoffs
Interview rounds
Placement trends
Backlog eligibility
Conflict detection
Out-of-corpus query detection
Project Demo
Features Demonstrated
Semantic Search
Vector Retrieval
Placement Query Answering
Trend Analysis
Conflict Detection
Chat Memory
Streamlit UI
Features
Core RAG Pipeline
PDF Loading
Text Chunking
Deduplication
Vector Embeddings
FAISS Vector Store
Semantic Retrieval
Reranking
Placement Intelligence Features
Company Package Analysis
CGPA Eligibility Analysis
Backlog Eligibility Queries
Interview Round Information
Trend Analysis
Conflict Detection
Fallback Detection
Context Retrieval
UI Features
Streamlit Chatbot Interface
Sidebar Query Suggestions
Retrieved Context Viewer
Trend Display
Chat History Storage
UML Diagrams
Use Case Diagram
                    +-------------------+
                    |       User        |
                    +-------------------+
                              |
        ------------------------------------------------
        |              |             |                 |
        v              v             v                 v

+----------------+ +----------------+ +----------------+
| Ask Query      | | View Trends    | | Detect Conflict|
+----------------+ +----------------+ +----------------+

                              |
                              v

                 +-------------------------+
                 | Placement RAG Assistant |
                 +-------------------------+
Sequence Diagram
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
Activity Diagram
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
Architecture Diagram
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
Tech Stack
Frontend
Streamlit
Backend
Python
AI / NLP
Sentence Transformers
FAISS
Semantic Search
PDF Processing
PyMuPDF
Camelot
Pandas
Folder Structure
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
Installation
Clone Repository
git clone https://github.com/Iswarya952/placement-intelligence-rag.git
cd placement-intelligence-rag
Install Dependencies
pip install -r requirements.txt
Run Streamlit UI
streamlit run ui.py
Sample Queries
Package Queries
Google package
Amazon package
Infosys package
CGPA Queries
Amazon CGPA
TCS CGPA
Companies with CGPA above 8.0
Interview Queries
Google interview rounds
Amazon interview rounds
TCS interview rounds
Backlog Queries
Which company allows 1 backlog
Which company allows 2 backlogs
Companies with zero backlogs
Trend Queries
Google trend
Infosys trend
Amazon trend
Python Queries
Which Python company gives highest package
Fallback Queries
Who won IPL 2025?

Expected Output:

Out-of-corpus query detected.
Modules Description
Module	Purpose
loader.py	PDF loading
chunker.py	Text chunking
deduplicator.py	Duplicate removal
vectorstore.py	FAISS vector creation
hybrid.py	Semantic retrieval
reranker.py	Retrieval filtering
reasoner.py	Answer generation
temporal.py	Trend analysis
fallback.py	Out-of-corpus detection
chat_memory.py	Chat history storage
Current Project Status
Completed
PDF Processing
Chunking
Deduplication
FAISS Retrieval
Semantic Search
Streamlit UI
Trend Analysis
Conflict Detection
Fallback Handling
Chat Memory
Future Improvements
LangChain Integration
Gemini/OpenAI Integration
Real LLM-based Reasoning
Multi-PDF Upload
Advanced Dashboard
Better Table Retrieval
Graph Understanding
Deployment on Streamlit Cloud
Output Screenshots
Example Outputs
Google Package Query
Google offers 42.0 LPA package.
Amazon CGPA Conflict
Official : 6.4
Portal : 7.0
Trend Analysis
2021 : 38.0 LPA
2022 : 40.0 LPA
2023 : 41.0 LPA
2024 : 42.0 LPA
Author
ishu

Placement Intelligence RAG Project

GitHub:

Iswarya952 GitHub

License

This project is developed for educational and research purposes.