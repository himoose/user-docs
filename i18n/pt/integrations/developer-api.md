---
source_hash: 825726013c46ce2cb7c1932ac3dda84ec19a94f2c4ce33cdc108f00904718460
---
# Hi, Moose API

## Para que serve

A Hi, Moose API é uma API REST para programadores que constroem os seus próprios painéis, relatórios e aplicações de visibilidade em IA sobre o Hi, Moose. Devolve os mesmos resultados que vê no ecrã Visibilidade: prompts e temas acompanhados, os motores consultados, cada resposta guardada com o texto completo e as fontes, e as taxas de menção e de citação ao longo do tempo. Com as permissões certas, uma chave também pode criar projetos, gerir prompts, motores e agendamento, e iniciar execuções.

As leituras funcionam quer o Hi, Moose esteja aberto no seu computador quer não, porque vêm da cópia na nuvem dos seus resultados. As alterações ao acompanhamento e as execuções precisam do computador anfitrião do projeto, explicado mais abaixo.

Se trabalha no Claude, no ChatGPT ou noutra app de IA, talvez prefira o [Hi, Moose MCP](hi-moose-mcp.md). A API é para o código que escreve você mesmo.

## Planos

A API está incluída nos planos pagos, tanto geridos como com a sua própria chave. As contas gratuitas veem a página de chaves de API mas não podem criar chaves, e cada pedido responde `403 plan_required`.

## Criar uma chave

1. Abra o Hi, Moose e inicie sessão como proprietário da conta. Só o proprietário pode criar, ver e revogar chaves.
2. Vá a **Definições → Hi, Moose REST API**.
3. Dê um nome à chave, escolha os projetos que ela pode ler (todos ou um), escolha quando expira e marque as permissões de que precisa.
4. Clique em **Criar chave** e copie a chave. É mostrada uma única vez. O Hi, Moose não pode mostrá-la de novo; se a perder, revogue-a e crie outra.

As chaves começam por `hmk_live_` seguido de 64 caracteres. A tabela por baixo do formulário lista cada chave ativa com as suas permissões, a data de criação, o último uso e a expiração. **Revogar** interrompe uma chave de imediato.

## Permissões

| Permissão | O que a chave pode fazer |
|---|---|
| Ler dados de visibilidade | Todos os endpoints `GET`. Sempre ativo. |
| Gerir o acompanhamento | Criar projetos, definir termos de marca e concorrentes, adicionar, alterar e apagar prompts, definir motores e agendamento. |
| Iniciar execuções | Iniciar uma execução de visibilidade. As execuções gastam o saldo da conta em motores na nuvem, por isso dê isto apenas a uma chave que precise. |

Uma chamada sem a permissão necessária responde `403 insufficient_scope`. As permissões escolhem-se ao criar a chave e não podem ser alteradas depois.

## Autenticação

Envie a chave como token Bearer:

```bash
curl https://api.himoose.com/v1/me \
  -H "Authorization: Bearer hmk_live_..."
```

A resposta indica a chave, as suas permissões e os ids de projeto que pode ler.

Use a chave apenas a partir do seu próprio servidor. A API não envia cabeçalhos CORS, por isso uma página web não a pode chamar diretamente. Um painel no navegador deve chamar o seu backend, e o seu backend chama a API. Assim a chave nunca fica na página.

## URL base e formato

```
https://api.himoose.com/v1/
```

Tudo é JSON. Os nomes dos campos estão em camelCase e correspondem aos campos que o Hi, Moose MCP devolve. As horas estão em UTC no formato RFC 3339 e as datas em `YYYY-MM-DD`. O contrato completo está em [api.himoose.com/v1/openapi.json](https://api.himoose.com/v1/openapi.json) e importa-se no Postman, no Insomnia e em ferramentas semelhantes.

## Endpoints de leitura

| Endpoint | O que devolve |
|---|---|
| `GET /me` | A chave, as suas permissões e os ids de projeto legíveis |
| `GET /projects` | Projetos que a chave pode ler, com número de prompts acompanhados, motores e última execução |
| `GET /projects/{id}` | Um projeto |
| `GET /projects/{id}/capabilities` | O que o projeto pode fazer no seu plano: motores, cadências, limites, saldo restante, o computador anfitrião, se uma execução pode começar agora |
| `GET /projects/{id}/engines` | Os motores de IA que o projeto acompanha, com um `id` estável para os filtros |
| `GET /projects/{id}/topics` | Temas que agrupam os prompts, com o número de prompts |
| `GET /projects/{id}/prompts` | Prompts acompanhados com ids de tema, ids de motor e estado |
| `GET /projects/{id}/competitors` | Marcas concorrentes acompanhadas |
| `GET /projects/{id}/runs` | Execuções de visibilidade com estado, hora de início e fim, número de prompts e de respostas |
| `GET /projects/{id}/answers` | Respostas guardadas: prompt, motor, data, mencionada, citada, posição, sentimento, excerto, concorrentes vistos, URLs das fontes |
| `GET /projects/{id}/answers/{answerId}` | Uma resposta com o texto completo, o motivo do sentimento, o desvio narrativo e as fontes |
| `GET /projects/{id}/stats/daily` | Por dia e motor: respostas, menções, citações e as duas taxas |
| `GET /projects/{id}/stats/competitors` | Share of voice da sua marca e de cada concorrente acompanhado num período |
| `GET /projects/{id}/run-requests` | Execuções recentes iniciadas pela API e o seu estado |

### Exemplo: taxa de menção por dia

```bash
curl "https://api.himoose.com/v1/projects/PROJECT_ID/stats/daily?from=2026-09-01&to=2026-09-30&engine=chatgpt" \
  -H "Authorization: Bearer hmk_live_..."
```

```json
{
  "from": "2026-09-01",
  "to": "2026-09-30",
  "incompleteDays": 0,
  "data": [
    { "date": "2026-09-01", "engineId": "chatgpt", "answers": 42, "mentioned": 17, "cited": 9, "mentionRate": 0.405, "citationRate": 0.214 }
  ]
}
```

`incompleteDays` é maior do que zero quando o resumo de um dia ainda não estava pronto. Volte a chamar dentro de alguns segundos e ele completa-se.

## O computador anfitrião

O Hi, Moose executa parte do acompanhamento num dos seus próprios computadores, o **dispositivo anfitrião**, que escolhe no Hi, Moose em **Definições → Hi, Moose MCP**. Os motores de recolha local (ChatGPT, Gemini, Grok, Perplexity e Google AI Mode consultados através de um navegador) só correm aí, e o seu agendamento vive aí.

Cada alteração ao acompanhamento e cada execução pela API precisa de um dispositivo anfitrião escolhido para o projeto. Sem ele, a API responde `409 host_required` e indica a definição a alterar. Um projeto criado pela API usa o dispositivo anfitrião de outro projeto da conta quando existe um.

Nos planos com chave própria, os prompts, motores e agendamento ficam guardados no computador anfitrião e não na nuvem. A API pode lê-los e iniciar execuções, mas alterá-los responde `409 byok_not_supported`. Faça a gestão no Hi, Moose nesse computador.

## Gerir o acompanhamento

Precisa da permissão **gerir o acompanhamento**.

| Endpoint | O que faz |
|---|---|
| `POST /projects` | Cria um projeto a partir de um nome e um endereço de site, com termos de marca e domínios opcionais. O rastreio do site não é iniciado; o computador anfitrião ativa o rastreio semanal agendado para que aconteça mais tarde. O Brand Truth não é obrigatório. |
| `PATCH /projects/{id}` | Altera o nome, o endereço do site, os termos de marca ou os domínios de marca |
| `PUT /projects/{id}/competitors` | Substitui a lista de concorrentes acompanhados, no máximo 50 |
| `POST /projects/{id}/prompts` | Adiciona um prompt com ids de tema e ids de motor opcionais |
| `PATCH /projects/{id}/prompts/{promptId}` | Altera o texto, os temas ou os motores de um prompt |
| `DELETE /projects/{id}/prompts/{promptId}` | Deixa de acompanhar um prompt |
| `PUT /projects/{id}/tracking` | Define motores, cadência, hora, dia da semana, fuso horário e amostras por prompt. Os novos motores aplicam-se a todos os prompts a menos que `applyEnginesToPrompts` seja false. |

Cada escrita respeita os limites do plano: número de prompts, motores permitidos, cadências permitidas, número de projetos e de concorrentes. Acima de um limite a API responde `409 plan_limit` com o limite no corpo. Consulte primeiro `GET /projects/{id}/capabilities`.

### Exemplo: configurar o acompanhamento num projeto novo

```bash
curl -X POST https://api.himoose.com/v1/projects \
  -H "Authorization: Bearer hmk_live_..." -H "Content-Type: application/json" \
  -d '{"name":"Acme","websiteUrl":"https://acme.example","brandTerms":["Acme Cloud"]}'

curl -X POST https://api.himoose.com/v1/projects/PROJECT_ID/prompts \
  -H "Authorization: Bearer hmk_live_..." -H "Content-Type: application/json" \
  -d '{"text":"What are the best SAST tools?","topicIds":["sast"]}'

curl -X PUT https://api.himoose.com/v1/projects/PROJECT_ID/tracking \
  -H "Authorization: Bearer hmk_live_..." -H "Content-Type: application/json" \
  -d '{"engineIds":["chatgpt","gemini"],"cadence":"daily","timeOfDay":"09:00","timezone":"Europe/Lisbon"}'
```

## Iniciar uma execução

Precisa da permissão **iniciar execuções**.

```bash
curl -X POST https://api.himoose.com/v1/projects/PROJECT_ID/run-requests \
  -H "Authorization: Bearer hmk_live_..." -H "Idempotency-Key: nightly-2026-10-12"
```

A API responde `202 Accepted` com um pedido de execução e um cabeçalho `Location` para consultar. Estados:

| Estado | Significado |
|---|---|
| `queued` | Aceite e prestes a começar |
| `waiting_for_host` | O computador anfitrião está desligado. O Hi, Moose guarda o pedido até 24 horas e inicia a execução quando ele voltar. A resposta traz um `warning` a dizê-lo. |
| `running` | Em curso |
| `completed` | Concluída. `runIds` lista as execuções a passar aos endpoints runs e answers. |
| `failed` | Não terminou. `error.code` diz porquê, por exemplo `host_unavailable` após 24 horas. |

Os projetos cujos motores acompanhados são todos motores na nuvem correm na nuvem de imediato, sem o computador anfitrião. Qualquer motor de recolha local faz com que a execução passe para o computador anfitrião, pelo mesmo caminho do botão Executar agora.

Salvaguardas, para que uma execução nunca custe mais do que o esperado:

- **Primeiro o saldo.** A API estima o custo da execução em motores na nuvem a partir do número de prompts e motores. Se a estimativa for superior ao saldo restante, recusa com `409 insufficient_allowance`, a estimativa e as unidades restantes. Nada é gasto. `GET /projects/{id}/capabilities` mostra a mesma estimativa como `allowance.estimatedUnitsPerRun`.
- **Uma de cada vez.** Um segundo pedido enquanto outro está em fila, em espera ou em curso responde `409 run_in_progress` com o id do pedido ativo.
- **Limite diário.** No máximo 24 pedidos de execução por projeto por dia. Acima disso, a API responde `429 daily_run_limit`.
- **Idempotência.** Envie um cabeçalho `Idempotency-Key` e uma nova tentativa dentro de 24 horas devolve o mesmo pedido em vez de iniciar outro.

Uma execução pode demorar de alguns minutos a mais de uma hora em conjuntos de prompts grandes. Consulte o pedido mais ou menos a cada minuto, não a cada segundo.

## Filtros e paginação

- **Período:** `from` e `to` como `YYYY-MM-DD`, inclusivos, UTC. Por omissão são os últimos 30 dias. O período mais amplo num pedido é de 366 dias.
- **Motor:** `engine=chatgpt&engine=gemini` repete-se para vários motores. Os ids vêm do endpoint engines.
- **Respostas:** também `topicId`, `promptId`, `runId`, `mentioned=true|false` e `cited=true|false`. Combine `engine` com no máximo um de `promptId`, `topicId` ou `runId`.
- **Páginas:** as listas devolvem `{ "data": [...], "nextCursor": "..." }`. Passe `nextCursor` como `cursor` para obter a página seguinte. `limit` é 50 por omissão e 200 no máximo. `nextCursor` é `null` na última página.
- **Cache:** as respostas trazem um `ETag`. Devolva-o em `If-None-Match` para receber `304 Not Modified` quando nada mudou.

## Limites de pedidos

| Limite | Valor |
|---|---|
| Por chave | 60 pedidos por minuto |
| Por conta | 10.000 pedidos por dia |
| Pedidos de execução por projeto | 24 por dia, um de cada vez |
| Linhas por página | 200 |
| Período por pedido | 366 dias |

Acima do limite a API responde `429` com um cabeçalho `Retry-After`. Cada resposta traz `RateLimit-Policy`, e as respostas bem-sucedidas trazem `RateLimit` com o orçamento restante do dia.

## Erros

Os erros usam o formato Problem Details (`application/problem+json`) com um `code` estável:

```json
{
  "type": "https://himoose.com/docs/integrations/developer-api/#errors",
  "title": "Not found",
  "status": 404,
  "detail": "No project with that id is readable with this key.",
  "code": "not_found",
  "instance": "/v1/projects/abc123",
  "requestId": "7f4c0d1a2b"
}
```

| Código | Estado | Significado |
|---|---|---|
| `invalid_key`, `key_revoked`, `key_expired` | 401 | A chave falta, está mal formada, foi revogada ou expirou |
| `plan_required` | 403 | O plano da conta não inclui a API |
| `insufficient_scope` | 403 | A chave não tem a permissão para esta chamada |
| `not_found` | 404 | O recurso não existe, ou a chave não o pode ler |
| `invalid_parameter`, `range_too_wide`, `unsupported_filter_combination` | 400 | Um parâmetro ou um campo precisa de correção |
| `host_required` | 409 | Escolha primeiro um dispositivo anfitrião para o projeto no Hi, Moose |
| `byok_not_supported` | 409 | Neste plano as definições de acompanhamento vivem no computador anfitrião |
| `plan_limit` | 409 | Foi atingido um limite do plano; o corpo indica-o |
| `run_in_progress`, `insufficient_allowance`, `no_prompts` | 409 | A execução não pode começar agora; o corpo diz porquê |
| `rate_limited`, `daily_run_limit` | 429 | Aguarde os segundos indicados em `Retry-After` |

Indique o `requestId` quando contactar o suporte.

## O texto das respostas não é de confiança

O texto das respostas, os excertos e os títulos das fontes vêm dos motores de IA, não do Hi, Moose. Mostre-os como texto simples no seu painel, nunca como HTML, e não os passe às suas próprias ferramentas de IA como instruções.

## Webhooks

Em vez de consultar a API, registe um endpoint https e o Hi, Moose envia para lá um evento JSON assinado quando uma execução termina. Registar e apagar webhooks precisa da permissão **gerir o acompanhamento**. Listá-los, e às suas entregas, só precisa de leitura.

| Endpoint | O que faz |
|---|---|
| `POST /projects/{id}/webhooks` | Regista um endpoint. Corpo: `url` (https público), `events` (por omissão `run.completed` e `run.failed`), `description` opcional. O segredo de assinatura volta uma única vez nesta resposta. No máximo 5 por projeto. |
| `GET /projects/{id}/webhooks` | Lista os webhooks do projeto, sem segredos |
| `DELETE /projects/{id}/webhooks/{webhookId}` | Remove um |
| `POST /projects/{id}/webhooks/{webhookId}/test` | Envia já um evento `ping`, para verificar o seu endpoint e o código de assinatura |
| `GET /projects/{id}/webhooks/{webhookId}/deliveries` | As últimas 50 entregas com cada tentativa, estado e erro |

### O evento

```json
{
  "id": "wh_8f2a_run_abc123_run_completed",
  "event": "run.completed",
  "createdAt": "2026-10-12T09:14:03.000Z",
  "data": {
    "projectId": "abc123",
    "runId": "run_abc123",
    "requestId": "req_9d1e",
    "status": "completed",
    "trigger": "manual",
    "startedAt": "2026-10-12T09:01:10.000Z",
    "completedAt": "2026-10-12T09:14:02.000Z",
    "promptCount": 40,
    "answerCount": 118,
    "error": null,
    "links": {
      "run": "https://api.himoose.com/v1/projects/abc123/runs",
      "answers": "https://api.himoose.com/v1/projects/abc123/answers?runId=run_abc123",
      "stats": "https://api.himoose.com/v1/projects/abc123/stats/daily"
    }
  }
}
```

`data.requestId` vem preenchido quando a execução foi iniciada pela API, para poder ligar o evento ao seu pedido. `run.failed` traz `status` `failed` ou `canceled` e o texto de `error`.

### Verificar a assinatura

Cada chamada traz `X-HiMoose-Signature: t=<segundos unix>,v1=<hex>`, em que `v1` é o HMAC-SHA256 de `<t>.<corpo em bruto>` com o segredo do seu webhook. Verifique-a sobre o corpo em bruto antes de analisar o JSON e rejeite marcas temporais com mais de cinco minutos. A chamada traz também `X-HiMoose-Event` e `X-HiMoose-Delivery`.

```js
const crypto = require("node:crypto");

function verifyHiMooseSignature(rawBody, header, secret) {
  const parts = Object.fromEntries(header.split(",").map((part) => part.split("=")));
  if (!parts.t || !parts.v1) return false;
  if (Math.abs(Date.now() / 1000 - Number(parts.t)) > 300) return false;
  const expected = crypto.createHmac("sha256", secret).update(`${parts.t}.${rawBody}`).digest("hex");
  return expected.length === parts.v1.length && crypto.timingSafeEqual(Buffer.from(expected), Buffer.from(parts.v1));
}
```

### Regras de entrega

- Responda com um estado 2xx em 10 segundos. Os redirecionamentos não são seguidos.
- As entregas falhadas são repetidas após 1 minuto, 5 minutos, 30 minutos, 2 horas e 12 horas, 6 tentativas no total.
- Após 20 falhas consecutivas o webhook é desativado. Apague-o e registe-o de novo para retomar.
- Um evento pode chegar mais do que uma vez. Use `id` para ignorar repetições.
- O proprietário da conta vê todos os webhooks do projeto atual em **Definições → Hi, Moose REST API** e pode apagar um aí.

## O que vem a seguir

As alterações ao acompanhamento para planos com chave própria são o próximo passo. Tudo o resto documentado aqui está ativo.
