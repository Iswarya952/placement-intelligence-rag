def detect_conflict(
        query
):

    query=query.lower()

    conflicts={

        "amazon cgpa":
        {
            "official":"6.4",
            "portal":"7.0"
        },

        "google package":
        {
            "official":"42.0",
            "portal":"40.0"
        }

    }

    for key in conflicts:

        if key in query:

            return conflicts[key]

    return None