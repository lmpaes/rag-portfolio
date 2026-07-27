"""Gabarito das perguntas de teste — definido ANTES de rodar o sistema (Fase 5)."""

PERGUNTAS = [
    # --- Diretas (6) ---
    {
        "id": 1,
        "categoria": "direta",
        "pergunta": "Qual é a escala de score de risco usada pelo Code Shield e quais são as faixas de risco atuais?",
        "documentos_esperados": ["politica-deteccao-fraude.docx"],
        "resposta_aceitavel": "Escala 0-1000; faixas atuais: Risco Baixo 0-299, Médio 300-599, Alto 600-849, Crítico 850-1000.",
    },
    {
        "id": 2,
        "categoria": "direta",
        "pergunta": "Qual o prazo para concluir uma investigação de fraude, segundo o procedimento de resposta a incidentes?",
        "documentos_esperados": ["procedimento-resposta-incidentes.docx"],
        "resposta_aceitavel": "Até 5 dias úteis.",
    },
    {
        "id": 3,
        "categoria": "direta",
        "pergunta": "Quanto custa a tarifa mensal da Code Conta Black?",
        "documentos_esperados": ["politica-contas-tarifas-cartoes.pdf"],
        "resposta_aceitavel": "R$ 39,90/mês.",
    },
    {
        "id": 4,
        "categoria": "direta",
        "pergunta": "O que é um chargeback?",
        "documentos_esperados": ["glossario-tecnico.md"],
        "resposta_aceitavel": "Contestação de transação de cartão pelo titular junto ao emissor, podendo gerar estorno.",
    },
    {
        "id": 5,
        "categoria": "direta",
        "pergunta": "Qual é a alçada de liberação manual do Coordenador de Prevenção a Fraudes?",
        "documentos_esperados": ["politica-deteccao-fraude.docx"],
        "resposta_aceitavel": "Até R$ 10.000,00.",
    },
    {
        "id": 6,
        "categoria": "direta",
        "pergunta": "A partir de que valor é obrigatório um Boletim de Ocorrência para o ressarcimento ao cliente?",
        "documentos_esperados": ["procedimento-resposta-incidentes.docx"],
        "resposta_aceitavel": "Acima de R$ 5.000,00 (ou qualquer valor em caso de conta laranja/terceiros).",
    },
    # --- Cruzando documentos (4) ---
    {
        "id": 7,
        "categoria": "cruzando_documentos",
        "pergunta": (
            "Um cliente teve uma fraude confirmada e quer saber em quanto tempo será ressarcido, "
            "e também quais critérios de score levaram ao bloqueio da transação."
        ),
        "documentos_esperados": [
            "procedimento-resposta-incidentes.docx",
            "politica-deteccao-fraude.docx",
        ],
        "resposta_aceitavel": (
            "Ressarcimento em até 7 dias úteis após confirmação (Doc 2); bloqueio automático "
            "ocorre a partir de score >= 900 (Doc 1)."
        ),
    },
    {
        "id": 8,
        "categoria": "cruzando_documentos",
        "pergunta": (
            "No Caso 01 dos Casos Históricos, qual política de score estava vigente e quais eram "
            "os limites de bloqueio automático dessa política antiga?"
        ),
        "documentos_esperados": ["casos-historicos-fraude.pdf", "politica-deteccao-fraude.docx"],
        "resposta_aceitavel": (
            "Caso 01 ocorreu sob a política antiga (Doc 3); a política antiga tinha 3 faixas e "
            "bloqueio automático a partir de score >= 950 (Doc 1, Seção 10)."
        ),
    },
    {
        "id": 9,
        "categoria": "cruzando_documentos",
        "pergunta": (
            "Por que o atendimento deve orientar o cliente a buscar o SAC antes da Ouvidoria, e "
            "quais são os horários de funcionamento de cada canal?"
        ),
        "documentos_esperados": ["faq-atendimento.md", "politica-deteccao-fraude.docx"],
        "resposta_aceitavel": (
            "Ouvidoria é instância de segunda linha; SAC funciona 24h, Ouvidoria em dias úteis "
            "das 9h às 18h."
        ),
    },
    {
        "id": 10,
        "categoria": "cruzando_documentos",
        "pergunta": (
            "Qual é o nome do sistema interno usado para registrar investigações de fraude, e como "
            "esse termo é descrito no glossário técnico?"
        ),
        "documentos_esperados": ["procedimento-resposta-incidentes.docx", "glossario-tecnico.md"],
        "resposta_aceitavel": "CodeCase — sistema de gestão de casos/investigações.",
    },
    # --- Fora do escopo (3) ---
    {
        "id": 11,
        "categoria": "fora_do_escopo",
        "pergunta": "Qual é a taxa de juros cobrada no cheque especial do Code Bank?",
        "documentos_esperados": [],
        "resposta_aceitavel": "Admitir que não há informação suficiente na base (produto não coberto).",
    },
    {
        "id": 12,
        "categoria": "fora_do_escopo",
        "pergunta": "Como faço para investir em CDB ou fundos de investimento pelo aplicativo do Code Bank?",
        "documentos_esperados": [],
        "resposta_aceitavel": "Admitir que não há informação suficiente na base (investimentos fora do escopo).",
    },
    {
        "id": 13,
        "categoria": "fora_do_escopo",
        "pergunta": "Qual é o limite de crédito máximo do Cartão Code Black e como ele é definido?",
        "documentos_esperados": [],
        "resposta_aceitavel": (
            "Admitir que não há informação suficiente — concessão/aumento de limite de crédito é "
            "explicitamente fora do escopo do Code Shield e dos documentos."
        ),
    },
    # --- Ambíguas / mal formuladas (3) ---
    {
        "id": 14,
        "categoria": "ambigua",
        "pergunta": "pq bloqueou mnha transferencia pix de 2000 reais recem cadastrei a chave",
        "documentos_esperados": ["politica-deteccao-fraude.docx"],
        "resposta_aceitavel": (
            "Deve identificar o gatilho: transferência Pix acima de R$ 1.000 para chave cadastrada "
            "há menos de 24h dispara bloqueio automático."
        ),
    },
    {
        "id": 15,
        "categoria": "ambigua",
        "pergunta": "quanto custa o cartao",
        "documentos_esperados": ["politica-contas-tarifas-cartoes.pdf"],
        "resposta_aceitavel": (
            "Deve trazer os valores dos 3 cartões (débito sem anuidade, Code isento, Code Black "
            "R$480/ano) ou pedir esclarecimento sobre qual cartão."
        ),
    },
    {
        "id": 16,
        "categoria": "ambigua",
        "pergunta": "score",
        "documentos_esperados": ["politica-deteccao-fraude.docx"],
        "resposta_aceitavel": "Deve trazer informação sobre o motor de score Code Shield e suas faixas.",
    },
    # --- Sinônimos / termos diferentes (3) ---
    {
        "id": 17,
        "categoria": "sinonimos",
        "pergunta": "O banco tem alguma proteção contra alguém tomar controle da minha conta sem eu perceber?",
        "documentos_esperados": ["glossario-tecnico.md", "politica-deteccao-fraude.docx"],
        "resposta_aceitavel": "Deve relacionar com Account Takeover (ATO) e os mecanismos antifraude do Code Shield.",
    },
    {
        "id": 18,
        "categoria": "sinonimos",
        "pergunta": "Quais golpes de manipulação psicológica contra clientes o banco já registrou historicamente?",
        "documentos_esperados": ["casos-historicos-fraude.pdf"],
        "resposta_aceitavel": "Deve relacionar com 'engenharia social' e citar casos históricos (ex.: golpe do falso funcionário).",
    },
    {
        "id": 19,
        "categoria": "sinonimos",
        "pergunta": "Existe algum jeito de não pagar a anuidade do cartão premium se eu gastar bastante todo mês?",
        "documentos_esperados": ["politica-contas-tarifas-cartoes.pdf"],
        "resposta_aceitavel": (
            "Isenção da anuidade do Cartão Code Black para fatura média mensal >= R$ 3.000 (últimos "
            "3 meses) ou saldo/investimento >= R$ 20.000."
        ),
    },
]
