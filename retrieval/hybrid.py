
from sentence_transformers import SentenceTransformer
import numpy as np


model=SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def retrieve(
        query,
        index,
        chunks,
        k=3
):

    query_embedding=model.encode(
        [query]
    )

    distances,ids=index.search(
        np.array(
            query_embedding,
            dtype="float32"
        ),
        k
    )

    results=[]

    for i in ids[0]:

        results.append(
            chunks[i]
        )

    return results