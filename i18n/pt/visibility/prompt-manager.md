---
source_hash: 52e4fc142ac45ba9ec93251b7b681cb95c1e09d409fef443f88b56ac8cbebaa7
---
# Gerenciador de Prompts

## Para que serve

O Gerenciador de Prompts é onde você monta e organiza as consultas reais que o Hi, Moose verifica nos mecanismos de IA: os prompts que seus clientes de fato digitariam ou perguntariam.

## Organizar prompts em categorias

Os prompts ficam agrupados em categorias exibidas na lista de filtros à esquerda: **Todos os prompts**, **Sem categoria** e as categorias personalizadas que você criar (por tema ou por campanha, por exemplo). Crie uma categoria nova no campo ao fim da lista. Espaços de trabalho do plano gratuito ficam limitados a 5 categorias.

## Adicionar e editar um prompt

Digite um prompt novo e adicione-o a uma categoria. Para cada prompt você pode:

- Editar o texto do prompt.
- Escolher em quais mecanismos de IA ele roda. **Selecionar modelos** abre um seletor com todos os mecanismos que o seu plano pode monitorar, versões por API e de consulta local (veja [os mecanismos que você pode monitorar](settings.md#os-mecanismos-que-voce-pode-monitorar)). Os mecanismos de consulta local precisam do aplicativo para desktop aberto quando a execução acontece.
- Aposentar o prompt (veja abaixo).
- Excluir o prompt.

Diferente de uma única configuração para a conta inteira, **a escolha de modelos é por prompt**: um prompt pode rodar só no ChatGPT e no Gemini enquanto outro cobre todos os mecanismos compatíveis, então você gasta sua cota apenas nos mecanismos que importam para aquela consulta.

## Buscar e selecionar vários prompts

**Buscar prompts** filtra a lista por texto. Marque vários prompts e a barra de ferramentas oferece **Atribuir categorias**, **Atribuir modelos**, **Aposentar selecionados** e **Excluir selecionados**, de modo que uma mudança em muitos prompts é salva em um único passo, e não prompt a prompt. Você só pode excluir os prompts que criou, a menos que seja o proprietário da equipe.

## Aposentar um prompt

Aposente um prompt quando ele ficou desatualizado mas o histórico ainda vale a pena guardar, por exemplo um prompt que cita o ano passado. Um prompt aposentado:

- mantém todos os resultados anteriores, então tendências e relatórios continuam a incluí-los;
- fica de fora das novas execuções, então não custa nada;
- fica de fora da lista de [Oportunidades](overview.md#oportunidades).

Os prompts aposentados ficam na seção **Prompts aposentados** da lista de filtros, cada um com a data em que foi aposentado, e **Restaurar** o devolve ao monitoramento. Adicionar um prompt novo com o mesmo texto de um aposentado não faz nada; restaure-o em vez disso. **Excluir** também tira um prompt do monitoramento futuro e mantém os dados históricos de execução para relatórios, mas não há como restaurar.

## Diagnostic Prompts

**Prompts de diagnóstico** é uma categoria reservada e gerenciada pelo sistema, alimentada pelo seu [Perfil de Verdade da Marca](../getting-started/context/brand-truth-profile.md). Em vez de escrevê-los à mão:

1. Clique em **Gerar a partir da Verdade da Marca** (ou configure antes seu Perfil de Verdade da Marca, se ainda não fez isso).
2. O Hi, Moose propõe prompts feitos especificamente para flagrar quando a IA descreve mal seus clientes, suas capacidades ou seus concorrentes.
3. Revise as sugestões numa janela: ative ou desative cada prompt, ajuste a redação ou remova algum por completo antes de adicioná-los ao monitoramento.
4. A janela mostra um custo estimado antes de você confirmar: prompts × modelos × execuções por semana ≈ total de execuções semanais.

Se o seu Perfil de Verdade da Marca ainda não tiver conteúdo suficiente para gerar prompts de diagnóstico significativos, o Hi, Moose diz isso em vez de produzir enchimento genérico: acrescente antes perguntas de clientes, capacidades principais ou concorrentes ao seu perfil.

## Armazenamento local dos prompts

Nos planos BYOK, que funcionam somente localmente, as categorias de prompts, as definições dos prompts e as seleções de modelos ficam salvas no seu dispositivo em vez de sincronizadas com a nuvem.
