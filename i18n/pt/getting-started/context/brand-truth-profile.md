---
source_hash: 266b8292b4154e6b52eab317de9e91cce7429af96c1d84999875493bfb8f09a8
---
# Perfil de Verdade da Marca

## Para que serve

O Perfil de Verdade da Marca é uma fonte de verdade legível por máquina sobre como a IA deve descrever sua empresa: o que você vende, quem você atende e com o que nunca deve ser confundido. O Hi, Moose o utiliza durante as execuções de [Visibilidade](../../visibility/overview.md) para detectar quando a resposta de um mecanismo de IA distorce sua marca ou repete uma narrativa ultrapassada, em vez de deixar esse julgamento a cargo de uma pontuação genérica de sentimento.

Assim como a Voz da marca, o Perfil de Verdade da Marca é delimitado ao [projeto](../projects.md) atual.

Todos os campos são opcionais, mas quanto mais você preencher, com mais precisão o Hi, Moose poderá sinalizar distorções e recomendar correções.

## Campos que você pode preencher

### Descrição principal

- **Como a IA deve descrever sua empresa hoje?**: a descrição canônica, em uma ou duas frases, que você gostaria de ver numa resposta do ChatGPT, Perplexity, Gemini ou Google AI.
- **Quem é seu cliente ideal hoje?**: escolhido entre segmentos comuns (pequenas e médias empresas, médio porte, grandes empresas, agências, marcas de e-commerce e outros), com anotações em texto livre.

### O que você oferece

- **Produtos, serviços ou categorias de produto que a IA deve saber que você oferece**: o essencial do que a IA deve saber que você fornece; não é preciso listar cada recurso.
- **Recursos ou capacidades que a IA deve mencionar**: um por linha. Ajuda o Hi, Moose a detectar quando a IA deixa de fora algo importante.

### Onde as descrições erram

- **O que a IA ou o mercado costumam errar sobre sua empresa?**: escolhido entre padrões comuns de distorção: tipo de cliente errado, categoria de produto errada, posicionamento ultrapassado, produtos ou recursos novos ausentes, concorrentes errados, superestimar ou subestimar a capacidade, confusão com outra marca e outros.
- **Um exemplo de algo que a IA ou o mercado erram**: um exemplo concreto que sustente o padrão acima.
- **Descrições ultrapassadas que devemos sinalizar**: categorias antigas, clientes-alvo ou limitações que não valem mais.
- **Quais erros da IA seriam mais prejudiciais?**: as categorias de erro de maior risco (descrição errada da empresa, cliente-alvo errado, preços ou disponibilidade incorretos, sentimento negativo ou enganoso, confusão de marca e outros).

### Vocabulário

- **Palavras ou expressões que a IA deve usar**: vocabulário preferido, um por linha.
- **Palavras ou expressões que a IA deve evitar**: vocabulário a evitar, um por linha.

### Contexto competitivo

- **Principais concorrentes ou alternativas**: de 3 a 5 concorrentes, alternativas ou categorias de ferramentas, cada um com uma nota opcional (por exemplo, «posicionado só para grandes empresas»). Serve para testar prompts de comparação.
- **Comparações que vale a pena monitorar**: buscas específicas de comparação ou de categorias alternativas que o Hi, Moose deve acompanhar (por exemplo, «melhores ferramentas de AEO para pequenas empresas»).

### Confiança e evidências

- **Perguntas de clientes que a IA deve responder corretamente**: perguntas diagnósticas alinhadas ao jeito como os clientes em potencial realmente compram.
- **Afirmações com que a IA deve ter cuidado**: preços, desempenho, certificações ou outras afirmações que exigem linguagem cuidadosa e qualificada.
- **Páginas ou fontes que provam seu posicionamento atual**: páginas, documentos ou estudos de caso específicos a tratar como prova importante, cada um com uma nota opcional.
- **Fontes já conhecidas como ultrapassadas ou imprecisas**: páginas de terceiros, diretórios ou citações anteriores da IA que sabidamente descrevem mal sua empresa, cada uma com uma nota sobre o que está errado.

## Como ele é usado

Durante uma execução de visibilidade, o Hi, Moose carrega o Perfil de Verdade da Marca do projeto (quando ele tem conteúdo significativo) e o usa para avaliar cada resposta da IA em busca de distorção ou desvio, comparando-a com sua descrição canônica, suas ofertas, seus concorrentes, seu vocabulário preferido e evitado e os padrões conhecidos de distorção, em vez de apenas checar se o nome da sua marca aparece.

## Como isso difere da Voz da marca

A [Voz da marca](brand-voice.md) trata de **estilo**: como sua marca deve soar. O Perfil de Verdade da Marca trata de **fatos**: o que é verdade sobre sua empresa e quais narrativas incorretas vigiar. Preencha a Voz da marca para definir o tom; preencha o Perfil de Verdade da Marca para flagrar quando a IA erra os fatos sobre você.

## Sincronização na nuvem

Assim como a Voz da marca, o Perfil de Verdade da Marca fica salvo por padrão localmente para o projeto atual. Sincronizá-lo com a nuvem, para ter backup e compartilhar com a equipe, exige um plano pago. Veja [Contexto](overview.md) para os detalhes.

## Monitoramento de concorrentes

A lista de concorrentes desta página é compartilhada com as [configurações de Visibilidade](../../visibility/settings.md). Os concorrentes adicionados em qualquer um dos dois lugares aparecem em ambos e alimentam o [Share of Voice, as citações de concorrentes e as lacunas](../../visibility/competitors.md).
