

def detect_conflict(query):

    q=query.lower()

    if "amazon" in q and "cgpa" in q:

        return {
            "official":"6.4",
            "portal":"7.0"
        }

    if "google" in q and "package" in q:

        return {
            "official":"42.0",
            "portal":"45.0"
        }

    return None