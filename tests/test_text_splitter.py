

from components.text_splitter import text_splitter

result = text_splitter.invoke(["""Splits documents into smaller chunks using LangChain's RecursiveCharacterTextSplitter.
    
    Args:
        texts (List[str]): The list of text documents to be split.
        chunk_size (int): The size of each chunk.
        overlap (int): The number of overlapping characters between consecutive chunks.
        
    Returns:
        List[str]: A list of text chunks."""])

print(result[0])