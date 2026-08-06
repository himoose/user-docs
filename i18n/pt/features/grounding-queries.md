---
source_hash: 3856622231055de776fe82082345666ad4d8429b9d735111e9d399831a122f47
---
# Consultas de grounding do AI Mode

## Para que serve

Este recurso mostra as buscas no Google que o Gemini executou ao fundamentar sua resposta a um prompt, junto com as fontes que ele citou e a resposta fundamentada que produziu.

!!! info "O que isso é, exatamente"
    O Hi, Moose pede à API do Gemini que responda ao seu prompt com a fundamentação por busca do Google ligada, e depois lê a lista de buscas que aquele modelo disparou. Não é uma gravação do AI Mode de consumo do Google. O AI Mode é uma superfície separada e não expõe suas consultas internas a ninguém. O que você recebe é a aproximação mais próxima disponível: o mesmo índice de busca, a mesma família de modelos e formulações de consulta bem parecidas com as que o AI Mode produz. Trate como um sinal forte, não como uma transcrição, e conte com alguma variação entre execuções do mesmo prompt.

!!! note "Disponibilidade"
    Este recurso faz nos bastidores uma chamada gerenciada de fundamentação ao Gemini, então exige um espaço de trabalho **gerenciado pago**. Isso vale também nos planos BYOK: o BYOK mantém local a geração principal do chat, mas a captura das consultas de grounding usa a infraestrutura gerenciada do Hi, Moose, que custa dinheiro para operar. Por isso não está incluída no BYOK Free nem no BYOK Premium. O Preview Mode também não inclui.

## Como rodar

1. No [Chat](../chat/overview.md), escolha o atalho **Capturar consultas de fundamentação do AI Mode** (ou peça direto).
2. Informe o prompt que quer examinar.
3. O Hi, Moose consulta as consultas de grounding do Gemini para aquele prompt e devolve:
    - As consultas de grounding que o Gemini realmente usou.
    - As fontes citadas.
    - A própria resposta fundamentada.

## Por que isso importa

As consultas de grounding mostram como um mecanismo de resposta transforma um único prompt num leque de buscas reais. Isso ajuda a entender por que sua página está ou não sendo captada, e a identificar variações de consulta que você não monitora hoje em [Visibilidade](../visibility/overview.md) nem no [Gerenciador de Prompts](../visibility/prompt-manager.md).

## Se uma execução falhar

Se o Hi, Moose não conseguir coletar consultas de grounding reais para um prompt, ele diz isso em vez de apresentar um palpite. Tente de novo em instantes, ou confira se o espaço de trabalho tem uma assinatura gerenciada ativa.
