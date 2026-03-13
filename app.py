import streamlit as st
import time

from core.pdf_reader import load_pdfs
from core.chunker import split_documents
from core.embedding import get_embedding_model
from core.search_index import create_vector_store
from core.answerengine import create_qa_chain


st.set_page_config(page_title="Research Paper QA", layout="wide")

st.title("Research Paper Question Answering System")
st.caption("Ask questions based on the  research papers")


st.sidebar.title("Settings")

top_k = st.sidebar.slider(
    "Number of context chunks",
    min_value=1,
    max_value=8,
    value=4
)

show_context = st.sidebar.checkbox("Show retrieved context", value=True)

st.sidebar.markdown("---")
st.sidebar.write("Example questions:")
st.sidebar.write("- What are reasoning models?")
st.sidebar.write("- What is a large language model?")
st.sidebar.write("- What are small language models?")


@st.cache_resource
def initialize_pipeline():

    docs = load_pdfs()

    chunks = split_documents(docs)

    embeddings = get_embedding_model()

    vectordb = create_vector_store(chunks, embeddings)

    llm, retriever = create_qa_chain(vectordb)

    return llm, retriever


llm, retriever = initialize_pipeline()



col1, col2 = st.columns([3,1])

with col1:
    question = st.text_input("Enter your question")

with col2:
    st.info("Ask anything related to the research papers.")



if question:

    start_time = time.time()

    with st.spinner("Searching documents and generating answer..."):

        docs = retriever.invoke(question)

        context = "\n\n".join(d.page_content for d in docs)

        prompt = f"""
Use the following context to answer the question.

Context:
{context}

Question:
{question}
"""

        response = llm.invoke(prompt)

    end_time = time.time()


    
    st.subheader("Answer")
    st.write(response.content)


    
    if show_context:

        with st.expander("Retrieved context"):

            for d in docs[:top_k]:
                st.write("Source:", d.metadata.get("source", "document"))
                st.write(d.page_content[:300])
                st.write("---")


    st.write(" Response time:", round(end_time - start_time, 2), "seconds")