# app/agents/dialogue_agent.py

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

class DialogueAgent:
    def __init__(self, client):
        self.client = client
        self.dialogue_prompt = """ You are an dialogue agent, you will be provided with a query {query} and the context {context} as well as and the relevant history of the conversation {relevant_memory}
        you will answer the query exclusively from the information provided in the context and use the
        history of the conversation to follow up the dialogue thread and make sure it is aligned.
        Before launching the response make sure all your reply is contained in the context and it is aligned with the previous conversation
        your response can only be based on the context provided, if the question is not found in the context, you say that you dont have the necessary information
        """
        self.prompt_template = PromptTemplate(template=self.dialogue_prompt, input_variables=["query", "relevant_memory", "context"])
        self.llm_chain = LLMChain(prompt=self.prompt_template, llm=self.client)

    def generate_response(self, query, relevant_memory, context):
        try:
            response = self.llm_chain.run({'query': query, 'relevant_memory': relevant_memory, 'context': context})
            return response
        except Exception as e:
            print(f"Error in DialogueAgent: {e}")
            return "I'm unable to respond at the moment."
