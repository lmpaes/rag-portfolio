from abc import ABC, abstractmethod

import anthropic

from src.config import ANTHROPIC_API_KEY, LLM_MODEL


class LLMProvider(ABC):
    @abstractmethod
    def gerar_resposta(self, prompt_sistema: str, contexto: str, pergunta: str) -> str:
        pass


class ClaudeProvider(LLMProvider):
    """Usa o modelo Haiku 4.5 via API da Anthropic."""

    def __init__(self, modelo: str = LLM_MODEL):
        self._client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
        self._modelo = modelo

    def gerar_resposta(self, prompt_sistema: str, contexto: str, pergunta: str) -> str:
        mensagem_usuario = (
            f"<documentos_relevantes>\n{contexto}\n</documentos_relevantes>\n"
            f"<pergunta>\n{pergunta}\n</pergunta>"
        )
        resposta = self._client.messages.create(
            model=self._modelo,
            max_tokens=1024,
            system=prompt_sistema,
            messages=[{"role": "user", "content": mensagem_usuario}],
        )
        return next(bloco.text for bloco in resposta.content if bloco.type == "text")


# Arquitetura preparada para um OllamaProvider (LLM local), sem implementação na v1.
