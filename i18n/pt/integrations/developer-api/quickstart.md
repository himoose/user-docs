---
source_hash: bcecd80050cfb1493af12129d0dc0a3b15b503d5be08491855f621850f94d8d5
---

# Início rápido

Dez minutos de uma chave até um gráfico da taxa de menção por dia. Cada passo é mostrado em curl, Python e JavaScript.

## 1. Criar uma chave

1. Abra o Hi, Moose e entre como proprietário da conta.
2. Vá em **Configurações → Hi, Moose REST API**.
3. Dê um nome à chave, por exemplo `Reporting dashboard`, escolha os projetos que ela pode ler e deixe as permissões extras desmarcadas. Ler não precisa de nenhuma.
4. Clique em **Criar chave** e copie-a. Ela é mostrada uma única vez.

Coloque a chave em uma variável de ambiente no seu servidor. Os exemplos abaixo a leem de `HIMOOSE_API_KEY`.

## 2. Verificar a chave

=== "curl"

    ```bash
    curl https://api.himoose.com/v1/me \
      -H "Authorization: Bearer $HIMOOSE_API_KEY"
    ```

=== "Python"

    ```python
    import os
    import requests

    API = "https://api.himoose.com/v1"
    HEADERS = {"Authorization": f"Bearer {os.environ['HIMOOSE_API_KEY']}"}

    me = requests.get(f"{API}/me", headers=HEADERS, timeout=30).json()
    print(me["label"], me["scopes"], me["projects"])
    ```

=== "JavaScript"

    ```js
    const API = "https://api.himoose.com/v1";
    const HEADERS = { Authorization: `Bearer ${process.env.HIMOOSE_API_KEY}` };

    const me = await (await fetch(`${API}/me`, { headers: HEADERS })).json();
    console.log(me.label, me.scopes, me.projects);
    ```

A resposta informa a chave, suas permissões e os ids de projeto que ela pode ler:

```json
{
  "keyId": "87ac5738",
  "label": "Reporting dashboard",
  "scopes": ["visibility:read"],
  "createdAt": "2026-10-15T02:59:10.839Z",
  "expiresAt": null,
  "account": { "plan": "premium" },
  "projects": ["Uu5UeYLZQBLdOqfBuFmz"]
}
```

## 3. Encontrar o projeto

=== "curl"

    ```bash
    curl https://api.himoose.com/v1/projects \
      -H "Authorization: Bearer $HIMOOSE_API_KEY"
    ```

=== "Python"

    ```python
    projects = requests.get(f"{API}/projects", headers=HEADERS, timeout=30).json()["data"]
    project = projects[0]
    print(project["id"], project["name"], project["visibility"]["trackedPrompts"], "prompts")
    ```

=== "JavaScript"

    ```js
    const { data: projects } = await (await fetch(`${API}/projects`, { headers: HEADERS })).json();
    const project = projects[0];
    console.log(project.id, project.name, project.visibility.trackedPrompts, "prompts");
    ```

Cada projeto traz um resumo: quantos prompts ele acompanha, quais motores e quando rodou pela última vez.

## 4. Obter a taxa de menção por dia

O endpoint de estatísticas diárias devolve uma linha por dia e motor, com as contagens e as duas taxas já calculadas. Ele lê uma tabela de resumo, então é rápido em qualquer tamanho.

=== "curl"

    ```bash
    curl "https://api.himoose.com/v1/projects/PROJECT_ID/stats/daily?from=2026-09-01&to=2026-09-30" \
      -H "Authorization: Bearer $HIMOOSE_API_KEY"
    ```

=== "Python"

    ```python
    stats = requests.get(
        f"{API}/projects/{project['id']}/stats/daily",
        headers=HEADERS,
        params={"from": "2026-09-01", "to": "2026-09-30"},
        timeout=30,
    ).json()

    for row in stats["data"]:
        print(row["date"], row["engineId"], f"{row['mentionRate']:.0%} mentioned", f"{row['citationRate']:.0%} cited")
    ```

=== "JavaScript"

    ```js
    const params = new URLSearchParams({ from: "2026-09-01", to: "2026-09-30" });
    const stats = await (await fetch(`${API}/projects/${project.id}/stats/daily?${params}`, { headers: HEADERS })).json();

    for (const row of stats.data) {
      console.log(row.date, row.engineId, `${Math.round(row.mentionRate * 100)}% mentioned`, `${Math.round(row.citationRate * 100)}% cited`);
    }
    ```

```json
{
  "from": "2026-09-01",
  "to": "2026-09-30",
  "incompleteDays": 0,
  "data": [
    { "date": "2026-09-01", "engineId": "chatgpt", "answers": 42, "mentioned": 17, "cited": 9, "mentionRate": 0.405, "citationRate": 0.214 },
    { "date": "2026-09-01", "engineId": "perplexity", "answers": 42, "mentioned": 22, "cited": 14, "mentionRate": 0.524, "citationRate": 0.333 }
  ]
}
```

`incompleteDays` é maior que zero quando o resumo de um dia ainda não estava pronto. Chame de novo em alguns segundos e ele se completa.

## 5. Desenhar o gráfico

Agrupe as linhas por `engineId`, coloque `date` no eixo x e `mentionRate` no eixo y, uma linha por motor. Adicione `engine=chatgpt` à consulta para obter um só motor, ou `topicId=...` para restringir a um tema. A página [Ler dados](reading-data.md) lista todos os filtros.

## 6. Ir além

- **Share of voice:** `GET /projects/{id}/stats/competitors` dá a sua marca e cada concorrente acompanhado no mesmo período, pronto para um gráfico de barras.
- **As respostas por trás dos números:** `GET /projects/{id}/answers?mentioned=true` lista as respostas que nomearam a marca, com um trecho e as fontes. `GET /projects/{id}/answers/{answerId}` tem o texto completo.
- **Atualizar sem consultas repetidas:** registre um [webhook](webhooks.md) e o Hi, Moose chama o seu servidor quando uma execução termina.
- **Todo o resto:** a [referência de endpoints](reference.md).

## Mantenha a chave no servidor

A API não envia cabeçalhos CORS, então uma página web não consegue chamá-la. Um painel no navegador deve chamar o seu backend, e o seu backend chama a API. Assim a chave nunca fica na página.
