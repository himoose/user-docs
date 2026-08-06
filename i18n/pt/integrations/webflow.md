---
source_hash: 67912e0c53e927d4836f8b9c545fb59268db0fbc9165037df2930f6cfada0988
---
# Webflow

## Para que serve

Conectar um site Webflow para que o Hi, Moose possa examinar suas páginas e conteúdos e preparar alterações com prévia para publicação: FAQ, pontos principais, rascunhos baseados em briefing e recomendações de auditorias de AEO.

## Configurar uma conexão

1. Abra **Conexões** no aplicativo para desktop e escolha Webflow.
2. Clique em **Conectar MCP do Webflow**. A página de autorização do Webflow abre no seu navegador. Conclua o OAuth ali para finalizar a conexão.
3. Depois de conectado, escolha qual site autorizado do Webflow o Hi, Moose deve usar neste [projeto](../getting-started/projects.md).

## Preparar um destino de prévia

O Hi, Moose consegue descobrir **superfícies de conteúdo** no seu site Webflow conectado: páginas, posts, itens de collection e código personalizado, além de um esqueleto de página em branco para conteúdo que ainda não existe. Escolha um destino, acrescente notas sobre a alteração ou a intenção de publicação e prepare como destino de prévia. Dali em diante você revisa o rascunho preparado igual a qualquer outra conexão. Veja [Rascunhos, prévia e publicação](../features/drafts-and-publishing.md).

## Prontidão para prévia e publicação

Nem toda conexão do Webflow consegue fazer tudo ainda. O Hi, Moose reporta um entre vários estados para o seu site conectado: pronto tanto para preparar prévias quanto para publicar, só prévia, só publicação, ou conectado mas ainda não pronto para nenhum dos dois. Superfícies exclusivas do Designer (alterações que exigem o Webflow Designer diretamente) ainda não têm suporte.

## Publicar em collections

Ao publicar numa collection, o Hi, Moose carrega antes os demais campos obrigatórios dela e pede que você os preencha, para que a publicação não falhe no meio do caminho por um campo que você não conseguia ver.

## Segurança

A autorização do Webflow acontece pelo seu navegador, e a conexão resultante é usada só pelo processo em segundo plano do aplicativo para desktop; não é exposta à interface.
