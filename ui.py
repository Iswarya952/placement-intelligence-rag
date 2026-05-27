import streamlit as st

from ingestion.loader import load_pdf
from ingestion.chunker import chunk_text
from ingestion.deduplicator import remove_duplicates

from retrieval.vectorstore import build_vectorstore
from retrieval.hybrid import retrieve
from retrieval.reranker import rerank

from retrieval.conflict_detector import detect_conflict
from tools.fallback import fallback_response

st.title(
    "Placement Intelligence RAG"
)

pdf_path = (
    "data/Placement_RAG_Dataset_Enhanced.pdf"
)

text = load_pdf(
    pdf_path
)

chunks = chunk_text(
    text
)

clean_chunks = remove_duplicates(
    chunks
)

index,_ = build_vectorstore(
    clean_chunks
)

query = st.text_input(
    "Ask placement query"
)

if query:

    conflict = detect_conflict(
        query
    )

    if conflict:

        st.warning(
            f"""
Official:
{conflict['official']}

Portal:
{conflict['portal']}
"""
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

    fallback = fallback_response(
        query,
        ranked
    )

    if fallback:

        st.error(
            fallback
        )

    else:

        for r in ranked:

            st.write(
                r[:500]
            )