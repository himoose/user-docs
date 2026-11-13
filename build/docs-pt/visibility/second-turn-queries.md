---
source_hash: bf06b2d4371815f46d4209e9c058c88a274ce098682e93731da1f9cafde41e72
---
!!! note "Tradução automática"
    Esta página foi traduzida por IA. A versão em inglês é a versão oficial.

    [Ler em inglês](https://himoose.com/docs/visibility/second-turn-queries/)

# Consultas de segundo turno

## Para que serve

Os mecanismos de IA costumam terminar uma resposta convidando a fazer a próxima pergunta. Uma consulta de segundo turno é essa próxima pergunta, escrita por extenso para fazer sentido sozinha. O Hi, Moose captura essas consultas durante as execuções de visibilidade e as lista na aba **Consultas de segundo turno**, com a frequência com que cada uma apareceu e a indicação de que seu site a cobre ou não.

Por exemplo, um mecanismo pode terminar uma resposta com "Quer que eu compare essas duas opções lado a lado?". A consulta de segundo turno é o que uma pessoa digitaria para aceitar, como "Comparar conversores de mesa com regulagem de altura e mesas completas com regulagem de altura para um escritório pequeno em casa".

## Como ativar

Abra as [Configurações de Visibilidade](settings.md#consultas-de-segundo-turno) e vá até a seção **Consultas de segundo turno**. Ative **Capturar consultas de segundo turno**. A opção vem desativada por padrão e é ativada separadamente em cada projeto.

Enquanto a opção está desativada, nada é capturado e a aba Consultas de segundo turno fica oculta.

Você pode ativar a opção com os planos gerenciados pagos, o BYOK Premium e o BYOK Agency. No Preview Mode e no BYOK Free, o botão de ativação aparece esmaecido e mostra a nota **Disponível nos planos pagos**.

A ativação adiciona uma pequena chamada ao modelo para cada resposta de uma execução. Nos planos gerenciados pagos, essas chamadas contam na cota do seu plano. No BYOK Premium e no BYOK Agency, elas são cobradas na sua chave do OpenRouter.

## A aba Consultas de segundo turno

A aba fica logo depois de **Oportunidades** no painel de Visibilidade. Ela só aparece quando a opção está ativada. Ela fica vazia até a primeira execução de visibilidade depois da ativação, porque as respostas de execuções anteriores não são processadas.

A aba segue o período e os filtros selecionados no topo de Visibilidade. Uma consulta é listada quando uma resposta desse período a continha.

### Visualizações

- **Mais frequentes** é a visualização padrão. Ela mostra uma única lista ordenada pelo número de respostas que continham cada consulta.
- **Por prompt** agrupa as consultas sob o prompt monitorado que cada uma seguiu.

### O que uma linha mostra

- A consulta.
- **Respostas com esta consulta: N**, em que N é o número de respostas que a continham.
- Os mecanismos e o tema.
- O resultado da [cobertura do site](#cobertura-do-site).
- **Mostrar detalhes**, que lista os prompts que a consulta seguiu em **Aparece depois destes prompts**, com um link **Ver resposta** para cada prompt. Também mostra as palavras finais do mecanismo.

## Como as novas consultas são classificadas

Na primeira vez que uma nova consulta aparece, o Hi, Moose verifica se ela é específica e próxima do tema o bastante para ser monitorada. Ele também verifica se ela significa o mesmo que uma consulta que já está na lista. Consultas que significam a mesma coisa são contadas juntas. As genéricas, como "conte-me mais", ficam de fora.

Essa classificação acontece quando você abre a aba. Na primeira vez que você a abre depois de uma execução, a aba mostra **Classificando novas consultas: X de Y**.

## Cobertura do site

Cada consulta é verificada uma vez em relação às páginas rastreadas do site do seu projeto. A linha mostra então um destes resultados:

- **Coberta no site:** seguido da página.
- **Coberta em parte no site:** seguido da página.
- **Sem cobertura no site**.

A cobertura é verificada de novo quando um novo rastreamento do site termina.

A verificação precisa de um rastreamento do site concluído no seu dispositivo, ou no dispositivo que hospeda o índice do site. Sem um rastreamento concluído, a linha mostra **Cobertura do site não verificada**. No aplicativo web sem um dispositivo desktop anfitrião, a cobertura não é verificada.

## Botões de cada linha

- **Adicionar aos prompts monitorados** adiciona a consulta como prompt monitorado sob o mesmo tema do prompt que ela seguiu. Depois o botão indica **Monitorando**.
- **Criar um rascunho** aparece quando seu site não cobre a consulta. Ele abre um novo chat com o formulário do [briefing de conteúdo](../features/content-briefs.md) já preenchido.
- **Atualizar esta página** aparece quando seu site cobre a consulta em parte. Ele abre o formulário de atualização de conteúdo dessa página, com a consulta como alvo.
- **Descartar** oculta a linha. **Mostrar descartadas** volta a exibir as linhas descartadas e **Restaurar** devolve uma linha à lista.

## Quando a lista é atualizada

Enquanto a opção está ativada, as novas consultas são capturadas de cada resposta em todas as execuções de visibilidade. Elas são classificadas na próxima vez que você abre a aba.

Como a aba segue o período selecionado, uma consulta deixa de ser listada quando nenhuma resposta desse período a continha. Escolha um período mais longo para vê-la de novo.

## Equipes e planos

Nos planos gerenciados pagos, as consultas capturadas, os descartes e os resultados de cobertura são sincronizados com a nuvem, de modo que os membros da equipe veem a mesma lista. No BYOK Premium e no BYOK Agency, tudo fica no seu dispositivo.

## O que não está incluído

- As perguntas "Related" do Perplexity e as perguntas "People also ask" do Google não são capturadas.
- As consultas de segundo turno não fazem parte do [relatório executivo em PDF](overview.md#exportar).
- As consultas de segundo turno não estão disponíveis pelas ferramentas do [Hi, Moose MCP](../integrations/hi-moose-mcp.md).
