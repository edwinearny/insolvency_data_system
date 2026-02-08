# Configuration

EMBEDDING_MODEL = "all-MiniLM-L6-v2"

# Cross-Encoder
RERANKER_MODEL = "cross-encoder/ms-marco-MiniLM-L-6-v2"

# ChromaDB
CHROMA_COLLECTION_NAME = "insolvency_docs"
CHROMA_PERSIST_DIR = "./chroma_db"

CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

# Retrieval Settings
TOP_K_RETRIEVAL = 20    # vector DB
TOP_K_RERANK = 5    # re-ranking
