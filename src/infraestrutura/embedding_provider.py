from abc import ABC, abstractmethod

import voyageai

from src.config import EMBEDDING_MODEL, VOYAGE_API_KEY


class EmbeddingProvider(ABC):
    @abstractmethod
    def embed(self, textos: list[str], input_type: str = "document") -> list[list[float]]:
        pass


class VoyageProvider(EmbeddingProvider):
    """Usa o modelo voyage-3.5 via API da Voyage AI."""

    def __init__(self, modelo: str = EMBEDDING_MODEL):
        self._client = voyageai.Client(api_key=VOYAGE_API_KEY)
        self._modelo = modelo

    def embed(self, textos: list[str], input_type: str = "document") -> list[list[float]]:
        resultado = self._client.embed(textos, model=self._modelo, input_type=input_type)
        return resultado.embeddings


# Arquitetura preparada para embeddings locais (ex.: sentence-transformers), sem implementação na v1.
