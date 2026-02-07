import os
import chromadb
from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
from src.config import (
    EMBEDDING_MODEL,
    CHROMA_COLLECTION_NAME,
    CHROMA_PERSIST_DIR,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
    TOP_K_RETRIEVAL
)

# ============================================
# Initialize models and database (runs once)
# ============================================
print("Loading embedding model...")
embedding_model = SentenceTransformer(EMBEDDING_MODEL)

print("Connecting to ChromaDB...")
chroma_client = chromadb.PersistentClient(path=CHROMA_PERSIST_DIR)
collection = chroma_client.get_or_create_collection(
    name=CHROMA_COLLECTION_NAME,
    metadata={"hnsw:space": "cosine"}
)

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=CHUNK_SIZE,
    chunk_overlap=CHUNK_OVERLAP,
    length_function=len,
    separators=["\n\n", "\n", ". ", " ", ""]
)

print("DataLayer ready!")


# ============================================
# Functions
# ============================================

def load_pdfs(folder_path):
    """Read all PDFs from a folder and extract text"""
    documents = []

    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            filepath = os.path.join(folder_path, filename)
            print(f"Reading: {filename}")

            try:
                reader = PdfReader(filepath)
                text = ""
                for page in reader.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"

                if text.strip():
                    documents.append({
                        "text": text,
                        "source": filename,
                        "pages": len(reader.pages)
                    })
                    print(f"  ✓ Extracted {len(reader.pages)} pages")
                else:
                    print(f"  ✗ No text found (might be scanned PDF)")

            except Exception as e:
                print(f"  ✗ Error reading {filename}: {e}")

    print(f"\nTotal documents loaded: {len(documents)}")
    return documents


def chunk_documents(documents):
    """Split documents into smaller chunks"""
    chunks = []

    for doc in documents:
        split_texts = text_splitter.split_text(doc["text"])

        for i, chunk_text in enumerate(split_texts):
            chunks.append({
                "text": chunk_text,
                "source": doc["source"],
                "chunk_id": f"{doc['source']}_chunk_{i}"
            })

    print(f"Total chunks created: {len(chunks)}")
    return chunks


def build_index(folder_path):
    """Full pipeline: Load PDFs → Chunk → Embed → Store in ChromaDB"""

    documents = load_pdfs(folder_path)
    if not documents:
        print("No documents found!")
        return 0

    chunks = chunk_documents(documents)
    if not chunks:
        print("No chunks created!")
        return 0

    print("Creating embeddings (this may take a minute)...")
    texts = [chunk["text"] for chunk in chunks]
    embeddings = embedding_model.encode(texts, show_progress_bar=True)

    print("Storing in ChromaDB...")
    batch_size = 500
    for i in range(0, len(chunks), batch_size):
        batch_chunks = chunks[i:i + batch_size]
        batch_embeddings = embeddings[i:i + batch_size].tolist()

        collection.add(
            ids=[chunk["chunk_id"] for chunk in batch_chunks],
            documents=[chunk["text"] for chunk in batch_chunks],
            embeddings=batch_embeddings,
            metadatas=[{"source": chunk["source"]} for chunk in batch_chunks]
        )
        print(f"  Stored batch {i // batch_size + 1}")

    total = collection.count()
    print(f"\n✓ Index built! Total chunks in database: {total}")
    return total


def search(query, top_k=TOP_K_RETRIEVAL):
    """Search the vector database for relevant chunks"""

    query_embedding = embedding_model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
        include=["documents", "metadatas", "distances"]
    )

    formatted_results = []
    for i in range(len(results["ids"][0])):
        formatted_results.append({
            "text": results["documents"][0][i],
            "source": results["metadatas"][0][i]["source"],
            "score": round(1 - results["distances"][0][i], 4)
        })

    return formatted_results


def get_collection_count():
    """Get the number of chunks in the database"""
    return collection.count()
