---
source_hash: 6467de19290f42e43d33241a37345989dbd6267011d89947d750f7e073ea66e2
---
!!! note "Tradução automática"
    Esta página foi traduzida por IA. A versão em inglês é a versão oficial.

    [Ler em inglês](https://himoose.com/docs/integrations/developer-api/webhooks/)


# Webhooks

Em vez de consultar a API repetidamente, registre um endpoint https e o Hi, Moose envia para lá um evento JSON assinado quando uma execução termina. Registrar, testar e excluir webhooks precisa da permissão **gerenciar o acompanhamento**. Listá-los, e às suas entregas, só precisa de leitura.

## Endpoints

| Endpoint | O que faz |
|---|---|
| `POST /projects/{id}/webhooks` | Registra um endpoint. Corpo: `url` (https público), `events` (padrão `run.completed` e `run.failed`), `description` opcional. O segredo de assinatura volta uma única vez nesta resposta. No máximo 5 por projeto. |
| `GET /projects/{id}/webhooks` | Lista os webhooks do projeto, sem segredos |
| `DELETE /projects/{id}/webhooks/{webhookId}` | Remove um |
| `POST /projects/{id}/webhooks/{webhookId}/test` | Envia um evento `ping` agora, para verificar o seu endpoint e o código de assinatura |
| `GET /projects/{id}/webhooks/{webhookId}/deliveries` | As últimas 50 entregas com cada tentativa, status e erro |

## Registrar um

```bash
curl -X POST https://api.himoose.com/v1/projects/PROJECT_ID/webhooks \
  -H "Authorization: Bearer hmk_live_..." -H "Content-Type: application/json" \
  -d '{"url":"https://reports.acme.example/himoose","description":"Nightly dashboard refresh"}'
```

```json
{
  "id": "BGXhe1dlOnmy36j6rRTa",
  "url": "https://reports.acme.example/himoose",
  "events": ["run.completed", "run.failed"],
  "description": "Nightly dashboard refresh",
  "active": true,
  "createdAt": "2026-10-15T03:20:10.000Z",
  "secret": "whsec_..."
}
```

Guarde `secret` junto com a sua chave. Ele só é mostrado nesta resposta. A URL precisa ser pública e usar https; endereços privados, localhost e http simples são recusados com `400 invalid_parameter`.

Depois envie um ping para você mesmo:

```bash
curl -X POST https://api.himoose.com/v1/projects/PROJECT_ID/webhooks/WEBHOOK_ID/test \
  -H "Authorization: Bearer hmk_live_..."
```

A resposta é o registro da entrega, e o endpoint deliveries mostra a tentativa com o status HTTP que o seu endpoint respondeu.

## O evento

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

| Evento | Quando |
|---|---|
| `run.completed` | Uma execução terminou e suas respostas estão salvas. Contam as execuções agendadas, as do botão Executar agora e as da API. |
| `run.failed` | Uma execução terminou com `status` `failed` ou `canceled`. `data.error` diz por quê. |
| `ping` | Enviado pelo endpoint de teste. `data` traz o id do projeto e uma mensagem. |

`data.requestId` vem preenchido quando a execução foi iniciada pela API, então você pode ligar o evento ao seu pedido de execução. Ele é `null` nas execuções agendadas e nas iniciadas no Hi, Moose.

O evento é um sinal, não os dados. Em `run.completed`, siga `data.links.answers` ou atualize suas estatísticas diárias. Os resumos diários dos dias da execução são reconstruídos em até dez minutos depois que a execução termina; `incompleteDays` na resposta das estatísticas indica quando eles ainda não estão prontos.

## Cabeçalhos

| Cabeçalho | Valor |
|---|---|
| `X-HiMoose-Signature` | `t=<unix seconds>,v1=<hex>`, veja abaixo |
| `X-HiMoose-Event` | O nome do evento |
| `X-HiMoose-Delivery` | O id da entrega, o mesmo do endpoint deliveries |
| `User-Agent` | `HiMoose-Webhooks/1.0` |
| `Content-Type` | `application/json` |

## Verificar a assinatura

`v1` é o HMAC-SHA256 de `<t>.<raw body>` com o segredo do seu webhook, como string hexadecimal em minúsculas. Verifique-a sobre o corpo bruto da requisição antes de interpretar o JSON, compare em tempo constante e rejeite timestamps com mais de cinco minutos.

=== "JavaScript"

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

=== "Python"

    ```python
    import hashlib
    import hmac
    import time

    def verify_himoose_signature(raw_body: bytes, header: str, secret: str) -> bool:
        parts = dict(part.split("=", 1) for part in header.split(",") if "=" in part)
        if "t" not in parts or "v1" not in parts:
            return False
        if abs(time.time() - int(parts["t"])) > 300:
            return False
        expected = hmac.new(secret.encode(), f"{parts['t']}.".encode() + raw_body, hashlib.sha256).hexdigest()
        return hmac.compare_digest(expected, parts["v1"])
    ```

A maioria dos frameworks web interpreta o JSON antes de o seu código rodar. Garanta que você assina os bytes como foram recebidos, não uma cópia serializada de novo, ou a assinatura não vai bater.

## Regras de entrega

- Responda com um status 2xx em até 10 segundos. Faça o trabalho depois de responder, não antes. Redirecionamentos não são seguidos.
- Entregas que falharam são repetidas depois de 1 minuto, 5 minutos, 30 minutos, 2 horas e 12 horas, 6 tentativas no total. Uma entrega fica `pending` enquanto restam tentativas, `delivered` depois de um 2xx e `failed` depois da última tentativa.
- Depois de 20 falhas consecutivas o webhook é desativado, `active` vira false e nenhum outro evento é enviado. Exclua-o e registre-o de novo para retomar.
- Um evento pode chegar mais de uma vez. Use `id` para ignorar repetições.
- Os eventos de um projeto podem chegar fora de ordem quando há uma nova tentativa no meio. Use `createdAt` se a ordem importar.

## Ver as entregas

```bash
curl https://api.himoose.com/v1/projects/PROJECT_ID/webhooks/WEBHOOK_ID/deliveries \
  -H "Authorization: Bearer hmk_live_..."
```

Cada entrega lista todas as tentativas com a hora, o status HTTP que o seu endpoint respondeu, quanto tempo levou e qualquer erro. Quando um endpoint se comporta mal, este é o primeiro lugar para olhar.

O proprietário da conta vê todos os webhooks do projeto atual em **Configurações → Hi, Moose REST API** com o status da última entrega, e pode excluir um por lá.
