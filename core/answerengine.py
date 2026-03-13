from langchain_groq import ChatGroq
import os


def create_qa_chain(vector_store):
    """
    Create QA system using Groq LLM + vector retriever
    """

    llm = ChatGroq(
     model="llama-3.1-8b-instant",
        api_key=os.getenv("GROQ_API_KEY"),
        temperature=0.2
    )

    retriever = vector_store.as_retriever(
        search_kwargs={"k": 4}
    )

    return llm, retriever