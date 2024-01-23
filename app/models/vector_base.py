# app/models/vector_base.py

from langchain.vectorstores import FAISS

class VectorBase:
    def __init__(self, embeddings_model):
        self.embeddings_model = embeddings_model
        self.vector_store = None

    def create_vector_base(self, documents):
        embeddings = [self.embeddings_model.generate_embeddings(doc) for doc in documents]
        self.vector_store = FAISS(embeddings)

    def search_similar_vectors(self, query_embedding, top_k=5):
        if self.vector_store is None:
            print("Vector base is not initialized.")
            return []

        return self.vector_store.search(query_embedding, top_k=top_k)
