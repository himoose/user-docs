---
source_hash: b5d0a07f31228ccaaa2c18a76dddb8de404f3871f7b879591e111c89bae3e9c5
---
# Player e incorporação

## Para que serve

Ajustar o visual do player de áudio incorporado à página que vai recebê-lo e depois copiar o código de incorporação. Abra a partir de um episódio pronto com **Personalizar player**, ou pela ação de incorporação na aba **Histórico**.

## Opções do player

- **Tema**: Escuro, Claro ou Automático. O automático segue a configuração do dispositivo de cada visitante.
- **Layout**: Completo ou Compacto.
- **Cor de destaque**: qualquer valor hexadecimal de 6 dígitos, por exemplo `#5688b0`.
- **Mostrar o título**: desligue quando a incorporação ficar abaixo de um título seu.
- **Título personalizado**: deixe em branco para usar o título do episódio.
- **Botão de transcrição**: mostre ou oculte o controle de transcrição no player.

Uma prévia ao vivo se atualiza conforme você altera as configurações. Se o script do player estiver inacessível durante a prévia, ela cai para uma marcação simples; o código de incorporação copiado continua correto.

## Copiar o código de incorporação

Clique em **Copiar código de incorporação** e cole na sua página.

- **WordPress**: cole no bloco HTML ou de código do post, ou use o [plugin Listen to This Article](https://wordpress.org/plugins/listen-to-this-article/).
- **Webflow**: cole num elemento Embed.
- **Grav**: cole no conteúdo da página, onde HTML bruto é permitido.

## A reprodução é restrita por domínio

O áudio gerado só toca no domínio do site do seu projeto e em `himoose.com`. Isso vem do campo de site do projeto, e é por isso que ele precisa estar preenchido antes de você gerar. Se incorporar o player num domínio não autorizado, a reprodução será recusada.

## Atribuição da agência

Nos planos com [marca white label](../agency/white-label.md), o player incorporado pode levar a atribuição da sua agência em vez da do Hi, Moose. Configure em **Configurações → Marca**:

- **Atribuição na incorporação de áudio**: o texto exibido no player. Deixe vazio para usar «Audio by» seguido do nome da sua agência.
- **Link de atribuição**: um endereço `https://` completo. Deixe vazio para reaproveitar seu link principal de marca.

A atribuição é um link real de volta para o seu site em cada página de cliente que leva o player, e é justamente aí que está o valor para agências.

!!! warning "A atribuição vale para o código copiado depois de salvar"
    Alterar a marca não reescreve as incorporações já colocadas. Copie o código de incorporação de novo depois de salvar para pegar a nova atribuição.

## Por que isso ajuda o AEO

A transcrição acrescenta à página texto estruturado, próprio e rastreável. É conteúdo real a mais que um mecanismo de resposta pode recuperar e citar, e pode reforçar os sinais de extraibilidade e abrangência numa [auditoria de AEO](../features/aeo-audits.md). Não é por si só um fator pontuado do tipo «tem mídia»: o valor está no texto que o player traz consigo.
