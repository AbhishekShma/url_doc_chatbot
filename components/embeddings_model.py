# components/embeddings_model.py

from langchain_community.embeddings import HuggingFaceEmbeddings

# Instantiate the model properly wrapped for LangChain
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/paraphrase-MiniLM-L6-v2"
)
