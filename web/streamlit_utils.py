# web/streamlit_utils.py

import streamlit as st

def display_conversation(conversation_history):
    """
    Displays the conversation history in the Streamlit app.

    :param conversation_history: A list of tuples (user_input, bot_response).
    """
    for user_input, bot_response in conversation_history:
        st.text_area("You:", user_input, height=75)
        st.text_area("Qigong Assistant:", bot_response, height=75)
