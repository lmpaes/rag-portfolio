import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from testes.gabarito import PERGUNTAS  # noqa: E402
from src.orquestracao.rag import RAG  # noqa: E402

_PAUSA_ENTRE_PERGUNTAS_SEGUNDOS = 3
_SAIDA = Path(__file__).resolve().parent / "resultados_avaliacao.md"


def _retrieval_ok(documentos_esperados: list[str], fontes: list[dict]) -> bool | None:
    if not documentos_esperados:
        return None  # fora do escopo: avaliação de faithfulness fica para leitura manual
    documentos_recuperados = {f["documento"] for f in fontes}
    return any(doc in documentos_recuperados for doc in documentos_esperados)


def rodar_avaliacao() -> None:
    rag = RAG()
    linhas = [
        "| id | categoria | pergunta | documentos esperados | documentos recuperados | resposta | retrieval ok? | observação |",
        "|---|---|---|---|---|---|---|---|",
    ]

    for i, item in enumerate(PERGUNTAS):
        if i > 0:
            time.sleep(_PAUSA_ENTRE_PERGUNTAS_SEGUNDOS)

        resultado = rag.responder(item["pergunta"])
        documentos_recuperados = sorted({f["documento"] for f in resultado["fontes"]})
        ok = _retrieval_ok(item["documentos_esperados"], resultado["fontes"])

        resposta_resumida = resultado["resposta"].replace("\n", " ").replace("|", "\\|")
        if len(resposta_resumida) > 300:
            resposta_resumida = resposta_resumida[:300] + "..."

        if ok is None:
            ok_texto = "n/a (fora do escopo)"
        else:
            ok_texto = "sim" if ok else "não"

        linhas.append(
            "| {id} | {categoria} | {pergunta} | {esperados} | {recuperados} | {resposta} | {ok} | |".format(
                id=item["id"],
                categoria=item["categoria"],
                pergunta=item["pergunta"].replace("|", "\\|"),
                esperados=", ".join(item["documentos_esperados"]) or "(nenhum)",
                recuperados=", ".join(documentos_recuperados) or "(nenhum)",
                resposta=resposta_resumida,
                ok=ok_texto,
            )
        )
        print(f"[{item['id']}/{len(PERGUNTAS)}] {item['categoria']} — retrieval ok: {ok_texto}")

    _SAIDA.write_text("\n".join(linhas), encoding="utf-8")
    print(f"\nResultados gravados em {_SAIDA}")


if __name__ == "__main__":
    rodar_avaliacao()
