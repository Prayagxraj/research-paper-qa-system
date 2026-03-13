from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(documents):
    """
    
    Chunking
    """


    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )

   
    document_chunks = splitter.split_documents(documents)

    return document_chunks