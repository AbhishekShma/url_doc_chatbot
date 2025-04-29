# URL Document Chatbot
## Overview
The URL Document Chatbot is a retrieval-augmented generation (RAG) application designed to answer user queries based on information fetched from URLs. The chatbot retrieves relevant documents, processes the data, and generates accurate answers using advanced language models like Hugging Face's TinyLlama. The system leverages a sliding memory window for context and uses a vector store for efficient retrieval of relevant documents.

This project showcases the integration of document retrieval, natural language understanding, and conversational AI, making it ideal for information extraction applications in real-world scenarios such as technical support, content summarization, and customer service automation.

## Key Features
**Document Retrieval**: Retrieves documents from provided URLs and uses them to answer user queries.

**Conversation History**: Supports maintaining a history of questions and answers to provide context and improve future responses.

**Retrieval-Augmented Generation**: Combines retrieved document context with language model responses to enhance accuracy and relevance.

**Streamlit Interface**: User-friendly web interface for easy interaction with the chatbot.


## Installation
Prerequisites
To run this application locally, you will need to have Python installed. You can install Python from the official site: https://www.python.org/downloads/.

## Setup Instructions
Clone the repository:

```bash
git clone https://github.com/AbhishekShma/url_doc_chatbot.git
cd url_doc_chatbot
Create and activate a virtual environment (optional but recommended):
```

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
## Install the required dependencies:

```bash
pip install -r requirements.txt
```
Create a .env file in the root of the project and add any necessary environment variables (e.g., Hugging Face tokens).

## Run the Streamlit app:

```bash
streamlit run app.py
```
Open the app in your web browser (default: http://localhost:8501).

## How to Use
**Input URLs**: Paste up to 5 URLs (one per line) into the provided text box in the app. The URLs should link to publicly accessible documents or pages that the chatbot can read.

**Ask Questions**: Once the documents are indexed, enter your questions into the text input field. The chatbot will fetch relevant information from the indexed documents and generate a response.

**Chat History**: The app keeps track of your conversation history, allowing you to refer back to previous questions and answers.

## Technologies Used:
**Streamlit**: For building the web interface.

**LangChain**: For chaining together models, retrievers, and other components in the QA pipeline.

**Hugging Face**: For providing pre-trained models like TinyLlama.

**Python**: Primary programming language used for the application.

## Testing
The project includes a suite of unit tests for various components to ensure correctness and functionality.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.