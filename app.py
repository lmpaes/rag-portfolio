import streamlit as st

from src.orquestracao.rag import RAG

CATEGORIAS_BASE = [
    "Política de Detecção de Fraude",
    "Procedimento de Resposta a Incidentes",
    "Casos Históricos de Fraude",
    "Glossário Técnico",
    "Política de Contas, Taxas e Cartões",
    "FAQ Interno de Atendimento",
]

st.set_page_config(page_title="Code Bank — Base de Conhecimento", page_icon="🏦")


@st.cache_resource
def carregar_rag() -> RAG:
    return RAG()


with st.sidebar:
    st.markdown("**Perfil:** Funcionário")
    st.markdown("### Base de Conhecimento")
    for categoria in CATEGORIAS_BASE:
        st.markdown(f"- {categoria}")

st.title("Code Bank — Assistente Interno")

if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

for mensagem in st.session_state.mensagens:
    with st.chat_message(mensagem["role"]):
        st.markdown(mensagem["content"])
        if mensagem.get("fontes"):
            with st.expander("Fontes"):
                for fonte in mensagem["fontes"]:
                    st.markdown(f"- **{fonte['documento']}** — {fonte['secao']}")

pergunta = st.chat_input("Pergunte sobre fraude, contas, taxas ou cartões...")

if pergunta:
    st.session_state.mensagens.append({"role": "user", "content": pergunta})
    with st.chat_message("user"):
        st.markdown(pergunta)

    with st.chat_message("assistant"):
        try:
            rag = carregar_rag()
            resultado = rag.responder(pergunta)
        except Exception:
            resultado = {
                "resposta": (
                    "Não foi possível gerar uma resposta agora. Verifique se a base de "
                    "conhecimento foi ingerida e se as chaves de API estão configuradas."
                ),
                "fontes": [],
            }
        st.markdown(resultado["resposta"])
        if resultado["fontes"]:
            with st.expander("Fontes"):
                for fonte in resultado["fontes"]:
                    st.markdown(f"- **{fonte['documento']}** — {fonte['secao']}")

    st.session_state.mensagens.append(
        {
            "role": "assistant",
            "content": resultado["resposta"],
            "fontes": resultado["fontes"],
        }
    )
