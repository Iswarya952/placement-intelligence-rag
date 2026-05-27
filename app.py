from ingestion.loader import load_pdf
from ingestion.chunker import chunk_text
from ingestion.deduplicator import remove_duplicates
from ingestion.table_extractor import extract_tables
from ingestion.chart_processor import extract_chart_pages

from retrieval.vectorstore import build_vectorstore
from retrieval.hybrid import retrieve
from retrieval.reranker import rerank
from retrieval.conflict_detector import detect_conflict

from tools.fallback import fallback_response


pdf_path = (
    "data/Placement_RAG_Dataset_Enhanced.pdf"
)


print(
    "\n===== PDF LOADING ====="
)

text = load_pdf(
    pdf_path
)


print(
    "\n===== CHUNKING ====="
)

chunks = chunk_text(
    text
)

clean_chunks = remove_duplicates(
    chunks
)

print(
    "Total chunks:",
    len(chunks)
)

print(
    "After dedup:",
    len(clean_chunks)
)



print(
    "\n===== TABLE EXTRACTION ====="
)

tables = extract_tables(
    pdf_path
)

print(
    "Tables found:",
    len(tables)
)


for t in tables[:3]:

    print(
        "\nPage:",
        t["page"]
    )

    print(
        t["data"].head()
    )



print(
    "\n===== CHART EXTRACTION ====="
)

charts = extract_chart_pages(
    pdf_path
)

print(
    "Charts found:",
    len(charts)
)

for c in charts:

    print(
        "\nChart Page:",
        c["page"]
    )

    print(
        c["text"][:300]
    )



print(
    "\n===== VECTORSTORE ====="
)

index, embeddings = build_vectorstore(
    clean_chunks
)

print(
    "Vectors:",
    index.ntotal
)



print(
    "\n===== RETRIEVAL TEST ====="
)

query = (
    "Google package"
)

results = retrieve(
    query,
    index,
    clean_chunks
)

ranked = rerank(
    query,
    results
)


for r in ranked:

    print(
        "\nRESULT:\n"
    )

    print(
        r[:500]
    )



print(
    "\n===== CONFLICT TEST ====="
)

query = (
    "Amazon CGPA"
)

conflict = detect_conflict(
    query
)


if conflict:

    print(
        "Conflict Found"
    )

    print(
        "Official:",
        conflict[
            "official"
        ]
    )

    print(
        "Portal:",
        conflict[
            "portal"
        ]
    )

else:

    print(
        "No conflict"
    )



print(
    "\n===== FALLBACK TEST ====="
)

query = (
    "Who won IPL 2025?"
)

results = retrieve(
    query,
    index,
    clean_chunks
)

fallback = fallback_response(
    query,
    results
)


if fallback:

    print(
        fallback
    )

else:

    print(
        "Answer exists"
    )



print(
    "\n===== PROJECT SUMMARY ====="
)

print(
    """
Completed Modules:

1. PDF Loader
2. Chunking
3. Deduplication
4. Table Extraction
5. Chart Extraction
6. FAISS Vector Store
7. Retrieval
8. Reranking
9. Conflict Detection
10. Fallback Handling
11. Streamlit UI
12. Temporal Reasoning
"""
)