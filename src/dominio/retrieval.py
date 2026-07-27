from src.config import TOP_K
from src.infraestrutura.embedding_provider import EmbeddingProvider
from src.infraestrutura.vector_store import VectorStore


class Retrieval:
    def __init__(self, embedding_provider: EmbeddingProvider, vector_store: VectorStore):
        self._embedding_provider = embedding_provider
        self._vector_store = vector_store

    def buscar(
        self,
        pergunta: str,
        top_k: int = TOP_K,
        limiar_distancia: float | None = None,
    ) -> list[dict]:
        embedding_pergunta = self._embedding_provider.embed([pergunta], input_type="query")[0]
        resultado_bruto = self._vector_store.buscar(embedding_pergunta, top_k)

        documentos = resultado_bruto["documents"][0]
        metadados = resultado_bruto["metadatas"][0]
        distancias = resultado_bruto["distances"][0]

        resultados = [
            {
                "texto": texto,
                "documento": meta["documento"],
                "secao": meta["secao"],
                "distancia": distancia,
            }
            for texto, meta, distancia in zip(documentos, metadados, distancias)
        ]

        if limiar_distancia is not None:
            resultados = [r for r in resultados if r["distancia"] <= limiar_distancia]

        return resultados
