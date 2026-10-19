---
source_hash: 44a098b9f501f2117290c2037c5635c5aa9f250b49d72a34e103dba9d3cb8b5b
---
!!! note "Tradução automática"
    Esta página foi traduzida por IA. A versão em inglês é a versão oficial.

    [Ler em inglês](http://localhost:8000/integrations/hi-moose-mcp/troubleshooting/)


# Solução de problemas

O que fazer quando o Hi, Moose MCP não responde como você espera. A maioria dos problemas se resume ao dispositivo host: o computador onde o Hi, Moose fica aberto e faz o trabalho.

## "O dispositivo host deste projeto não deu sinal"

O computador escolhido como dispositivo host está desligado, em suspensão, sem conexão, ou o Hi, Moose está fechado ou sem sessão iniciada nele.

1. Abra o Hi, Moose nesse computador e entre na sua conta.
2. Espere um minuto e peça de novo. O host dá sinal a cada poucos minutos enquanto o Hi, Moose está aberto.
3. Se o computador não vai voltar, escolha outro em **Configurações → Hi, Moose MCP**. Só o proprietário da conta pode trocar o dispositivo host.

Os trabalhos esperam até 15 minutos pelo dispositivo host. Depois disso eles expiram e o app recebe uma mensagem informando isso; peça de novo quando o host voltar.

## "Este projeto não tem dispositivo host"

Ninguém escolheu ainda um dispositivo host para o projeto. Abra o Hi, Moose no computador que deve fazer o trabalho, vá em **Configurações → Hi, Moose MCP** e escolha-o. Cada projeto tem o seu próprio dispositivo host, então um projeto novo também precisa de um.

## O app diz que o trabalho ainda está em andamento

Briefs, rascunhos, auditorias e áudio levam minutos, e alguns apps param de esperar antes de o trabalho terminar. Peça para o app verificar de novo; ele busca o resultado com o id de trabalho que recebeu. O trabalho também fica salvo na sua [Library](../../library/overview.md) no Hi, Moose, então nada se perde se o chat seguir em frente.

O áudio é o que leva mais tempo: cerca de 5 minutos para um episódio curto, 9 para padrão e 15 para profundo. Enquanto isso o dispositivo host não trabalha em mais nada, então um segundo pedido espera atrás dele.

## O app escolheu o projeto errado

As ferramentas recebem o projeto pelo nome. Diga-o no pedido, por exemplo "para o projeto Acme", ou peça para o app listar os projetos primeiro e depois escolher. Se dois projetos têm nomes parecidos, use exatamente o nome mostrado no Hi, Moose.

## O conector não conecta

- **A página de login nunca abre.** Confira se o endereço do servidor é `https://mcp.himoose.com/mcp`, sem caracteres a mais no final, e se o app está usando OAuth, não uma chave de API.
- **O código de login expirou.** O código vale por dois minutos. Comece a conexão de novo a partir do app.
- **Claude Team ou Enterprise.** Um proprietário precisa adicionar o conector para a organização antes que os membros possam se conectar.
- **ChatGPT.** Servidores MCP personalizados exigem um plano pago, e em workspaces Business e Enterprise um proprietário pode precisar permitir conectores personalizados ou ativar o Modo desenvolvedor primeiro. Os nomes dos menus mudam; veja [Conectar no ChatGPT](../hi-moose-mcp.md#connect-in-chatgpt).

## O app estava conectado e agora não está

O acesso expira sozinho depois de 30 dias sem uso, e o proprietário da conta pode revogar um app em **Configurações → Hi, Moose MCP**. Conecte de novo a partir do app.

## Os resultados parecem desatualizados

- **Cobertura do site e links internos** leem o rastreamento mais recente do seu site e indicam a data dele. Páginas publicadas depois disso não são incluídas. Rode um rastreamento no Hi, Moose e peça de novo.
- **Visibilidade e oportunidades** leem apenas resultados guardados e nunca executam novas verificações. Elas cobrem os prompts acompanhados nos motores acompanhados no período indicado na resposta. Para ver um tema novo, adicione um prompt para ele na tela Visibilidade e deixe uma execução acontecer.

## Algo rodou sem você esperar

A tabela **Trabalhos recentes de agentes** em **Configurações → Hi, Moose MCP** lista todos os trabalhos: o que foi pedido, por qual app, quando e se terminou. Os trabalhos rodam com a conta que está com a sessão iniciada no dispositivo host, então um app conectado só pode ler e gravar na Library dessa conta.

## Ainda com problemas

Escreva para o suporte com o nome do projeto, qual app você estava usando, mais ou menos quando aconteceu e o que o app disse. A tabela de trabalhos de agentes também ajuda.
