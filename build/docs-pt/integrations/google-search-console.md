---
source_hash: 07b1b5e8bf746dc48362fa004a86b7566ef960fafcbe265cebb6ecd32d7aff91
---
!!! note "Tradução automática"
    Esta página foi traduzida por IA. A versão em inglês é a versão oficial.

    [Ler em inglês](https://himoose.com/docs/integrations/google-search-console/)

# Google Search Console

## Para que serve

Conectar o Google Search Console para que o Hi, Moose traga seus dados de desempenho de busca do Google (impressões, cliques e consultas) para a mesma base local de evidências usada por [Visibilidade](../visibility/overview.md), [auditorias de AEO](../features/aeo-audits.md) e [briefings de conteúdo](../features/content-briefs.md).

!!! note "Disponibilidade"
    A conexão com o Google Search Console está incluída em todos os planos pagos: BYOK Premium, BYOK Agency e todos os planos gerenciados. Não está incluída no BYOK Free nem no Preview Mode. Veja [Tipos de conta e planos](../getting-started/account-modes.md).

## Por que isso fica local

O acesso ao Search Console exige as credenciais OAuth da sua conta do Google, e o Hi, Moose as trata como sensíveis por concepção: a autorização acontece no seu navegador e os tokens resultantes ficam guardados **somente na sua máquina**. Os serviços em nuvem do Hi, Moose nunca recebem seus tokens de acesso, tokens de atualização ou segredos de cliente do Google para essa conexão: o aplicativo para desktop é a única coisa que fala com o Google Search Console em seu nome.

## Configurar uma conexão

1. Abra **Conexões** no aplicativo para desktop e escolha Google Search Console.
2. Autorize o acesso no seu navegador.
3. Vincule uma propriedade do Search Console ao [projeto](../getting-started/projects.md) ativo.

## O que você pode fazer com isso

- Puxar um retrato local do desempenho de páginas e consultas da propriedade vinculada.
- Comparar o retrato mais recente com uma janela anterior para ver mudanças relevantes.
- Perguntar sobre seus dados do Search Console direto no chat. O Moose consulta de forma agêntica, estreitando por várias consultas para responder a uma pergunta vaga, em vez de rodar um relatório fixo. O modelo interpreta sua pergunta, mas é o aplicativo para desktop que valida e executa cada consulta localmente, então seus dados e a guarda dos tokens ficam no dispositivo.
- Levar as evidências do Search Console ao diagnóstico de visibilidade e à priorização de quais páginas merecem um briefing de conteúdo ou uma auditoria de AEO.

## Onde os dados ficam

Os dados do Search Console trazidos ao Hi, Moose ficam guardados **localmente no seu dispositivo**, e não na nuvem do Hi, Moose. Fazem parte da sua base local de evidências e entram num [backup local](../getting-started/settings.md#dados-e-backup) em vez de sincronizar entre máquinas.

## Escopo atual

Esta conexão é somente leitura na versão 1: o Hi, Moose não escreve de volta no Search Console. Por ora, dá para vincular uma propriedade por projeto.

O Search Console exige um plano pago. Não está incluído no Preview Mode nem no BYOK Free.

!!! note "Atualize o aplicativo se a conexão falhar no Windows"
    Os instaladores para Windows anteriores à versão 0.3.245 saíram sem as credenciais do Google de que a conexão precisa, então conectar sempre falhava no aplicativo instalado. Atualizar resolve.
