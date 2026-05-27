import pdfplumber

def extract_chart_pages(
        pdf_path
):

    chart_pages=[]

    with pdfplumber.open(
        pdf_path
    ) as pdf:

        for i,page in enumerate(
            pdf.pages
        ):

            text=page.extract_text()

            if text and (
                "trend" in text.lower()
                or "chart" in text.lower()
            ):

                chart_pages.append(
                    {
                        "page":i+1,
                        "text":text[:1000]
                    }
                )

    return chart_pages