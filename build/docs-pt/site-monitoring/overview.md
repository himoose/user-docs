---
source_hash: 87a7b6f091685fae0a59b09ee8abe0ec965085647eb82bd29c1661777efb87ab
---
!!! note "Tradução automática"
    Esta página foi traduzida por IA. A versão em inglês é a versão oficial.

    [Ler em inglês](https://himoose.com/docs/site-monitoring/overview/)

# Monitoramento do site

## Para que serve

O Hi, Moose mantém um retrato local do seu site: quais páginas existem, o que há nelas e o que mudou desde a última vez. Esse retrato alimenta três coisas: os alertas de alterações relevantes para AEO na sua [Caixa de entrada](../inbox/overview.md), o índice de busca semântica que o Moose usa para responder perguntas sobre o seu próprio site, e o inventário de páginas de que as [auditorias](../features/aeo-audits.md) e os [briefings](../features/content-briefs.md) se servem.

Tudo isso fica em **Configurações → Monitoramento do site**, delimitado ao projeto atual.

## O rastreamento agendado

Ative **Executar rastreamento semanal do site** e o Hi, Moose atualiza as páginas monitoradas semanalmente, avisando quando surgirem alterações significativas. Escolha o dia e a hora no seu horário local.

Os rastreamentos manuais continuam disponíveis de qualquer forma. **Executar rastreamento agora** inicia imediatamente um rastreamento completo, com o progresso na barra de status no rodapé da janela. Você pode **parar** um rastreamento em andamento, e as páginas encontradas até ali são mantidas em vez de descartadas.

Sites grandes levam alguns minutos.

## O índice de busca

Abaixo dos controles de rastreamento fica o **Índice de pesquisa**, o índice semântico local que o Moose usa para responder perguntas sobre as páginas do seu site. Ele informa quantas páginas estão indexadas, quantos trechos essas páginas produziram e quando foi a última atualização.

A indexação é por trecho, não por página. Uma página longa vira muitos trechos pesquisáveis separadamente, e é por isso que o Moose consegue citar um parágrafo específico em vez de dizer que uma página trata «de modo geral» de um assunto.

- **Reconstruir índice** reindexa do zero.
- Se houver páginas novas ou alteradas desde a última atualização do índice, o Hi, Moose informa quantas. Elas serão indexadas no próximo rastreamento, ou você pode reconstruir o índice agora.

!!! note "O índice é honesto sobre o que não tem"
    Se você perguntar ao Moose sobre uma página que não foi indexada, ele diz isso e indica que você rode um rastreamento, em vez de deduzir algo a partir da URL da página.

## Páginas monitoradas

As páginas que o Hi, Moose verifica em busca de alterações relevantes para AEO. Páginas encontradas pela descoberta do site, pelo [Google Search Console](../integrations/google-search-console.md) e pelas [execuções de visibilidade](../visibility/overview.md) aparecem aqui automaticamente.

Você também pode adicionar páginas à mão com a URL completa, pesquisar e filtrar a lista, navegar por páginas e remover as que não interessam.

## Caminhos bloqueados

Os rastreamentos pulam os caminhos bloqueados e tudo o que está sob eles, e as páginas correspondentes saem do monitoramento.

A correspondência é por prefixo de segmento do caminho. Bloquear `/results/` cobre `/results/` e todos os seus subcaminhos, mas **não** `/results-archive/`: o segmento precisa coincidir, não só a cadeia de texto.

É a ferramenta certa para páginas de resultados de busca, páginas de listagem filtrada, arquivos paginados e qualquer outra coisa que gere um grande número de URLs quase idênticas que você prefere não rastrear, não indexar e sobre as quais não quer alertas.

## O que chega à sua Caixa de entrada

Um rastreamento produz **um único resumo por execução**, não um item por página alterada. O resumo abre numa tabela das páginas alteradas com o que mudou, um nível de impacto e ações por página.

Os níveis de impacto são **Crítico**, **Notável**, **Baixo**, **Inacessível** e **Não revisado**.

Dois controles regulam o ruído:

- **Incluir alterações informativas de AEO**: desativado por padrão. Quando ativado, alterações de baixo impacto também geram itens na Caixa de entrada.
- **Gravidade mínima das notificações do sistema operacional**: só itens da Caixa de entrada nesse nível ou acima disparam uma notificação do sistema. Ajuste para Informação se quiser que alterações de baixo impacto também apareçam no nível do sistema operacional.

## Perguntar ao Moose o que mudou

O resumo traz a ação **Perguntar ao Moose sobre tudo isso**, que entrega ao chat a captura completa do rastreamento e pergunta o que importa mais e por onde começar. Cada página tem sua própria ação **Perguntar ao Moose**, que passa apenas a alteração registrada daquela página.

As duas se limitam à captura registrada. Se ela não explicar por que algo mudou, o Moose tem instrução de dizer isso em vez de inventar um motivo.

## Páginas inacessíveis

Se uma página ou o site inteiro não puder ser acessado, isso é reportado como um tipo de alteração próprio em vez de ser ignorado em silêncio. Uma queda do site inteiro gera um único item **Site inacessível** em vez de um alerta por página.
