

import camelot


def extract_tables(pdf_path):

    tables=camelot.read_pdf(
        pdf_path,
        pages="all"
    )

    extracted=[]

    for i,table in enumerate(tables):

        extracted.append(
            {
                "page":table.page,
                "data":table.df
            }
        )

    return extracted