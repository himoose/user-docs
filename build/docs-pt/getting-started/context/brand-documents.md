---
source_hash: 399cb3ab67be171f7aec402853ccc087cffad8b03562b16db57f4d80c7058766
---
!!! note "Tradução automática"
    Esta página foi traduzida por IA. A versão em inglês é a versão oficial.

    [Ler em inglês](https://himoose.com/docs/getting-started/context/brand-documents/)

# Documentos de marca

## Para que serve

Os Documentos de marca permitem carregar os documentos de marca que a sua equipa já mantém, como um message house, um guia de estilo ou mensagens de posicionamento e de persona. O Hi, Moose lê-os antes de escrever qualquer coisa para o projeto, para que briefings, rascunhos, FAQ e respostas do chat sigam as suas regras e usem as mensagens aprovadas.

Não precisa de colar um message house de 50 páginas em cada pedido. O Hi, Moose divide cada documento em secções, mantém as suas regras de escrita ativas em todos os trabalhos e só vai buscar as outras secções quando um trabalho precisa delas.

Também pode usar os seus documentos para [preencher a Voz da marca e o Perfil de Verdade da Marca](#preencher-os-perfis-a-partir-dos-documentos) de uma só vez.

Os Documentos de marca pertencem ao [projeto](../projects.md) atual. Abra-os a partir do cartão **Documentos de marca** no ecrã [Contexto](overview.md).

## Carregar um documento

1. Abra o **Contexto** e clique em **Carregar um documento de marca** no cartão Documentos de marca (ou em **Gerir documentos de marca** quando já tiver documentos).
2. Clique em **Carregar documento** e escolha um ficheiro.
3. O Hi, Moose lê o ficheiro, divide-o em secções, etiqueta cada secção e indexa-a para pesquisa. O progresso aparece no ecrã.

**Ficheiros suportados:** Markdown, texto simples, Word (`.docx`) e PDF.

Os títulos tornam-se secções, por isso um documento com títulos claros funciona melhor. Um message house com um título para cada pilar, persona e produto divide-se sem problemas. Um PDF que seja um único bloco de texto não.

Documentos grandes podem demorar vários minutos a etiquetar. Pode sair do ecrã enquanto isso acontece. O Hi, Moose continua a trabalhar e avisa quando o documento estiver pronto, com uma notificação se a aplicação estiver em segundo plano.

**Limites:** até 25 documentos por projeto e cerca de 500.000 caracteres por documento.

## Como as secções são organizadas

Cada secção recebe um tipo. O tipo decide quando o Hi, Moose a usa.

| Tipo | O que inclui | Quando é usado |
|---|---|---|
| **Regras** | Como escrever para esta marca: voz, nomes, palavras a usar e a evitar. | Sempre ativo, em todos os trabalhos. |
| **Núcleo da empresa** | Posicionamento e identidade que servem para qualquer peça. | Sempre ativo, em todos os trabalhos. |
| **Provas** | Números, clientes, citações e ligações que o Hi, Moose pode citar. | Chamado quando é relevante. |
| **Textos aprovados** | Texto reutilizável, como propostas de valor e boilerplates. | Chamado quando é relevante. |
| **Playbooks** | Mensagens para um público, produto, solução ou setor. | Chamado quando é relevante. |

As secções também podem ter indicadores:

- **Sempre ativo**: a secção entra em todos os trabalhos.
- **Apenas interno**: o documento marca esta secção como interna. O Hi, Moose usa-a para orientar o posicionamento, mas nunca a cita nem a parafraseia no conteúdo.
- **Rascunho**: a secção está marcada como rascunho no documento de origem.
- **Verificar aprovação**: a origem indica que o conteúdo precisa de aprovação antes de ser usado.
- **Editado aqui**: alterou a secção dentro do Hi, Moose.

Os indicadores ajudam, mas não são uma garantia. Leia cada rascunho antes de o publicar.

### Verificar e editar secções

Clique em **Ver secções** num documento para ver as secções agrupadas por tipo. Clique em **Editar secção** para corrigir o texto de uma secção e depois em **Guardar secção**. As secções editadas ficam marcadas como **Editado aqui**.

Se o ecrã mostrar **Etiquetado apenas pelos títulos**, não havia nenhum modelo disponível quando o documento foi processado, por isso as secções foram etiquetadas só a partir dos títulos. Ligue uma chave OpenRouter, carregue um modelo local ou inicie sessão num plano pago e depois substitua o documento para obter etiquetas mais completas.

## Substituir um documento e histórico de versões

Quando o seu message house mudar, clique em **Substituir** e carregue o novo ficheiro. O Hi, Moose compara-o com a versão anterior e só relê as secções que mudaram. O documento mostra quantas secções foram adicionadas, alteradas e removidas.

As últimas cinco versões de cada documento ficam listadas em **Versões**. Carregar um ficheiro idêntico não altera nada.

Clique em **Remover** para apagar um documento com todas as versões e secções. Os briefings e rascunhos que já escreveu mantêm o conteúdo.

## Ver o que o Moose vai usar

Antes de escrever, pode verificar que secções um trabalho iria buscar. Em **Ver o que o Moose vai usar**, escreva um tema ou o tipo de peça que pretende escrever (por exemplo, «publicação no LinkedIn sobre segurança de código com IA para engenheiros de segurança») e clique em **Mostrar secções**.

O Hi, Moose lista as secções que iria buscar. Clique em **Mostrar o texto exato que o Moose recebe** para ver o texto completo que receberia. Se nada corresponder o suficiente, as regras sempre ativas continuam a aplicar-se.

## Preencher os perfis a partir dos documentos

Se os seus documentos já descrevem a voz, o público, as ofertas e os concorrentes, não precisa de os voltar a escrever na [Voz da marca](brand-voice.md) e no [Perfil de Verdade da Marca](brand-truth-profile.md).

1. No ecrã Documentos de marca, clique em **Preencher perfis a partir dos documentos**.
2. O Hi, Moose lê os seus documentos e sugere valores para os campos da Voz da marca e do Perfil de Verdade da Marca. A caixa de diálogo pergunta «Preencher Brand Voice e Brand Truth a partir destes documentos?».
3. Reveja as sugestões. Cada uma mostra a citação do documento que a sustenta.
4. Escolha os campos que quer e clique em **Aplicar N campos** (o botão mostra quantos campos escolheu).

Nada é guardado até aplicar. Como as sugestões vêm marcadas:

- Os campos **Vazio hoje** vêm marcados por predefinição.
- Os campos **Difere do atual** vêm desmarcados, para que a sua própria redação prevaleça, a menos que escolha o contrário. O valor atual aparece ao lado da sugestão.
- Uma sugestão é descartada se o texto citado não aparecer palavra por palavra no documento. A caixa de diálogo indica quantas foram descartadas.

Campos que o Hi, Moose pode preencher:

- **Voz da marca:** nome da marca, resumo, público, tom, estilo de escrita, valores da marca, termos secundários da marca, terminologia preferida e a evitar, e provas.
- **Perfil de Verdade da Marca:** como a IA deve descrever a empresa, segmentos e notas sobre o cliente ideal, produtos e serviços, capacidades principais, representações erradas comuns, narrativas desatualizadas, vocabulário preferido e a evitar, concorrentes, afirmações sensíveis e os erros mais prejudiciais.

Preencher perfis precisa de um modelo: uma chave OpenRouter, um modelo local ou um plano pago.

## Onde os seus documentos são usados

Quando um projeto tem documentos de marca, o Hi, Moose usa-os em:

- [Briefings de conteúdo](../../features/content-briefs.md), [rascunhos de post](../../features/blog-post-draft.md), [Pontos principais](../../features/key-points.md) e no [Gerador de FAQ](../../features/faq-generator.md). Cada um recebe as regras sempre ativas e as secções que melhor correspondem ao tema.
- [Chat](../../chat/overview.md). As suas regras fazem parte de cada conversa, e o chat pode pesquisar os seus documentos quando uma pergunta precisa de detalhes sobre produto, persona ou provas.
- Na pesquisa do [Send Moose](../../send-moose/overview.md) e na revisão final do conteúdo gerado, que recebem ambas as suas regras.

Os Documentos de marca funcionam em conjunto com a Voz da marca e o Perfil de Verdade da Marca. Esses perfis continuam a ser o resumo curto de quem é a sua marca. Os documentos acrescentam o detalhe completo por trás dele.

## Armazenamento e sincronização

Os documentos de marca ficam guardados localmente para o projeto atual. Num plano pago, sincronizam com o resto do projeto, para que toda a equipa tenha os mesmos documentos e fiquem com cópia de segurança. Enquanto chegam alterações de um colega, o ecrã mostra **A sincronizar a partir da sua equipa...**.

Remover um projeto remove também os respetivos documentos de marca.
