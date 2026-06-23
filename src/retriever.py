"""
Retriever module – FAISS-based semantic search.
"""
import os
import pickle
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

class Retriever:
    def init(self, index_path="data/vector_store/full_faiss_index.bin",
                 metadata_path="data/vector_store/full_metadata.pkl",
                 model_name="all-MiniLM-L6-v2"):
        self.index = faiss.read_index(index_path)
        with open(metadata_path, "rb") as f:
            self.metadata = pickle.load(f)
        self.model = SentenceTransformer(model_name, device="cuda" if import('torch').cuda.is_available() else "cpu")

    def retrieve(self, query, top_k=5):
        q_emb = self.model.encode(query, normalize_embeddings=True).astype('float32').reshape(1, -1)
        distances, indices = self.index.search(q_emb, top_k)
        results = []
        for i, idx in enumerate(indices[0]):
            results.append({
                'score': float(distances[0][i]),
                'complaint_id': self.metadata['complaint_ids'][idx],
                'product': self.metadata['products'][idx],
                'chunk_text': self.metadata['chunk_texts'][idx],
                'chunk_index': self.metadata['chunk_indices'][idx]
            })
        return results
