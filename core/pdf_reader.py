import os
from langchain_community.document_loaders import PyPDFLoader

PDF_FOLDER = "documents"

def load_pdfs():

    ''' Ihave written this docstring for better readability
    This is to load PDF files from Documents folder and retrun them as list of lanchain document for next processing '''


    documents = []

    for filename in os.listdir(PDF_FOLDER):
        if filename.endswith(".pdf"):
            print(f"Loading PDF :{filename}")
            file_path = os.path.join(PDF_FOLDER, filename)

            loader = PyPDFLoader(file_path)
            pages = loader.load()

            documents.extend(pages)

    return documents