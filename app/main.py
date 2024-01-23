# app/main.py

import streamlit as st
from chatbot import Chatbot
from data_loader import DataLoader
from config import OPENAI_API_KEY

def main():
    # Initialize the DataLoader and load & process the data
    data_loader = DataLoader("./data/Database.xlsx")
    documents = data_loader.load_and_process()

    # Initialize the Chatbot
    chatbot = Chatbot(OPENAI_API_KEY)
    chatbot.generate_embeddings_and_vector_base(documents)

    # Streamlit Web Interface
    st.title("Qigong Assistant")

    # Chat Interface
    user_input = st.text_input("Your question:", key="user_input")

    if user_input:
        with st.spinner('Generating response...'):
            # Assuming the conversation history is maintained in a session state
            conversation_history = st.session_state.get("conversation_history", [])
            response = chatbot.generate_response(user_input, conversation_history)

            # Update conversation history
            conversation_history.append({"user": user_input, "bot": response})
            st.session_state["conversation_history"] = conversation_history

            # Display the conversation
            for chat in conversation_history:
                st.text_area("You", chat["user"], height=75)
                st.text_area("Qigong Assistant", chat["bot"], height=75)

if __name__ == "__main__":
    main()
