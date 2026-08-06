---
source_hash: 9705deb0dc37b51cf84f956088049d0d7d87b416de55439c84ef17b2ef0d3d9c
---
!!! note "Tradução automática"
    Esta página foi traduzida por IA. A versão em inglês é a versão oficial.

    [Ler em inglês](https://himoose.com/docs/inbox/overview/)

# Caixa de entrada

## Para que serve

A Caixa de entrada é onde o Hi, Moose traz à tona o que merece sua atenção: achados triados, auditorias e eventos de publicação, cada um ligado a um artefato real em vez de a uma notificação genérica. Ela transforma sinais espalhados (variações de sentimento na visibilidade, desvio narrativo, imprecisões de paridade de recursos, resultados de auditorias de AEO, desfechos de publicação e pedidos de aprovação) em uma única fila de trabalho priorizada.

## O que aparece na Caixa de entrada

Todo item da Caixa de entrada aponta para algo concreto que você pode abrir e resolver:

- **Sinais de visibilidade**: sentimento negativo ou misto detectado numa resposta da IA, desvio narrativo ou imprecisão de paridade de recursos em relação ao seu [Perfil de Verdade da Marca](../getting-started/context/brand-truth-profile.md), ou uma [execução de visibilidade](../visibility/overview.md) concluída ou com falha.
- **Resultados de auditorias de AEO**: uma auditoria concluída, ou uma auditoria cujo plano de ação trouxe uma recomendação de alta prioridade.
- **Alterações detectadas no site**: um único resumo por rastreamento do [monitoramento do site](../site-monitoring/overview.md), que abre em uma tabela com todas as páginas alteradas e seu nível de impacto. Páginas inacessíveis e quedas do site inteiro são reportadas como tipos de alteração próprios.
- **Relatórios de fluxos de trabalho**: resultados da execução de um [fluxo de trabalho](../workflows/overview.md), por exemplo uma varredura agendada que gerou posts novos ou apontou uma oportunidade na busca com IA.
- **Eventos de publicação**: uma publicação que **falhou**, ou uma alteração aguardando sua aprovação. Publicações bem-sucedidas não criam mais um item na Caixa de entrada, porque uma parede de avisos de «deu certo» acaba enterrando os que exigem sua atenção.
- **Uma mensagem de boas-vindas** do Moose ao terminar a configuração inicial, apontando um primeiro passo sensato.

Cada item traz uma próxima ação sugerida quando faz sentido: abrir o artefato, iniciar um briefing, dar sequência a uma auditoria, revisar um rascunho, aprovar uma alteração ou repetir uma execução que falhou. Assim você não apenas lê uma notificação, mas fica a um clique de agir.

Os resumos de monitoramento do site também trazem a ação **Perguntar ao Moose sobre tudo isso**, que entrega a captura do rastreamento ao [chat](../chat/overview.md) e pergunta por onde começar.

## Filtrar a Caixa de entrada

Dois filtros determinam o que você vê:

- **Status**: o padrão é **Ativos**, ou seja, tudo o que não foi descartado (itens abertos, em andamento e concluídos). Mude para um status específico, ou para **Todos** para incluir os itens descartados que você queira retomar.
- **Gravidade**: **Crítico**, **Aviso**, **Notificação**, **Informação**, ou todas.

Os itens ficam agrupados por data (por exemplo, «Ontem», «Mais antigos») com uma contagem por grupo, para você ver rapidamente quanto está esperando. Caixas volumosas são paginadas em vez de carregadas de uma vez.

**Marcar tudo como lido** limpa o indicador em toda a sua Caixa de entrada, não só na página que você está vendo.

!!! note "A Caixa de entrada guarda os 200 itens mais recentes"
    Os mais antigos são removidos automaticamente. A Caixa de entrada é uma fila de trabalho, não um arquivo: tudo o que é duradouro fica na [Biblioteca de artefatos](../library/overview.md) ou no artefato para o qual o item aponta.

## Controlar o que notifica você

Clique em **Notificações** para abrir suas preferências de notificação por projeto. O que cada configuração faz está em [Notificações da Caixa de entrada](notifications.md).

## Gerenciado e BYOK

A Caixa de entrada funciona igual, seja seu espaço de trabalho gerenciado ou BYOK: os itens são gravados pelo lado que de fato gerou o evento subjacente (a nuvem nos fluxos de trabalho gerenciados, o processo local do desktop no BYOK), e você vê uma fila unificada nos dois casos.
