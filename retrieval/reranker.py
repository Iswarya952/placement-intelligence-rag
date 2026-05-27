from rapidfuzz import fuzz

def rerank(
        query,
        results
):

    scored=[]

    for r in results:

        score = fuzz.partial_ratio(
            query.lower(),
            r.lower()
        )

        scored.append(
            (score, r)
        )

    scored.sort(
        reverse=True
    )

    return [
        x[1]
        for x in scored
    ]