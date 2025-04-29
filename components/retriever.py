# components/retriever.py
from langchain_core.vectorstores import VectorStoreRetriever
from langchain_community.vectorstores.faiss import FAISS

def create_retriever(vectorstore: FAISS, search_type: str = "mmr", k: int = 5) -> VectorStoreRetriever:
    retriever = vectorstore.as_retriever(
        search_type=search_type,
        search_kwargs={"k": k}
    )
    return retriever