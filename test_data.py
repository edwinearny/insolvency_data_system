# from src.data import build_index, search
#
# # Build index from your PDFs
# total_chunks = build_index("data/raw")
#
# # Test a search
# if total_chunks > 0:
#     results = search("What is insolvency?")
#     print("\n--- Search Results ---")
#     for i, result in enumerate(results[:3]):
#         print(f"\nResult {i+1} [Score: {result['score']}]")
#         print(f"Source: {result['source']}")
#         print(f"Text: {result['text'][:200]}...")
