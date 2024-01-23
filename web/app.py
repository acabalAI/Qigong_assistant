# web/app.py

import streamlit as st
from app.chatbot import Chatbot
from app.data_loader import DataLoader
from app.config import OPENAI_API_KEY
from streamlit_utils import display_conversation

def main():
    st.title("Qigong Assistant Chatbot")

    # Initialize the DataLoader and load & process the data
    data_loader = DataLoader("./data/Database.xlsx")
    documents = data_loader.load_and_process()

    # Initialize the Chatbot
    chatbot = Chatbot(OPENAI_API_KEY)
    chatbot.generate_embeddings_and_vector_base(documents)

    # User input
    user_input = st.text_input("Ask me anything about Qigong:", key="user_input")

    if user_input:
        with st.spinner('Thinking...'):
            # Generate response from the chatbot
            conversation_history = st.session_state.get("conversation_history", [])
            response = chatbot.generate_response(user_input, conversation_history)
            
            # Update conversation history
            conversation_history.append((user_input, response))
            st.session_state["conversation_history"] = conversation_history

            # Display the conversation
            display_conversation(conversation_history)

if __name__ == "__main__":
    main()

