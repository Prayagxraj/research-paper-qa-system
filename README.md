This project is a small document question answering system and it was built using Python,Langchain,Groq API and Streamlit

In this  Project we have used two research papers as a  DataSource provided by DKAI TECH  hiring team as the part of task.  
The system reads these PDF's and allows the user to ask questions  related to thier content , Our Goal is to allow the user to ask question about the research paper and retrieve the information from the text inside the PDF

FLOWCHART-:

    1.  Loads research papers in PDF format
	2.	Extracts the text from those PDFs
	3.	Splits the text into smaller chunks
	4.	Converts those chunks into embeddings
	5.	Stores the embeddings in a Chroma vector database
	6.	Retrieves the most relevant chunks when a question is asked
	7.	Uses a language model to generate an answer based on that context

    The user interacts with the System through a streamlit web interface where questions can be entered.


    Technology used :->
    PYTHON
    LangChain
    Groq API
    Chroma Vector database
    Sentence Transformers 
    Streamlit 
 


 Full line by line explanation of this Project with working Youtube Link -> 


## Dependency Management

All required dependencies are listed in `requirements.txt`.
The file was generated from the project virtual environment using the following command:
pip freeze > requirements.txt