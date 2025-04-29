from langchain_core.runnables import RunnableLambda
from typing import Dict
from components.embeddings_model import embedding_model  # Importing embedding_model from components

# Function to process the query and generate an embedding
def process_query(query: str, embedding_model: RunnableLambda) -> Dict:
    """
    Converts the user query into an embedding using the provided embedding model,
    and returns the original query along with the embedding.
    
    Args:
        query (str): The raw user query.
        embedding_model (RunnableLambda): The embedding model used to generate embeddings.
        
    Returns:
        Dict: A dictionary containing the query and its embedding.
    """
    # Generate the embedding for the query
    query_embedding = embedding_model.invoke([query])
    
    # Return both the embedding and the original query
    return {"query_embedding": query_embedding[0][0], "query": query}

# Wrap the function in a RunnableLambda to make it compatible with Langchain's chain
user_query = RunnableLambda(process_query)
