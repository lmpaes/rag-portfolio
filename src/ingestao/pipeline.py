import time
from pathlib import Path

from voyageai.error import RateLimitError

from src.config import DOCUMENTOS_DIR
from src.dominio.chunking import Chunk, chunk_documento, texto_para_embedding
from src.infraestrutura.embedding_provider import VoyageProvider
from src.infraestrutura.vector_store import VectorStore

_EXTENSOES_SUPORTADAS = {".docx", ".pdf", ".md"}

# Conta Voyage sem método de pagamento cadastrado: limite reduzido de 3 RPM / 10K TPM.
# Lotes pequenos com pausa entre chamadas e retry em caso de estouro evitam falha na ingestão.
_LOTE_MAX_CARACTERES = 6000
_PAUSA_ENTRE_LOTES_SEGUNDOS = 25
_PAUSA_RETRY_SEGUNDOS = 65
_MAX_TENTATIVAS = 5


def _embedar_com_retry(embedding_provider: VoyageProvider, lote: list[str]) -> list[list[float]]:
    for tentativa in range(1, _MAX_TENTATIVAS + 1):
        try:
            return embedding_provider.embed(lote, input_type="document")
        except RateLimitError:
            if tentativa == _MAX_TENTATIVAS:
                raise
            time.sleep(_PAUSA_RETRY_SEGUNDOS)
    raise AssertionError("inalcançável")


def _embedar_em_lotes(embedding_provider: VoyageProvider, textos: list[str]) -> list[list[float]]:
    embeddings: list[list[float]] = []
    lote: list[str] = []
    caracteres_no_lote = 0

    def _processar_lote() -> None:
        if lote:
            embeddings.extend(_embedar_com_retry(embedding_provider, lote))

    for texto in textos:
        if lote and caracteres_no_lote + len(texto) > _LOTE_MAX_CARACTERES:
            _processar_lote()
            time.sleep(_PAUSA_ENTRE_LOTES_SEGUNDOS)
            lote = []
            caracteres_no_lote = 0
        lote.append(texto)
        caracteres_no_lote += len(texto)

    _processar_lote()
    return embeddings


def rodar_ingestao(diretorio: Path = DOCUMENTOS_DIR) -> None:
    arquivos = sorted(
        f for f in diretorio.iterdir() if f.suffix.lower() in _EXTENSOES_SUPORTADAS
    )

    todos_chunks: list[Chunk] = []
    for arquivo in arquivos:
        todos_chunks.extend(chunk_documento(arquivo))

    embedding_provider = VoyageProvider()
    vector_store = VectorStore()
    vector_store.limpar()

    textos_embedding = [texto_para_embedding(c) for c in todos_chunks]
    textos_armazenamento = [c.texto for c in todos_chunks]
    embeddings = _embedar_em_lotes(embedding_provider, textos_embedding)
    ids = [f"{c.documento}-{i}" for i, c in enumerate(todos_chunks)]
    metadados = [{"documento": c.documento, "secao": c.secao} for c in todos_chunks]

    vector_store.adicionar(
        ids=ids, embeddings=embeddings, documentos=textos_armazenamento, metadados=metadados
    )

    print(f"Arquivos processados: {len(arquivos)}")
    for arquivo in arquivos:
        print(f"  - {arquivo.name}")
    print(f"Total de chunks gravados: {len(todos_chunks)}")


if __name__ == "__main__":
    rodar_ingestao()
