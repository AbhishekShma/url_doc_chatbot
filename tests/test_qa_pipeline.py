from pipelines.qa_pipeline import qa_pipeline
from pipelines.indexing_pipeline import indexing_pipeline

def test_qa_pipeline():
    # Sample input
    urls = ["https://www.theguardian.com/world/live/2025/apr/29/spain-portugal-power-cut-outage-barcelona-madrid-europe-latest-live-news"]
    store_name = "test_store"
    query = "What happened in spain on 28 april 2025?"

    # Step 1: Get the retriever using indexing_pipeline
    retriever = indexing_pipeline(urls, store_name)

    if not retriever:
        print("Failed to create retriever.")
        return

    # Step 2: Initialize an empty chat history for the test
    chat_history = []

    # Step 3: Run QA pipeline with retriever and chat history
    response = qa_pipeline(retriever=retriever, query=query)

    # Step 4: Show result
    print("\nLLM Response:")
    print(response if response else "No response generated.")

    # Optionally, assert a response to check the correctness
    assert response, "No response generated"

    # You could also add more tests here, such as verifying the format of the answer.

# Run the test
test_qa_pipeline()
