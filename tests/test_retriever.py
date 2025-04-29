# test_retriever.py

from components.vectorstore import create_vectorstore
from components.retriever import create_retriever

# Sample dummy chunks
chunks = [
    "The Eiffel Tower is located in Paris.",
    "The Great Wall of China is one of the wonders of the world.",
    "The Taj Mahal is a famous monument in India.",
    "Mount Everest is the highest mountain in the world."
]

print("Creating vectorstore...")
vectorstore = create_vectorstore(chunks)
print("Vectorstore created successfully!")

print("Creating retriever...")
retriever = create_retriever(vectorstore,"mmr",2)
print("Retriever created successfully!")

# Test a sample query
query = "Where is the Eiffel Tower?"
retrieved_docs = retriever.invoke(query)

print("\nRetrieved Documents:")
for i, doc in enumerate(retrieved_docs):
    print(f"{i+1}. {doc.page_content}")
