import streamlit as st
from src.data import search, get_collection_count
from src.query import enhance_query
from src.ranking import rerank

# ============================================
# Page Setup
# ============================================
st.set_page_config(page_title="UK Insolvency IR System", page_icon="⚖️", layout="wide")
st.title("⚖️ UK Insolvency Information Retrieval System")
st.write("Search through UK insolvency law documents using AI-powered semantic search.")

# Show database info
chunk_count = get_collection_count()
st.sidebar.header("📊 System Info")
st.sidebar.write(f"Documents indexed: **{chunk_count}** chunks")

# ============================================
# Search Bar
# ============================================
query = st.text_input("🔍 Enter your query:", placeholder="e.g. What happens when a company cannot pay its debts?")

if query:
    # Step 1: Enhance query
    enhanced = enhance_query(query)

    # Show enhanced query
    with st.expander("🧠 Query Intelligence"):
        st.write(f"**Original query:** {query}")
        st.write(f"**Enhanced query:** {enhanced}")

    # Step 2: Search
    with st.spinner("Searching..."):
        raw_results = search(enhanced)

    # Step 3: Re-rank
    with st.spinner("Ranking results..."):
        ranked_results = rerank(query, raw_results)

    # ============================================
    # Display Results
    # ============================================
    st.subheader(f"📄 Top {len(ranked_results)} Results")

    for i, result in enumerate(ranked_results):
        with st.container():
            col1, col2 = st.columns([3, 1])

            with col1:
                st.markdown(f"### Result {i + 1}")
                st.write(result["text"])

            with col2:
                st.metric("Rerank Score", result["rerank_score"])
                st.metric("Search Score", result["score"])
                st.caption(f"📁 {result['source']}")

            st.divider()
