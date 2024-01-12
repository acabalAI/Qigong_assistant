
import streamlit as st

template= """
         You will be provided with a query {query} and the history of the conversation {history}
         and a context {context}
         and will answer the query exclusively from the information provided in the context and use the 
         history to follow up the dialogue thread.
         Before launching the response make sure all your reply is contained in the context
        """
        
def get_conversation_string():
    conversation_string = ""
    for i in range(len(st.session_state['responses'])-1):
        
        conversation_string += "Human: "+st.session_state['requests'][i] + "\n"
        conversation_string += "Bot: "+ st.session_state['responses'][i+1] + "\n"
    return conversation_string