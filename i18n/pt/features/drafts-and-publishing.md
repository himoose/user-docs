---
source_hash: d13fbe0e44e283bca3759e24ae06c4632b5ccb20e66f5806145543eb82fe5f65
---
# Rascunhos, prévia e publicação

## Para que serve

O Hi, Moose não para na recomendação: ele acompanha você de um briefing ou de uma ideia de alteração até a alteração publicada, com uma etapa de prévia e uma de aprovação no meio, e um registro do que aconteceu.

## Draft Studio

No Draft Studio os rascunhos são escritos e lapidados. A geração de rascunhos foi feita para se apoiar num [briefing de conteúdo](content-briefs.md) em vez de funcionar como um expansor de texto às cegas: se um trabalho exige planejamento estruturado, o Hi, Moose gera ou confirma o briefing primeiro e escreve a partir dele. O Draft Studio também permite editar textos longos diretamente.

### Tipos de conteúdo

A geração de rascunhos segue os mesmos tipos de modelo disponíveis ao [criar um briefing de conteúdo](content-briefs.md#criar-um-briefing). Quatro têm atalho próprio no Chat, cada um com sua estrutura: [rascunho de post de blog](blog-post-draft.md), [post de glossário](glossary-post.md), [conteúdo de landing page](landing-page-content.md) e [conteúdo de página de produto](product-page-content.md). O modelo de página de soluções também está disponível ao criar um briefing, só que sem atalho dedicado.

Todos os modelos seguem o mesmo fluxo com briefing antes; só a estrutura muda, então um rascunho de landing page é planejado e moldado de forma diferente de um post de blog, mesmo os dois partindo de um [briefing de conteúdo](content-briefs.md).

Quando você pede um post e o Hi, Moose produz um briefing, ele segue em frente e gera o rascunho em vez de parar esperando que você peça de novo.

### Links internos

Os rascunhos novos são cruzados com o seu site indexado, e links internos pertinentes entram onde realmente fazem sentido. Isso exige um [índice de busca](../site-monitoring/overview.md) montado: sem ele não há para onde apontar, e o Hi, Moose não inventa links.

## Preparar uma alteração

Venha ela de um rascunho baseado em briefing, das [FAQ](faq-generator.md), dos [pontos principais](key-points.md) ou de uma recomendação de [auditoria de AEO](aeo-audits.md), uma alteração proposta é preparada como **proposta de alteração**, um artefato duradouro e não apenas texto de chat, antes que qualquer coisa toque seu site em produção.

## Prévia

Antes de você aprovar qualquer coisa, o Hi, Moose pode gerar uma prévia da alteração preparada para você ver como ela fica na página real. Para alterações que outra pessoa precisa revisar, o Hi, Moose pode gerar um link de revisão compartilhado, assinado e com validade, para que um colega ou cliente revise sem acessar o aplicativo para desktop.

## Aprovar e publicar

- **Aprovar**: aceitar explicitamente uma alteração preparada antes que ela possa ser publicada. Prévia e publicação são sempre etapas separadas; gerar um rascunho ou uma prévia nunca conta como «pronto» por si só.
- **Publicar**: depois de aprovada, o Hi, Moose publica a alteração pela conexão correspondente ([WordPress](../integrations/wordpress.md), [Webflow](../integrations/webflow.md) ou [Grav](../integrations/grav.md)) e registra o que foi publicado, quando e por quê.

### Comportamento por CMS

**WordPress**: os rascunhos podem ir para um site conectado como rascunhos preparados em vez de irem direto ao ar, e o fluxo de publicação se ajusta conforme o destino já esteja preparado ou publicado. Depois que você envia um rascunho, o Hi, Moose lembra, então você não consegue enviar o mesmo várias vezes sem querer.

**Webflow**: publicar numa collection carrega antes os demais campos obrigatórios dela e pede que você os preencha, para que a publicação não falhe no meio do caminho por um campo que você não conseguia ver.

Uma publicação que falha chega à sua [Caixa de entrada](../inbox/overview.md). Uma bem-sucedida não, de propósito.

## Fila de trabalho

Na Fila de trabalho se acumulam as alterações preparadas, as prévias pendentes e os itens à espera da sua aprovação, para que nada fique só dentro de uma conversa de chat esperando ser esquecido.

## Biblioteca e histórico

- A **[Biblioteca de artefatos](../library/overview.md)** guarda os artefatos duradouros que você gerou (briefings, rascunhos, conjuntos de FAQ, pontos principais, auditorias de AEO) para você encontrá-los e reaproveitá-los em vez de gerar tudo de novo.
- **[Chats (histórico)](../chat/chats-history.md)** é o histórico das suas sessões de chat salvas: reabra, renomeie ou exclua uma conversa anterior. É histórico de conversas, não um registro de publicações nem de resultados de visibilidade; um registro dedicado que ligue as alterações publicadas ao sinal de visibilidade que as motivou está previsto, mas ainda não foi construído.

## Por que isso importa

Esse caminho de prévia, aprovação e publicação é o que transforma uma recomendação em ação concluída e rastreável. Um fluxo que só produz conselhos é incompleto; um fluxo que termina numa alteração revisada, aprovada e publicada, com um registro que a liga ao sinal de visibilidade original, é a razão de existir do Hi, Moose.
