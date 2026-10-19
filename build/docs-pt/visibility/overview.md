---
source_hash: e5cf87efe7298e31a0e0c034a7c0d36431b70c08378225d4dd5c73357dd59a4f
---
!!! note "Tradução automática"
    Esta página foi traduzida por IA. A versão em inglês é a versão oficial.

    [Ler em inglês](https://himoose.com/docs/visibility/overview/)

# Visibilidade

## Para que serve

O painel de Visibilidade mostra como sua marca realmente se sai na busca com IA: as consultas que os clientes usam para encontrar você, se sua marca entra na lista de indicações e se os mecanismos de IA a descrevem com precisão. É a visão principal para as etapas **monitorar** e **detectar** do [ciclo central de operações](../index.md#o-ciclo-central-de-operacoes).

O painel tem seis abas:

| Aba | A que ela responde |
|---|---|
| **Visão geral** | Como estou indo? |
| **[Concorrência](competitors.md)** | Como estou indo em relação a eles? |
| **Menções** | Quais marcas são citadas nessas respostas? |
| **Citações** | Em quais fontes os mecanismos realmente se apoiam? |
| **Temas e mecanismos** | Onde exatamente estou forte ou fraco? |
| **Prompts** | O que aconteceu em cada prompt individual? |

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

## A aba Visão geral

A Visão geral abre com um resumo escrito do recorte atual: alguns parágrafos que dizem onde você está, o que se moveu e o que merece atenção, em frases e não em números. Ele é gerado a partir da mesma folha de dados que o relatório usa, e você pode pedir **Reescrever o resumo** se quiser outra redação. Quando não há nenhum modelo disponível para escrevê-lo, a Visão geral recorre a uma versão construída direto dos números e avisa isso.

Abaixo do resumo há dois blocos:

- **Onde você está**: seu Share of Voice, a taxa de menção sobre as respostas lidas, as citações, a posição média quando você é citado e a taxa de menção por mecanismo, com todo o conjunto de marcas monitoradas ao lado.
- **A IA está descrevendo você com precisão?**: alinhamento de posicionamento, distribuição de tom e uma lista de **respostas que merecem revisão**: as respostas específicas em que um mecanismo descreveu mal uma capacidade ou se afastou do seu posicionamento. Cada uma abre a resposta ou salta para ela na aba Prompts.

## Menções

A aba **Menções** é a lista completa de cada marca, produto ou site que os mecanismos citaram nas respostas do recorte atual: não apenas você e seus concorrentes monitorados, mas todos que apareceram.

Cada linha mostra em quantas respostas a marca foi citada, esse dado como porcentagem das respostas do recorte, sua parcela de todas as menções, sua posição média entre as marcas citadas numa resposta e seu veredito de sentimento mais frequente. Passe o mouse sobre qualquer valor de sentimento para ver a divisão positivo/misto/neutro/negativo, e sobre um cabeçalho de coluna para a definição exata.

Acima da tabela, uma **tendência de presença nas menções** traça as marcas mais mencionadas, e você, ao longo do tempo.

É aqui que você encontra os concorrentes que não sabia que tinha. As marcas são lidas do texto da resposta pelo modelo de pontuação, então a lista revela nomes que você nunca adicionou ao seu monitoramento.

## Citações

A aba **Citações** é a mesma ideia aplicada às fontes: cada domínio ou página que os mecanismos citaram no recorte atual.

Alterne entre **Por domínio** e **Por URL de página**, e filtre por **Tudo** ou **Nem você nem um concorrente** para ver as fontes de terceiros que estão moldando as respostas. Cada fonte é categorizada: sua marca, concorrente, rede social, site de avaliações, publicação, referência, desenvolvimento ou outros.

As colunas são:

| Coluna | O que significa |
|---|---|
| **Prompts citados** | Em quantas respostas esse domínio ou URL foi citado |
| **Presença %** | Esse dado como parcela das respostas do recorte |
| **Contagem de citações** | Quantas vezes foi citado no total, contando repetições |
| **Visibilidade %** | Sua parcela de todas as citações do recorte |
| **Posição média** | Sua posição média nas listas de citações dos mecanismos |
| **Variação** | Movimento em relação ao período de comparação ou à execução anterior |

**Detalhes** em qualquer linha lista as páginas por trás dela e os prompts pelos quais cada página foi citada. Qualquer domínio da tabela pode ser adicionado direto aos seus concorrentes monitorados com **Monitorar como concorrente**, então um nome descoberto aqui entra no [Share of Voice](competitors.md) sem precisar digitar de novo.

As duas tabelas baixam em CSV.

!!! note "Mecanismos que não navegam não devolvem citações"
    As citações vêm de mecanismos que consultam a web enquanto respondem. Um modelo local, ou um mecanismo que responde só a partir do próprio treinamento, não devolve nenhuma, então uma tabela vazia sob um filtro estreito não significa necessariamente um problema no seu site.

## Temas e mecanismos

Esta aba decompõe o desempenho de duas formas:

- **Taxa de menção por tema**: com que frequência cada marca aparece nas respostas de IA para cada tema.
- **Tendência da taxa de menção por tema**: o mesmo dado, distribuído no tempo.
- **Taxa de menção por plataforma**: um mapa de calor da frequência com que cada marca aparece nas respostas de cada plataforma no período.

Os temas vêm das categorias dos seus prompts. Se seus prompts não estiverem categorizados, esta aba pede que você os organize no [Gerenciador de Prompts](prompt-manager.md) em vez de mostrar um gráfico vazio.

## Exportar

**Exportar** oferece dois formatos:

- **Planilha CSV**: todos os resultados da visão atual, para Excel ou Google Sheets.
- **Relatório executivo em PDF**: um relatório completo de treze seções sobre a visão atual, escrito para ser entregue a alguém que não estava na sala.

O relatório abre com uma narrativa escrita em vez de uma pilha de gráficos, e então percorre: onde você está, se a IA está descrevendo você com precisão, o movimento no período, mecanismo por mecanismo, onde a IA cita você, perguntas que os concorrentes ganham, por que os concorrentes são citados, o campo completo, marcas citadas nas respostas de IA, domínios que a IA cita, taxa de menção por mecanismo, taxa de menção por tema e uma seção final explicando como ler cada métrica.

As exportações respeitam os filtros ativos, e a capa do PDF informa quais filtros foram aplicados, para que um relatório não seja confundido com um retrato completo da conta. Nos planos pagos, o PDF leva sua [marca white label](../agency/white-label.md), se você a tiver configurado.

## Executar verificações de visibilidade

Clique em **Executar agora** para uma verificação sob demanda. O comportamento depende do seu [plano](../getting-started/account-modes.md):

- O **Preview Mode** faz consultas locais direto do seu dispositivo às superfícies públicas de busca com IA. O Hi, Moose pede confirmação antes, porque verificações em sequência podem disparar bloqueios temporários por limite de requisições nessas superfícies. A avaliação de sentimento, narrativa e paridade precisa de um modelo local Gemma 4 ativo; sem ele, essas verificações são puladas.
- Os **planos BYOK** rodam localmente com a sua chave do OpenRouter.
- Os **planos gerenciados** rodam pela infraestrutura do Hi, Moose. Se o seu espaço de trabalho não tiver cota suficiente neste mês para o agendamento atual, as execuções agendadas ficam pausadas até você mudar de plano, ajustar sua [frequência de execução](settings.md#agendamento-das-execucoes) ou a cota renovar. O Hi, Moose informa quantas unidades faltam em relação às restantes.

Você pode interromper uma execução antes do fim, e execuções interrompidas por uma atualização do aplicativo retomam em vez de se perderem.

## Quanto histórico é mantido

Cada observação que uma execução produz é arquivada localmente, para que tendências, comparações e as tabelas de Menções e Citações possam olhar mais para trás do que as últimas execuções. O arquivo guarda até **400 dias** por espaço de trabalho e até 200.000 observações; passando de qualquer um dos limites, as linhas mais antigas são descartadas.

Nos planos gerenciados pagos, as execuções de visibilidade que rodam na sua máquina também sincronizam seus resultados para a nuvem, de modo que os colegas vejam o mesmo histórico que você, e não apenas as execuções que aconteceram no próprio dispositivo deles.

## Para onde ir a partir daqui

- **[Concorrentes e Share of Voice](competitors.md)**: posição competitiva, citações de concorrentes e lacunas.
- **[Gerenciador de Prompts](prompt-manager.md)**: adicionar, organizar e categorizar os prompts monitorados.
- **[Configurações de Visibilidade](settings.md)**: agendamento das execuções, modelo de avaliação, monitoramento de concorrentes, termos e domínios secundários da marca e modelos padrão.
