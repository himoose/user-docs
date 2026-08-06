---
source_hash: 05fae21b2ec70be5a8bae1ca0e58f085c9da2140a80bae1dc2e083051aeffb43
---
# Contexto

## Para que serve

O **Contexto** é a camada de fundamentação na navegação esquerda do aplicativo para desktop. É o contexto operacional compartilhado do seu projeto atual: as informações que o operador, o chat e todos os recursos de geração reaproveitam em vez de começar do zero a cada pedido.

O Contexto tem três partes distintas:

| | Alcance | Para que serve |
|---|---|---|
| **[Voz da marca](brand-voice.md)** | Por projeto | Como sua marca deve soar: tom, público, valores, terminologia. Define o estilo de escrita de tudo o que o Hi, Moose gera. |
| **[Perfil de Verdade da Marca](brand-truth-profile.md)** | Por projeto | Uma fonte de verdade legível por máquina sobre o que sua empresa é, vende e atende de fato. Serve para detectar quando as respostas da IA distorcem isso ou se afastam. |
| **[Sobre você](about-you.md)** | Por dispositivo, não por projeto | Anotações sobre você como pessoa: sua função, seus objetivos e seu jeito de trabalhar, para que o chat conheça a pessoa e não só a marca. |

## Por que são três artefatos separados

A Voz da marca e o Perfil de Verdade da Marca respondem a perguntas diferentes, mesmo descrevendo os dois a sua marca:

- A **Voz da marca** responde a «como isso deve soar?»: tom, estilo, preferências de vocabulário. É uma orientação criativa e estilística para o conteúdo gerado.
- O **Perfil de Verdade da Marca** responde a «o que é verdade sobre nós?»: descrição canônica, cliente ideal, ofertas, concorrentes e os pontos específicos em que a IA costuma errar. É uma referência factual para flagrar distorções, não um guia de estilo.

**Sobre você** difere dos dois: não trata da marca de forma alguma. É contexto pessoal sobre **você**, a pessoa que usa o aplicativo, salvo localmente no seu dispositivo em vez de vinculado a um projeto. Por isso acompanha você entre projetos, em vez de zerar a cada troca de espaço de trabalho.

## Onde o Contexto é usado

- A **Voz da marca** é reaproveitada nos [Briefings de conteúdo](../../features/content-briefs.md), no [Gerador de FAQ](../../features/faq-generator.md), no [Extrator de Pontos principais](../../features/key-points.md), em [rascunhos, prévia e publicação](../../features/drafts-and-publishing.md) e nas recomendações das [auditorias de AEO](../../features/aeo-audits.md).
- O **Perfil de Verdade da Marca** é reaproveitado durante as execuções de [Visibilidade](../../visibility/overview.md), em que o Hi, Moose verifica se a resposta de um mecanismo de IA sobre sua marca bate com sua descrição canônica, suas ofertas, seus concorrentes e os padrões conhecidos de distorção.
- **Sobre você** é reaproveitado no [Chat](../../chat/overview.md), para que as respostas considerem sua função, seus objetivos e seu estilo de comunicação preferido.

## Como preencher

Cada artefato indica quantos campos você preencheu e mostra uma prévia curta assim que você adiciona algo. Todos os campos dos três artefatos são opcionais: o Hi, Moose funciona com contexto parcial e fica mais preciso conforme você acrescenta mais.

No caso específico da Voz da marca, você não precisa preencher cada campo à mão: uma ação de **preenchimento automático** pode rastrear o site do seu projeto localmente e sugerir valores para os campos vazios.

## Armazenamento local e sincronização na nuvem

Por padrão, a Voz da marca e o Perfil de Verdade da Marca ficam salvos **localmente para o projeto atual**, e Sobre você fica salvo **localmente no seu dispositivo**. A sincronização na nuvem, que faz backup da Voz da marca e do Perfil de Verdade da Marca e os compartilha com a equipe, está disponível em **todos os planos pagos**, incluindo os planos BYOK pagos. O Preview Mode e o BYOK Free permanecem apenas locais; ao mudar para um plano superior, a sincronização é ativada, de modo que sua equipe compartilhe a mesma base e ela fique protegida se algo acontecer com a sua máquina.

!!! note "Nos planos BYOK"
    O rastreamento do contexto da marca (a etapa de preenchimento automático) e a análise do Perfil de Verdade da Marca rodam localmente no aplicativo para desktop. O Hi, Moose não precisa ver o conteúdo do seu site nos próprios servidores para montar ou usar esse contexto.
