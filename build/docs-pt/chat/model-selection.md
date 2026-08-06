---
source_hash: 90bb543cefb714f7fdb6facb1f7799b751aff22949ece082264e7713b4992995
---
!!! note "Tradução automática"
    Esta página foi traduzida por IA. A versão em inglês é a versão oficial.

    [Ler em inglês](https://himoose.com/docs/chat/model-selection/)

# Seleção de modelo

## Para que serve

Todo chat é movido por um modelo de IA específico, e o seletor de modelo permite ver e trocar qual você está usando, incluindo modelos locais no dispositivo.

## Escolher um modelo

Abra o seletor de modelo para ver os modelos disponíveis no seu [plano](../getting-started/account-modes.md). Cada opção traz etiquetas, para você saber o que está levando antes de trocar:

- **Grátis** / **HiMoose Cloud** / **Pago ou BYOK**: quais planos podem usar aquele modelo.
- **Speed: Slow / Average / Very Fast**: uma noção aproximada do tempo de resposta.
- **Local**: roda inteiramente no seu dispositivo (veja abaixo).
- Uma **etiqueta de multiplicador** nos modelos mais caros, mostrando quanto a mais do seu saldo eles consomem em relação à opção padrão.

A oferta acompanha o que os fornecedores de modelos lançam e hoje inclui as famílias Claude, GPT, Gemini e Gemma. Se um modelo não estiver disponível no seu plano, o Hi, Moose diz isso diretamente em vez de trocar em silêncio por outro.

## Modelos locais

Os modelos locais aprovados, como o Gemma 4 do Google, rodam **inteiramente no seu computador**. Nenhum token consumido, nenhuma ida à nuvem e nenhum dado sai do seu dispositivo. Na primeira vez que você seleciona um modelo local, o Hi, Moose orienta a instalação.

Depois de baixadas e ativadas, as respostas locais são rápidas em Apple Silicon. Em Macs com processador Intel o modelo roda na CPU e fica bem mais lento que os modelos na nuvem; o Hi, Moose avisa isso antes de você iniciar o download.

Modelos locais não são uma versão reduzida. O Gemma 4 tem suporte a chamada de ferramentas, então as [ferramentas do chat](tools-and-specialists.md) funcionam num modelo local como funcionam num modelo na nuvem.

!!! note "O Preview Mode depende de um modelo local"
    No plano gratuito, as [auditorias de AEO](../features/aeo-audits.md) e a avaliação de visibilidade só rodam com um modelo local ativo. É o principal motivo para configurar um logo no começo.

## Modelos mais caros

Alguns modelos consomem bem mais do seu saldo que a opção padrão. Se você escolher um, o Hi, Moose confirma antes e mostra aproximadamente quantas vezes mais tokens ele usa, para você não esgotar o saldo sem querer.

Os modelos mais caros são limitados por plano. Se o seu não os inclui, eles aparecem como indisponíveis em vez de ficarem ocultos.

## Fundamentação por busca web

O chat pode fundamentar as respostas em resultados de busca em tempo real para a conversa atual. Está disponível no BYOK Premium, no BYOK Agency e em todos os planos gerenciados. Não está incluído no BYOK Free nem no Preview Mode.

## Idioma

O chat segue uma preferência de idioma, então você pode trabalhar num idioma diferente do que a interface do aplicativo usa.

## Quando um modelo não pode ser usado

Pode aparecer uma mensagem no lugar da resposta se:

- o modelo selecionado estiver temporariamente indisponível (tente outro),
- o modelo não for permitido no seu plano (escolha um que esteja incluído), ou
- uma imagem tiver sido anexada a um modelo que não aceita entrada de imagem. O Hi, Moose indica um modelo que aceita e oferece a troca.

## Como isso se encaixa com o BYOK

Nos planos BYOK, a seleção de modelo determina qual modelo a sua chave do OpenRouter chama. A inferência continua rodando localmente no aplicativo para desktop. Veja [Tipos de conta e planos](../getting-started/account-modes.md) para entender como o acesso a modelos muda entre os planos.

Sua chave do OpenRouter é salva por conta, e não por dispositivo. Se você ainda não tiver salvo nenhuma, o Hi, Moose pede na primeira vez que um recurso precisar dela, em vez de falhar em silêncio.
