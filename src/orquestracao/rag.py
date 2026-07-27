from src.dominio.prompt_builder import PROMPT_SISTEMA_FUNCIONARIO, montar_contexto
from src.dominio.retrieval import Retrieval
from src.infraestrutura.embedding_provider import VoyageProvider
from src.infraestrutura.llm_provider import ClaudeProvider
from src.infraestrutura.vector_store import VectorStore


class RAG:
    """Camada de orquestração: única porta de entrada usada pela interface."""

    def __init__(self):
        embedding_provider = VoyageProvider()
        vector_store = VectorStore()
        self._retrieval = Retrieval(embedding_provider, vector_store)
        self._llm = ClaudeProvider()

    def responder(self, pergunta: str) -> dict:
        resultados = self._retrieval.buscar(pergunta)
        contexto = montar_contexto(resultados)
        resposta = self._llm.gerar_resposta(PROMPT_SISTEMA_FUNCIONARIO, contexto, pergunta)

        fontes = []
        vistos = set()
        for resultado in resultados:
            chave = (resultado["documento"], resultado["secao"])
            if chave not in vistos:
                vistos.add(chave)
                fontes.append({"documento": resultado["documento"], "secao": resultado["secao"]})

        return {"resposta": resposta, "fontes": fontes}
