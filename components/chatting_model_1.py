# components/chatting_model.py

from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from langchain_huggingface import HuggingFacePipeline, ChatHuggingFace

def create_chat_model(model_id: str):
    """
    Creates a HuggingFace chat model using the specified model ID.

    Args:
    - model_id (str): The identifier of the pre-trained model from HuggingFace.

    Returns:
    - ChatHuggingFace: A LangChain chat model ready for use.
    """
    
    tokenizer = AutoTokenizer.from_pretrained(model_id)

    if tokenizer.pad_token is None:
        tokenizer.add_special_tokens({'pad_token': tokenizer.eos_token})
    
    model = AutoModelForCausalLM.from_pretrained(model_id)
    model.resize_token_embeddings(len(tokenizer))

    # Updated to use max_new_tokens instead of max_length
    text_pipeline = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        device=-1,
        pad_token_id=tokenizer.pad_token_id,
        max_new_tokens=512,  # Output size
        temperature=0.7,
        do_sample=True,
    )

    llm = HuggingFacePipeline(pipeline=text_pipeline)
    chat_model = ChatHuggingFace(llm=llm)

    return chat_model

