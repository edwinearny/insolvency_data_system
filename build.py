from src.data import build_index

# Build index from your PDFs (run this only once)
total_chunks = build_index("data/raw")
print(f"\nDone! {total_chunks} chunks stored in database.")
