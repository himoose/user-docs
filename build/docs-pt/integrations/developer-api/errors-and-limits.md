---
source_hash: 85fe7ea99ed19540350085410907cba880592b989251ce17fdb81570b24829a2
---
!!! note "Tradução automática"
    Esta página foi traduzida por IA. A versão em inglês é a versão oficial.

    [Ler em inglês](https://himoose.com/docs/integrations/developer-api/errors-and-limits/)


# Erros e limites

## Erros

Os erros usam o formato Problem Details (`application/problem+json`, RFC 9457) com um `code` estável sobre o qual o seu código pode decidir:

```json
{
  "type": "https://himoose.com/docs/integrations/developer-api/errors-and-limits/#errors",
  "title": "Not found",
  "status": 404,
  "detail": "No project with that id is readable with this key.",
  "code": "not_found",
  "instance": "/v1/projects/abc123",
  "requestId": "7f4c0d1a2b"
}
```

- `code` é o campo a testar no código. Ele nunca muda de significado.
- `detail` é escrito para uma pessoa e a redação pode mudar.
- `type` aponta para a seção da documentação sobre esse tipo de erro.
- `requestId` identifica a requisição. Informe-o ao entrar em contato com o suporte. Ele também é enviado no cabeçalho `X-Request-Id` em toda resposta.

Alguns erros trazem campos extras, indicados na tabela.

## Códigos de erro

| Código | Status | Significado | O que fazer |
|---|---|---|---|
| `invalid_key` | 401 | Sem cabeçalho `Authorization`, uma chave no formato errado ou uma chave que o Hi, Moose não conhece | Envie `Authorization: Bearer hmk_live_...`. Confira se a chave foi copiada por inteiro. |
| `key_revoked` | 401 | A chave foi revogada em Configurações | Crie uma chave nova. |
| `key_expired` | 401 | A chave passou da data de expiração | Crie uma chave nova. |
| `plan_required` | 403 | O plano da conta não inclui a API | Mude para um plano pago. |
| `insufficient_scope` | 403 | A chave não tem a permissão para esta chamada. O corpo a informa em `scope`. | Crie uma chave com essa permissão. |
| `not_found` | 404 | O recurso não existe, ou a chave não pode lê-lo. Os dois casos não são distinguidos. | Confira o id e o acesso a projetos da chave. |
| `method_not_allowed` | 405 | O endpoint existe, mas não com este método | Veja a [referência](reference.md). |
| `invalid_parameter` | 400 | Um parâmetro de consulta ou um campo do corpo está faltando, malformado ou fora do intervalo. `detail` o informa. | Corrija a requisição. |
| `range_too_wide` | 400 | De `from` a `to` vão mais de 366 dias | Peça um período mais curto. |
| `unsupported_filter_combination` | 400 | Filtros que não podem ser combinados, por exemplo `engine` com dois de `promptId`, `topicId` e `runId` | Tire um filtro. |
| `host_required` | 409 | O projeto não tem computador host escolhido | Escolha um no Hi, Moose em **Configurações → Hi, Moose MCP**. |
| `byok_not_supported` | 409 | Neste plano as configurações de acompanhamento vivem no computador host, então a API não pode alterá-las | Altere-as no Hi, Moose nesse computador. |
| `plan_limit` | 409 | Um limite do plano foi atingido. O corpo traz `limit`. | Consulte `GET /projects/{id}/capabilities` para ver os limites. |
| `run_in_progress` | 409 | Já há um pedido de execução na fila, em espera ou em andamento. O corpo traz `requestId` e `requestStatus`. | Espere ele terminar. |
| `insufficient_allowance` | 409 | A execução custaria mais que o saldo restante. O corpo traz `estimatedUnits`, `remainingUnits` e `periodEndsAt`. | Recarregue o saldo, ou reduza prompts, motores ou amostras. |
| `no_prompts` | 409 | O projeto não tem nenhum prompt acompanhado com motor | Adicione prompts e motores primeiro. |
| `rate_limited` | 429 | O limite por minuto ou por dia foi atingido | Espere os segundos indicados em `Retry-After`. |
| `daily_run_limit` | 429 | O projeto já fez seus 24 pedidos de execução de hoje | Tente amanhã. |
| `internal` | 500 | Algo falhou do lado do Hi, Moose | Tente de novo com intervalos crescentes. Se persistir, entre em contato com o suporte com o `requestId`. |

Um `502` ou `503` sem corpo significa que a API não conseguiu alcançar seu backend. Tente de novo com intervalos crescentes.

## Limites de requisições

| Limite | Valor |
|---|---|
| Por chave | 300 requisições por minuto |
| Por conta | 50.000 requisições por dia |
| Pedidos de execução por projeto | 24 por dia, um de cada vez |
| Webhooks por projeto | 5 |
| Linhas por página | 200 |
| Período por requisição | 366 dias |

Acima do limite a API responde `429 rate_limited` com um cabeçalho `Retry-After`. Toda resposta traz `RateLimit-Policy`, e as respostas bem-sucedidas trazem `RateLimit` com o orçamento restante do dia, seguindo o rascunho IETF de cabeçalhos de limite de requisições:

```
RateLimit-Policy: "per-minute";q=300;w=60, "per-day";q=50000;w=86400
RateLimit: "per-day";r=49871;t=61234
```

O limite por minuto é contado por chave na borda da rede e é aproximado; um pico curto um pouco acima dele pode passar. O limite por dia é contado por conta, somando todas as suas chaves.

## Ficar abaixo dos limites

- **Faça cache do seu lado.** As estatísticas diárias trazem `Cache-Control: max-age=60`. Um painel que atualiza a cada minuto lê o resumo uma vez por minuto por gráfico, não uma vez por visitante.
- **Use os resumos.** As estatísticas diárias e de concorrentes são construídas a partir de uma tabela de resumo. Desenhe os gráficos a partir delas e leia respostas individuais só quando alguém abrir uma linha.
- **Use ETags.** As respostas trazem um `ETag`. Devolva-o em `If-None-Match` e um `304` quase não custa nada.
- **Use webhooks** em vez de consultar repetidamente até uma execução terminar. Veja [Webhooks](webhooks.md).
- **Recue em um 429.** Espere os segundos de `Retry-After` e depois tente de novo. Não tente de novo na hora.

## Ids de requisição

Toda resposta traz `X-Request-Id`. Registre-o ao lado do seu próprio log de requisições, para que um relato de problema possa ser ligado aos logs do Hi, Moose. Os corpos de erro o repetem como `requestId`.
