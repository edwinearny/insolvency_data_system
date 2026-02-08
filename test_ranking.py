from src.data import search
from src.query import enhance_query
from src.ranking import rerank

query = "What happens when a company cannot pay its debts?"

# Enhance query, Search DB with initial ranking, re-rank
enhanced = enhance_query(query)
print("Original : ", query)
print("Enhanced : ", enhanced)

raw_results = search(enhanced)
print("Number of results:",  {len(raw_results)})

ranked_results = rerank(query, raw_results)

print(f"Re-ranked results: {len(ranked_results)}")
print(" $$$$$$$  Top Results :::")
for i, result in enumerate(ranked_results):
    print(f"\nRank {i+1}")
    print(f"  Rerank Score: {result['rerank_score']}")
    print(f"  Search Score: {result['score']}")
    print(f"  Source: {result['source']}")
    print(f"  Text: {result['text'][:200]}...")
