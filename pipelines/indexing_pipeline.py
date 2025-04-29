# pipelines/indexing_pipeline.py
from components.document_loader import document_loader
from components.text_splitter import text_splitter
from components.vectorstore import create_vectorstore
from components.retriever import create_retriever
from utils.file_utils import clear_vectorstore
from langchain_core.vectorstores import VectorStoreRetriever
from langchain_community.vectorstores.faiss import FAISS
from typing import List
import os
import pickle

# Directory to persist vectorstores (optional improvement)
STORE_DIR = "./vectorstores" 
#clear_vectorstore(STORE_DIR)
os.makedirs(STORE_DIR, exist_ok=True)

def indexing_pipeline(urls: List[str], store_name: str = "default") -> VectorStoreRetriever:
    """
    Full pipeline to:
    - Load documents from URL(s)
    - Split text
    - Embed and store in vector store
    - Return a retriever object

    Args:
        urls (List[str]): List of URLs to process
        store_name (str): Name used to save/load the vectorstore

    Returns:
        VectorStoreRetriever: retriever for later querying
    """
    store_path = os.path.join(STORE_DIR, f"{store_name}.pkl")

    # Check if we already have a stored FAISS vectorstore
    if os.path.exists(store_path):
        with open(store_path, "rb") as f:
            vectorstore = pickle.load(f)
    else:
        # 1. Load
        documents = document_loader.invoke(urls)

        # 2. Split
        chunks = text_splitter.invoke(documents)

        # 3. Embed & Store
        vectorstore = create_vectorstore(chunks)

        # 4. Persist the FAISS store
        with open(store_path, "wb") as f:
            pickle.dump(vectorstore, f)

    # 5. Create and return retriever
    return create_retriever(vectorstore)