---
source_hash: 6b12d8d972a33f212f60d823c287d184f083cfb60d8934f6b9ac8571ceb3c32e
---
!!! note "Tradução automática"
    Esta página foi traduzida por IA. A versão em inglês é a versão oficial.

    [Ler em inglês](https://himoose.com/docs/chat/tools-and-specialists/)

# Ferramentas e especialistas do chat

## Para que serve

Além de digitar um pedido, o campo de composição do chat oferece algumas formas a mais de moldar o que o Hi, Moose faz com sua mensagem: anexar contexto, escolher um especialista para focar a conversa ou disparar um atalho rápido.

## Anexos

Clique no botão de anexo no campo de composição para acrescentar contexto à sua mensagem:

- **Enviar arquivo ou imagem**: `.txt`, `.md`, `.csv`, `.doc`, `.docx`, `.pdf`, `.xls`, `.xlsx`, `.jpg` e `.png`. Planilhas viram texto legível, então você pode entregar uma pasta de trabalho ao Moose e perguntar o que há nela.
- **Capturar a tela**: escolha um monitor ou uma janela e arraste para recortar exatamente a área que quer enviar. No macOS, na primeira vez você precisa conceder ao Hi, Moose acesso à gravação de tela.
- **Adicionar da Biblioteca**: anexe um artefato salvo da [Biblioteca de artefatos](../library/overview.md) (um briefing, um rascunho, pontos principais ou FAQ) como contexto, em vez de colar de novo.
- **Banco de dados vetorial do site**: anexe o site indexado do seu projeto para que o Moose responda a partir das suas páginas reais, e não do que ele supõe que esteja nelas. Monte o índice em [Monitoramento do site](../site-monitoring/overview.md).

## Ferramentas que o Moose pode usar

O chat não se limita a gerar texto. No decorrer de uma conversa, o Moose pode usar ferramentas em seu nome e mostra quando faz isso.

| Ferramenta | O que faz |
|---|---|
| Busca web | Resultados em tempo real, nos planos que incluem busca web no chat |
| Ler uma página | Consultar uma URL específica |
| Busca no índice do site | Responder a partir das suas páginas indexadas |
| Search Console | Consultar seus dados conectados do [Search Console](../integrations/google-search-console.md) |
| Verificação instantânea da marca | Consultar uma query em cinco mecanismos de IA; veja [Verificação instantânea da marca](../tools/instant-brand-check.md) |
| Verificação de cobertura | Descobrir se seu site já cobre um assunto |
| Geração de imagens | Produzir uma imagem para um rascunho |
| Ajuda sobre o aplicativo | Apontar a documentação certa ou o suporte |

O uso de ferramentas funciona igual nos planos gerenciados, nos planos BYOK e nos modelos locais Gemma 4.

!!! note "Perguntas sobre o Search Console são respondidas de forma agêntica"
    O Moose consulta seus dados do Search Console de modo iterativo em vez de rodar um relatório fixo. Se você fizer uma pergunta vaga, ele estreita o escopo por várias consultas até respondê-la, em vez de devolver um despejo genérico.

## Especialistas

Os especialistas são portas de entrada focadas para o mesmo operador principal. Não são ferramentas nem memórias separadas, só um jeito de apontar a conversa para uma tarefa específica. Abra o seletor de especialista para escolher um:

- **Especialista em Content Brief**: montar um briefing enxuto com estrutura e próximos passos.
- **Especialista em Google Search Console**: perguntar ao Moose sobre seus dados conectados do [Google Search Console](../integrations/google-search-console.md). Esse especialista precisa de uma conta do Search Console conectada ou de uma propriedade salva no projeto ativo antes de responder a partir dos seus dados.
- **Especialista em geração de áudio**: transformar um pedido num roteiro falado limpo.
- **Especialista em rascunhos**: gerar conteúdo de rascunho pronto para revisão e edição.
- **Especialista em FAQ**: redigir FAQ concisas em torno das perguntas de maior valor.
- **Especialista em Pontos principais**: destacar primeiro as conclusões mais importantes.

Com um especialista ativo, a etiqueta dele aparece na conversa, e você pode removê-la a qualquer momento para voltar ao chat geral.

### Especialistas personalizados

Você também pode criar seu próprio especialista local: dê um nome e um resumo do trabalho que ele deve cobrir, depois escolha a quais partes do seu contexto ele tem acesso: contexto de projeto, perfil da marca, contexto do site, histórico do chat, saída voltada a rascunho ou saída em markdown. Especialistas personalizados também podem ser importados, se alguém compartilhar um com você.

## Atalhos rápidos

O campo de composição traz atalhos de um clique para as tarefas mais comuns, entre eles:

- [Rodar uma auditoria de AEO](../features/aeo-audits.md)
- [Criar um briefing de conteúdo com base em pesquisa](../features/content-briefs.md)
- [Criar FAQ com base em pesquisa](../features/faq-generator.md)
- [Gerar pontos principais otimizados](../features/key-points.md)
- [Criar um rascunho de post de blog](../features/blog-post-draft.md)
- [Criar um post de glossário](../features/glossary-post.md)
- [Criar conteúdo de landing page](../features/landing-page-content.md)
- [Criar conteúdo de página de produto](../features/product-page-content.md)
- [Capturar consultas de grounding do Google AI Mode para um prompt](../features/grounding-queries.md)
- [Capturar consultas fan-out do ChatGPT para um prompt](../features/fan-out-queries.md)
- [Transformar conteúdo em texto para áudio](../audio/overview.md)

O mesmo conjunto está no **[menu Ferramentas](../tools/overview.md)** da barra superior, agrupado por tarefa e com busca.

Os atalhos de consultas de grounding e de consultas fan-out mostram as buscas que um mecanismo de IA conectado à web executou ao responder um prompt, junto com as fontes citadas. Os dois funcionam fazendo uma chamada gerenciada ao Gemini ou à OpenAI e lendo depois as buscas que aquela chamada realizou, então são uma aproximação próxima do que o AI Mode e o ChatGPT Search fazem, e não um registro desses produtos. Como essa chamada roda na nossa infraestrutura, ambos exigem um **espaço de trabalho gerenciado pago**, e isso vale também nos planos BYOK, já que a etapa de captura usa a infraestrutura gerenciada do Hi, Moose e não a sua chave local.

O atalho de áudio abre a tela [Áudio](../audio/overview.md) no aplicativo para desktop. Antes ele levava ao aplicativo web antigo; não leva mais.
