# app.py

import streamlit as st
from pipelines.indexing_pipeline import indexing_pipeline
from pipelines.qa_pipeline import qa_pipeline
from utils.file_utils import clear_vectorstore


# Page config
st.set_page_config(page_title="URL Q&A App", layout="wide")

# Initialize session state
if "retriever" not in st.session_state:
    st.session_state.retriever = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "urls_input" not in st.session_state:
    st.session_state.urls_input = ""

st.title("Ask Questions Based on URLs:")

# --- Step 1: Input URLs ---
st.subheader("Step 1: Paste URLs (1 per line, up to 5):")
urls_input = st.text_area(
    label="",
    value=st.session_state.urls_input,
    height=150,
    placeholder="https://example.com/article\nhttps://another-page.com",
    key="urls_input_box"
)

# Automatically trigger indexing on URL input change
if urls_input != st.session_state.urls_input:
    st.session_state.urls_input = urls_input
    STORE_DIR = "./vectorstores" 
    #clear_vectorstore(STORE_DIR)
    urls = [u.strip() for u in urls_input.splitlines() if u.strip()]
    if not (1 <= len(urls) <= 5):
        st.warning("Please enter 1 to 5 valid URLs.")
        st.session_state.retriever = None
    else:
        with st.spinner("Indexing..."):
            try:
                st.session_state.retriever = indexing_pipeline(urls,store_name = "cs_soft")
                st.success("Documents indexed successfully!")
                st.session_state.chat_history = []
            except Exception as e:
                st.error(f"Indexing failed: {e}")
                st.session_state.retriever = None

# --- Step 2: Q&A Interface ---
if st.session_state.retriever:
    st.subheader("Step 2: Ask a Question")

    user_question = st.text_input("Type your question and hit Enter:")
    if user_question.strip():
        with st.spinner("Generating answer..."):
            try:
                response = qa_pipeline(
                                        retriever=st.session_state.retriever,
                                        query=user_question.strip(),
                                        chat_history=st.session_state.chat_history
                                      )
                st.session_state.chat_history.append({
                    "question": user_question.strip(),
                    "answer": response
                })
            except Exception as e:
                st.error(f"Answering failed: {e}")

# --- Step 3: Chat History ---
if st.session_state.chat_history:
    st.subheader("Chat History")
    for idx, qa in enumerate(reversed(st.session_state.chat_history), 1):
        st.markdown(f"**Q{idx}:** {qa['question']}")
        st.markdown(f"**A{idx}:** {qa['answer']}")
