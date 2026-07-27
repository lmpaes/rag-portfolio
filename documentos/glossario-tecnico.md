# Glossário Técnico de Fraude e Produtos Bancários

> Code Bank — Base de Conhecimento Interna · Versão 1.1 · Atualizado em 27/07/2026 · Uso Interno

Este glossário reúne os termos técnicos usados pelas áreas de Atendimento e de Prevenção e Investigação de Fraude do Code Bank, organizados em duas categorias: **termos técnicos de mercado** (conceitos gerais do setor bancário e de prevenção a fraudes, válidos para qualquer instituição financeira) e **termos e sistemas internos do Code Bank** (nomes próprios definidos nos demais documentos desta base de conhecimento). Cada entrada é autossuficiente; as entradas de nomes próprios indicam o documento e a seção onde o critério completo está definido, para consulta aprofundada.

---

## Termos Técnicos de Mercado

### Account Takeover (ATO)
Tomada de controle não autorizada de uma conta legítima por um fraudador, geralmente via phishing, malware ou vazamento de credenciais.

### Alçada
Limite de autoridade/valor que um cargo possui para aprovar ou decidir sobre uma operação sem escalonamento.

### ANPD
Autoridade Nacional de Proteção de Dados — órgão responsável por fiscalizar a LGPD.

### Antifraude (Sistema Antifraude)
Conjunto de sistemas e regras que analisam transações em tempo real para identificar e bloquear atividades suspeitas.

### Bacen / BCB
Banco Central do Brasil — autoridade monetária e reguladora do Sistema Financeiro Nacional.

### Biometria Comportamental
Técnica que analisa padrões de uso (digitação, toque, navegação) para identificar anomalias que indiquem uso por pessoa diferente do titular.

### BIN (Bank Identification Number)
Primeiros dígitos do número do cartão que identificam a instituição emissora e o tipo de produto.

### Boletim de Ocorrência (BO)
Registro formal de um crime junto à autoridade policial, frequentemente usado como evidência em processos de contestação/ressarcimento.

### Card Not Present (CNP)
Transação realizada sem apresentação física do cartão (compras online, por telefone), com maior exposição a fraude.

### Chargeback
Contestação de uma transação de cartão feita pelo titular junto ao emissor, que pode resultar em estorno ao cliente e repasse do prejuízo ao lojista/adquirente, conforme regras da bandeira.

### Chave Pix
Identificador (CPF, e-mail, telefone ou chave aleatória) que associa uma conta a um "apelido" usado em transações Pix.

### Compliance
Área responsável por assegurar que a instituição cumpra leis, regulamentações e políticas internas aplicáveis, atuando na prevenção e mitigação de riscos legais e regulatórios.

### Conta Laranja
Conta bancária usada, em nome de terceiro, para receber e transferir valores de origem ilícita, dificultando o rastreamento.

### Contestação
Solicitação formal do cliente para questionar uma cobrança ou transação que não reconhece.

### CVV (Card Verification Value)
Código de segurança impresso no cartão, usado para validar transações não presenciais.

### DICT (Diretório de Identificadores de Contas Transacionais)
Diretório centralizado do Banco Central que associa chaves Pix às contas correspondentes, consultado no momento de uma transferência e utilizado também no acionamento do MED.

### Dispositivo Confiável/Reconhecido
Aparelho previamente registrado pelo cliente como habitual, usado como fator de risco em decisões antifraude.

### DOC (Documento de Ordem de Crédito)
Modalidade de transferência entre instituições diferentes, hoje em desuso, com compensação em até 1 dia útil.

### Engenharia Social
Técnica de manipulação psicológica usada por fraudadores para induzir a vítima a fornecer dados sensíveis ou autorizar transações.

### Estorno
Devolução de um valor debitado indevidamente ou contestado, creditado de volta à conta ou fatura do cliente.

### Falso Negativo (antifraude)
Transação fraudulenta que não foi identificada/bloqueada pelo sistema.

### Falso Positivo (antifraude)
Transação legítima incorretamente identificada e bloqueada como suspeita.

### IOF
Imposto sobre Operações Financeiras — imposto federal incidente sobre diversas operações financeiras, incluindo câmbio e certas transações internacionais com cartão.

### KYC (Know Your Customer)
Conjunto de processos de verificação de identidade e devida diligência na abertura e manutenção de contas, exigido por regulação de prevenção à lavagem de dinheiro.

### LGPD
Lei Geral de Proteção de Dados (Lei nº 13.709/2018) — regula o tratamento de dados pessoais no Brasil.

### MED (Mecanismo Especial de Devolução)
Mecanismo do Bacen, operado via Pix, para bloqueio cautelar e devolução de valores em casos de fraude comprovada.

### Onboarding
Processo de abertura e ativação inicial de uma conta, incluindo etapas de KYC.

### Ouvidoria
Canal de segunda instância para reclamações não resolvidas satisfatoriamente pelo SAC, de manutenção obrigatória para instituições financeiras reguladas pelo Bacen/CMN. Ver Documento 1 – Política de Detecção de Fraude, Seção 1, para o contato específico do Code Bank.

### Pix
Sistema de pagamentos instantâneos do Banco Central, disponível 24/7. Gratuito para Pessoa Física.

### PLD/AML (Prevenção à Lavagem de Dinheiro)
Políticas e controles para identificar, monitorar e reportar operações suspeitas de lavagem de dinheiro ou financiamento ao terrorismo, exigidos pelo Bacen e pelo COAF.

### SAC (Serviço de Atendimento ao Consumidor)
Canal obrigatório de atendimento ao cliente para reclamações, dúvidas e solicitações, regulado por norma federal específica. Ver Documento 1 – Política de Detecção de Fraude, Seção 1, para o contato específico do Code Bank.

### Scoring (Score de Risco)
Pontuação numérica atribuída a uma transação ou cliente, calculada por modelo estatístico, que estima a probabilidade de fraude.

### TED (Transferência Eletrônica Disponível)
Transferência entre contas de instituições diferentes, geralmente compensada no mesmo dia útil.

---

## Termos e Sistemas Internos do Code Bank

### Analista de Prevenção a Fraudes
Cargo de Nível 1 da trilha de Prevenção e Investigação de Fraude do Code Bank. Analisa alertas do motor Code Shield, conduz a investigação inicial de casos e libera ou mantém bloqueios dentro da própria alçada. Ver Documento 1 – Política de Detecção de Fraude, Seção 3.

### Analista de Relacionamento
Cargo de linha de frente da trilha de Atendimento do Code Bank. É o primeiro contato do cliente, mas não integra a trilha de decisão de fraude. Ver Documento 1 – Política de Detecção de Fraude, Seção 3.

### Aviso de Viagem
Funcionalidade do aplicativo Code Bank que permite ao cliente informar previamente uma viagem internacional, suprimindo o gatilho de bloqueio automático por compra internacional durante o período informado. Ver Documento 1 – Política de Detecção de Fraude, Seção 6.

### Cartão Code e Cartão Code Black
Linha de cartões de crédito do Code Bank. O Cartão Code é o cartão de entrada, sem anuidade; o Cartão Code Black é a versão premium, com anuidade sujeita a isenção condicionada e participação no programa Code Rewards. Ver Documento 5 – Política de Contas, Taxas e Cartões, para tarifas e condições completas.

### Code Bank
Nome comercial da instituição financeira 100% digital documentada nesta base de conhecimento. O aplicativo/internet banking utiliza o mesmo nome da instituição. Ver Documento 1 – Política de Detecção de Fraude, Seção 1.

### Code Conta, Code Conta Plus e Code Conta Black
Linha de contas digitais do Code Bank: Code Conta (entrada, gratuita), Code Conta Plus (padrão, com tarifa mensal) e Code Conta Black (premium, com tarifa mensal mais alta e benefícios adicionais). Ver Documento 5 – Política de Contas, Taxas e Cartões, para tarifas e condições completas.

### CodeCase
Sistema interno de gestão de casos do Code Bank, usado para registrar e acompanhar toda investigação de suspeita de fraude, do status inicial ao encerramento. Ver Documento 2 – Procedimento de Resposta a Incidentes, Seção 1.

### Code Rewards
Programa de pontos do Code Bank, exclusivo para portadores do Cartão Code Black, com acúmulo de 1 ponto por R$ 1,00 gasto. Ver Documento 5 – Política de Contas, Taxas e Cartões.

### Code Shield
Motor de score de risco de fraude proprietário do Code Bank, usado exclusivamente para avaliação de risco de fraude transacional — não alimenta decisões de concessão de crédito ou de limite. Ver Documento 1 – Política de Detecção de Fraude, Seção 4.

### Comitê de Risco e Fraude
Instância máxima de decisão da trilha de Prevenção e Investigação de Fraude do Code Bank, acionada para casos que excedem a alçada do Gerente de Risco e Fraude ou que envolvem exceção à política vigente. Ver Documento 1 – Política de Detecção de Fraude, Seção 3.

### Coordenador de Prevenção a Fraudes
Cargo de Nível 2 da trilha de Prevenção e Investigação de Fraude do Code Bank. Revisa casos escalonados pelo Analista de Prevenção a Fraudes e decide sobre bloqueios de maior valor ou complexidade. Ver Documento 1 – Política de Detecção de Fraude, Seção 3.

### Gerente de Risco e Fraude
Cargo de Nível 3 da trilha de Prevenção e Investigação de Fraude do Code Bank. Decide sobre casos de alto valor ou complexidade e aprova exceções pontuais à Política de Detecção de Fraude. Ver Documento 1 – Política de Detecção de Fraude, Seção 3.

### Status de Caso
Conjunto fechado de sete rótulos usados para classificar o andamento de um caso de fraude no Code Bank: Aberto, Em Análise, Aguardando Cliente, Escalonado, Confirmado – Fraude, Confirmado – Falso Positivo e Encerrado. Ver Documento 1 – Política de Detecção de Fraude, Seção 8, e Documento 2 – Procedimento de Resposta a Incidentes, Seção 3.

### Supervisor de Atendimento
Cargo de supervisão da trilha de Atendimento do Code Bank. Escalona casos que fogem do roteiro padrão de atendimento. Ver Documento 1 – Política de Detecção de Fraude, Seção 3.

### "Travar Cartão"
Função do aplicativo Code Bank que permite ao cliente bloquear e desbloquear seu cartão a qualquer momento. Ver Documento 5 – Política de Contas, Taxas e Cartões, Seção 4.

---

## Histórico de Revisões

| Versão | Data | Descrição |
|---|---|---|
| 1.0 | 01/06/2026 | Emissão inicial deste glossário, com 33 termos técnicos de mercado e 15 termos/sistemas internos do Code Bank. |
| 1.1 | 27/07/2026 | Corrigida a referência da entrada "Travar Cartão" (era Documento 1, passou a Documento 5), corrigindo lacuna identificada na auditoria de consistência final. |
