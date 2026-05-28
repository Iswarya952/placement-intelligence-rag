# tools/fallback.py

def fallback_response(
        query,
        results
):

    query=query.lower()

    out_of_scope=[
        "ipl",
        "cricket",
        "movie",
        "weather",
        "stock",
        "bitcoin"
    ]

    for word in out_of_scope:

        if word in query:

            return "Out-of-corpus query detected"

    if len(results)==0:

        return "No relevant information found"

    return None