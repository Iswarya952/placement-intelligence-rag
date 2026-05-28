import streamlit as st

from ingestion.loader import load_pdf
from ingestion.chunker import chunk_text
from ingestion.deduplicator import remove_duplicates

from retrieval.vectorstore import build_vectorstore
from retrieval.hybrid import retrieve
from retrieval.reranker import rerank

from tools.reasoner import generate_answer
from tools.temporal import get_trend
from tools.fallback import fallback_response

from memory.chat_memory import save_chat


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


# =========================
# LOAD PDF
# =========================

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

index, embeddings = build_vectorstore(
    clean_chunks
)


# =========================
# USER QUERY
# =========================

query=st.text_input(
    "Ask placement query"
)


# =========================
# MAIN
# =========================

if query:


    # =========================
    # RETRIEVE
    # =========================

    results=retrieve(
        query,
        index,
        clean_chunks
    )

    ranked=rerank(
        query,
        results
    )


    # =========================
    # ANSWER
    # =========================

    answer=generate_answer(
        query,
        ranked
    )


    # =========================
    # FALLBACK
    # =========================

    fallback=fallback_response(
        query,
        ranked
    )


    # =========================
    # DISPLAY ANSWER
    # =========================

    if answer:

        st.success(
            answer
        )

        save_chat(
            query,
            answer
        )


    elif fallback:

        st.error(
            fallback
        )


    else:

        st.warning(
            "No exact answer found."
        )


    # =========================
    # TREND
    # =========================

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


    # =========================
    # CONTEXT
    # =========================

    if ranked:

        with st.expander(
            "Retrieved Context"
        ):

            for r in ranked:

                if len(r.split()) > 30:

                    st.write(
                        r[:300]
                    )


# =========================
# SIDEBAR
# =========================

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

✔ Chat Memory
"""
)


st.sidebar.subheader(
    "Sample Queries"
)

st.sidebar.write(
"""
• Google package

• Amazon CGPA

• Google trend

• Infosys trend

• Google interview rounds

• TCS interview rounds

• Companies with CGPA above 8.0

• Which company allows 1 backlog

• Which company allows 2 backlogs

• Companies with zero backlogs

• Which Python company gives highest package

• Who won IPL 2025?
"""
)