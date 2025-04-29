from components.chatting_model import create_chat_model
from langchain_core.messages import HumanMessage
from langchain_core.vectorstores import VectorStoreRetriever
from utils.response_utils import format_llm_output


def qa_pipeline(
    retriever: VectorStoreRetriever,
    query: str,
    chat_history: list = None,
    model_id: str = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
) -> str:
    """
    Takes a retriever and a user query, runs retrieval-augmented generation with optional chat history.
    """
    # Step 1: Retrieve relevant chunks
    docs = retriever.invoke(query)
    context = "\n\n".join([doc.page_content for doc in docs])

    # Step 2: Construct chat history as text
    chat_context = ""
    if chat_history:
        for qa in chat_history[-5:]:  # last 5 interactions for context
            chat_context += f"User: {qa['question']}\nAssistant: {qa['answer']}\n"

    # Step 3: Combine everything into prompt
    full_prompt = f"""
    You are a helpful assistant. Answer the question based on the context below.

    Chat History:
    {chat_context}
    -------------End of chat history-----------------------
    Context:
    {context}
    -------------Context ends here ------------------------

    Question to answer, may or may not use the above context:
    {query}
    """

    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": full_prompt}
    ]

    chat_model = create_chat_model(model_id)
    response = chat_model.invoke(messages)

    return format_llm_output(response.content)
