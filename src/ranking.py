from sentence_transformers import CrossEncoder
from src.config import RERANKER_MODEL, TOP_K_RERANK


print("Loading reranker model...")
reranker = CrossEncoder(RERANKER_MODEL)
print("Reranker ready!")


def normalize_scores(scores):  #Convert raw scores to 0-1 range
    min_score = min(scores)
    max_score = max(scores)

    if max_score == min_score:
        return [0.5] * len(scores)

    return [(s - min_score) / (max_score - min_score) for s in scores]


def rerank(query, results, top_k=TOP_K_RERANK): #cross encoder
    if not results:
        return []

    #Created query-doc pairs, raw scores from cross-encoder, normalize
    pairs = [[query, result["text"]] for result in results]
    raw_scores = reranker.predict(pairs)
    norm_scores = normalize_scores(raw_scores)

    for i, result in enumerate(results):
        result["rerank_score"] = round(float(norm_scores[i]), 4)

    # Sort
    ranked = sorted(results, key=lambda x: x["rerank_score"], reverse=True)

    return ranked[:top_k]
