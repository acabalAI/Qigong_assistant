# app/agents/revision_agent.py

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

class RevisionAgent:
    def __init__(self, client):
        self.client = client
        self.revision_prompt = """ you are an agent charged with ensuring that the output provided by the system is aligned with the context provided,
        for that you will be provided with a user input {query} and a context {context} and an intermediate response {intermediate_response},
        you will modify the intermediate response to make sure it is aligned with the query and contains exclusively information provided by the context
        """
        self.prompt_template = PromptTemplate(template=self.revision_prompt, input_variables=["query", "context", "intermediate_response"])
        self.llm_chain = LLMChain(prompt=self.prompt_template, llm=self.client)

    def revise_response(self, query, context, intermediate_response):
        try:
            revised_response = self.llm_chain.run({'query': query, "context": context, "intermediate_response": intermediate_response})
            return revised_response
        except Exception as e:
            print(f"Error in RevisionAgent: {e}")
            return "I'm unable to refine the response at the moment."
