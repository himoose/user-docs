---
source_hash: f262de43811a037ebe40f0f411828409a4bc1eda0f592f12d08358e5530d41e6
---
!!! note "Tradução automática"
    Esta página foi traduzida por IA. A versão em inglês é a versão oficial.

    [Ler em inglês](https://himoose.com/docs/integrations/hi-moose-mcp/security/)


# Segurança e tratamento de dados

Esta página é para as pessoas que analisam um conector antes de uma equipe conectá-lo. Ela descreve como o Hi, Moose MCP funciona hoje, na ordem em que uma análise de segurança costuma perguntar. Última verificação contra o servidor em produção: 2026-10-19.

## Respostas curtas

| Pergunta | Resposta |
|---|---|
| Quem opera o servidor? | O Hi, Moose, fabricante do app. Não um terceiro. |
| A lista de ferramentas pode mudar depois de conectarmos? | Não. As ferramentas são código fixo. A lista exata é publicada com um hash em [mcp.himoose.com/tools.json](https://mcp.himoose.com/tools.json). |
| Como as pessoas fazem login? | OAuth 2.1, o fluxo padrão de MCP remoto, com a conta existente do Hi, Moose. Sem chaves de API. |
| Quanto tempo duram os tokens? | Tokens de acesso, uma hora. Tokens de atualização expiram após 30 dias sem uso, no máximo 90 dias. |
| Podemos revogar o acesso? | Sim, por app, no Hi, Moose em **Configurações → Hi, Moose MCP**. |
| O que um app conectado pode alterar? | Trabalho de conteúdo e leituras dentro dos projetos da conta conectada. Ele não pode publicar, excluir, nem alterar configurações, membros da equipe ou rastreamento. |
| Ele alcança algo fora do Hi, Moose? | Não. Ele nunca vê as conversas, arquivos, repositórios ou outros conectores do app de onde é usado. |
| Onde o trabalho roda? | No app Hi, Moose em um dispositivo que você escolhe, o dispositivo host. |
| O texto externo nos resultados é marcado? | Sim. Trechos de páginas e respostas de mecanismos de IA voltam entre marcadores rotulados como dados, não instruções. |
| Onde relatamos um problema? | [legal@himoose.com](mailto:legal@himoose.com), ou a [página de contato](https://himoose.com/pt/contact/). |

## Quem opera o servidor

O Hi, Moose MCP é construído e operado pelo Hi, Moose. É o único servidor MCP que alcança uma conta do Hi, Moose, e não é um servidor da comunidade nem de terceiros. O endereço do servidor é:

```text
https://mcp.himoose.com/mcp
```

O servidor em si é pequeno. Ele cuida do login e dos tokens, oferece a lista de ferramentas e repassa cada solicitação para a nuvem do Hi, Moose, que a entrega ao dispositivo host. O trabalho, como ler o rastreamento do site ou escrever um brief, roda no app Hi, Moose nesse dispositivo, do mesmo jeito que roda quando alguém clica no botão dentro do app.

## A lista de ferramentas é publicada e não muda

Um servidor MCP pode, em princípio, mudar as descrições das suas ferramentas depois que você conecta, ou esconder nelas instruções para o agente de IA. O nome que a OWASP dá a isso é envenenamento de ferramentas (tool poisoning).

As ferramentas do Hi, Moose MCP são código fixo no servidor. Os nomes, as descrições e os esquemas de entrada não mudam entre chamadas, e nenhum conteúdo do usuário é escrito neles. Uma ferramenta nova significa uma nova versão do servidor.

A lista exata que o servidor entrega está publicada em:

```text
https://mcp.himoose.com/tools.json
```

Ela traz a versão do servidor, a data da última mudança na lista, o número de ferramentas, o texto completo de cada ferramenta, o texto de instruções que o servidor dá ao agente e um hash SHA-256. O hash cobre o JSON compacto dos campos `instructions` e `tools`, então você pode recalculá-lo a partir do arquivo ou compará-lo com o que o seu cliente MCP recebeu. Anote o hash nas suas notas de análise e compare-o periodicamente. O mesmo hash é o cabeçalho `ETag` do arquivo.

Antes de alguém fazer login, a página de consentimento mostra a mesma lista de ferramentas em palavras simples, sob "Este app poderá" e "Ele não poderá".

## Login e tokens

Todo cliente segue o mesmo fluxo: Claude na web, o app desktop do Claude, Claude Code, ChatGPT e qualquer outro app MCP. Não há atalho, token compartilhado nem chave de API.

- OAuth 2.1 como descreve a especificação atual de autorização do MCP: metadados de recurso protegido (RFC 9728) com um desafio `WWW-Authenticate`, metadados do servidor de autorização (RFC 8414), PKCE obrigatório para todo cliente, indicadores de recurso (RFC 8707) para que um token deste servidor não possa ser reutilizado em outro lugar, registro dinâmico de clientes (RFC 7591) e Client ID Metadata Documents, e revogação de tokens (RFC 7009).
- O login acontece em `console.himoose.com`, com a conta existente do Hi, Moose da pessoa, por e-mail e senha ou com o Google. O app MCP nunca vê a senha. O Hi, Moose MCP conhece apenas o id e o e-mail da conta, e quais projetos a conta pode ver.
- A página de consentimento nomeia o app que está pedindo acesso. Quando o app publica a sua identidade, a página mostra o domínio do publicador. Quando não publica, a página diz "Nome não verificado".
- Tokens de acesso duram uma hora. Tokens de atualização duram no máximo 90 dias e expiram após 30 dias sem uso. Tokens, códigos e segredos são armazenados apenas como hashes.
- Uma conexão pertence a uma pessoa. Membros da equipe conectam com as próprias contas.

Para desconectar um app, abra o Hi, Moose e vá em **Configurações → Hi, Moose MCP**. A tabela **Apps conectados** lista cada app com login na conta, com o domínio do publicador e a hora da conexão. **Revogar** desconecta esse app em até um minuto. O app só pode conectar de novo passando pelo login outra vez.

## O que um app conectado pode e não pode fazer

Tudo o que um app conectado pode fazer está listado no [guia de configuração](../hi-moose-mcp.md) e descrito ferramenta por ferramenta na [referência das ferramentas](tools.md). É trabalho de conteúdo e pesquisa dentro dos projetos da conta: briefs, rascunhos, imagens, FAQs, pontos-chave, auditorias AEO, planos de links internos, episódios de áudio, verificações de cobertura e leituras de resultados de busca por IA armazenados.

Ele não pode:

- Publicar em um site, nem alterar nada nele
- Excluir nada
- Alterar configurações, membros da equipe, cobrança ou o dispositivo host
- Alterar o que o Hi, Moose rastreia, nem iniciar uma execução de visibilidade
- Alcançar qualquer conta diferente da que fez login
- Alcançar qualquer coisa no app de onde é usado: nem conversas, arquivos, repositórios, memória ou outros conectores

Toda solicitação nomeia um projeto. Antes de qualquer trabalho começar, o Hi, Moose verifica se a conta conectada tem acesso a esse projeto. Uma solicitação para um projeto que a conta não pode ver falha na hora.

## Onde o trabalho roda e quais dados se movem

O Hi, Moose MCP nunca tem uma cópia do rastreamento do site, do perfil Brand Truth ou da Library. Eles ficam no app Hi, Moose no dispositivo host, o único computador ou servidor que você escolhe em Configurações. O host roda cada trabalho do mesmo jeito que o app roda a partir de um botão.

Este é o caminho de uma solicitação:

1. O app MCP envia ao servidor o nome da ferramenta e a sua entrada.
2. O servidor verifica o token e pede à nuvem do Hi, Moose que crie um registro de trabalho para o projeto. A nuvem verifica o acesso ao projeto e grava o registro.
3. O dispositivo host, que observa os trabalhos dos seus projetos, pega o trabalho e o executa.
4. O host grava o resultado no registro de trabalho e o salva na Library. O servidor devolve o resultado ao app MCP.

O que isso significa para os seus dados:

- A solicitação e o resultado passam pela nuvem do Hi, Moose (Google Cloud, região dos Estados Unidos) como um registro de trabalho. O registro fica com o projeto para que a tabela **Trabalhos recentes de agentes** em Configurações possa mostrar o que foi pedido, por qual app e conta, e se terminou.
- Imagens geradas são guardadas no armazenamento em nuvem do Hi, Moose da conta e devolvidas como um link.
- Chamadas a modelos usam o mesmo caminho do app: os modelos gerenciados do seu plano, as suas próprias chaves de modelo se você as trouxe, ou um modelo local se você roda um. Conectar um app MCP não muda quais modelos veem o seu conteúdo.
- Os registros do próprio servidor guardam o nome da ferramenta, quanto tempo a chamada levou e se o cliente usou streaming. Eles nunca guardam a entrada nem o resultado.

## Texto externo nos resultados

Alguns resultados contêm texto que o Hi, Moose não escreveu: trechos de páginas do seu site, texto âncora citado de uma página, pequenos extratos do que um mecanismo de IA respondeu, ou o texto completo de uma resposta armazenada. Um texto assim pode trazer instruções dirigidas a um agente de IA. O nome que a OWASP dá a isso é injeção indireta de prompt.

Todo resultado que traz texto externo o marca. O texto volta entre um marcador de início e um de fim, com uma linha antes dizendo de onde ele veio e que tudo entre os marcadores é dado, não instrução. A forma estruturada do mesmo resultado traz um campo `dataNotice` que diz a mesma coisa. Isso vale para `check_site_coverage`, `run_aeo_audit`, `find_internal_links`, `visibility_check_topic`, `visibility_get_answer` e `visibility_list_opportunities`.

Briefs, rascunhos, FAQs, pontos-chave e roteiros de áudio são escritos pelo Hi, Moose para você. A pesquisa por trás deles é lida no dispositivo host e não é repassada ao agente.

Marcadores ajudam um agente a tratar o texto como dado. Eles não tornam um agente imune a instruções no conteúdo que ele lê, e nenhum fornecedor de ferramentas pode prometer isso. Mantenha as permissões do agente que você conecta tão restritas quanto a tarefa dele exige, como faria com qualquer conector.

## Relatar um problema de segurança

Escreva para [legal@himoose.com](mailto:legal@himoose.com) ou use a [página de contato](https://himoose.com/pt/contact/). Conte o que você encontrou e como reproduzir. Respondemos a todo relato e dizemos o que mudamos.
