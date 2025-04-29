# components/vectorstore.py

from langchain_community.vectorstores.faiss import FAISS
from components.embeddings_model import embedding_model  # <-- using wrapped object

def create_vectorstore(chunks):
    """
    Create a FAISS vector store from a list of document chunks.

    Args:
        chunks (List[str]): 
            The list of document text chunks to be embedded and stored.

    Returns:
        vectorstore (FAISS): 
            A FAISS vector store populated with embeddings and documents.
    """
    # Use FAISS.from_texts - embeds and builds index automatically
    vectorstore = FAISS.from_texts(
        texts=chunks,
        embedding=embedding_model
    )
    return vectorstore
