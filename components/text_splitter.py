#components/text_splitter.py
from langchain_core.runnables import RunnableLambda
from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List

# Function to split text into smaller chunks using LangChain's RecursiveCharacterTextSplitter
def split_text(texts: List[str], chunk_size: int =1000 , overlap: int = 100) -> List[str]:
    """
    Splits documents into smaller chunks using LangChain's RecursiveCharacterTextSplitter.
    
    Args:
        texts (List[str]): The list of text documents to be split.
        chunk_size (int): The size of each chunk.
        overlap (int): The number of overlapping characters between consecutive chunks.
        
    Returns:
        List[str]: A list of text chunks.
    """
    # Initialize the LangChain RecursiveCharacterTextSplitter
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=overlap,
    )
    
    # Split each document in the list of texts
    chunks = []
    for text in texts:
        document_chunks = text_splitter.split_text(text)  # Split the document into chunks
        chunks.extend(document_chunks)  # Add chunks to the list

    return chunks

# Wrap the function in a RunnableLambda
text_splitter = RunnableLambda(split_text)
