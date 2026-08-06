---
source_hash: 3de48b1823942dd1ca44b6be6cf581f170fdffe9e0e850d467f3322e9e89f1a8
---
# Áudio

## Para que serve

Transformar um artigo numa conversa de duas vozes e depois baixar o MP3 ou incorporar o player no seu site. O player vem com uma transcrição, o que coloca na página texto real, próprio e rastreável: conteúdo que um mecanismo de resposta consegue recuperar.

O Áudio fica no aplicativo para desktop, em **Áudio** na barra lateral, dividido em três abas: **Gerar**, **Histórico** e **Análises**.

!!! note "O Áudio saiu do aplicativo web antigo"
    A geração de áudio ficava em `app.himoose.com` com o nome «Listen to this Article». Agora ela faz parte do aplicativo para desktop, com delimitação por projeto, análises de audiência e personalização do player que a versão web não tinha.

## Antes de começar

Defina primeiro o site do projeto. A reprodução fica restrita ao domínio do seu projeto e a `himoose.com`, então o Hi, Moose precisa conhecer o domínio antes de gerar qualquer coisa. Se não estiver definido, a aba Gerar mostra o aviso **Definir site** no lugar do editor.

A disponibilidade do áudio depende do seu [plano](../getting-started/account-modes.md): BYOK Premium e BYOK Agency incluem 15 gerações por mês, os planos gerenciados são ilimitados e os planos gratuitos não incluem áudio.

## Escolher uma fonte

Três formas de trazer conteúdo:

- **URL do artigo**: cole uma URL publicada e clique em **Buscar**. O Hi, Moose extrai o conteúdo e mostra o domínio, a contagem de palavras e o tempo estimado de leitura. O artigo precisa estar acessível publicamente, não atrás de login ou paywall.
- **Colar texto**: dê um título ao episódio e cole direto o roteiro ou o texto do artigo.
- **Enviar arquivo**: solte um `.txt`, `.md`, `.docx`, `.doc` ou `.pdf`. O arquivo é lido no seu dispositivo e o texto dele entra no fluxo de colagem.

## Moldar a conversa

**Foco** (opcional) direciona o que a conversa deve aprofundar. Há sugestões rápidas para os ângulos mais comuns: principais conclusões, explicar para quem está começando, questionar o argumento, para quem isso importa.

**Duração** define o tempo pretendido:

| Duração | Tempo | Roteiro aproximado |
|---|---|---|
| Short | 4-5 min | ~700 palavras |
| Standard | 8-10 min | ~1.400 palavras |
| Deep dive | 15-18 min | ~2.600 palavras |

**Idioma** segue por padrão o idioma do artigo. Altere para mudar tanto o roteiro quanto as vozes.

**Vozes** vêm como duplas de apresentador e convidado, com três combinações prontas (calorosa e curiosa, calma e analítica, animada e cética) ou uma dupla personalizada escolhida por você.

## Direção avançada

Opcional, e tudo o que ficar em branco segue o artigo e a dupla de vozes. São sete campos: direção do apresentador, direção do convidado, cenário, estilo, ritmo, sotaque e contexto adicional.

- **Cenário**: entrevista de estúdio, conversa informal, mesa-redonda, ligação de ouvinte, conversa em movimento
- **Estilo**: explicativo, debate, narrativo, entrevista, descontraído
- **Ritmo**: mais lento, natural, mais rápido
- **Sotaque**: americano (neutro), britânico, australiano, irlandês, indiano ou internacional neutro

Qualquer um desses campos pode ser substituído por uma descrição sua.

**Contexto adicional** serve para o que o artigo não diz: como pronunciar o nome de um produto, quais afirmações evitar, quem é o público.

!!! warning "O contexto orienta o tom, não os fatos"
    O Hi, Moose não inventa fatos para atender a uma direção. O contexto adicional muda o enquadramento e a entrega; não acrescenta evidências que não estão na fonte.

Quando chegar a ajustes que agradem, **Salvar como padrão do projeto** reaproveita tudo no próximo episódio deste projeto.

## Gerar

Clique em **Gerar áudio**. O editor mostra um tempo estimado de renderização antes de começar. A geração roda em segundo plano, então você pode sair da tela e continuar trabalhando: o episódio pronto aparece na lista **Recentes** da barra lateral, e um clique abre aquele episódio direto.

Ao terminar, você tem:

- Um player com busca, saltos de 15 segundos para trás e para frente e velocidade de reprodução
- **Baixar MP3**
- **Compartilhar** para copiar o link do áudio
- A **transcrição** completa, com contagem de turnos e de palavras, e um botão de copiar
- **Incorporar no seu site**, descrito em [Player e incorporação](player-and-embed.md)
- **Gerar de novo com edições** e **Editar configurações**, para ajustar a direção e rodar outra vez

## Histórico

A aba **Histórico** lista todos os episódios do projeto atual com duração, data de criação e status. Os episódios são delimitados por projeto, então trocar de projeto muda o que você vê.

- Busque episódios por nome
- Filtre por **Todos**, **Pronto** ou **Requer atenção**
- Reproduza, baixe, abra as opções de incorporação ou abra o episódio completo
- **Tente novamente** um episódio que falhou

Os status são Pronto, Processando, Reproduzindo, Falhou e Cancelado.

## Para onde ir a partir daqui

- **[Player e incorporação](player-and-embed.md)**: tema, layout, cor de destaque e código de incorporação.
- **[Análises de audiência](analytics.md)**: o que acontece depois que o player está numa página.
