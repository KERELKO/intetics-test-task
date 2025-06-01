import openai
import numpy as np

from app.types import QuestionAnswer


def cosine_similarity(vec1: list[float], vec2: list[float]) -> float:
    """
    Compute the cosine similarity between two vectors.

    Args:
        vec1 (list[float]): The first vector.
        vec2 (list[float]): The second vector.

    Returns:
        float: The cosine similarity between vec1 and vec2.
    """
    np_array_1 = np.array(vec1)
    np_array_2 = np.array(vec2)
    return np.dot(
        np_array_1, np_array_2
    ) / (np.linalg.norm(np_array_1) * np.linalg.norm(np_array_2))


class EmbeddingService:
    """
    A service for generating and processing text embeddings using OpenAI models.
    """

    def __init__(self, model: str):
        self.emb_model = model

    def build_embedding_list(self, data: list[QuestionAnswer]) -> list[list[float]]:
        """
        Generate embeddings for a list of question-answer objects.

        Args:
            data (list[QuestionAnswer]): A list of question-answer dictionaries,
                                         each containing a 'question' field.

        Returns:
            list[list[float]]: A list of embedding vectors corresponding to the input questions.
        """
        result = []
        for d in data:
            embedding = openai.embeddings.create(
                input=d['question'], model=self.emb_model,
            ).data[0].embedding
            result.append(embedding)
        return result

    def query_embedding(self, input: str) -> list[float]:
        """
        Generate an embedding vector for a given input string.

        Args:
            input (str): The input text to embed.

        Returns:
            list[float]: The embedding vector for the input text.
        """
        embedding = openai.embeddings.create(
            input=input, model=self.emb_model,
        ).data[0].embedding
        return embedding

    def find_top_k_indices(
        self, query_embedding: list[float], embedding_list: list[list[float]], k: int = 3,
    ) -> list[int]:
        """
        Find the indices of the top-k most similar embeddings to a query embedding.

        Args:
            query_embedding (list[float]): The embedding vector of the query.
            embedding_list (list[list[float]]): A list of embedding vectors to compare against.
            k (int, optional): The number of top similar items to return. Defaults to 3.

        Returns:
            list[int]: The indices of the top-k most similar embeddings.
        """
        similarities = [cosine_similarity(query_embedding, emb) for emb in embedding_list]
        return list(map(lambda x: int(x), sorted(similarities, reverse=True)[:k]))
