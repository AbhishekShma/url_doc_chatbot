# components/document_loader.py

from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import WikipediaLoader
from langchain_core.runnables import RunnableLambda
from typing import List

# Function to load and parse content from a single URL using WebBaseLoader
def load_document(url: str) -> str:
    """
    Loads and returns plain text from a URL using LangChain's WebBaseLoader.
    """
    loader = WebBaseLoader(url)
    #loader = WikipediaLoader(url)
    docs = loader.load()  # Returns a list of Document objects
    return docs[0].page_content if docs else ""

# Function to handle a list of URLs
def load_documents(urls: List[str]) -> List[str]:
    """
    Loads and returns plain text contents from a list of URLs using WebBaseLoader.
    """
    docs = []
    for url in urls:
        text = load_document(url)
        docs.append(text)
    return docs

# Wrap the function in a RunnableLambda
document_loader = RunnableLambda(load_documents)
