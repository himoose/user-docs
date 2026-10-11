---
source_hash: 5b66e35e4cc4b5ac9c7567edd481631bcbd56d2ff1ca7f0d3e2f1b0c1fbbd5c3
---
# Hi, Moose MCP

## Para que serve

O Hi, Moose MCP permite que os apps de IA em que você já trabalha usem o Hi, Moose. Adicione-o como conector MCP no Claude, no ChatGPT ou em qualquer outro app compatível com MCP com login, entre com a sua conta Hi, Moose e peça trabalho ao Hi, Moose de dentro desse app. MCP (Model Context Protocol) é o padrão que esses apps usam para se conectar a ferramentas externas.

O trabalho roda em um dos seus próprios dispositivos, o **dispositivo host**, onde o Hi, Moose fica aberto e com a sessão iniciada. Os resultados voltam para o app e são salvos na sua [Library](../library/overview.md).

## O que um app conectado pode fazer

Com as ferramentas atuais, um app conectado pode:

- Listar seus projetos Hi, Moose
- Listar os briefs e rascunhos salvos na sua Library
- Verificar se o seu site já cobre um tema, com as páginas que o cobrem e a data do rastreamento verificado
- Criar um brief de conteúdo
- Escrever um rascunho a partir de um brief
- Criar uma imagem destacada
- Escrever perguntas frequentes com esquema FAQPage para um rascunho salvo ou uma página do seu site
- Escrever os pontos-chave de um rascunho salvo ou de uma página do seu site
- Executar uma auditoria AEO de uma página publicada, um rascunho salvo ou um texto colado, com pontuações, problemas e correções propostas
- Buscar o trabalho pronto

Ele não pode alterar configurações nem membros da equipe, e não pode excluir nada. Mais ferramentas estão a caminho.

## Antes de começar

1. Abra o Hi, Moose no dispositivo que deve executar o trabalho e entre na sua conta.
2. Vá em **Configurações → Hi, Moose MCP** e escolha esse dispositivo como dispositivo host do projeto. Só o proprietário da conta pode escolher o dispositivo host.
3. Copie o endereço do servidor mostrado ali:

```
https://mcp.himoose.com/mcp
```

## Conectar no Claude

No Claude.ai e no app de desktop do Claude:

1. Abra **Configurações → Conectores** (também em claude.ai/customize/connectors).
2. Escolha **Adicionar conector personalizado**, cole o endereço do servidor e clique em **Adicionar**. Deixe os campos de cliente OAuth vazios.
3. Clique em **Conectar** ao lado de Hi, Moose MCP. Uma página do Hi, Moose abre, mostra o que o app poderá fazer e pede que você entre com a sua conta Hi, Moose.
4. Comece um chat novo e peça, por exemplo, "Liste meus projetos Hi, Moose".

Nos planos Team e Enterprise, um proprietário adiciona primeiro o conector para a organização e depois cada membro se conecta.

No Claude Code:

```
claude mcp add --transport http himoose https://mcp.himoose.com/mcp
```

Depois rode `/mcp` dentro do Claude Code e siga o login.

## Conectar no ChatGPT

O ChatGPT aceita servidores MCP personalizados nos planos pagos. Os nomes dos menus mudam de vez em quando; este é o caminho atual.

1. Abra **Configurações → Apps** (chamado **Conectores** em algumas versões). Em workspaces Business e Enterprise, um proprietário pode precisar permitir conectores personalizados primeiro.
2. Escolha **Adicionar** e depois **Criar servidor MCP personalizado**. Versões antigas mostram **Criar app MCP** e podem exigir antes o **Modo desenvolvedor** nas configurações avançadas.
3. Cole o endereço do servidor, escolha **OAuth** como autenticação e salve.
4. Entre com a sua conta Hi, Moose na página que abre.
5. Em um chat, ative o conector para aquela conversa e peça trabalho ao Hi, Moose.

## Outros apps

Qualquer app que consiga adicionar um servidor MCP remoto com login OAuth funciona do mesmo jeito: adicione o endereço do servidor, entre com a sua conta Hi, Moose e use a partir dali.

## Como um pedido é executado

1. O app envia o seu pedido ao Hi, Moose MCP.
2. O Hi, Moose MCP o repassa ao dispositivo host, que executa o trabalho com o rastreamento, o Brand Truth e a pesquisa do projeto.
3. O resultado volta para o app e é salvo na sua Library.

Um brief, rascunho, imagem, conjunto de perguntas frequentes ou lista de pontos-chave leva de um a três minutos; uma auditoria AEO, de dois a quatro. Se o app disser que o trabalho ainda está em andamento, peça para ele verificar de novo; ele busca o resultado quando estiver pronto. Se o dispositivo host estiver desligado ou desconectado, o app recebe uma mensagem informando isso.

Os trabalhos rodam com a conta que está com a sessão iniciada no dispositivo host, então a Library que eles leem e gravam é a dessa conta. A tabela **Trabalhos recentes de agentes** em Configurações mostra o que foi pedido, por qual app e se terminou.

## Desconectar um app

Vá em **Configurações → Hi, Moose MCP**. A tabela **Apps conectados** lista cada app com sessão iniciada na sua conta. **Revogar** encerra a sessão desse app. Pode levar até um minuto para valer, e o app pode se conectar de novo mais tarde. O acesso também expira sozinho depois de 30 dias sem uso.
