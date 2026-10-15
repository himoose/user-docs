---
source_hash: 57477f3edd7e63b53a23c12a7676c0c723e2f37903e1f4aa75a613f296e8277b
---
!!! note "Tradução automática"
    Esta página foi traduzida por IA. A versão em inglês é a versão oficial.

    [Ler em inglês](https://himoose.com/docs/integrations/wordpress/)

# WordPress

## Para que serve

Conectar um site WordPress ao Hi, Moose para que o aplicativo para desktop possa preparar e aplicar alterações de conteúdo diretamente (FAQ, pontos principais, rascunhos baseados em briefing e recomendações de auditorias de AEO), com uma etapa de prévia e uma de aprovação antes de qualquer coisa ir ao ar.

## Como a conexão funciona

O aplicativo para desktop é o lado ativo dessa conexão: ele localiza o post de destino, busca o conteúdo atual, monta a alteração proposta localmente e chama direto por HTTPS os endpoints REST do seu site WordPress para preparar a alteração. Seu site WordPress fica passivo: expõe um endpoint que espera ser chamado e nunca precisa procurar o Hi, Moose por conta própria.

Isso significa que:

- O token do seu site e as credenciais de conexão nunca ficam com a interface, só com o processo em segundo plano do aplicativo para desktop.
- Nos planos BYOK, as etapas de modelo local envolvidas em preparar uma alteração (como achar o trecho exato de conteúdo a substituir) rodam com a sua chave do OpenRouter, e não por uma chamada hospedada pelo Hi, Moose.

## Configurar uma conexão

1. Abra **Conexões** no aplicativo para desktop e escolha WordPress.
2. Baixe o plugin conector, instale no painel do WordPress e cole ali a URL do seu site e a chave de API deste projeto nas configurações do plugin.
3. De volta ao Hi, Moose, salve a conexão e confirme que o conector reporta um ping bem-sucedido do seu site.

## Ambientes

Cada instalação do WordPress que você conecta (produção, homologação ou ambas) é um **ambiente** próprio, com token de site e segredo HMAC próprios, totalmente isolados entre si. Escolha qual ambiente é o destino padrão de novas alterações e alterne entre eles quando quiser. Se um site de homologação estiver atrás de autenticação HTTP Basic, você pode salvar essas credenciais especificamente para aquele ambiente, para que o Hi, Moose consiga alcançá-lo.

## Patches

Cada alteração no WordPress, venha ela das [FAQ](../features/faq-generator.md), dos [pontos principais](../features/key-points.md), de um [rascunho](../features/drafts-and-publishing.md) ou de uma substituição manual de texto criada por você, é registrada como um **patch**: uma entrada local de registro por ambiente, com status próprio.

Um patch passa por estados explícitos: **Rascunho**, **Preparada**, **Aplicado**, **Descartado**, **Revertido** ou **Falhou**. Na lista de patches você pode:

- **Preparar** um patch no seu site WordPress para prévia.
- **Aplicar** um patch preparado para colocá-lo no ar.
- **Descartar** um patch que não pretende usar.
- **Reverter** um patch aplicado.
- **Promover** um patch para outro ambiente (de homologação para produção, por exemplo) e prepará-lo lá para revisão.

Depois que você envia um rascunho, o Hi, Moose lembra, então você não consegue enviar o mesmo várias vezes sem querer.

## Plugin Listen to this Article

O plugin do WordPress **Listen to This Article**, que é separado, incorpora o player de áudio e a transcrição gerados pelo [Áudio](../audio/overview.md) no aplicativo para desktop. Instale por [wordpress.org/plugins/listen-to-this-article](https://wordpress.org/plugins/listen-to-this-article/), ou cole o código de incorporação direto no seu post. Veja [Player e incorporação](../audio/player-and-embed.md).

## Requisitos

- WordPress 6.0 ou superior, com acesso de administrador para instalar a conexão no seu site.
- Um projeto configurado no aplicativo para desktop.
