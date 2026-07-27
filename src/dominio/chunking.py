import re
from dataclasses import dataclass
from pathlib import Path

import docx
import pypdf
from docx.oxml.table import CT_Tbl
from docx.oxml.text.paragraph import CT_P
from docx.table import Table as DocxTable
from docx.text.paragraph import Paragraph as DocxParagraph
from langchain_text_splitters import RecursiveCharacterTextSplitter

from src.config import CHUNK_OVERLAP, CHUNK_SIZE

_HEADING_STYLES = {"Heading 1", "Heading 2", "Heading 3"}
_PDF_HEADING_PATTERN = re.compile(r"^\d+(\.\d+)*\s+\S")
_PDF_HEADING_MAX_LEN = 100

# Sem tokenizer instalado no projeto: aproxima tokens por caracteres (~4 chars/token).
_CHARS_POR_TOKEN = 4


@dataclass
class Chunk:
    texto: str
    documento: str
    secao: str


def _fechar_secao(chunks: list[Chunk], documento: str, secao: str, corpo: list[str]) -> None:
    texto = "\n".join(corpo).strip()
    if texto:
        chunks.append(Chunk(texto=texto, documento=documento, secao=secao))


def texto_para_embedding(chunk: Chunk) -> str:
    """Contextualiza o texto para gerar o embedding, sem alterar o texto exibido/armazenado.

    O heading da seção não faz parte de `chunk.texto` (só vira metadado `secao`), então
    perguntas que citam o identificador da seção (ex. "Caso 01") não casam semanticamente
    com o corpo do chunk. Prepender o heading aqui corrige isso sem duplicar a informação
    no texto que o Claude vê em <documentos_relevantes>.
    """
    if chunk.secao == chunk.documento:
        return chunk.texto
    return f"{chunk.secao}\n\n{chunk.texto}"


def _iter_blocos_docx(d: docx.Document):
    for filho in d.element.body.iterchildren():
        if isinstance(filho, CT_P):
            yield DocxParagraph(filho, d)
        elif isinstance(filho, CT_Tbl):
            yield DocxTable(filho, d)


def _tabela_para_texto(tabela: DocxTable) -> str:
    linhas = [
        " | ".join(celula.text.strip() for celula in linha.cells) for linha in tabela.rows
    ]
    return "\n".join(linhas)


def chunk_docx(caminho: Path) -> list[Chunk]:
    documento = caminho.name
    d = docx.Document(str(caminho))
    chunks: list[Chunk] = []
    secao_atual = documento
    corpo: list[str] = []

    for bloco in _iter_blocos_docx(d):
        if isinstance(bloco, DocxTable):
            texto_tabela = _tabela_para_texto(bloco)
            if texto_tabela.strip():
                corpo.append(texto_tabela)
            continue

        texto = bloco.text.strip()
        if not texto:
            continue
        if bloco.style.name in _HEADING_STYLES:
            _fechar_secao(chunks, documento, secao_atual, corpo)
            secao_atual = texto
            corpo = []
        else:
            corpo.append(texto)

    _fechar_secao(chunks, documento, secao_atual, corpo)
    return chunks


def chunk_pdf(caminho: Path) -> list[Chunk]:
    documento = caminho.name
    leitor = pypdf.PdfReader(str(caminho))
    texto_completo = "\n".join(pagina.extract_text() for pagina in leitor.pages)

    chunks: list[Chunk] = []
    secao_atual = documento
    corpo: list[str] = []

    for linha in texto_completo.splitlines():
        linha_strip = linha.strip()
        if not linha_strip:
            continue
        eh_heading = (
            len(linha_strip) < _PDF_HEADING_MAX_LEN
            and _PDF_HEADING_PATTERN.match(linha_strip) is not None
        )
        if eh_heading:
            _fechar_secao(chunks, documento, secao_atual, corpo)
            secao_atual = linha_strip
            corpo = []
        else:
            corpo.append(linha_strip)

    _fechar_secao(chunks, documento, secao_atual, corpo)
    return chunks


def chunk_markdown(caminho: Path) -> list[Chunk]:
    documento = caminho.name
    linhas = caminho.read_text(encoding="utf-8").splitlines()

    chunks: list[Chunk] = []
    categoria_atual = documento
    secao_atual = documento
    corpo: list[str] = []

    for linha in linhas:
        if linha.startswith("### "):
            _fechar_secao(chunks, documento, secao_atual, corpo)
            secao_atual = f"{categoria_atual} > {linha[4:].strip()}"
            corpo = []
        elif linha.startswith("## "):
            _fechar_secao(chunks, documento, secao_atual, corpo)
            categoria_atual = linha[3:].strip()
            secao_atual = categoria_atual
            corpo = []
        else:
            corpo.append(linha)

    _fechar_secao(chunks, documento, secao_atual, corpo)
    return chunks


def aplicar_fallback(chunks: list[Chunk]) -> list[Chunk]:
    limite_caracteres = CHUNK_SIZE * _CHARS_POR_TOKEN
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=limite_caracteres,
        chunk_overlap=CHUNK_OVERLAP * _CHARS_POR_TOKEN,
    )

    resultado: list[Chunk] = []
    for chunk in chunks:
        if len(chunk.texto) <= limite_caracteres:
            resultado.append(chunk)
            continue
        for trecho in splitter.split_text(chunk.texto):
            resultado.append(Chunk(texto=trecho, documento=chunk.documento, secao=chunk.secao))
    return resultado


def chunk_documento(caminho: Path) -> list[Chunk]:
    extensao = caminho.suffix.lower()
    if extensao == ".docx":
        chunks = chunk_docx(caminho)
    elif extensao == ".pdf":
        chunks = chunk_pdf(caminho)
    elif extensao == ".md":
        chunks = chunk_markdown(caminho)
    else:
        raise ValueError(f"Extensão não suportada: {extensao}")

    return aplicar_fallback(chunks)
