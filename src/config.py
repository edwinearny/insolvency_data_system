# ============================================
# Configuration for Insolvency IR System
# ============================================

# Embedding Model (free, from HuggingFace)
EMBEDDING_MODEL = "all-MiniLM-L6-v2"

# Cross-Encoder Re-ranker (free, from HuggingFace)
RERANKER_MODEL = "cross-encoder/ms-marco-MiniLM-L-6-v2"

# ChromaDB Settings
CHROMA_COLLECTION_NAME = "insolvency_docs"
CHROMA_PERSIST_DIR = "./chroma_db"

# Chunking Settings
CHUNK_SIZE = 500        # tokens per chunk
CHUNK_OVERLAP = 50      # overlap between chunks

# Retrieval Settings
TOP_K_RETRIEVAL = 20    # how many chunks to retrieve from vector DB
TOP_K_RERANK = 5        # how many to show after re-ranking