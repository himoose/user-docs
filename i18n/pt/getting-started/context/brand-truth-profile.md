---
source_hash: 5904a00ba3d332904ad56c2821ae256bf5463e1eabcaa2b39e0c5d75e3fe3d67
---
# Perfil de Verdade da Marca

## Para que serve

O Perfil de Verdade da Marca é uma fonte de verdade legível por máquina sobre como a IA deve descrever a sua empresa: o que vende, quem serve e com o que nunca deve ser confundida. O Hi, Moose usa-o durante as execuções de [Visibilidade](../../visibility/overview.md) para detetar quando a resposta de um motor de IA distorce a sua marca ou repete uma narrativa desatualizada, em vez de deixar esse julgamento a uma pontuação genérica de sentimento.

Tal como a Voz da marca, o Perfil de Verdade da Marca pertence ao [projeto](../projects.md) atual.

Todos os campos são opcionais, mas quanto mais preencher, com mais precisão o Hi, Moose consegue assinalar distorções e recomendar correções.

## Campos que pode preencher

Pode preencher estes campos à mão ou deixar o Hi, Moose sugerir valores a partir do seu message house ou dos documentos de posicionamento. Veja [Preencher a partir dos documentos de marca](#preencher-a-partir-dos-documentos-de-marca) abaixo.

### Descrição principal

- **Como a IA deve descrever sua empresa hoje?**: a descrição canónica, numa ou duas frases, que gostaria de ver numa resposta do ChatGPT, Perplexity, Gemini ou Google AI.
- **Quem é seu cliente ideal hoje?**: escolhido entre segmentos comuns (PME, empresas de média dimensão, grandes empresas, agências, marcas de comércio eletrónico e outros), com notas em texto livre.

### O que oferece

- **Produtos, serviços ou categorias de produtos que a IA deve saber que você oferece**: o essencial do que a IA deve saber que fornece. Não é preciso listar cada funcionalidade.
- **Recursos ou funcionalidades que a IA deve mencionar**: um por linha. Ajuda o Hi, Moose a detetar quando a IA deixa de fora algo importante.

### Onde as descrições erram

- **O que a IA ou o mercado costuma entender errado sobre sua empresa?**: escolhido entre padrões comuns de distorção: tipo de cliente errado, categoria de produto errada, posicionamento desatualizado, produtos ou funcionalidades novos em falta, concorrentes errados, exagerar ou subestimar capacidades, confusão com outra marca e outros.
- **Um exemplo de algo que a IA ou o mercado entende errado**: um exemplo concreto que ilustre o padrão acima.
- **Descrições desatualizadas que devemos sinalizar**: categorias antigas, clientes-alvo ou limitações que já não se aplicam.
- **Quais erros da IA seriam mais prejudiciais?**: as categorias de erro de maior risco (descrição errada da empresa, cliente-alvo errado, preços ou disponibilidade incorretos, sentimento negativo ou enganador, confusão de marca e outros).

### Vocabulário

- **Palavras ou frases que a IA deve usar**: vocabulário preferido, um por linha.
- **Palavras ou frases que a IA deve evitar**: vocabulário a evitar, um por linha.

### Contexto competitivo

- **Principais concorrentes ou alternativas**: 3 a 5 concorrentes, alternativas ou categorias de ferramentas, cada um com uma nota opcional (por exemplo, «posicionado só para grandes empresas»). Serve para testar prompts de comparação.
- **Comparações que vale a pena monitorizar**: pesquisas específicas de comparação ou de categorias alternativas que o Hi, Moose deve acompanhar (por exemplo, «melhores ferramentas de AEO para pequenas empresas»).

### Confiança e evidências

- **Perguntas de clientes que a IA deve responder corretamente**: perguntas de diagnóstico alinhadas com a forma como os potenciais clientes compram.
- **Afirmações com que a IA deve ter cuidado**: preços, desempenho, certificações ou outras afirmações que exigem linguagem cuidadosa e ressalvas.
- **Páginas ou fontes que comprovam o seu posicionamento atual**: páginas, documentos ou estudos de caso específicos a tratar como prova importante, cada um com uma nota opcional.
- **Fontes já conhecidas como desatualizadas ou imprecisas**: páginas de terceiros, diretórios ou citações anteriores da IA que se sabe descreverem mal a sua empresa, cada uma com uma nota sobre o que está errado.

## Preencher a partir dos documentos de marca

Carregue o seu message house ou os documentos de posicionamento em [Documentos de marca](brand-documents.md) e clique em **Preencher perfis a partir dos documentos**. O Hi, Moose sugere valores para campos como a descrição canónica, o cliente ideal, as ofertas, os concorrentes e as afirmações sensíveis. Cada sugestão mostra a citação de onde veio, e as sugestões que o documento não sustenta palavra por palavra são descartadas. Os campos vazios vêm marcados por predefinição. Os campos que já preencheu vêm desmarcados.

## Como é usado

### Detetar distorções

Durante uma execução de visibilidade, o Hi, Moose carrega o Perfil de Verdade da Marca do projeto (quando tem conteúdo relevante) e usa-o para avaliar cada resposta da IA quanto a distorções ou desvios. Compara a resposta com a sua descrição canónica, as suas ofertas, os seus concorrentes, o vocabulário preferido e a evitar e os padrões conhecidos de distorção, em vez de apenas verificar se o nome da sua marca aparece.

### Escrever conteúdo dirigido ao seu comprador

O perfil também alimenta as ferramentas de conteúdo. Os [briefings de conteúdo](../../features/content-briefs.md), os [rascunhos de post](../../features/blog-post-draft.md), os [pontos principais](../../features/key-points.md) e as [FAQ](../../features/faq-generator.md) leem o perfil antes de escrever o que quer que seja, incluindo os seus **segmentos de cliente ideal** e as notas livres ao lado deles.

É a diferença entre um briefing escrito para «leitores interessados no tema» e um escrito para equipas de operações de empresas de média dimensão que estão a avaliar uma mudança de fornecedor. Preencher os campos de cliente ideal uma vez muda o resultado de todas as ferramentas de escrita a partir daí, o que os torna dos campos mais valiosos deste ecrã.

O [Send Moose](../../send-moose/overview.md) também lê o perfil em trabalhos sobre a sua própria marca.

## Em que difere da Voz da marca

A [Voz da marca](brand-voice.md) trata do **estilo**: como a sua marca deve soar. O Perfil de Verdade da Marca trata dos **factos**: o que é verdade sobre a sua empresa e que narrativas incorretas vigiar. Preencha a Voz da marca para definir o tom. Preencha o Perfil de Verdade da Marca para detetar quando a IA erra os factos sobre si.

## Sincronização na nuvem

Tal como a Voz da marca, o Perfil de Verdade da Marca fica guardado por predefinição localmente para o projeto atual. Sincronizá-lo com a nuvem, para ter uma cópia de segurança e partilhá-lo com a equipa, exige um plano pago. Veja [Contexto](overview.md) para mais detalhes.

## Monitorização de concorrentes

A lista de concorrentes desta página é partilhada com as [definições de Visibilidade](../../visibility/settings.md). Os concorrentes adicionados em qualquer um dos dois sítios aparecem em ambos e alimentam o [Share of Voice, as citações de concorrentes e as lacunas](../../visibility/competitors.md).
