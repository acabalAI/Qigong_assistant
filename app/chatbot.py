# app/chatbot.py

from services.openai_service import OpenAIService
from agents.memory_agent import MemoryAgent
from agents.dialogue_agent import DialogueAgent
from agents.revision_agent import RevisionAgent
from models.embeddings import EmbeddingModel
from models.vector_base import VectorBase
from utils.text_utils import split_text_into_chunks
from config import OPENAI_API_KEY

class Chatbot:
    def __init__(self, api_key=OPENAI_API_KEY):
        self.openai_service = OpenAIService(api_key)
        self.embedding_model = EmbeddingModel(model_name="text-embedding-ada-002")
        self.vector_base = VectorBase(self.embedding_model)

        # Initialize agents
        self.memory_agent = MemoryAgent(self.openai_service)
        self.dialogue_agent = DialogueAgent(self.openai_service)
        self.revision_agent = RevisionAgent(self.openai_service)

    def generate_embeddings_and_vector_base(self, documents):
        """
        Generate embeddings for the documents and create a vector base.

        :param documents: List of documents to be embedded.
        """
        docs_chunks = split_text_into_chunks(' '.join(documents))
        self.vector_base.create_vector_base(docs_chunks)

    def generate_response(self, user_query, conversation_history):
        """
        Generates a response to the user query.

        :param user_query: The query from the user.
        :param conversation_history: The conversation history for context.
        :return: Generated response.
        """
        try:
            # Retrieve relevant context and memory
            relevant_context = self.vector_base.search_similar_vectors(self.embedding_model.generate_embeddings(user_query))
            relevant_memory = self.memory_agent.retrieve_memory(user_query, conversation_history)

            # Generate dialogue response
            response_tmp = self.dialogue_agent.generate_response(user_query, relevant_memory, relevant_context)
            
            # Revise the response
            response = self.revision_agent.revise_response(user_query, relevant_context, response_tmp)

            return response
        except Exception as e:
            print(f"Error in generating response: {e}")
            return "Sorry, I'm unable to process your request right now."

    # Additional methods for chatbot functionalities can be added here
