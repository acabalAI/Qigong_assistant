# app/models/embeddings.py

from langchain.embeddings import OpenAIEmbeddings

class EmbeddingModel:
    def __init__(self, model_name):
        self.model = OpenAIEmbeddings(model=model_name)

    def generate_embeddings(self, text):
        try:
            return self.model.embed_text(text)
        except Exception as e:
            print(f"Error in generating embeddings: {e}")
            return None
