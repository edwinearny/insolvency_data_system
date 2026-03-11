from src.data import search
from src.query import enhance_query
from src.ranking import rerank
from src.generator import generate_answer

# Query
query = "What is insolvency?"

# Step 1: Enhance
enhanced = enhance_query(query)
print(f"Enhanced query: {enhanced}")

# Step 2: Search
raw_results = search(enhanced)
print(f"Found {len(raw_results)} results")

# Step 3: Re-rank
ranked_results = rerank(query, raw_results)
print(f"Top {len(ranked_results)} re-ranked")

# Step 4: Generate answer (NEW - RAG step)
answer = generate_answer(query, ranked_results)
print(f"\n--- Answer ---")
print(answer)