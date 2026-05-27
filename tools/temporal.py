def temporal_query(
        query
):

    query=query.lower()

    trends={

        "google":

        {
            "2021":38.0,
            "2022":40.0,
            "2023":41.0,
            "2024":42.0
        },

        "infosys":

        {
            "2021":36.0,
            "2022":39.0,
            "2023":41.5,
            "2024":42.9
        }

    }

    for company in trends:

        if company in query:

            return trends[
                company
            ]

    return None