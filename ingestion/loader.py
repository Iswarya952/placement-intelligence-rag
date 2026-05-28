
from langchain_community.document_loaders import PyPDFLoader

def load_pdf(pdf_path):

    loader = PyPDFLoader(pdf_path)

    documents = loader.load()

    text = ""

    for doc in documents:

        text += doc.page_content

    return text