# memory/chat_memory.py

import json
import os


def save_chat(
        query,
        answer
):

    history=[]

    if os.path.exists(
        "memory/history.json"
    ):

        with open(
            "memory/history.json",
            "r"
        ) as f:

            try:

                history=json.load(f)

            except:

                history=[]

    history.append(
        {
            "query":query,
            "answer":answer
        }
    )

    with open(
        "memory/history.json",
        "w"
    ) as f:

        json.dump(
            history,
            f,
            indent=4
        )