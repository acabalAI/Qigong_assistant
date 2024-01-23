# app/agents/memory_agent.py

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

class MemoryAgent:
    def __init__(self, client):
        self.client = client
        self.memory_prompt = """ you are an agent that retrieves the relevant part of the conversation {conversation_history} according to the user query {query},
        you will return exclusively those elements of the conversation history which are relevant to the query as a list.
        the content you provide should be included in the conversation history, you should not add anything else to it
        """
        self.prompt_template = PromptTemplate(template=self.memory_prompt, input_variables=["query", "conversation_history"])
        self.llm_chain = LLMChain(prompt=self.prompt_template, llm=self.client)

    def retrieve_memory(self, query, conversation_history):
        try:
            relevant_memory = self.llm_chain.run({'query': query, "conversation_history": conversation_history})
            return relevant_memory
        except Exception as e:
            print(f"Error in MemoryAgent: {e}")
            return []
