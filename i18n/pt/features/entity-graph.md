---
source_hash: 1d8f1dffb939a9b3587c4b3a3f298386f6f202a5a02672b6b3dfd79bbccc2135
---
# Entity Graph

## Para que serve

Um entity graph é o mapa daquilo de que seu site realmente trata: as pessoas, os produtos, os lugares, as organizações e os temas que suas páginas nomeiam, e como essas coisas se conectam.

Isso importa porque os mecanismos de resposta não leem seu site como uma lista de páginas. Eles o leem como um conjunto de coisas e relações. Um site que deixa claro "somos esta empresa, fazemos estes produtos, para estes clientes, nesta categoria" dá ao mecanismo algo para recuperar e citar. Um site em que isso fica subentendido, mas nunca é dito, o deixa adivinhando.

O entity graph mostra quais dessas coisas seu site já deixou claras, quais estão frágeis e com o que um mecanismo sairia de lá.

Comece em **Ferramentas → Criar um entity graph**, ou simplesmente peça no [chat](../chat/overview.md).

## Antes de poder construir um

O grafo é construído a partir das páginas que o Hi, Moose já rastreou, então o projeto precisa de **um site e de pelo menos um rastreamento concluído**. Se ainda não houver nenhum, o cartão de entrada avisa e leva você ao [Monitoramento do site](../site-monitoring/overview.md) para executar um.

O cartão informa com o que está trabalhando: quantas páginas rastreadas e a data do último rastreamento concluído.

## Rápido ou completo

Duas profundidades:

- **Rápido**: só dados estruturados. Lê a marcação schema, os metadados e a estrutura de página que seu site já publica. Roda na hora e não custa nada.
- **Completo**: tudo o que o rápido faz, mais uma passagem de IA que lê suas páginas principais e nomeia as entidades que não estão marcadas em lugar nenhum. Leva alguns minutos.

No modo completo você escolhe quantas páginas principais a passagem de IA pode ler. Execuções maiores demoram mais e, nos planos gerenciados, as chamadas ao modelo na nuvem consomem sua cota mensal. A passagem roda no modelo selecionado no menu de modelos do chat, então escolha o modelo primeiro se quiser um específico: um modelo local carregado mantém tudo na sua máquina e sem custo.

## O que volta

O grafo reporta:

- **Entidades**: tudo o que foi encontrado, com tipo, apelidos, em quantas páginas aparece e uma pontuação de **saliência** para o quanto é central no site.
- **Relações**: como essas entidades se conectam, divididas em três tipos:
    - **Rotuladas**: uma relação que seus dados estruturados ou a passagem de IA declaram explicitamente.
    - **Página compartilhada**: duas entidades que aparecem repetidamente nas mesmas páginas.
    - **Semânticas**: duas entidades que a linguagem trata como relacionadas mesmo onde nada as liga.
- **Entidades por tipo**: a distribuição, muitas vezes a visão isolada mais útil. Um site que vende software e mostra quarenta pessoas e três produtos tem um problema de narrativa que vale a pena conhecer.

Uma tabela de **entidades principais** mostra as mais salientes com tipo, número de páginas e saliência. O conjunto completo é exportado em **CSV** ou **PDF**; a tabela na tela tem um limite, e ela informa quantas outras as exportações contêm.

## Quando a passagem de IA não roda

O modo completo degrada em vez de falhar. Se a passagem de IA não puder rodar, você ainda recebe o grafo a partir dos dados estruturados, das páginas compartilhadas e da similaridade semântica, e o cartão diz qual caso se aplicou:

- **Nenhum modelo disponível**: carregue um modelo local ou adicione uma chave da OpenRouter, e então reconstrua no modo completo.
- **Nada novo para ler**: todas as páginas elegíveis já haviam sido analisadas numa execução anterior.
- **A passagem falhou**: não conseguiu concluir.
- **A cota acabou**: nos planos gerenciados a passagem para quando os créditos mensais acabam, e o grafo inclui tudo o que foi analisado até ali.

## O Moose pode ler de volta

Depois que um grafo existe, o [chat](../chat/tools-and-specialists.md) pode consultá-lo diretamente. Pergunte em quais entidades seu site é mais forte, o que está conectado a um produto específico ou o que falta ao lado de um tema que você quer ganhar, e o Moose lê o grafo em vez de rastrear de novo ou chutar.

O [Send Moose](../send-moose/overview.md) também o lê, como parte da inteligência de site que ele leva para um trabalho.

## Para onde ir a partir daqui

- **[Monitoramento do site](../site-monitoring/overview.md)**: o rastreamento de que o grafo é feito.
- **[Briefings de conteúdo](content-briefs.md)**: transformar uma lacuna do grafo numa página.
- **[Auditorias de AEO](aeo-audits.md)**: verificar se uma página específica declara suas entidades com clareza.
