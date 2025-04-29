# tests/test_indexing_pipeline.py
from pipelines.indexing_pipeline import indexing_pipeline
from components.retriever import create_retriever

def test_indexing_pipeline():
    # Provide sample URLs to index
    urls = [
        "https://www.cssoftsolutions.com/"
    ]
    
    # Run the indexing pipeline
    store_name = "test_store"
    vectorstore_retriever = indexing_pipeline(urls, store_name)
    
    # Check if the vectorstore retriever is created
    if vectorstore_retriever:
        print("Vectorstore retriever created successfully!")
    else:
        print("Failed to create vectorstore retriever.")
    
    # Now you can query the retriever
    query = "What is cssoftsolutions?"
    retrieved_docs = vectorstore_retriever.invoke(query)
    
    if retrieved_docs:
        print(f"Documents retrieved for query '{query}':")
        for doc in retrieved_docs:
            print(f"-----------------Document-------------:\n{doc}\n\n")
    else:
        print("No documents retrieved.")

# Run the test
test_indexing_pipeline()
