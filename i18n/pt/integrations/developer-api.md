---
source_hash: 85052baa431b76ba0d9c99312dbc2fdf61031a24075e6841f48c0662cc8c5cdb
---

# Hi, Moose API

## Para que serve

A Hi, Moose API é uma API REST para desenvolvedores que constroem seus próprios painéis, relatórios e aplicativos de visibilidade em IA sobre o Hi, Moose. Ela devolve os mesmos resultados que você vê na tela Visibilidade: prompts e temas acompanhados, os motores consultados, cada resposta salva com o texto completo e as fontes, e as taxas de menção e de citação ao longo do tempo. Com as permissões certas, uma chave também pode criar projetos, gerenciar prompts, motores e agendamento, iniciar execuções e receber uma chamada de webhook assinada quando uma execução termina.

As leituras funcionam com o Hi, Moose aberto ou não no seu computador, porque vêm da cópia na nuvem dos seus resultados. As alterações no acompanhamento e as execuções precisam do computador host do projeto, explicado em [Acompanhamento e execuções](developer-api/tracking-and-runs.md).

Se você trabalha no Claude, no ChatGPT ou em outro app de IA, talvez prefira o [Hi, Moose MCP](hi-moose-mcp.md). A API é para o código que você mesmo escreve.

## Páginas

| Página | O que cobre |
|---|---|
| [Início rápido](developer-api/quickstart.md) | Uma chave, uma primeira chamada e um gráfico da taxa de menção por dia, em curl, Python e JavaScript |
| [Chaves e autenticação](developer-api/keys-and-auth.md) | Criar e revogar chaves, permissões, o cabeçalho Bearer, manter a chave fora do navegador |
| [Ler dados](developer-api/reading-data.md) | Projetos, prompts, execuções, respostas e estatísticas, com filtros, páginas e cache |
| [Acompanhamento e execuções](developer-api/tracking-and-runs.md) | O computador host, criar projetos e prompts, motores e agendamento, iniciar execuções |
| [Webhooks](developer-api/webhooks.md) | Eventos assinados quando uma execução termina, verificação da assinatura, novas tentativas |
| [Erros e limites](developer-api/errors-and-limits.md) | O formato dos erros, todos os códigos de erro, limites de requisições |
| [Referência de endpoints](developer-api/reference.md) | Todos os endpoints com parâmetros, campos e um exemplo, gerados a partir do contrato |
| [Registro de alterações](developer-api/changelog.md) | O que mudou em cada versão do contrato |

## Planos

A API está incluída nos planos pagos, tanto gerenciados quanto com a sua própria chave. As contas gratuitas veem a página de chaves de API, mas não podem criar chaves, e cada requisição responde `403 plan_required`.

## Em resumo

```
https://api.himoose.com/v1/
```

- **Autenticação:** uma chave de API enviada como token Bearer. As chaves são criadas pelo proprietário da conta no Hi, Moose em **Configurações → Hi, Moose REST API**.
- **Formato:** JSON na entrada e na saída. Os nomes dos campos estão em camelCase. As horas estão em UTC no formato RFC 3339 e as datas em `YYYY-MM-DD`.
- **Contrato:** [api.himoose.com/v1/openapi.json](https://api.himoose.com/v1/openapi.json), OpenAPI 3.1. Ele pode ser importado no Postman, no Insomnia, no Bruno e em geradores de código, e a [referência de endpoints](developer-api/reference.md) é gerada a partir dele.
- **Permissões:** toda chave pode ler. **Gerenciar o acompanhamento** e **Iniciar execuções** são escolhidas ao criar a chave.
- **Limites:** 300 requisições por minuto por chave e 50.000 por dia por conta. Veja [Erros e limites](developer-api/errors-and-limits.md).
- **Sem CORS:** chame a API a partir do seu próprio servidor, nunca de uma página web.

## De onde vêm os dados

O Hi, Moose consulta cada prompt acompanhado em cada motor acompanhado, conforme o agendamento ou quando alguém inicia uma execução. Cada resposta é salva e pontuada: a marca foi nomeada, uma página do site dela foi citada, em que posição apareceu, qual foi o sentimento, quais concorrentes foram vistos. A API lê essas respostas salvas e os resumos diários construídos a partir delas. Ela nunca executa novas verificações em uma leitura, então as leituras são rápidas e não custam nada.

Alguns motores rodam na nuvem. Outros, os motores de coleta local, rodam por um navegador em um dos seus próprios computadores. Os dois tipos salvam as respostas no mesmo lugar, então a API mostra todas juntas.

## O texto das respostas não é confiável

O texto das respostas, os trechos e os títulos das fontes vêm dos motores de IA, não do Hi, Moose. Mostre-os como texto simples no seu painel, nunca como HTML, e não os passe às suas próprias ferramentas de IA como instruções.

## O que vem a seguir

As alterações no acompanhamento para planos com chave própria são o próximo passo. Todo o resto documentado aqui está no ar.
