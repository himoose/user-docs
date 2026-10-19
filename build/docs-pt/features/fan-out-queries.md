---
source_hash: 3b2a6720bd62d36c159ec05f39cfb8f6e59efa7a27d7e6054053a2fcb1d2c950
---
!!! note "Tradução automática"
    Esta página foi traduzida por IA. A versão em inglês é a versão oficial.

    [Ler em inglês](https://himoose.com/docs/features/fan-out-queries/)

# Consultas fan-out do ChatGPT

## Para que serve

Este recurso captura as buscas «fan-out» individuais que a etapa de busca web da OpenAI executou ao responder ao seu prompt, junto com as fontes citadas e uma prévia da resposta.

!!! info "O que isso é, exatamente"
    O Hi, Moose chama a API Responses da OpenAI com a ferramenta de busca web ligada e depois lê as buscas que aquela execução realizou. Não é uma captura do fan-out do produto de consumo ChatGPT, que a OpenAI não expõe. O que você recebe é a aproximação mais próxima disponível: a mesma camada de busca web, movida pela mesma família de modelos, então a expansão de consultas acompanha de perto o que o ChatGPT Search faz. Trate como um sinal forte, não como uma transcrição, e conte com alguma variação entre execuções do mesmo prompt.

!!! note "Disponibilidade"
    Este recurso faz nos bastidores uma captura gerenciada do rastro de busca web da OpenAI, então exige um espaço de trabalho **gerenciado pago**. Isso vale também nos planos BYOK: o BYOK mantém local a execução principal dos modelos, mas a captura do fan-out usa a infraestrutura gerenciada do Hi, Moose, que custa dinheiro para operar. Por isso não está incluída no BYOK Free nem no BYOK Premium. O Preview Mode também não inclui.

## Como rodar

1. No [Chat](../chat/overview.md), escolha o atalho **Capturar consultas fan-out do ChatGPT** (ou peça direto).
2. Informe o prompt que quer examinar.
3. O Hi, Moose captura a resposta do ChatGPT e devolve:
    - As consultas fan-out distintas que o ChatGPT executou.
    - As fontes citadas.
    - Uma prévia da resposta.

Se a OpenAI não expôs nenhuma consulta fan-out distinta numa execução específica, o Hi, Moose mostra assim mesmo o rastro de busca gerenciado e as fontes citadas que conseguiu capturar, em vez de apresentar um resultado vazio ou inventado.

## Por que isso importa

As consultas fan-out revelam a expansão de consultas por trás de uma resposta fundamentada na web, o que ajuda a entender quais formulações específicas estão gerando (ou deixando de gerar) citações ao seu conteúdo. Isso alimenta diretamente o que você monitora em [Visibilidade](../visibility/overview.md) e o que planeja nos [Briefings de conteúdo](content-briefs.md).
