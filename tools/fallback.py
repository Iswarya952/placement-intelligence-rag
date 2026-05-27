def fallback_response(
        query,
        results
):

    if len(results)==0:

        return (
            "Information not found "
            "in placement dataset"
        )

    joined=" ".join(
        results
    ).lower()

    words=query.lower().split()

    matches=0

    for w in words:

        if w in joined:

            matches+=1

    if matches==0:

        return (
            "Out-of-corpus query detected"
        )

    return None