# Research Paper Question Answering System

This project is a small document question answering system and it was built using Python,Langchain,Groq API and Streamlit

In this  Project we have used two research papers as a  DataSource provided by DKAI TECH  hiring team as the part of task.  
The system reads these PDF's and allows the user to ask questions  related to thier content , Our Goal is to allow the user to ask question about the research paper and retrieve the information from the text inside the PDF

# WORKFLOW -:

    1.  Loads research papers in PDF format
	2.	Extracts the text from those PDFs
	3.	Splits the text into smaller chunks
	4.	Converts those chunks into embeddings
	5.	Stores the embeddings in a Chroma vector database
	6.	Retrieves the most relevant chunks when a question is asked
	7.	Uses a language model to generate an answer based on that context

    The user interacts with the System through a streamlit web interface where questions can be entered.


# ARCHITECTURE-:

PDF Documents
      ↓
Text Extraction
      ↓
Chunking
      ↓
Embeddings
      ↓
Chroma Vector Database
      ↓
Retriever
      ↓
LLM (Groq)
      ↓
Streamlit Interface



# Technology used :->


    PYTHON
    LangChain
    Groq API
    Chroma Vector database
    Sentence Transformers 
    Streamlit 
 




## Dependency 

All required dependencies are listed in requirements.txt



## How to Run the Project

Follow these steps to run the project on your system.

### 1. Clone the repository

git clone https://github.com/Prayagxraj/research-paper-qa-system.git

### 2. Navigate to the project directory

cd research-paper-qa-system

### 3. Create a virtual environment

python -m venv venv

### 4. Activate the virtual environment

Mac :
source venv/bin/activate

Windows:

venv\Scripts\activate

### 5. Install the required dependencies

pip install -r requirements.txt

## 6 Environment Variable

This project requires a Groq API key.
Before running the application, set the environment variable:

GROQ_API_KEY="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"

### 7. Run the Streamlit application

streamlit run app.py

After running the command, the Streamlit interface will open in the browser where users can ask questions related to the research papers.


