from core.pdf_reader import load_pdfs
from core.chunker import split_documents
from core.embedding import get_embedding_model
from core.search_index import create_vector_store
from core.answerengine import create_qa_chain



documents = load_pdfs()


chunks = split_documents(documents)

embedding_model = get_embedding_model()


vector_store = create_vector_store(chunks, embedding_model)


llm, retriever = create_qa_chain(vector_store)


query = "What are reasoning models?"


retrieved_docs = retriever.invoke(query)


context = "\n\n".join(doc.page_content for doc in retrieved_docs)

prompt = f"""
Answer the question using the context below.

Context:
{context}

Question:
{query}
"""


response = llm.invoke(prompt)

print("\nAnswer:\n")
print(response.content)