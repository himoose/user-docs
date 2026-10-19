---
source_hash: 638e427715918eeab4249561f6f095b46f57a8531e8ee857a78f4e07d0941c4e
---
!!! note "Tradução automática"
    Esta página foi traduzida por IA. A versão em inglês é a versão oficial.

    [Ler em inglês](https://himoose.com/docs/integrations/developer-api/tracking-and-runs/)


# Acompanhamento e execuções

Alterar o que o Hi, Moose acompanha precisa da permissão **gerenciar o acompanhamento**. Iniciar uma execução precisa da permissão **iniciar execuções**. As duas são escolhidas ao criar a chave, veja [Chaves e autenticação](keys-and-auth.md#permissions).

## O computador host

O Hi, Moose roda parte do acompanhamento em um dos seus próprios computadores, o **dispositivo host**, que você escolhe no Hi, Moose em **Configurações → Hi, Moose MCP**. Os motores de coleta local (ChatGPT, Gemini, Grok, Perplexity e Google AI Mode consultados por um navegador) só rodam lá, e o agendamento deles vive lá.

Toda alteração no acompanhamento e toda execução pela API precisa de um dispositivo host escolhido para o projeto. Sem ele, a API responde `409 host_required` e informa a configuração a alterar. Um projeto criado pela API usa o dispositivo host de outro projeto da conta quando existe um.

Depois de uma alteração no acompanhamento, a API entrega ao computador host uma pequena tarefa para buscar as novas configurações. O host faz isso em até um minuto enquanto o Hi, Moose estiver aberto nele, ou na próxima vez que abrir. De qualquer forma, as leituras mostram as novas configurações na hora.

Nos planos com chave própria, os prompts, motores e agendamento ficam salvos no computador host e não na nuvem. A API pode lê-los e iniciar execuções, mas alterá-los responde `409 byok_not_supported`. Gerencie-os no Hi, Moose nesse computador.

`GET /projects/{id}/capabilities` diz antes de você escrever: o plano, os motores e cadências permitidos, os limites, o computador host e se ele está online, e se uma execução poderia começar agora.

## Gerenciar o acompanhamento

| Endpoint | O que faz |
|---|---|
| `POST /projects` | Cria um projeto a partir de um nome e um endereço de site, com termos de marca e domínios opcionais. O rastreamento do site não é iniciado; o computador host ativa o rastreamento semanal agendado para que ele aconteça mais tarde. O Brand Truth não é obrigatório. |
| `PATCH /projects/{id}` | Altera o nome, o endereço do site, os termos de marca ou os domínios de marca |
| `PUT /projects/{id}/competitors` | Substitui a lista de concorrentes acompanhados, no máximo 50 |
| `POST /projects/{id}/prompts` | Adiciona um prompt com ids de tema e ids de motor opcionais |
| `PATCH /projects/{id}/prompts/{promptId}` | Altera o texto, os temas ou os motores de um prompt, ou retoma um prompt pausado |
| `DELETE /projects/{id}/prompts/{promptId}` | Para de acompanhar um prompt. As respostas salvas são mantidas. |
| `PUT /projects/{id}/tracking` | Define os motores padrão, a cadência, a hora, o dia da semana, o fuso horário e as amostras por prompt |

Toda escrita respeita os limites do plano: número de prompts, motores permitidos, cadências permitidas, número de projetos e de concorrentes. Acima de um limite a API responde `409 plan_limit` com o limite no corpo.

### Motores nos prompts

Cada prompt tem sua própria lista de motores. `PUT /projects/{id}/tracking` com `engineIds` define o padrão para os prompts adicionados depois e deixa todos os prompts existentes como estão. Para alterar os motores dos prompts existentes, envie `applyEnginesToPrompts: true` na mesma chamada, o que define a nova lista em todos os prompts do projeto, ou altere os prompts um a um com `PATCH /projects/{id}/prompts/{promptId}`.

Um prompt sem motores é mantido, mas pulado nas execuções. `POST /projects/{id}/prompts` sem `engineIds` dá ao novo prompt os motores padrão do projeto.

### Substituir é substituir

`PUT /projects/{id}/competitors` substitui a lista inteira. Envie a lista completa que você quer manter, não só as adições. Uma lista vazia remove todos os concorrentes. O mesmo vale para `brandTerms` e `brandDomains` em `PATCH /projects/{id}`.

### Exemplo: configurar o acompanhamento em um projeto novo

```bash
curl -X POST https://api.himoose.com/v1/projects \
  -H "Authorization: Bearer hmk_live_..." -H "Content-Type: application/json" \
  -d '{"name":"Acme","websiteUrl":"https://acme.example","brandTerms":["Acme Cloud"]}'

curl -X PUT https://api.himoose.com/v1/projects/PROJECT_ID/tracking \
  -H "Authorization: Bearer hmk_live_..." -H "Content-Type: application/json" \
  -d '{"engineIds":["chatgpt","gemini"],"cadence":"daily","timeOfDay":"09:00","timezone":"America/Chicago"}'

curl -X POST https://api.himoose.com/v1/projects/PROJECT_ID/prompts \
  -H "Authorization: Bearer hmk_live_..." -H "Content-Type: application/json" \
  -d '{"text":"What are the best SAST tools?","topicIds":["sast"]}'

curl -X PUT https://api.himoose.com/v1/projects/PROJECT_ID/competitors \
  -H "Authorization: Bearer hmk_live_..." -H "Content-Type: application/json" \
  -d '[{"name":"Competitor One","domain":"competitor-one.example"},{"name":"Competitor Two","domain":"competitor-two.example"}]'
```

Definir os motores antes de adicionar prompts faz com que cada novo prompt os receba como padrão.

### Agendamento

| Campo | Valores |
|---|---|
| `cadence` | `manual` (agendamento desligado), `daily`, `weekdays`, `weekly` |
| `timeOfDay` | `HH:MM` no fuso horário do projeto |
| `weeklyDay` | `monday` a `sunday`, usado por `weekly` |
| `timezone` | Um nome IANA como `Europe/Berlin` |
| `samplesPerPrompt` | Quantas vezes cada prompt é consultado por motor em uma execução. Mais amostras gastam mais saldo. |

O plano decide quais cadências são permitidas; o endpoint capabilities as lista.

## Iniciar uma execução

```bash
curl -X POST https://api.himoose.com/v1/projects/PROJECT_ID/run-requests \
  -H "Authorization: Bearer hmk_live_..." -H "Idempotency-Key: nightly-2026-10-12"
```

A API responde `202 Accepted` com um pedido de execução e um cabeçalho `Location` para consultar:

```json
{
  "id": "NKxlhmW52Pkc2QwVD4oP",
  "status": "queued",
  "mode": "host",
  "createdAt": "2026-10-15T03:39:56.404Z",
  "updatedAt": "2026-10-15T03:39:56.404Z",
  "completedAt": null,
  "runIds": [],
  "promptCount": 5,
  "estimatedUnits": 0,
  "warning": null,
  "error": null,
  "host": { "online": true, "lastSeenAt": "2026-10-15T03:39:20.475Z" }
}
```

| Status | Significado |
|---|---|
| `queued` | Aceito e prestes a começar |
| `waiting_for_host` | O computador host está desligado. O Hi, Moose guarda o pedido por até 24 horas e inicia a execução quando ele voltar. A resposta traz um `warning` dizendo isso. |
| `running` | Em andamento |
| `completed` | Concluída. `runIds` lista as execuções a passar aos endpoints runs e answers. |
| `failed` | Não terminou. `error.code` diz por quê, por exemplo `host_unavailable` depois de 24 horas. |
| `canceled` | Interrompida a partir do Hi, Moose antes de terminar |

`mode` diz onde a execução roda. Projetos cujos motores acompanhados são todos motores na nuvem rodam na nuvem na hora, sem o computador host. Qualquer motor de coleta local faz a execução passar para o computador host, pelo mesmo caminho do botão Executar agora. Nos dois casos o projeto precisa de um computador host escolhido.

### Salvaguardas

Para que uma execução nunca custe mais do que você espera:

- **Primeiro o saldo.** A API estima o custo da execução em motores na nuvem a partir do número de prompts e motores. Se a estimativa for maior que o saldo restante, ela recusa com `409 insufficient_allowance`, a estimativa e as unidades restantes. Nada é gasto. `GET /projects/{id}/capabilities` mostra a mesma estimativa como `allowance.estimatedUnitsPerRun`.
- **Uma de cada vez.** Um segundo pedido enquanto outro está na fila, em espera ou em andamento responde `409 run_in_progress` com o id do pedido ativo.
- **Limite diário.** No máximo 24 pedidos de execução por projeto por dia. Acima disso, a API responde `429 daily_run_limit`.
- **Idempotência.** Envie um cabeçalho `Idempotency-Key` e uma nova tentativa dentro de 24 horas devolve o mesmo pedido com `200` e `replayed: true` em vez de iniciar outra execução.
- **Algo para rodar.** Um projeto sem nenhum prompt com motor responde `409 no_prompts`.

### Acompanhar uma execução

Consulte `GET /projects/{id}/run-requests/{requestId}` mais ou menos a cada minuto. Uma execução pode levar de alguns minutos a mais de uma hora em conjuntos de prompts grandes. Quando `status` for `completed`, `runIds` tem a execução a ler:

```bash
curl "https://api.himoose.com/v1/projects/PROJECT_ID/answers?runId=RUN_ID" \
  -H "Authorization: Bearer hmk_live_..."
```

Para evitar consultas repetidas, registre um [webhook](webhooks.md). O evento `run.completed` traz `requestId`, então você pode ligá-lo ao pedido que fez.

As execuções iniciadas pela API aparecem no Hi, Moose como qualquer outra execução, e na tabela **Trabalhos recentes de agentes** em **Configurações → Hi, Moose MCP** com o nome da chave.
