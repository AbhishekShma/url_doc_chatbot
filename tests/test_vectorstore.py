from components.vectorstore import create_vectorstore

# Test data (a list of document chunks)
document_chunks = [
    "This is the first document chunk.",
    "Here is the second document chunk.",
    "This is the third document chunk.",
    "Another document chunk here."
]

# Create the vectorstore
vectorstore = create_vectorstore(document_chunks)

# Print out the vectorstore details to ensure it has been created
print("Vectorstore created successfully!")
print(f"{vectorstore}")