from src.data import search
from src.query import enhance_query
from src.ranking import rerank

# Original query
query = "What happens when a company cannot pay its debts?"

# Step 1: Enhance query
enhanced = enhance_query(query)
print(f"Original query:  {query}")
print(f"Enhanced query:  {enhanced}")

# Step 2: Search vector DB
raw_results = search(enhanced)
print(f"\nRaw results: {len(raw_results)} chunks found")

# Step 3: Re-rank
ranked_results = rerank(query, raw_results)

# Show results
print(f"Re-ranked results: {len(ranked_results)}")
print("\n--- Top Results ---")
for i, result in enumerate(ranked_results):
    print(f"\nRank {i+1}")
    print(f"  Rerank Score: {result['rerank_score']}")
    print(f"  Search Score: {result['score']}")
    print(f"  Source: {result['source']}")
    print(f"  Text: {result['text'][:200]}...")
