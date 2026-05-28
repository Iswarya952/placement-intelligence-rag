

from sentence_transformers import CrossEncoder


reranker=CrossEncoder(
    "cross-encoder/ms-marco-MiniLM-L-6-v2"
)


def rerank(
        query,
        results
):

    pairs=[]

    for r in results:

        pairs.append(
            [query,r]
        )

    scores=reranker.predict(
        pairs
    )

    ranked=sorted(
        zip(results,scores),
        key=lambda x:x[1],
        reverse=True
    )

    final_results=[]

    for r,s in ranked:

        final_results.append(r)

    return final_results