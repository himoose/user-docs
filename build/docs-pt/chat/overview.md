---
source_hash: 799fa86d4b93065bdbc58d1b0a7cc5400446cfdee289750eafd31c6a0c8371b2
---
!!! note "Tradução automática"
    Esta página foi traduzida por IA. A versão em inglês é a versão oficial.

    [Ler em inglês](https://himoose.com/docs/chat/overview/)

# Visão geral do Chat

## Para que serve

No Chat você fala direto com o operador do Hi, Moose, o mesmo agente principal descrito em toda esta documentação, e não com uma ferramenta separada. Ele está disponível na tela **Início** e na tela dedicada de chat, e toda conversa pode puxar o [Contexto](../getting-started/context/overview.md) do seu projeto, os arquivos anexados e os especialistas salvos para fundamentar as respostas.

## Iniciar uma conversa

- Clique em **Novo chat** para começar do zero, ou continue uma conversa existente.
- O campo de composição traz atalhos rápidos para as tarefas mais comuns.
- Escolha algo específico no **[menu Ferramentas](../tools/overview.md)** da barra superior.
- Ou escreva seu pedido em linguagem comum. O Hi, Moose decide se responde direto, faz uma pergunta de acompanhamento ou executa um recurso como os [Briefings de conteúdo](../features/content-briefs.md) ou as [auditorias de AEO](../features/aeo-audits.md) e devolve um artefato duradouro.

## Como o Hi, Moose decide o que fazer

Não existe lista de palavras-chave. O Moose interpreta o que você pede e encaminha conforme isso, então você pode formular do jeito que quiser e obter o mesmo resultado.

Dois comportamentos valem conhecer:

- **Pedidos explícitos executam a coisa.** Peça uma auditoria e você recebe o formulário da auditoria.
- **Pedidos implícitos apenas oferecem.** Se sua pergunta só sugere um recurso, o Moose responde à pergunta e coloca o recurso como sugestão de um toque logo abaixo. Ele não sequestra a conversa.

!!! note "Perguntas de acompanhamento continuam sendo perguntas"
    Fazer uma pergunta logo depois de o Moose produzir um rascunho dá uma resposta sobre aquele rascunho, não um rascunho novo. Peça explicitamente uma reescrita quando quiser uma.

## Anexar contexto

O menu de anexos oferece quatro opções:

- **Enviar arquivo ou imagem**: `.txt`, `.md`, `.csv`, `.doc`, `.docx`, `.pdf`, `.xls`, `.xlsx`, `.jpg` e `.png`. Planilhas viram texto legível em vez de serem tratadas como arquivos opacos.
- **Capturar a tela**: escolha um monitor ou uma janela e depois recorte a área desejada. No macOS isso exige permissão de gravação de tela, e o Hi, Moose orienta você a concedê-la.
- **Adicionar da Biblioteca**: anexe itens salvos da [Biblioteca de artefatos](../library/overview.md) como contexto.
- **Banco de dados vetorial do site**: entregue ao Moose seu site indexado para que ele responda a partir das suas páginas reais. Veja [Monitoramento do site](../site-monitoring/overview.md).

## O que torna uma resposta fundamentada

Enquanto o Hi, Moose trabalha, ele mostra o que está de fato fazendo: buscar resultados em tempo real, coletar perguntas de «As pessoas também perguntam», rastrear o domínio de um concorrente, ler uma página, indexar resultados, consultar dados do Search Console ou aplicar sua voz da marca salva. É um rastro visível das evidências reais por trás da resposta, não um indicador decorativo.

## Para onde ir a partir daqui

- **[Ferramentas e especialistas do chat](tools-and-specialists.md)**: as ferramentas que o Moose pode usar e os especialistas salvos.
- **[O menu Ferramentas](../tools/overview.md)**: iniciar uma tarefa específica sem precisar descrevê-la.
- **[Seleção de modelo](model-selection.md)**: qual modelo de IA move seu chat, incluindo as opções locais e BYOK.
- **[Chats (histórico)](chats-history.md)**: encontrar, renomear e reabrir conversas anteriores.
