---
source_hash: a8e831ea98a893f4158e5124991eae0686f8eb64e2448fe9541f8444c4680099
---
# Auditorias de AEO

## Para que serve

Uma auditoria de AEO (otimização para mecanismos de resposta) avalia o quanto uma página está pronta para ser compreendida, recuperada e citada por sistemas de IA como ChatGPT, Google AI Overviews, Perplexity e Gemini, e então entrega um plano de ação priorizado e apoiado em evidências para melhorá-la.

Isso substitui «dicas de AEO» avulsas por um artefato duradouro e comparável: cada auditoria produz um placar e um plano de ação que você pode reconsultar, e auditorias posteriores na mesma página mostram se suas alterações de fato moveram a pontuação.

## O que é avaliado

A pontuação geral é uma combinação ponderada de oito categorias, cada uma de 0 a 100:

1. **Atualidade**: sinais de atualidade e de atualização.
2. **Estrutura**: títulos, listas, tabelas e parágrafos que um mecanismo de resposta consiga analisar.
3. **Semantic Clarity**: o quanto o conteúdo se alinha à sua consulta-alvo e à intenção dela.
4. **Facilidade de extração**: com que facilidade um mecanismo de resposta extrai uma definição, um dado ou um ponto principal.
5. **Citation Potential**: sinais de atribuição e de fontes, com base nos links de referência externos da página.
6. **Abrangência**: cobertura dos subtemas que pessoas e mecanismos de resposta esperam para a consulta.
7. **Trust Signals**: consistência, especificidade e cautela das afirmações no modo como a página apresenta atribuição e fontes. Esta categoria não confere as afirmações contra fontes externas: ela mede o quanto as próprias afirmações da página são bem atribuídas e específicas.
8. **Answer Readiness**: resposta direta perto do começo, uma ideia por bloco, linguagem referencial clara (evitando «isso/ele/eles» vagos) e nomeação consistente das entidades. A avaliação considera o idioma em inglês, alemão, espanhol, francês, italiano e português.

A auditoria também acompanha sinais de Engagement, Entity Recognition e Media Enrichment, embora eles não entrem na pontuação geral nem apareçam no placar.

## Verificações de infraestrutura e recuperação

Ao lado da avaliação de conteúdo, cada auditoria verifica se um mecanismo de resposta consegue sequer recuperar a página:

- **Acesso dos rastreadores de IA**: confere as regras do robots.txt para cada um dos tokens específicos de rastreador de IA usados por OpenAI, Anthropic, Perplexity, Google e Bing (tratando à parte os rastreadores de treinamento, de indexação e de consulta ao vivo, já que um site pode bloquear um e liberar outro). Um rastreador de recuperação ou indexação bloqueado é marcado como crítico; um agente de consulta ao vivo bloqueado é de prioridade média; e um bloqueio só de treinamento é anotado como escolha de política legítima e neutra, que não afeta as citações.
- **Renderização no servidor e detecção de casca renderizada no cliente**: a maioria dos rastreadores de IA não executa JavaScript. Se o conteúdo essencial de uma página só aparece depois da renderização no cliente, isso é marcado como achado crítico e de destaque, não como nota técnica menor, porque é um problema de recuperação que vem antes de qualquer otimização de conteúdo.
- **Higiene de recuperação**: confere uma amostra de links internos em busca de links quebrados e cadeias de redirecionamento.
- **Presença no índice do Bing**: verifica se a página parece indexada pelo Bing, já que o Microsoft Copilot e parte da busca do ChatGPT se apoiam no índice do Bing. Os veredictos são deliberadamente cautelosos: um resultado inconclusivo é reportado como inconclusivo em vez de chutado, e o veredicto «não listada» só aparece quando a verificação tem sinal real que o sustente.

## Contexto externo e de cobertura

- **Panorama de citações**: quando roda pesquisa em tempo real, a auditoria informa quais domínios um mecanismo de resposta de fato citou para a consulta-alvo, se o site auditado está entre eles e se fontes de terceiros (sites de comunidade, sites de avaliações, Wikipédia, YouTube) dominam a resposta. Isso é apresentado como contexto que, em boa parte, você não corrige editando sua própria página, e não entra na pontuação.
- **Seu próprio histórico de visibilidade**: se a URL auditada foi citada nas suas [execuções de visibilidade](../visibility/overview.md) recentes, a auditoria puxa esse dado, para que as recomendações levem em conta como a página já se comporta nas respostas de IA em vez de tratá-la como incógnita. Execuções que falharam ficam de fora disso, para que uma queda não seja lida como ausência de citações.
- **Cobertura fan-out**: confere a página contra consultas relacionadas para as quais um mecanismo de resposta poderia expandir a consulta original (perguntas de «As pessoas também perguntam», buscas relacionadas, palavras-chave secundárias). Quando várias delas não são tratadas na página, isso vira uma recomendação concreta de cobrir essas perguntas relacionadas.

## Níveis de evidência nas recomendações

Cada problema e cada recomendação recebem uma etiqueta conforme a força da evidência por trás:

- **Comprovado**: pré-condições de recuperação com forte respaldo empírico (acesso dos rastreadores, renderização no servidor, links funcionando, indexação nos buscadores).
- **Indicativa**: apoiadas em pesquisa observacional em larga escala, mas sem garantia (resposta no começo, atualidade, clareza estrutural).
- **Best-practice**: plausíveis e baratas, mas sem prova de que movam as citações de IA (acrescentar estatísticas, citações ou refinar as fontes).

A auditoria não recomenda marcação schema/JSON-LD, arquivos `llms.txt` nem táticas de acúmulo de palavras-chave como formas de melhorar as citações de IA, já que a pesquisa atual não sustenta tratá-los como alavancas de citação.

## Quantas recomendações você recebe

O número de recomendações depende de quantos problemas reais são encontrados, ponderado pela pontuação geral da página: uma página com problemas de verdade recebe mais recomendações, e uma que já pontua bem recebe menos, às vezes nenhuma. O número nunca é inflado para bater uma meta fixa.

## Rodar uma auditoria

1. Informe uma URL em produção ou cole um rascunho, junto com a consulta-alvo que alguém usaria para achar esse conteúdo.
2. O Hi, Moose captura um retrato delimitado do conteúdo e da estrutura da página, usando como evidência principal a versão estática (sem renderização por JavaScript), porque é o que mais se aproxima do que a maioria dos rastreadores de IA realmente vê.
3. Quando é útil, coleta evidências reais de mecanismos de resposta ou de citações para a consulta-alvo.
4. Se o seu projeto tiver uma propriedade do [Google Search Console](../integrations/google-search-console.md) conectada para essa URL, seus dados de desempenho entram na priorização e na cautela das recomendações. Isso não muda a pontuação de AEO em si.
5. O Hi, Moose avalia a página, cria uma linha de base (ou confere contra uma anterior) e monta a auditoria como um artefato duradouro com um plano de próxima ação explícito.

## Verificar a melhora

Como cada auditoria é salva como linha de base, rodar uma auditoria nova na mesma página depois das alterações produz um **resultado de verificação**, que mostra se a pontuação realmente melhorou, e não apenas se você fez edições.

## Integridade

As auditorias de AEO nunca inventam evidências. Se o Hi, Moose não conseguir coletar as evidências ou concluir de fato uma etapa de avaliação, a auditoria falha explicitamente e diz por quê, em vez de apresentar um palpite como resultado pronto. Se a pesquisa em tempo real e a análise de concorrentes não concluírem numa auditoria gerenciada paga, a auditoria termina mesmo assim com as evidências de página disponíveis, com uma nota explícita de que a pesquisa em tempo real não estava disponível naquela execução.

## Direitos por plano

- O **Preview Mode (gratuito)** roda as auditorias num modelo local Gemma 4 ativo. Não existe mais uma cota gratuita mensal de auditorias na nuvem: configure um [modelo local](../getting-started/settings.md#local-model) e as auditorias ficam gratuitas, quantas vezes você quiser.
- Os **planos BYOK** rodam as auditorias localmente com a sua chave do OpenRouter.
- Os **planos gerenciados** usam os modelos gerenciados do Hi, Moose no saldo normal de créditos da sua conta. Não há uma moeda separada de «créditos de auditoria» para acompanhar.

## Próximas ações após uma auditoria

O plano de ação de uma auditoria leva direto a outros recursos: criar um [briefing de conteúdo](content-briefs.md), preparar uma [alteração com prévia](drafts-and-publishing.md) ou acrescentar FAQ ou pontos principais. A auditoria é, portanto, um ponto de partida para agir, e não apenas um relatório.
