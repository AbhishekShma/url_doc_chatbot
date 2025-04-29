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
    
    # models
    from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

    #model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
    model_id = "meta-llama/Llama-3.2-3B-Instruct"

    tokenizer = AutoTokenizer.from_pretrained(model_id)


    print(tokenizer.chat_template is not None)


    if tokenizer.pad_token is None:
        tokenizer.add_special_tokens({'pad_token': '[PAD]'})

    model = AutoModelForCausalLM.from_pretrained(model_id)
    model.resize_token_embeddings(len(tokenizer))  # only needed if fine-tuning

    text_pipeline = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        device=-1,
        pad_token_id=tokenizer.pad_token_id,
        max_length=1024,
        temperature=0.7,
        truncation=True

    )

    llm = HuggingFacePipeline(pipeline=text_pipeline)
    chat_model = ChatHuggingFace(llm=llm)


    return chat_model