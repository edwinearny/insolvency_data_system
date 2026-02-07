from sentence_transformers import CrossEncoder
from src.config import RERANKER_MODEL, TOP_K_RERANK

# ============================================
# Setup (runs once)
# ============================================
print("Loading reranker model...")
reranker = CrossEncoder(RERANKER_MODEL)
print("Reranker ready!")


# ============================================
# Functions
# ============================================

def normalize_scores(scores):
    """Convert raw scores to 0-1 range"""
    min_score = min(scores)
    max_score = max(scores)

    # Avoid division by zero
    if max_score == min_score:
        return [0.5] * len(scores)

    return [(s - min_score) / (max_score - min_score) for s in scores]


def rerank(query, results, top_k=TOP_K_RERANK):
    """Re-rank search results using cross-encoder"""

    if not results:
        return []

    # Create query-document pairs
    pairs = [[query, result["text"]] for result in results]

    # Get raw scores from cross-encoder
    raw_scores = reranker.predict(pairs)

    # Normalize to 0-1 range
    norm_scores = normalize_scores(raw_scores)

    # Attach scores to results
    for i, result in enumerate(results):
        result["rerank_score"] = round(float(norm_scores[i]), 4)

    # Sort by score (highest first)
    ranked = sorted(results, key=lambda x: x["rerank_score"], reverse=True)

    return ranked[:top_k]