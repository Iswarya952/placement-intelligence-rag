import streamlit as st

from ingestion.loader import load_pdf
from ingestion.chunker import chunk_text
from ingestion.deduplicator import remove_duplicates

from retrieval.vectorstore import build_vectorstore
from retrieval.hybrid import retrieve
from retrieval.reranker import rerank
from retrieval.conflict_detector import detect_conflict

from tools.fallback import fallback_response
from tools.temporal import temporal_query


st.set_page_config(
    page_title="Placement Intelligence RAG",
    layout="wide"
)


st.title(
    "🎯 Placement Intelligence RAG"
)

st.write(
    "Ask placement related queries"
)


pdf_path = (
    "data/Placement_RAG_Dataset_Enhanced.pdf"
)


@st.cache_resource
def load_pipeline():

    text = load_pdf(
        pdf_path
    )

    chunks = chunk_text(
        text
    )

    clean_chunks = remove_duplicates(
        chunks
    )

    index, embeddings = build_vectorstore(
        clean_chunks
    )

    return (
        clean_chunks,
        index
    )


clean_chunks, index = load_pipeline()


query = st.text_input(
    "Ask placement query"
)


if query:

    st.subheader(
        "Query"
    )

    st.write(
        query
    )


    conflict = detect_conflict(
        query
    )

    if conflict:

        st.warning(
            f"""
Conflict Found

Official:
{conflict['official']}

Portal:
{conflict['portal']}
"""
        )


    trend = temporal_query(
        query
    )

    if trend:

        st.subheader(
            "Trend Analysis"
        )

        for year, value in trend.items():

            st.write(
                f"{year} : {value} LPA"
            )

        st.stop()



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

        st.stop()



    st.subheader(
        "Retrieved Results"
    )



    for i, r in enumerate(
            ranked,
            start=1
    ):

        st.write(
            f"Result {i}"
        )

        st.write(
            r[:700]
        )

        st.divider()