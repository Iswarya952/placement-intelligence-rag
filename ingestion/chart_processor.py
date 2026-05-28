
import fitz


def extract_chart_pages(pdf_path):

    doc=fitz.open(pdf_path)

    chart_pages=[]

    keywords=[
        "trend",
        "chart",
        "graph"
    ]

    for page_num in range(len(doc)):

        page=doc[page_num]

        text=page.get_text().lower()

        for keyword in keywords:

            if keyword in text:

                chart_pages.append(
                    {
                        "page":page_num+1,
                        "text":text[:1000]
                    }
                )

                break

    return chart_pages