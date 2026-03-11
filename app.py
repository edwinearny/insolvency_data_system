import streamlit as st
from src.data import search, get_collection_count
from src.query import enhance_query
from src.ranking import rerank
from src.generator import generate_answer

st.title("UK Insolvency IR System")

query = st.text_input("Enter your query:")

if query:  # Enhance, Search, Rank, Display
    enhanced = enhance_query(query)
    st.write(f"**Enhanced query:** {enhanced}")
    raw_results = search(enhanced)
    ranked_results = rerank(query, raw_results)

    # RAG
    with st.spinner("Generating answer..."):
        answer = generate_answer(query, ranked_results)

    st.subheader("💡 Answer")
    st.write(answer)

    # Show source chunks
    st.subheader("📄 Sources")
    for i, result in enumerate(ranked_results):
        with st.expander(f"Result {i + 1} — {result['source']}"):
            st.write(result["text"])
            st.write(f"Rerank Score: **{result['rerank_score']}** | Search Score: **{result['score']}**")