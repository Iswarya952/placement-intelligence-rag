from ingestion.loader import load_pdf
from ingestion.chunker import chunk_text
from ingestion.deduplicator import remove_duplicates
from ingestion.table_extractor import extract_tables
from retrieval.vectorstore import build_vectorstore
from retrieval.hybrid import retrieve
pdf_path = "data/Placement_RAG_Dataset_Enhanced.pdf"

text = load_pdf(pdf_path)

chunks = chunk_text(text)

clean_chunks = remove_duplicates(chunks)

print("Total chunks:", len(chunks))
print("After dedup:", len(clean_chunks))

print("\n===== TABLE EXTRACTION =====\n")

tables = extract_tables(pdf_path)

print("Tables found:", len(tables))

for t in tables[:3]:

    print(
        "\nPage:",
        t["page"]
    )

    print(
        t["data"].head()
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

query = "What is the package offered by Google?"

results = retrieve(
    query,
    index,
    clean_chunks
)

for r in results:

    print(
        "\nRESULT:\n"
    )

    print(r[:500])