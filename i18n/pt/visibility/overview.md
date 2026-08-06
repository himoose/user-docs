---
source_hash: 40b089c8c06f81c797410e131c0f51ee08f0beba3baaaf1ad18b0794a101df1a
---
# Visibilidade

## Para que serve

O painel de Visibilidade mostra como sua marca realmente se sai na busca com IA: as consultas que os clientes usam para encontrar você, se sua marca entra na lista de indicações e se os mecanismos de IA a descrevem com precisão. É a visão principal para as etapas **monitorar** e **detectar** do [ciclo central de operações](../index.md#o-ciclo-central-de-operacoes).

O painel tem três abas:

| Aba | A que ela responde |
|---|---|
| **Visão geral** | Como estou indo? |
| **[Concorrência](competitors.md)** | Como estou indo em relação a eles? |
| **Temas e mecanismos** | Onde exatamente estou forte ou fraco? |

## Métricas

Cada execução reporta algumas métricas principais para o período selecionado:

- **Participação nas menções**: com que frequência sua marca é mencionada nos prompts e mecanismos monitorados.
- **Participação nas citações**: com que frequência seu domínio é de fato citado como fonte.
- **Sentimento**: o tom médio (positivo, misto, neutro, negativo) das menções.
- **Posição média**: onde sua marca costuma aparecer quando entra numa lista ou num ranking. Mostra **Dados insuficientes** enquanto não houver menções posicionadas suficientes para uma média.
- **Desvio de narrativa**: se as respostas da IA estão se afastando do seu posicionamento pretendido.
- **Paridade de recursos**: se as respostas da IA representam com precisão o que você oferece.

Narrative Drift e Feature Parity mostram **Não avaliado** com um link de configuração enquanto você não preencher seu Perfil de Verdade da Marca. Essas duas métricas só fazem sentido quando o Hi, Moose sabe o que é verdade sobre sua marca para comparar. Veja [Perfil de Verdade da Marca](../getting-started/context/brand-truth-profile.md).

!!! note "Observações que falharam são excluídas, não contadas como ausência"
    Se um mecanismo estava indisponível ou uma requisição falhou, aquela observação fica de fora de todas as métricas em vez de ser pontuada como «sua marca não foi mencionada». Uma execução com problemas de conexão reporta menos observações em vez de indicar uma queda que não existiu. A visão por prompt marca essas como **Resposta indisponível** e informa quantas foram excluídas.

## Filtros e período

- Filtre por **Tema**, **Mecanismo de IA**, **Prompt** (seleção múltipla com busca), **Página**, **Sentimento**, **Narrativa** ou **Paridade de recursos**, ou limpe todos os filtros de uma vez.
- O filtro **Página** restringe a URLs específicas e permite busca por caminho. Ele mostra corretamente os mecanismos em que a URL **não** foi citada, então você vê tanto onde uma página falta quanto onde ela aparece.
- Defina um intervalo de datas em **Período** e clique em **Aplicar**, ou clique em **Comparar** para sobrepor um período anterior ou a execução anterior.

## Tendência ao longo do tempo

O gráfico de tendência traça **Menções**, **Citações**, **% positivo** ou a posição média em intervalos de **dia**, **semana** ou **mês**, separados por mecanismo de IA ou com **Todos os modelos** somados, para você ver se um mecanismo específico está movendo os números.

## Detalhe por prompt

Abaixo do gráfico:

- **Taxa de menção** separa os resultados por mecanismo, mostrando quais mencionaram você e quais não.
- **Páginas mais citadas** mostra quais URLs suas estão sendo citadas e por quais mecanismos.
- **Detalhamento por prompt** expande qualquer prompt monitorado para ver os resultados individuais por mecanismo, incluindo a resposta completa da IA e o raciocínio de sentimento, narrativa e paridade de recursos.

Cada prompt traz um link para **investigar no chat**, que entrega os dados exatos da observação ao Moose e pede uma recomendação: se o próximo passo deve ser uma [auditoria de AEO](../features/aeo-audits.md) de uma página existente ou um novo [briefing com rascunho](../features/content-briefs.md).

## Temas e mecanismos

Esta aba decompõe o desempenho de duas formas:

- **Taxa de menção por tema**: com que frequência cada marca aparece nas respostas de IA para cada tema.
- **Tendência da taxa de menção por tema**: o mesmo dado, distribuído no tempo.
- **Taxa de menção por plataforma**: um mapa de calor da frequência com que cada marca aparece nas respostas de cada plataforma no período.

Os temas vêm das categorias dos seus prompts. Se seus prompts não estiverem categorizados, esta aba pede que você os organize no [Gerenciador de Prompts](prompt-manager.md) em vez de mostrar um gráfico vazio.

## Exportar

**Exportar** oferece dois formatos:

- **Planilha CSV**: todos os resultados da visão atual, para Excel ou Google Sheets.
- **Relatório executivo em PDF**: um relatório pronto para impressão da visão atual, incluindo os gráficos e dados competitivos da aba Concorrência.

As exportações respeitam os filtros ativos, e a capa do PDF informa quais filtros foram aplicados, para que um relatório não seja confundido com um retrato completo da conta. Nos planos pagos, o PDF leva sua [marca white label](../agency/white-label.md), se você a tiver configurado.

## Executar verificações de visibilidade

Clique em **Executar agora** para uma verificação sob demanda. O comportamento depende do seu [plano](../getting-started/account-modes.md):

- O **Preview Mode** faz consultas locais direto do seu dispositivo às superfícies públicas de busca com IA. O Hi, Moose pede confirmação antes, porque verificações em sequência podem disparar bloqueios temporários por limite de requisições nessas superfícies. A avaliação de sentimento, narrativa e paridade precisa de um modelo local Gemma 4 ativo; sem ele, essas verificações são puladas.
- Os **planos BYOK** rodam localmente com a sua chave do OpenRouter.
- Os **planos gerenciados** rodam pela infraestrutura do Hi, Moose. Se o seu espaço de trabalho não tiver cota suficiente neste mês para o agendamento atual, as execuções agendadas ficam pausadas até você mudar de plano, ajustar sua [frequência de execução](settings.md#agendamento-das-execucoes) ou a cota renovar. O Hi, Moose informa quantas unidades faltam em relação às restantes.

Você pode interromper uma execução antes do fim, e execuções interrompidas por uma atualização do aplicativo retomam em vez de se perderem.

## Para onde ir a partir daqui

- **[Concorrentes e Share of Voice](competitors.md)**: posição competitiva, citações de concorrentes e lacunas.
- **[Gerenciador de Prompts](prompt-manager.md)**: adicionar, organizar e categorizar os prompts monitorados.
- **[Configurações de Visibilidade](settings.md)**: agendamento das execuções, modelo de avaliação, monitoramento de concorrentes, termos e domínios secundários da marca e modelos padrão.
