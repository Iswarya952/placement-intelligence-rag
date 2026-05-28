# tools/temporal.py

def get_trend(query):

    q=query.lower()

    if "google" in q:

        return {
            "2021":38.0,
            "2022":40.0,
            "2023":41.0,
            "2024":42.0
        }

    if "infosys" in q:

        return {
            "2021":36.0,
            "2022":39.0,
            "2023":41.5,
            "2024":42.9
        }

    if "amazon" in q:

        return {
            "2021":22.0,
            "2022":25.0,
            "2023":27.0,
            "2024":28.6
        }

    return None