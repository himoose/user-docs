---
source_hash: 1c85ff53a55d4b6ecb7d8fbdd11b64ab53c6c37bdd4cb12540b5dc7616afc495
---
# Concorrentes e Share of Voice

## Para que serve

Responder à pergunta que seus próprios números não respondem: quando um assistente de IA recomenda algo da sua categoria, com que frequência é você, e quem é escolhido no seu lugar?

Você encontra isso em **Visibilidade → Concorrência**.

## Configurar os concorrentes

Adicione concorrentes em **Visibilidade → Configurações → Monitoramento de concorrentes**. Cada um pede um nome e, opcionalmente, um site.

Essa lista é compartilhada com o seu [Perfil de Verdade da Marca](../getting-started/context/brand-truth-profile.md), então concorrentes adicionados em qualquer um dos dois lugares aparecem em ambos.

Quantos são monitorados nas execuções de visibilidade depende do seu plano: **5 no Preview Mode e no BYOK Free, 15 em todos os planos pagos**. A tela de configurações informa o número e avisa se sua lista for maior, para que você saiba que só os primeiros são monitorados.

De três a cinco concorrentes reais funcionam melhor do que uma lista longa. São as marcas com que você é de fato comparado, não o setor inteiro.

## Share of Voice

O **Share of Voice** é a fatia de atenção que cada marca recebe nas respostas de IA no período, mas nem toda menção vale o mesmo.

Ser citado em primeiro numa resposta vale mais do que ser citado em sexto, porque é esse o nome que o leitor leva embora. Por isso cada menção é ponderada pelo lugar que a marca ocupa na resposta:

| Posição na resposta | Peso |
|---|---|
| 1ª | 1,00 |
| 2ª | 0,70 |
| 3ª | 0,50 |
| 4ª | 0,35 |
| 5ª | 0,25 |
| 6ª ou depois | 0,15 |

Uma menção em que não foi possível ler a posição conta como 0,50. Além disso, uma resposta que **cita o site da própria marca** soma outros 0,50, porque uma citação é um sinal mais forte do que apenas o nome.

A pontuação ponderada de cada marca é então dividida pelo total de todas as marcas monitoradas, o que dá a sua parcela.

A aba Concorrência abre com sua posição, e a lista ordenada abaixo mostra cada marca monitorada com sua parcela. Ao lado ficam a **parcela de menções** e a **parcela de citações**, que são as contagens simples, sem ponderação, para você ver o quadro bruto junto do ponderado.

!!! note "Por que o número ponderado pode discordar da contagem simples"
    Você pode ser mencionado tanto quanto um concorrente e ainda assim ficar atrás dele no Share of Voice, se ele aparece sempre em primeiro e você sempre em quarto. Essa diferença é justamente o ponto da métrica: ela está dizendo que as menções existem, mas a proeminência não, o que é um problema diferente e tem outra solução.

!!! warning "Share of Voice não é taxa de menção"
    São dois números diferentes e eles se movem de forma independente.

    O **Share of Voice** é a sua fatia ponderada da atenção total dada às marcas. Ele é relativo: um concorrente pode derrubá-lo sem que nada mude do seu lado.

    A **taxa de menção** (na aba Visão geral) é a proporção de prompts monitorados em que sua marca foi mencionada. Ela é absoluta, não ponderada, e ignora os concorrentes por completo.

    Sua taxa de menção pode subir enquanto seu Share of Voice cai, se os concorrentes cresceram mais rápido que você. Vale acompanhar os dois, por razões diferentes.

## Tendência do Share of Voice

O gráfico de tendência traça o **Share of Voice** ou a **taxa de menção** ao longo do tempo, para você ver se uma mudança veio do seu avanço, do avanço de um concorrente ou de a categoria inteira ter ficado mais barulhenta.

## Principais citações de concorrentes

Quais páginas dos concorrentes os mecanismos de IA realmente citam como fonte. É o painel mais diretamente acionável da aba: são as URLs específicas que ganham as citações que você quer, e mostram o que os mecanismos de resposta consideram hoje a melhor fonte sobre essas perguntas.

Compare com **Páginas mais citadas** na aba Visão geral, que mostra o mesmo para o seu domínio.

## Lacunas em relação aos concorrentes

Perguntas em que um concorrente apareceu numa resposta de IA e sua marca não.

Cada lacuna mostra quais concorrentes apareceram e em quais mecanismos ela foi observada, com uma etiqueta:

- **Sem visibilidade**: sua marca não aparece para essa pergunta em nenhum mecanismo.
- **Parcial**: sua marca aparece para essa pergunta, só não em todos os mecanismos. A linha informa em quais você aparece.

Linhas parciais muitas vezes não pedem ação nenhuma. Uma pergunta em que você aparece em quatro de cinco mecanismos não é o mesmo problema que uma em que você não aparece em lugar algum, e a etiqueta existe justamente para você distinguir as duas num relance.

Se a lista estiver truncada, estreite o intervalo de datas ou os filtros para ver o resto.

## De onde vêm os dados de concorrentes

As menções e citações de concorrentes são extraídas das mesmas observações das execuções de visibilidade que as suas. Nada extra é executado, e os sites dos concorrentes não são rastreados para esses painéis. Se uma execução falhou ou um modelo estava indisponível, essas observações são excluídas em vez de contadas como ausência.

## No relatório executivo

Share of Voice, principais citações de concorrentes e lacunas estão todos no [relatório executivo](overview.md#exportar) exportado, então o quadro competitivo chega a clientes e gestores sem que você precise reconstruí-lo à mão.
