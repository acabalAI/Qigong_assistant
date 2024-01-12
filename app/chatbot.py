from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
import streamlit as st
from utils import template
from data_loader import *

class Chatbot:
    def __init__(self, api_key):
        self.openai_api_key = api_key
        self.llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=api_key)
        self.embed_model = OpenAIEmbeddings(model="text-embedding-ada-002")
        data_loader=DataLoader("./data/Database.xlsx")
        self.documents=data_loader.load_and_process()
        
    def generate_embeddings(self):
        
        text_splitter = CharacterTextSplitter(separator="\n", chunk_size=700, chunk_overlap=200, length_function=len)
        docs_split = text_splitter.split_text(self.documents)

        # Create embeddings and search for relevant context
        self.vector_base = FAISS.from_texts(docs_split, self.embed_model)
    
        
        
        # Additional initializations if necessary

    def generate_response(self, user_query,history):
        """
        Generates a response to the user query based on the given context.

        :param user_query: The query from the user.
        :param context: The context or background information for the query.
        :return: Generated response.
        """
        # Split the context text for embedding
        relevant_context = self.vector_base.similarity_search(user_query)
        print(relevant_context)

        # Generate a response using the language model
        prompt_template = PromptTemplate(template=template, input_variables=["query", "context","history"])
        llm_chain = LLMChain(prompt=prompt_template, llm=self.llm)

        response = llm_chain.run({'query': user_query, 'context': relevant_context,'history':history})
        return response
