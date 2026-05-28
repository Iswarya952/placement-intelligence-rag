# app.py

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
from tools.temporal import get_trend
from tools.reasoner import generate_answer


pdf_path="data/Placement_RAG_Dataset_Enhanced.pdf"

text=load_pdf(pdf_path)

chunks=chunk_text(text)

clean_chunks=remove_duplicates(chunks)

print("Total chunks:",len(chunks))
print("After dedup:",len(clean_chunks))

tables=extract_tables(pdf_path)

print("Tables found:",len(tables))

charts=extract_chart_pages(pdf_path)

print("Chart pages:",len(charts))

index,embeddings=build_vectorstore(
    clean_chunks
)

print("Vectors:",index.ntotal)

query="Google package"

answer=generate_answer(query)

print(answer)

results=retrieve(
    query,
    index,
    clean_chunks
)

ranked=rerank(
    query,
    results
)

for r in ranked:

    print("\nRESULT:\n")

    print(r[:300])

trend=get_trend(query)

print(trend)

conflict=detect_conflict(
    "Amazon CGPA"
)

print(conflict)

fallback=fallback_response(
    "Who won IPL 2025?",
    results
)

print(fallback)