from rapidfuzz import fuzz

def remove_duplicates(chunks):

    unique=[]

    for chunk in chunks:

        duplicate=False

        for existing in unique:

            score=fuzz.ratio(
                chunk,
                existing
            )

            if score > 95:

                duplicate=True
                break

        if not duplicate:

            unique.append(chunk)

    return unique