from components.document_loader import document_loader
from components.text_splitter import text_splitter
from components.vectorstore import create_vectorstore
from components.retriever import create_retriever

# Step 1: Load documents from a list of URLs
urls = [
    "https://www.cssoftsolutions.com/"
]
documents = document_loader.invoke(urls)

# Step 2: Split the loaded documents into smaller chunks
chunks = text_splitter.invoke(documents)

# Step 3: Create a vector store from the document chunks
vectorstore = create_vectorstore(chunks)

# Step 4: Create a retriever from the vector store
retriever = create_retriever(vectorstore,"similarity",20)

# Step 5: Test the retriever with a sample query
query = "Tell me about csSoftSolutions."
retrieved_documents = retriever.invoke(query)

# Output the retrieved documents to see if it matches expectations
print("Retrieved Documents:")
for doc in retrieved_documents:
    print(f"--------------Document----------------: \n{doc.page_content}\n\n")  # Print the text of each retrieved document

