#utils/file_utils.py

import os
import shutil

def clear_vectorstore(dir_path: str):
    """
    Deletes the FAISS vector store directory if it exists.

    Args:
        dir_path (str): Path to the vector store directory.
    """
    if os.path.exists(dir_path):
        shutil.rmtree(dir_path)
        print(f"[INFO] Cleared existing vector store at: {dir_path}")

#clear_vectorstore("./vectorstores")