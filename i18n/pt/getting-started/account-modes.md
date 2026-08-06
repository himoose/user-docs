---
source_hash: 807f4fd0f8157bf27491590b13dd7b2b18f5cb12dd648c025f2c46cabf3ea0ed
---
# Tipos de conta e planos

O Hi, Moose executa o trabalho de IA de duas formas: com a sua chave do OpenRouter (BYOK) ou com os modelos gerenciados do Hi, Moose. É essa escolha, e não o preço, a verdadeira bifurcação. Todo o resto é quantidade de projetos, assentos e créditos mensais.

Os planos ficam agrupados em duas abas na tela **Fazer upgrade**: **Inicial** e **Empresas e agências**.

## As duas formas de executar a IA

### BYOK: traga sua própria chave

Você fornece uma chave de API do [OpenRouter](https://openrouter.ai) e as chamadas aos modelos são executadas **pelo aplicativo para desktop, na sua máquina**, com essa chave. O Hi, Moose nunca encaminha a inferência BYOK pelos próprios servidores, então sua chave e seus prompts ficam locais.

Pagar por um plano BYOK não muda isso. Você paga por mais capacidade de trabalho (projetos, assentos, memória, fluxos de trabalho, Search Console), não para que o Hi, Moose execute suas chamadas aos modelos. O custo dos modelos vai direto para o OpenRouter e não há nenhum medidor de tokens do Hi, Moose para acompanhar.

### Gerenciado: quem executa os modelos é o Hi, Moose

Sem chave de API. Os modelos gerenciados do Hi, Moose fazem o trabalho e você consome um saldo mensal de **créditos**. Um medidor só, e não vários. O suporte a modelos locais continua disponível como opção no dispositivo em todos os planos gerenciados.

## Planos Startup

### Preview Mode (gratuito)

O Preview Mode é a forma gratuita de experimentar o Hi, Moose. Ele é realmente local: 1 projeto, 1 assento, armazenamento local e execuções de visibilidade que consultam as superfícies públicas de busca com IA direto do seu dispositivo.

- 1 projeto, 1 assento de usuário
- Somente LLMs gratuitos e locais
- Execuções de visibilidade locais
- Armazenamento e recuperação de contexto, Voz da marca e guia de estilo
- Conexões: WordPress, Webflow, Grav
- Dados limitados de busca em tempo real e de concorrentes, qualidade de IA limitada, opções de exportação limitadas

!!! warning "O Preview Mode precisa de um modelo local para pontuação e auditorias"
    O Preview Mode não inclui nenhuma cota de IA na nuvem. As [auditorias de AEO](../features/aeo-audits.md) e a avaliação de sentimento, narrativa e paridade de recursos nas [execuções de visibilidade](../visibility/overview.md) só funcionam depois que você ativa um modelo local Gemma 4 em **Configurações → Local Model**. Enquanto não houver um ativo, essas verificações são puladas em vez de rodarem na nuvem.

### BYOK Free

A forma gratuita de trabalhar com a sua chave. Mesmo formato de 1 projeto e 1 assento do Preview Mode, mas com acesso a todos os modelos que o OpenRouter oferece, e não só aos gratuitos.

- 1 projeto, 1 assento de usuário
- Sua própria chave do OpenRouter, tokens ilimitados
- Todos os LLMs, incluindo os modelos locais
- Execuções de visibilidade somente locais
- Conexões: WordPress, Webflow, Grav
- Armazenamento e recuperação de contexto limitados, [Biblioteca de artefatos](../library/overview.md) limitada
- Sem busca web no chat, sem fluxos de trabalho, sem Google Search Console

### BYOK Premium: 39 USD por mês ou 390 USD por ano

O plano local completo, e o ponto em que os assentos de equipe e o agendamento são liberados.

- 3 projetos, mais projetos adicionais por 10 USD ao mês cada
- Até 10 assentos de equipe
- Execuções de visibilidade completas com agendamento personalizado
- Busca web a partir do chat
- Armazenamento e recuperação de contexto completos, [Biblioteca de artefatos](../library/overview.md) completa
- [Fluxos de trabalho](../workflows/overview.md)
- Voz da marca, guia de estilo e [Perfil de Verdade da Marca](context/brand-truth-profile.md)
- Conexões: WordPress, Webflow, Grav, [Google Search Console](../integrations/google-search-console.md)
- 15 [gerações de áudio](../audio/overview.md) por mês

### Planos gerenciados

Os três funcionam com os modelos do Hi, Moose e incluem assentos de equipe ilimitados, gerações de áudio ilimitadas, logs administrativos com exportação e armazenamento local e na nuvem.

| Plano | Preço | Projetos | Créditos mensais | Modelos |
|---|---|---|---|---|
| Standard | 79 USD/mês ou 849 USD/ano | 3 | 1.700.000 | Modelos padrão, mais os locais |
| Professional | 129 USD/mês ou 1.389 USD/ano | 5 | 3.000.000 | Todos os modelos, mais os locais |
| Premium | 249 USD/mês ou 2.689 USD/ano | 10 | 6.000.000 | Todos os modelos, mais os locais |

## Planos Enterprise e para agências

### BYOK Agency: 149 USD por mês ou 1.490 USD por ano

O BYOK Premium na escala de uma agência. O mesmo funcionamento local e o mesmo conjunto de recursos, dimensionados para atender muitos clientes.

- 25 projetos, mais projetos adicionais por 10 USD ao mês cada
- Até 25 assentos de equipe
- 15 gerações de áudio por mês
- [Marca white label](../agency/white-label.md) em relatórios e incorporações de áudio, como em todos os planos pagos

### Planos gerenciados para agências

| Plano | Preço | Projetos | Créditos mensais | Armazenamento |
|---|---|---|---|---|
| Agent Core | 449 USD/mês ou 4.849 USD/ano | 25 | 15.000.000 | Nuvem da equipe |
| Agent Studio | 999 USD/mês ou 10.789 USD/ano | 75 | 40.000.000 | Nuvem da equipe |
| Agent Scale | 1.999 USD/mês ou 21.589 USD/ano | Ilimitados | 120.000.000 | Nuvem da equipe |

## Comparativo rápido

| | Preview Mode | BYOK Free | BYOK Premium | BYOK Agency | Planos gerenciados |
|---|---|---|---|---|---|
| Precisa de chave de API própria | Não | Sim | Sim | Sim | Não |
| Onde a inferência roda | No seu dispositivo | No seu dispositivo | No seu dispositivo | No seu dispositivo | Nuvem do Hi, Moose (local opcional) |
| Projetos | 1 | 1 | 3 | 25 | De 3 a ilimitados |
| Assentos de equipe | 1 | 1 | 10 | 25 | Ilimitados |
| Busca web no chat | Não | Não | Sim | Sim | Sim |
| [Fluxos de trabalho](../workflows/overview.md) | Não | Não | Sim | Sim | Sim |
| [Google Search Console](../integrations/google-search-console.md) | Não | Não | Sim | Sim | Sim |
| [Áudio](../audio/overview.md) | Não | Não | 15 por mês | 15 por mês | Ilimitado |
| [Marca white label](../agency/white-label.md) | Não | Não | Sim | Sim | Sim |

## Assentos, projetos e créditos

Os **projetos adicionais** custam 10 USD ao mês cada em todos os planos pagos. Adicione ou remova em **Fazer upgrade → Projetos extras**.

Os **assentos** são a verdadeira fronteira entre gratuito e pago. O Preview Mode e o BYOK Free ficam limitados ao titular da conta. O BYOK Premium permite até 10, o BYOK Agency até 25, e os planos gerenciados não têm limite, porque todos os membros consomem o saldo de créditos do titular.

As **recargas de crédito** ficam disponíveis nos planos gerenciados quando o saldo acaba no meio do mês:

- 500.000 créditos por 25 USD
- 2.500.000 créditos por 100 USD

As recargas são compras avulsas, não assinaturas. Só são consumidas depois que os créditos mensais acabam e nunca expiram.

!!! note "As reproduções de áudio são medidas à parte"
    Todo plano que inclui áudio também inclui as primeiras 10.000 reproduções em toda a conta. Acima disso, as reproduções são cobradas a 5,00 USD a cada 10.000 por mês. Nos planos gerenciados, a *geração* de áudio também consome seu saldo de créditos.

## Cupons

Se você tiver um código de desconto, informe-o no checkout, na tela **Fazer upgrade**.

## Mudar de plano

Você pode mudar de plano a qualquer momento em **Configurações → Conta** ou na tela **Fazer upgrade**. Se estiver saindo de um plano gerenciado para um BYOK, adicione antes sua chave de API do OpenRouter. O Hi, Moose valida a chave antes de direcionar o roteamento de IA para ela.

Sua chave do OpenRouter é salva por conta, e não por dispositivo, então ela acompanha você em uma nova instalação.
