import chromadb

from src.config import CHROMA_COLLECTION_NAME, CHROMA_PERSIST_DIR


class VectorStore:
    """Wrapper do ChromaDB embarcado (sem servidor externo)."""

    def __init__(self, collection_name: str = CHROMA_COLLECTION_NAME):
        self._client = chromadb.PersistentClient(path=str(CHROMA_PERSIST_DIR))
        self._collection = self._client.get_or_create_collection(name=collection_name)

    def adicionar(
        self,
        ids: list[str],
        embeddings: list[list[float]],
        documentos: list[str],
        metadados: list[dict],
    ) -> None:
        self._collection.add(
            ids=ids,
            embeddings=embeddings,
            documents=documentos,
            metadatas=metadados,
        )

    def buscar(self, embedding_query: list[float], top_k: int) -> dict:
        return self._collection.query(
            query_embeddings=[embedding_query],
            n_results=top_k,
        )

    def limpar(self) -> None:
        nome = self._collection.name
        self._client.delete_collection(name=nome)
        self._collection = self._client.get_or_create_collection(name=nome)
