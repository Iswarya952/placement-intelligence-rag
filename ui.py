import streamlit as st

from ingestion.loader import load_pdf
from ingestion.chunker import chunk_text
from ingestion.deduplicator import remove_duplicates

from retrieval.vectorstore import build_vectorstore
from retrieval.hybrid import retrieve
from retrieval.reranker import rerank
from retrieval.conflict_detector import detect_conflict

from tools.fallback import fallback_response
from tools.temporal import get_trend
from tools.reasoner import generate_answer


st.set_page_config(
    page_title="Placement Intelligence RAG",
    layout="wide"
)


st.title(
    "🎯 Placement Intelligence RAG Assistant"
)

st.subheader(
    "Placement Intelligence Chatbot"
)


pdf_path="data/Placement_RAG_Dataset_Enhanced.pdf"

text=load_pdf(
    pdf_path
)

chunks=chunk_text(
    text
)

clean_chunks=remove_duplicates(
    chunks
)

index,embeddings=build_vectorstore(
    clean_chunks
)


query=st.text_input(
    "Ask placement query"
)


if query:


    answer=generate_answer(
        query
    )


    if answer:

        st.success(
            answer
        )


    trend=get_trend(
        query
    )

    if trend:

        st.info(
f"""
📈 Trend Analysis

2021 : {trend['2021']} LPA

2022 : {trend['2022']} LPA

2023 : {trend['2023']} LPA

2024 : {trend['2024']} LPA
"""
        )


    results=retrieve(
        query,
        index,
        clean_chunks
    )


    ranked=rerank(
        query,
        results
    )


    fallback=fallback_response(
        query,
        ranked
    )


    if fallback:

        st.error(
            fallback
        )

    elif not answer:

        st.warning(
"""
No exact answer found.

Try placement queries:

• Google package

• Amazon CGPA

• Google trend

• Google interview rounds

• Companies with CGPA above 8.0

• Which company allows 1 backlog
"""
        )


    if ranked:

        with st.expander(
            "Retrieved context available"
        ):

            for r in ranked:

                st.write(
                    r[:500]
                )


st.sidebar.title(
    "Project Info"
)

st.sidebar.write(
"""
Modules

✔ PDF Loader

✔ Chunking

✔ Deduplication

✔ Table Extraction

✔ Chart Extraction

✔ FAISS Retrieval

✔ Reranking

✔ Conflict Detection

✔ Fallback

✔ Temporal Reasoning
"""
)