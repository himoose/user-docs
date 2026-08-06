---
source_hash: 185a9611ccdaef3c98b73cc4349bc1d586a1fa03b38212ecab7ffca94af54a21
---
# Configurações de Visibilidade

## Para que serve

As configurações de Visibilidade controlam com que frequência o Hi, Moose verifica a visibilidade, qual modelo avalia os resultados e quais termos de marca e domínios contam nas suas métricas. Os prompts e os temas ficam no [Gerenciador de Prompts](prompt-manager.md); esta tela trata da mecânica das execuções.

## Agendamento das execuções

- **Frequência**: diária, dias úteis, semanal ou somente manual.
- **Horário preferido de execução** e, na frequência semanal, um **dia da semana**. As execuções acontecem no seu fuso horário local.
- **Amostras por prompt**: as execuções agendadas podem repetir cada prompt várias vezes e tirar a média dos resultados para uma taxa de visibilidade mais estável. O botão manual **Executar agora** usa sempre uma única amostra. Aumentar esse valor multiplica o consumo de tokens na mesma proporção, e o Hi, Moose avisa antes de você salvar um valor mais alto.

!!! note "Execuções agendadas exigem este dispositivo ligado"
    No **Preview Mode** e nos planos **BYOK**, o agendamento roda localmente na sua máquina: uma execução agendada não começa com o computador desligado, em suspensão ou com o Hi, Moose totalmente fechado. Mantenha o aplicativo aberto (ou minimizado na bandeja do sistema) para que as execuções agendadas aconteçam. Os **planos gerenciados** liberam um agendador na nuvem sempre ativo, que não depende do seu dispositivo estar ligado. Os mecanismos de consulta local continuam exigindo o aplicativo aberto em qualquer plano, porque essas verificações partem da sua máquina.

## Notificações por e-mail

Ative **Relatórios por e-mail das execuções de visibilidade agendadas** para receber o relatório de visibilidade por e-mail quando as execuções agendadas terminarem. É uma preferência pessoal de notificação, separada das [configurações de notificação da Caixa de entrada](../inbox/notifications.md).

## Termos e domínios secundários da marca

- **Termos secundários da marca**: formulações alternativas ou variações de grafia da sua marca que também devem contar como menção.
- **Domínios secundários**: outros domínios que devem contar como citações válidas da marca neste projeto, além do domínio principal.

## Monitoramento de concorrentes

Adicione as marcas com que este projeto é comparado. Cada concorrente pede um nome e, opcionalmente, um site.

Quando uma resposta de IA menciona ou cita um deles, o dado alimenta o [Share of Voice, as citações de concorrentes e as lacunas](competitors.md).

Essa lista é compartilhada com o seu [Perfil de Verdade da Marca](../getting-started/context/brand-truth-profile.md), então concorrentes adicionados em qualquer um dos dois lugares aparecem em ambos. Há um limite de quantos são monitorados nas execuções de visibilidade: a tela informa o número e avisa se sua lista o ultrapassa, para você saber que só os primeiros estão sendo monitorados.

## Modelo de avaliação

Escolha o modelo que o Hi, Moose usa para avaliar sentimento, desvio narrativo e paridade de recursos depois que uma resposta é capturada:

- O **padrão automático** se adapta ao seu plano:
    - O **Preview Mode** usa um modelo local Gemma 4 ativo. A avaliação é pulada enquanto não houver um instalado e ativo (Configurações → Local Model).
    - Os **planos BYOK** avaliam com a sua chave do OpenRouter.
    - Os **planos gerenciados** avaliam pelo roteamento de modelos gerenciados do Hi, Moose (a avaliação por modelo local continua valendo onde há suporte).
- Você também pode selecionar um modelo específico em vez do automático.

Os modelos gratuitos do OpenRouter não são mais oferecidos como opção de avaliação. Eles se mostraram pouco confiáveis na avaliação estruturada, a ponto de os resultados não valerem o relato.

## Modelos padrão para novos prompts

Escolha quais mecanismos ficam pré-selecionados sempre que você adiciona um prompt no [Gerenciador de Prompts](prompt-manager.md); depois você pode alterar a seleção prompt a prompt. Os modelos marcados como **Pago** exigem um plano pago ou BYOK; o Preview Mode fica limitado aos modelos de consulta local. Cada modelo marcado aqui entra no consumo de tokens quando as verificações de visibilidade rodam.

## Refazer a configuração inicial

Rode de novo o assistente de configuração de visibilidade a qualquer momento para atualizar do zero seu domínio monitorado, seus prompts e suas preferências de monitoramento.
