import pdfplumber
import pandas as pd

def extract_tables(path):

    all_tables = []

    with pdfplumber.open(path) as pdf:

        for page_no, page in enumerate(pdf.pages):

            tables = page.extract_tables()

            for table in tables:

                if table and len(table) > 1:

                    try:

                        df = pd.DataFrame(
                            table[1:],
                            columns=table[0]
                        )

                        all_tables.append(
                            {
                                "page": page_no + 1,
                                "data": df
                            }
                        )

                    except:
                        pass

    return all_tables