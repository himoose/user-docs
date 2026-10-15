---
source_hash: 422edf700d29e3ee080f114ca1c4fbdc3f92677eb196cdf636fdac1f0e5e4cad
---

# Registro de alterações

A versão do contrato está em `info.version` do [openapi.json](https://api.himoose.com/v1/openapi.json) e no título da [referência de endpoints](reference.md). A URL base continua `/v1` em todas as versões listadas aqui; uma mudança incompatível ganharia uma nova URL base e um aviso com bastante antecedência.

## 1.2.1, 2026-10-15

Primeira versão pública.

- **Leitura:** projetos, motores, temas, prompts, concorrentes, execuções, respostas com texto completo, estatísticas diárias, estatísticas de concorrentes e capacidades.
- **Gerenciar o acompanhamento:** criar e alterar projetos, substituir concorrentes, adicionar, alterar e excluir prompts, definir motores e agendamento.
- **Execuções:** iniciar uma execução com verificação do saldo, uma de cada vez, 24 por dia, com chaves de idempotência e um status para consultar.
- **Webhooks:** eventos `run.completed` e `run.failed` com assinaturas HMAC, novas tentativas e um registro de entregas.
- **Limites:** 300 requisições por minuto por chave, 50.000 por dia por conta.
- `PUT /projects/{id}/tracking` com `engineIds` altera apenas os motores padrão. Os prompts existentes mantêm seus motores a menos que `applyEnginesToPrompts` seja `true`.

## Planejado

- Alterações no acompanhamento nos planos com chave própria, cujas configurações vivem hoje no computador host.
- Oportunidades, a fila de trabalho por prioridade do separador Oportunidades.
