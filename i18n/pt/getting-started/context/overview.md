---
source_hash: 25544d4dba4331f336f53923c9a635bc4442b022e472aec88392d921d34dfefb
---
# Contexto

## Para que serve

O **Contexto** é a camada de fundamentação na navegação à esquerda da aplicação de desktop. É o contexto operacional partilhado do seu projeto atual: a informação que o operador, o chat e todas as capacidades de geração reutilizam, em vez de começarem do zero a cada pedido.

O Contexto tem quatro partes:

| | Âmbito | Para que serve |
|---|---|---|
| **[Voz da marca](brand-voice.md)** | Por projeto | Como a sua marca deve soar: tom, público, valores, terminologia. Define o estilo de escrita de tudo o que o Hi, Moose gera. |
| **[Perfil de Verdade da Marca](brand-truth-profile.md)** | Por projeto | Uma fonte de verdade legível por máquina sobre o que a sua empresa é, vende e serve. Serve para detetar quando as respostas da IA distorcem essa verdade ou se afastam dela. |
| **[Documentos de marca](brand-documents.md)** | Por projeto | O seu message house, guia de estilo e documentos de posicionamento. O Hi, Moose divide-os em secções, aplica as suas regras de escrita a tudo e vai buscar o resto quando um trabalho precisa. |
| **[Sobre você](about-you.md)** | Por dispositivo, não por projeto | Notas sobre si enquanto pessoa: a sua função, os seus objetivos e a forma como gosta de trabalhar, para que o chat conheça a pessoa e não só a marca. |

## Porque são artefactos separados

A Voz da marca e o Perfil de Verdade da Marca respondem a perguntas diferentes, embora ambos descrevam a sua marca:

- A **Voz da marca** responde a «como deve isto soar?»: tom, estilo, preferências de vocabulário. É uma orientação criativa e estilística para o conteúdo gerado.
- O **Perfil de Verdade da Marca** responde a «o que é verdade sobre nós?»: descrição canónica, cliente ideal, ofertas, concorrentes e os pontos específicos em que a IA costuma errar. É uma referência factual para detetar distorções, não um guia de estilo.

Os **Documentos de marca** guardam o material de origem completo por trás dos dois. A Voz da marca e o Perfil de Verdade da Marca continuam a ser resumos curtos. Os documentos guardam o detalhe, e o Hi, Moose pesquisa neles as secções que se adequam a cada trabalho. Também os pode usar para preencher os dois perfis.

**Sobre você** é diferente de todos estes: não trata da marca. É contexto pessoal sobre **si**, a pessoa que usa a aplicação, guardado localmente no seu dispositivo em vez de associado a um projeto. Por isso acompanha-o de projeto para projeto, em vez de ser reposto sempre que muda de espaço de trabalho.

## Onde o Contexto é usado

- A **Voz da marca** é reutilizada nos [Briefings de conteúdo](../../features/content-briefs.md), no [Gerador de FAQ](../../features/faq-generator.md), no [Extrator de Pontos principais](../../features/key-points.md), em [rascunhos, pré-visualização e publicação](../../features/drafts-and-publishing.md) e nas recomendações das [auditorias de AEO](../../features/aeo-audits.md).
- O **Perfil de Verdade da Marca** é reutilizado durante as execuções de [Visibilidade](../../visibility/overview.md), em que o Hi, Moose verifica se a resposta de um motor de IA sobre a sua marca corresponde à sua descrição canónica, às suas ofertas, aos seus concorrentes e aos padrões conhecidos de distorção.
- Os **Documentos de marca** são reutilizados nos Briefings de conteúdo, nos rascunhos de post, nos Pontos principais, no Gerador de FAQ, na pesquisa do [Send Moose](../../send-moose/overview.md) e no [Chat](../../chat/overview.md), onde o chat também os pode pesquisar. Veja [Onde os seus documentos são usados](brand-documents.md#onde-os-seus-documentos-sao-usados).
- **Sobre você** é reutilizado no [Chat](../../chat/overview.md), para que as respostas tenham em conta a sua função, os seus objetivos e o seu estilo de comunicação preferido.

## Como preencher

Cada artefacto indica quantos campos preencheu e mostra uma pré-visualização curta assim que adiciona alguma coisa. Todos os campos são opcionais: o Hi, Moose funciona com contexto parcial e fica mais preciso à medida que acrescenta mais.

No caso da Voz da marca, não precisa de preencher cada campo à mão: uma ação de **preenchimento automático** pode rastrear o site do seu projeto localmente e sugerir valores para os campos vazios.

Se já tem um message house ou um guia de estilo, carregue-o em [Documentos de marca](brand-documents.md) e clique em **Preencher perfis a partir dos documentos**. O Hi, Moose sugere valores para a Voz da marca e para o Perfil de Verdade da Marca, cada um sustentado por uma citação do documento, e escolhe quais aplicar.

## Armazenamento local e sincronização na nuvem

Por predefinição, a Voz da marca, o Perfil de Verdade da Marca e os Documentos de marca ficam guardados **localmente para o projeto atual**, e Sobre você fica guardado **localmente no seu dispositivo**. A sincronização na nuvem, que cria uma cópia de segurança da Voz da marca, do Perfil de Verdade da Marca e dos Documentos de marca e os partilha com a equipa, está disponível em **todos os planos pagos**, incluindo os planos BYOK pagos. O Preview Mode e o BYOK Free ficam apenas locais. Ao mudar para um plano pago, a sincronização é ativada, para que a sua equipa partilhe a mesma base e esta fique protegida se acontecer alguma coisa ao seu computador.

!!! note "Nos planos BYOK"
    O rastreamento do contexto da marca (o passo de preenchimento automático) e a análise do Perfil de Verdade da Marca são executados localmente na aplicação de desktop. O Hi, Moose não precisa de ver o conteúdo do seu site nos próprios servidores para criar ou usar este contexto.
