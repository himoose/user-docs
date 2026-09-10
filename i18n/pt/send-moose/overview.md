---
source_hash: 7e432cdd4918eeb01a120c373ca83181288da1c2c0b01d3aee18207e05092124
---
# Send Moose

## Para que serve

O Send Moose é onde você entrega um trabalho em vez de fazê-lo você mesmo. Você descreve a tarefa em linguagem simples ("descubra quem está sendo recomendado no nosso lugar para software de gestão de projetos e por quê", "verifique se nossa página de preços ainda bate com o que as páginas comparativas dos concorrentes dizem") e o Moose vai lá e faz, usando a web e tudo o que o Hi, Moose já sabe sobre o seu projeto.

É a diferença entre um chat que responde a você e um agente que vai trabalhar. O chat é uma conversa; o Send Moose é um trabalho que você despacha e ao qual volta depois.

Ele fica na barra lateral, em **Send Moose**.

!!! warning "O Send Moose é experimental"
    Ele está no aplicativo e funciona, mas é a parte mais nova e menos assentada do Hi, Moose. Fique de olho na qualidade do que volta, e nos planos pagos fique de olho no consumo de tokens: o Scout e o Skeptic rodam na nuvem mesmo quando o Moose roda local.

## O que o Moose traz consigo

Um agente web genérico começa do zero e precisa que você conte tudo. O Moose chega já conectado ao seu projeto:

| Ele pode ler | O que isso significa |
|---|---|
| Seus dados de visibilidade | Visão geral, Share of Voice, concorrentes, temas, prompts e o que mudou |
| Seu índice do site | Páginas rastreadas, o que mudou nelas, links internos e seu [entity graph](../features/entity-graph.md) |
| Seu histórico de AEO | Auditorias anteriores e seus detalhes, contexto de citações, acesso de rastreadores, cobertura de temas |
| [Google Search Console](../integrations/google-search-console.md) | Seus dados reais de consultas e páginas, consultados de forma iterativa |
| Sua [Biblioteca](../library/overview.md) | Briefings, rascunhos, pontos principais, FAQs e auditorias que você já criou |
| Trabalhos anteriores | O que ele encontrou e decidiu em execuções anteriores deste projeto |

Ele também pode rodar uma [verificação de visibilidade](../visibility/overview.md) ao vivo ou uma [auditoria de AEO](../features/aeo-audits.md) no meio de um trabalho, quando a resposta exige, em vez de dizer para você ir executá-la.

## Enviar um trabalho

Descreva a tarefa e aperte **Send Moose**. Duas opções moldam como ele conduz:

- **Trabalho profundo**: deixe o trabalho levar horas se precisar: muito mais páginas, muito mais buscas, mais pontos de checagem. Use quando a pergunta for realmente ampla, não para uma consulta rápida.
- **Anexar arquivos**: até seis arquivos por trabalho, como contexto que ele lê enquanto trabalha.

Você pode marcar **Avise-me quando o Moose terminar** e sair. O trabalho continua rodando esteja você olhando ou não, e fique você na tela ou não.

## Ver ele trabalhar

**Ver navegador** abre a instância de navegador que o Moose está usando, para você ver as páginas conforme ele as lê. **Assumir o controle** passa o navegador para você se ele travar em algo que você resolve num segundo, como um aviso de cookies ou um login, e **Voltar ao trabalho** devolve para ele.

Você pode fechar essa janela quando quiser. O Moose segue trabalhando.

## Moose, Scout e Skeptic

No plano gratuito, o Moose trabalha sozinho.

Os planos pagos colocam outros dois agentes no trabalho:

- **Scout** encontra ângulos que passam despercebidos ao Moose.
- **Skeptic** contesta as evidências antes que cheguem ao seu resultado.

Você pode falar com qualquer um deles no meio do trabalho pelo thread: dizer algo ao Moose, pedir outro ângulo ao Scout, pedir ao Skeptic que aperte mais numa afirmação. **Continuar** e **Checar mais cinco resultados** estendem uma execução que parou num ponto útil.

O Scout e o Skeptic sempre rodam na nuvem pela OpenRouter, mesmo quando o Moose está num modelo local, então eles custam tokens.

## Quando o Moose precisa de você

Duas coisas param um trabalho e esperam por você em vez de adivinhar:

- **Precisa da sua aprovação**: o Moose está prestes a executar uma ação num site real, como apertar um botão de formulário. Ele mostra o botão exato e espera por **Aprovar e continuar** ou **Não faça**.
- **Precisa da sua ajuda**: ele travou em algo que só você pode responder. Digite uma resposta, ou aperte **Deixe o Moose decidir** para que ele mesmo resolva.

Nada é publicado, enviado ou submetido em lugar nenhum sem você aprovar antes. Isso vale também para execuções agendadas.

## Ler o resultado

Um trabalho concluído tem quatro abas:

- **Resultado**: o que ele encontrou, redigido.
- **Colaboração**: como foi, e quem contribuiu com o quê: notas que o Scout acrescentou, objeções que o Skeptic levantou, vezes em que você interveio.
- **Fontes**: cada página que ele abriu, com as evidências que tirou de cada uma.
- **Atividade**: a execução completa, filtrável por ferramentas ou por agentes.

Dali você pode **Salvar na Biblioteca**, **Baixar relatório** ou fazer uma pergunta de acompanhamento sobre o resultado no [chat](../chat/overview.md). Os arquivos que o Moose salvou durante o trabalho aparecem em **Arquivos que o Moose salvou**: abra-os, salve uma cópia ou mostre-os na pasta. Ele pode salvar arquivos CSV, Markdown, texto puro, PDF e Word.

## Conteúdo que o Moose cria

O Moose pode produzir artefatos reais do Hi, Moose como parte de um trabalho, não só uma resposta escrita: um **briefing de conteúdo**, um **rascunho**, **pontos principais**, **FAQs** ou uma **auditoria de AEO**. Eles caem na sua [Biblioteca](../library/overview.md) como qualquer outra coisa, e o resultado do trabalho leva direto a eles.

## Executar um trabalho de forma agendada

**Executar de forma agendada** transforma um trabalho pontual num recorrente: todo dia, em dias úteis, toda semana ou todo mês, em um ou mais horários.

Os trabalhos agendados aparecem em **Trabalhos agendados** e podem ser pausados, retomados ou excluídos. Eles rodam sem supervisão: o Moose toma as decisões pequenas sozinho, e segue sem publicar nem enviar nada sem a sua aprovação.

## Trabalhos anteriores

Todo trabalho fica guardado em **Trabalhos anteriores**, com busca e filtros por **Concluídos**, **Chamados de volta**, **Não concluídos** e **Bloqueados**, agrupados em hoje, esta semana e antes. Os trabalhos pertencem ao projeto em que foram executados.

## Configurações

As **configurações do Send Moose** são salvas por projeto:

- **LLM do Moose**: Automático usa o maior modelo local instalado, ou o modelo na nuvem do seu plano quando a IA local está desligada. Você também pode fixar um modelo específico.
- **LLM do Scout** e **LLM do Skeptic**: só nos planos pagos, com Gemma 4 31B como padrão.
- **Modelo de conteúdo**: qual modelo escreve os briefings, rascunhos e FAQs que ele cria. Por padrão, o mesmo que o Moose usa.
- **Mecanismo de busca**: com qual mecanismo ele pesquisa.

Tudo o que estiver marcado como **Consome tokens** roda na nuvem pela OpenRouter, e não no seu computador. Trabalhos profundos duram mais, então custam mais.

## Do que ele precisa

- **Um modelo local, ou um plano pago.** O Moose pensa num modelo Gemma que roda no seu computador. Baixe uma vez pelo aviso na tela e os trabalhos não custam nada. Planos pagos podem colocá-lo num modelo na nuvem. Se você desligou a IA local e está no plano gratuito, o Send Moose avisa e oferece religá-la.
- **Um site no projeto**, para trabalhos sobre o seu próprio site, sua marca ou seus concorrentes. Trabalhos gerais de web funcionam bem sem isso.

## Para onde ir a partir daqui

- **[Chat](../chat/overview.md)**: para o trabalho que você quer conduzir passo a passo em vez de despachar.
- **[Fluxos de trabalho](../workflows/overview.md)**: para uma receita fixa que roda a partir de um gatilho, em vez de um trabalho aberto.
- **[Biblioteca](../library/overview.md)**: onde ficam os relatórios e o conteúdo vindos de um trabalho.
