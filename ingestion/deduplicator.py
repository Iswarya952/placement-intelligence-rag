# ingestion/deduplicator.py

def remove_duplicates(chunks):

    unique_chunks=[]

    seen=set()

    for chunk in chunks:

        cleaned=chunk.strip()

        if cleaned not in seen:

            seen.add(cleaned)

            unique_chunks.append(cleaned)

    return unique_chunks