from src.data import search, get_collection_count

# Check if database has data
print(f"Chunks in database: {get_collection_count()}")

# Test search
query = "What is insolvency?"
results = search(query)

print(f"\nQuery: {query}")
print("@@@@@@@ Results ::::::")
for i, result in enumerate(results[:5]):
    print(f"\nResult {i+1} [Score: {result['score']}]")
    print(f"Source: {result['source']}")
    print(f"Text: {result['text'][:200]}...")
