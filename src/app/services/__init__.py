import openai
import numpy as np

from app.types import QuestionAnswer


def cosine_similarity(vec1: list[float], vec2: list[float]):
    np_array_1 = np.array(vec1)
    np_array_2 = np.array(vec2)
    return np.dot(
        np_array_1, np_array_2
    ) / (np.linalg.norm(np_array_1) * np.linalg.norm(np_array_2))


class EmbeddingService:
    def __init__(self, model: str):
        self.emb_model = model

    def build_embedding_list(self, data: list[QuestionAnswer]) -> list[list[float]]:
        result = []
        for d in data:
            embedding = openai.embeddings.create(
                input=d['question'], model=self.emb_model,
            ).data[0].embedding
            result.append(embedding)
        return result

    def query_embedding(self, input: str) -> list[float]:
        embedding = openai.embeddings.create(
            input=input, model=self.emb_model,
        ).data[0].embedding
        return embedding

    def find_top_k_indices(
        self, query_embedding: list[float], embedding_list: list[list[float]], k: int = 3,
    ) -> list[int]:
        similarities = [cosine_similarity(query_embedding, emb) for emb in embedding_list]
        return list(map(lambda x: int(x), sorted(similarities, reverse=True)[:k]))
