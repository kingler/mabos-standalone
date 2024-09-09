from typing import Any, List, Union

import numpy as np
from pydantic import BaseModel, Field
from sentence_transformers import SentenceTransformer


class SentenceTransformerWrapper(BaseModel):
    model: Any = Field(default_factory=lambda: SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2"))
    
    class Config:
        arbitrary_types_allowed = True
    
    def __init__(self, model_name: str = 'sentence-transformers/all-MiniLM-L6-v2'):
        super().__init__()
        self.model = SentenceTransformer(model_name)
    
    def encode(self, sentences: Union[str, List[str]], batch_size: int = 32) -> np.ndarray:
        return self.model.encode(sentences, batch_size=batch_size)

    def cosine_similarity(self, embedding1: np.ndarray, embedding2: np.ndarray) -> float:
        return np.dot(embedding1, embedding2) / (np.linalg.norm(embedding1) * np.linalg.norm(embedding2))

    def find_most_similar(self, query: str, corpus: List[str]) -> tuple:
        query_embedding = self.encode(query)
        corpus_embeddings = self.encode(corpus)
        similarities = [self.cosine_similarity(query_embedding, ce) for ce in corpus_embeddings]
        most_similar_idx = np.argmax(similarities)
        return corpus[most_similar_idx], similarities[most_similar_idx]

    def get_embedding_dimension(self) -> int:
        return self.model.get_sentence_embedding_dimension()