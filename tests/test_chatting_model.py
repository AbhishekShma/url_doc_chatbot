from components.chatting_model import create_chat_model

def test_chat_model_response():
    # Test with a valid model ID
    model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
    try:
        # Create the chat model
        chat_model = create_chat_model(model_id)
        
        # Define a prompt using the ChatML format
        prompt = """
        <|system|> You are a helpful assistant. <|user|> What happened in Spain and Portugal on 20 April 2025? <|assistant|>
        """
        
        # Get the model response
        response = chat_model.invoke(prompt)
        
        # Extract only the assistant's reply (the last part after <|assistant|>)
        assistant_reply = response.content.strip()  # Remove any leading/trailing whitespace
        
        # Print the assistant's response
        print(f"Assistant's response: {assistant_reply}")
        
    except Exception as e:
        print(f"Error during testing: {e}")

# Run the test
test_chat_model_response()
