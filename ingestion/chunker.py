def chunk_text(
        text,
        size=120
):

    chunks=[]

    words=text.split()

    for i in range(
        0,
        len(words),
        size
    ):

        chunk=" ".join(
            words[i:i+size]
        )

        chunks.append(
            chunk
        )

    return chunks