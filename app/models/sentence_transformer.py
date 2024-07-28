import numpy as np
from typing import List, Union, Any, Tuple
from sentence_transformers import SentenceTransformer
from pydantic import BaseModel, Field

class SentenceTransformerWrapper(BaseModel):
    """
    A wrapper class for SentenceTransformer with additional utility methods.
    """
    model: Any = Field(default_factory=lambda: SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2"))
    
    class Config:
        arbitrary_types_allowed = True
    
    def __init__(self, model_name: str = 'sentence-transformers/all-MiniLM-L6-v2'):
        """
        Initialize the SentenceTransformerWrapper.

        Args:
            model_name (str): The name of the pre-trained model to use.
        """
        super().__init__()
        self.model = SentenceTransformer(model_name)
    
    def encode(self, sentences: Union[str, List[str]], batch_size: int = 32) -> np.ndarray:
        """
        Encode the input sentence(s) into embeddings.

        Args:
            sentences (Union[str, List[str]]): The input sentence(s) to encode.
            batch_size (int): The batch size for encoding.

        Returns:
            np.ndarray: The encoded embeddings.
        """
        return self.model.encode(sentences, batch_size=batch_size)

    def cosine_similarity(self, embedding1: np.ndarray, embedding2: np.ndarray) -> float:
        """
        Calculate the cosine similarity between two embeddings.

        Args:
            embedding1 (np.ndarray): The first embedding.
            embedding2 (np.ndarray): The second embedding.

        Returns:
            float: The cosine similarity between the two embeddings.
        """
        return np.dot(embedding1, embedding2) / (np.linalg.norm(embedding1) * np.linalg.norm(embedding2))

    def find_most_similar(self, query: str, corpus: List[str]) -> Tuple[str, float]:
        """
        Find the most similar sentence in the corpus to the query.

        Args:
            query (str): The query sentence.
            corpus (List[str]): The list of sentences to compare against.

        Returns:
            Tuple[str, float]: The most similar sentence and its similarity score.
        """
        query_embedding = self.encode(query)
        corpus_embeddings = self.encode(corpus)
        similarities = [self.cosine_similarity(query_embedding, ce) for ce in corpus_embeddings]
        most_similar_idx = np.argmax(similarities)
        return corpus[most_similar_idx], similarities[most_similar_idx]

    def get_embedding_dimension(self) -> int:
        """
        Get the dimension of the sentence embeddings.

        Returns:
            int: The dimension of the sentence embeddings.
        """
        return self.model.get_sentence_embedding_dimension()

    def normalize_embedding(self, embedding: np.ndarray) -> np.ndarray:
        """
        Normalize the input embedding to unit length.

        Args:
            embedding (np.ndarray): The input embedding.

        Returns:
            np.ndarray: The normalized embedding.
        """
        return embedding / np.linalg.norm(embedding)

    def batch_cosine_similarity(self, embeddings1: np.ndarray, embeddings2: np.ndarray) -> np.ndarray:
        """
        Calculate cosine similarities between two sets of embeddings.

        Args:
            embeddings1 (np.ndarray): The first set of embeddings.
            embeddings2 (np.ndarray): The second set of embeddings.

        Returns:
            np.ndarray: A matrix of cosine similarities.
        """
        normalized_embeddings1 = np.array([self.normalize_embedding(e) for e in embeddings1])
        normalized_embeddings2 = np.array([self.normalize_embedding(e) for e in embeddings2])
        return np.dot(normalized_embeddings1, normalized_embeddings2.T)