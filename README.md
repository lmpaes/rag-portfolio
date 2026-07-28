# Code Bank — RAG Portfolio

Base de conhecimento interna (RAG — Retrieval-Augmented Generation) para funcionários de um banco fictício 100% digital, o **Code Bank**, cobrindo detecção de fraude, procedimentos internos, contas, tarifas e políticas de cartão.

## Sobre o projeto

Um funcionário do Code Bank faz uma pergunta em linguagem natural (ex.: *"quais são as faixas de score de risco atuais?"*) e recebe uma resposta fundamentada exclusivamente nos documentos internos da base, com citação de fonte (documento + seção) para rastreabilidade.

A base de conhecimento é composta por 6 documentos fictícios, mas realistas, escritos especificamente para este projeto — política de detecção de fraude, procedimento de resposta a incidentes, casos históricos, glossário técnico, política de contas/tarifas/cartões e FAQ de atendimento — em três formatos (DOCX, PDF, Markdown), gerados a partir de um documento canônico único para garantir consistência de nomes, valores e critérios entre todos eles.

## Stack

| Camada | Tecnologia |
|---|---|
| Geração (LLM) | [Claude Haiku 4.5](https://www.anthropic.com) (Anthropic) |
| Embeddings | `voyage-3.5` (Voyage AI) |
| Vector store | [ChromaDB](https://www.trychroma.com/) (embarcado, sem servidor) |
| Interface | [Streamlit](https://streamlit.io/) |
| Parsing de documentos | `python-docx`, `pypdf` |
| Chunking | `langchain-text-splitters` (fallback de tamanho fixo) |
| Deploy | [Render](https://render.com) (free tier) |

## Arquitetura

Arquitetura em camadas, com Adapter Pattern para isolar a lógica de negócio dos provedores externos:

```
app.py (Streamlit)              → Interface
src/orquestracao/rag.py         → Orquestração (recebe pergunta → retrieval → prompt → geração)
src/dominio/                    → Domínio (chunking, retrieval, prompt builder)
src/infraestrutura/             → Infraestrutura (adapters: ClaudeProvider, VoyageProvider, VectorStore)
```

Cada camada superior conhece apenas a interface da camada inferior, nunca sua implementação — trocar de provedor de LLM ou de embeddings é uma mudança de configuração, não uma reescrita de código. `LLMProvider` e `EmbeddingProvider` são classes abstratas; `ClaudeProvider` e `VoyageProvider` são as únicas implementações reais desta v1 (a arquitetura já está preparada para um `OllamaProvider` local ou embeddings locais, caso venha a ser necessário).

**Chunking por estrutura:** DOCX e PDF são segmentados por título/seção natural do documento (incluindo tabelas, que viram texto tabular dentro do chunk correspondente); Markdown é segmentado por entrada (`###`). Um fallback de tamanho fixo, com overlap, evita chunks grandes demais para o embedding representar bem.

## Rodando localmente

```bash
git clone https://github.com/lmpaes/rag-portfolio.git
cd rag-portfolio
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env
# preencha ANTHROPIC_API_KEY e VOYAGE_API_KEY no .env

streamlit run app.py
```

A base vetorial (`.chroma/`) já vem pronta no repositório — não é necessário rodar a ingestão para testar. Caso queira reprocessar os documentos do zero:

```bash
python -m src.ingestao.pipeline
```

## Testes e avaliação

19 perguntas de teste em 5 categorias (diretas, cruzando documentos, fora de escopo, ambíguas/mal formuladas, sinônimos), com gabarito definido **antes** de rodar o sistema. Resultados completos, incluindo retrieval precision, faithfulness e um teste de defesa contra prompt injection, em [`testes/resultados_avaliacao.md`](testes/resultados_avaliacao.md).

## Decisões técnicas (resumo)

- **Haiku 4.5 em vez de Sonnet** para geração: em RAG, a qualidade da resposta depende mais da qualidade do retrieval do que do poder do modelo de geração — Haiku responde com precisão a um custo e velocidade muito menores.
- **ChromaDB embarcado em vez de um vector store gerenciado**: zero infraestrutura extra, foco no aprendizado de RAG (chunking, embeddings, retrieval) em vez de configuração de banco de dados.
- **Similarity search puro nesta v1** (sem hybrid search/reranking) — avaliado como suficiente após os testes; evolução natural caso o volume/diversidade de perguntas justifique.

## Evolução futura

A mesma base de documentos poderia atender diretamente o cliente final (não só o funcionário), com tom de resposta simplificado e um filtro de visibilidade por documento/seção (`interno` / `público` / `ambos`) para impedir que critérios sensíveis (ex.: limiares exatos de bloqueio por fraude) sejam expostos fora do público interno. Não implementado nesta v1.
