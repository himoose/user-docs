---
source_hash: b6472884da7df3e651f78be6893eb9896b38a6327a26378ca1d4cc26b2d0454e
---
!!! note "Tradução automática"
    Esta página foi traduzida por IA. A versão em inglês é a versão oficial.

    [Ler em inglês](https://himoose.com/docs/visibility/prompt-manager/)

# Gerenciador de Prompts

## Para que serve

O Gerenciador de Prompts é onde você monta e organiza as consultas reais que o Hi, Moose verifica nos mecanismos de IA: os prompts que seus clientes de fato digitariam ou perguntariam.

## Organizar prompts em categorias

Os prompts ficam agrupados em categorias exibidas na lista de filtros à esquerda: **Todos os prompts**, **Sem categoria** e as categorias personalizadas que você criar (por tema ou por campanha, por exemplo). Crie uma categoria nova no campo ao fim da lista. Espaços de trabalho do plano gratuito ficam limitados a 5 categorias.

## Adicionar e editar um prompt

Digite um prompt novo e adicione-o a uma categoria. Para cada prompt você pode:

- Editar o texto do prompt.
- Escolher em quais mecanismos ou modelos de IA ele roda. **Selecionar modelos** abre um seletor com ChatGPT, Claude, Gemini, Grok, Perplexity, Google AI Mode, Google AI Overview e Bing Copilot (a disponibilidade depende do seu plano e, nos mecanismos de consulta local, de o aplicativo para desktop estar em execução).
- Excluir o prompt.

Diferente de uma única configuração para a conta inteira, **a escolha de modelos é por prompt**: um prompt pode rodar só no ChatGPT e no Gemini enquanto outro cobre todos os mecanismos compatíveis, então você gasta sua cota apenas nos mecanismos que importam para aquela consulta.

## Diagnostic Prompts

**Prompts de diagnóstico** é uma categoria reservada e gerenciada pelo sistema, alimentada pelo seu [Perfil de Verdade da Marca](../getting-started/context/brand-truth-profile.md). Em vez de escrevê-los à mão:

1. Clique em **Gerar a partir da Verdade da Marca** (ou configure antes seu Perfil de Verdade da Marca, se ainda não fez isso).
2. O Hi, Moose propõe prompts feitos especificamente para flagrar quando a IA descreve mal seus clientes, suas capacidades ou seus concorrentes.
3. Revise as sugestões numa janela: ative ou desative cada prompt, ajuste a redação ou remova algum por completo antes de adicioná-los ao monitoramento.
4. A janela mostra um custo estimado antes de você confirmar: prompts × modelos × execuções por semana ≈ total de execuções semanais.

Se o seu Perfil de Verdade da Marca ainda não tiver conteúdo suficiente para gerar prompts de diagnóstico significativos, o Hi, Moose diz isso em vez de produzir enchimento genérico: acrescente antes perguntas de clientes, capacidades principais ou concorrentes ao seu perfil.

## Armazenamento local dos prompts

Nos planos BYOK, que funcionam somente localmente, as categorias de prompts, as definições dos prompts e as seleções de modelos ficam salvas no seu dispositivo em vez de sincronizadas com a nuvem.
