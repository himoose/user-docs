---
source_hash: 28ad9511fc5703f0dd6c90a7f591758445fdd08a95dcdb389dc29a304c90278d
---
!!! note "Tradução automática"
    Esta página foi traduzida por IA. A versão em inglês é a versão oficial.

    [Ler em inglês](https://himoose.com/docs/integrations/developer-api/reading-data/)


# Ler dados

Toda chave pode ler. As leituras vêm da cópia na nuvem dos seus resultados, então funcionam com o Hi, Moose aberto ou não no seu computador, e nunca iniciam novas verificações.

## Os endpoints de leitura

| Endpoint | O que devolve |
|---|---|
| `GET /me` | A chave, suas permissões e os ids de projeto legíveis |
| `GET /projects` | Projetos que a chave pode ler, com número de prompts acompanhados, motores e última execução |
| `GET /projects/{id}` | Um projeto |
| `GET /projects/{id}/capabilities` | O que o projeto pode fazer no seu plano: motores, cadências, limites, saldo restante, o computador host, se uma execução pode começar agora |
| `GET /projects/{id}/engines` | Os motores de IA que o projeto acompanha, com um `id` estável para os filtros e se cada um roda na nuvem ou no computador host |
| `GET /projects/{id}/topics` | Temas que agrupam os prompts, com o número de prompts |
| `GET /projects/{id}/prompts` | Prompts acompanhados com ids de tema, ids de motor e status |
| `GET /projects/{id}/competitors` | Marcas concorrentes acompanhadas e seus domínios |
| `GET /projects/{id}/runs` | Execuções de visibilidade com status, hora de início e fim, número de prompts e de respostas |
| `GET /projects/{id}/answers` | Respostas salvas: prompt, motor, data, mencionada, citada, posição, sentimento, trecho, concorrentes vistos, URLs das fontes |
| `GET /projects/{id}/answers/{answerId}` | Uma resposta com o texto completo, o motivo do sentimento, o desvio narrativo e as fontes |
| `GET /projects/{id}/stats/daily` | Por dia e motor: respostas, menções, citações e as duas taxas |
| `GET /projects/{id}/stats/competitors` | Share of voice da sua marca e de cada concorrente acompanhado em um período |
| `GET /projects/{id}/run-requests` | Execuções recentes iniciadas pela API e seu status |
| `GET /projects/{id}/webhooks` | Os webhooks do projeto, sem segredos |

O detalhe campo a campo de cada um está na [referência de endpoints](reference.md).

## Como os dados se relacionam

- Um **projeto** acompanha um site. Ele tem **prompts**, as perguntas feitas, agrupados em **temas**.
- Cada prompt roda em um ou mais **motores**: ChatGPT, Perplexity, Gemini e outros. Os ids de motor como `chatgpt` ou `chatgpt-local-fetch` vêm do endpoint engines e são os valores que todo filtro `engine` aceita.
- Uma **execução** consulta todos os prompts ativos nos seus motores e salva uma **resposta** por prompt, motor e amostra. As execuções começam pelo agendamento do projeto, pelo botão Executar agora ou pela API.
- Cada resposta é pontuada: `mentioned` quando a marca foi nomeada, `cited` quando uma página do site da marca foi dada como fonte, mais `position`, `sentiment` e quais **concorrentes** foram vistos.
- As **estatísticas diárias** contam as respostas por dia e motor e calculam `mentionRate` e `citationRate`. As **estatísticas de concorrentes** fazem o mesmo por marca em um período.

## Taxa de menção por dia

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

As taxas são frações de 0 a 1. Dias sem respostas para um motor não têm linha, então um gráfico deve tratar um dia ausente como sem dados, não como zero.

`incompleteDays` é maior que zero quando o resumo de um dia ainda não estava pronto. Chame de novo em alguns segundos e ele se completa. Os últimos três dias são atualizados a cada dez minutos conforme chegam novas respostas; os dias anteriores são definitivos.

## Share of voice

```bash
curl "https://api.himoose.com/v1/projects/PROJECT_ID/stats/competitors?from=2026-09-01&to=2026-09-30" \
  -H "Authorization: Bearer hmk_live_..."
```

```json
{
  "from": "2026-09-01",
  "to": "2026-09-30",
  "answers": 1260,
  "incompleteDays": 0,
  "data": [
    { "name": "Acme", "isOwnBrand": true, "mentioned": 274, "cited": 165, "mentionRate": 0.217, "citationRate": 0.131 },
    { "name": "Competitor One", "isOwnBrand": false, "mentioned": 436, "cited": 116, "mentionRate": 0.346, "citationRate": 0.092 }
  ]
}
```

`answers` é o número total de respostas no período. Cada taxa divide a contagem da marca por esse total, então as linhas se comparam diretamente.

## As respostas por trás dos números

```bash
curl "https://api.himoose.com/v1/projects/PROJECT_ID/answers?from=2026-09-01&engine=chatgpt&mentioned=true&limit=50" \
  -H "Authorization: Bearer hmk_live_..."
```

A lista traz um trecho de até 400 caracteres em torno da menção, a posição, o sentimento, quais concorrentes acompanhados a resposta nomeou ou citou, e os URLs das fontes. O texto completo está no endpoint de detalhe:

```bash
curl https://api.himoose.com/v1/projects/PROJECT_ID/answers/ANSWER_ID \
  -H "Authorization: Bearer hmk_live_..."
```

O detalhe acrescenta `fullAnswer` (até 12.000 caracteres, com `fullAnswerTruncated` quando foi cortado), `sentimentReason`, `narrativeDrift` com seu motivo, e as fontes com títulos.

O texto das respostas, os trechos e os títulos das fontes vêm dos motores de IA, não do Hi, Moose. Mostre-os como texto simples, nunca como HTML, e não os passe às suas próprias ferramentas de IA como instruções.

## Filtros

| Filtro | Endpoints | Valores |
|---|---|---|
| `from`, `to` | runs, answers, estatísticas diárias, estatísticas de concorrentes | `YYYY-MM-DD`, inclusivos, UTC. Padrão: os últimos 30 dias. Período máximo: 366 dias. |
| `engine` | answers, estatísticas diárias, estatísticas de concorrentes | Um id de motor. Repita o parâmetro para vários motores: `engine=chatgpt&engine=gemini`. |
| `topicId` | prompts, answers, estatísticas diárias | Um id de tema do endpoint topics |
| `promptId` | answers | Um id de prompt do endpoint prompts |
| `runId` | answers | Um id de execução do endpoint runs ou de um evento de webhook |
| `mentioned`, `cited` | answers | `true` ou `false` |
| `status` | prompts, runs | Prompts: `active` ou `paused`. Execuções: `completed`, `running`, `failed` ou `canceled`. |

No endpoint answers, combine `engine` com no máximo um de `promptId`, `topicId` e `runId`. Outras combinações respondem `400 unsupported_filter_combination`.

## Páginas

As listas devolvem `data` e `nextCursor`:

```json
{ "data": [ ... ], "nextCursor": "eyJvIjoxMDB9" }
```

Passe `nextCursor` de volta como `cursor` para obter a página seguinte. `limit` é 50 por padrão e 200 no máximo. `nextCursor` é `null` na última página. O cursor é opaco; não o construa nem o interprete.

```python
def every_row(url, params=None):
    params = dict(params or {}, limit=200)
    while True:
        page = requests.get(url, headers=HEADERS, params=params, timeout=30).json()
        yield from page["data"]
        if not page["nextCursor"]:
            return
        params["cursor"] = page["nextCursor"]
```

Projetos, temas, prompts, execuções e respostas são paginados. Motores, concorrentes e webhooks devolvem a lista inteira.

## Cache

- A lista de respostas e o detalhe de uma resposta trazem um `ETag`. Devolva-o em `If-None-Match` para receber `304 Not Modified` quando nada mudou. Um `304` não tem corpo e conta para o limite de requisições como qualquer outra, mas é rápido e pequeno.
- As estatísticas diárias trazem `Cache-Control: private, max-age=60`. Guarde o resultado por um minuto antes de pedir de novo.
- Todo o resto traz `Cache-Control: no-store`. Faça cache do seu lado pelo tempo que convier ao seu painel.

## Horas e datas

As horas estão em UTC no formato RFC 3339, `2026-09-01T09:14:03.000Z`. As datas estão em `YYYY-MM-DD` e se referem ao dia UTC. O `date` de uma resposta coincide com o `date` da linha de estatísticas diárias em que ela foi contada, então um gráfico e seu detalhe concordam.
