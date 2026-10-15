---
source_hash: 02739399b48594689facbef6808edfaaedea42f90e6577cf6c6b9bb9f23939c1
---
!!! note "Tradução automática"
    Esta página foi traduzida por IA. A versão em inglês é a versão oficial.

    [Ler em inglês](https://himoose.com/docs/integrations/hi-moose-mcp/tools/)


# Referência de ferramentas

Todas as ferramentas que o Hi, Moose MCP oferece a um app conectado, com o que cada uma recebe e o que devolve. Você não chama as ferramentas diretamente: o app escolhe a ferramenta a partir do que você pede. Esta página diz o que pedir e o que esperar.

Todas as ferramentas, exceto `list_projects` e `get_result`, recebem um **projeto**, pelo nome mostrado no Hi, Moose. Diga o nome do projeto no pedido quando tiver mais de um, por exemplo "para o projeto Acme".

## Quanto tempo leva

| Ferramenta | Tempo típico |
|---|---|
| Listar projetos, briefs, rascunhos | Alguns segundos |
| Verificar cobertura do site | Menos de um minuto |
| Verificação de visibilidade, ler uma resposta | Alguns segundos |
| Lista de oportunidades | De alguns segundos a um minuto |
| Brief de conteúdo, rascunho, perguntas frequentes, pontos-chave, imagem destacada | De um a três minutos |
| Auditoria AEO | De dois a quatro minutos |
| Links internos | Cerca de um minuto |
| Episódio de áudio | 5 minutos para curto, 9 para padrão, 15 para profundo |

Quando uma ferramenta demora mais do que o app está disposto a esperar, ela responde "ainda em andamento" com um id de trabalho. O app então usa `get_result` para buscar o trabalho pronto; peça para ele verificar de novo se não fizer isso.

## Projetos e Library

### list_projects

Lista os projetos Hi, Moose em que você pode trabalhar. Todas as outras ferramentas precisam de um projeto, então o app normalmente chama esta primeiro.

Peça: "Liste meus projetos Hi, Moose."

### list_briefs

Lista os briefs de conteúdo salvos na Library de um projeto, do mais recente para o mais antigo, até 50. Use quando você se referir a um brief feito antes.

Peça: "Mostre os briefs salvos para a Acme."

### list_drafts

Lista os rascunhos salvos na Library de um projeto, do mais recente para o mais antigo, até 50.

Peça: "Quais rascunhos eu tenho na Acme?"

### get_result

Busca o trabalho iniciado por outra ferramenta, pelo id do trabalho. Espera até um minuto para ele terminar. O app chama esta ferramenta sozinho; você só precisa dela quando o app disser que o trabalho ainda está em andamento e você quiser que ele verifique de novo.

## Cobertura do site

### check_site_coverage

Verifica no rastreamento mais recente do seu site se há páginas que já cobrem um ou mais temas.

| Entrada | Obrigatório | Significado |
|---|---|---|
| topics | sim | De uma a quinze frases curtas, como "geração de SBOM para Python" |
| parentTopic | não | O assunto mais amplo a que os temas pertencem, usado para julgar cobertura parcial |

Para cada tema ela responde **covered**, **partial**, **uncovered** ou **unknown**, com os URLs das páginas mais próximas como evidência e a data do rastreamento verificado. Unknown significa que a verificação não pôde rodar para aquele tema, não que o site não o cobre.

Peça: "Nosso site já cobre SCA vs SAST?"

## Conteúdo

### create_content_brief

Cria um brief de conteúdo informado pela pesquisa: objetivo, público, justificativa, grupos de palavras-chave, estrutura recomendada e restrições, com base em resultados de pesquisa ao vivo, no rastreamento do seu site, nas diretrizes de marca e no Brand Truth.

| Entrada | Obrigatório | Significado |
|---|---|---|
| topic | sim | O tema, a pergunta ou o título provisório, até 400 caracteres |
| targetUrl | não | A página do seu site para a qual o brief é feito |
| templateType | não | O tipo de conteúdo: "Blog post", "Landing page", "Comparison page", "Guide" |
| guidance | não | Requisitos decididos em outro lugar: ângulo, pontos obrigatórios, tom. Até 4.000 caracteres. |

Devolve o brief como texto mais um id de brief que a ferramenta de rascunho usa. Salvo na Library.

Peça: "Escreva um brief de conteúdo para um guia de geração de SBOM para equipes Python."

### create_draft

Escreve um primeiro rascunho publicável a partir de um brief, na voz da sua marca, com base no brief, no Brand Truth e nas diretrizes de marca, com links internos escolhidos a partir do rastreamento do seu site e uma passagem de polimento.

| Entrada | Obrigatório | Significado |
|---|---|---|
| briefId | um dos dois | Um brief feito no Hi, Moose |
| brief | um dos dois | Um brief escrito em outro lugar, como texto, até 60.000 caracteres |
| briefTitle | não | O título provisório, ao passar um brief como texto |
| templateType | não | O tipo de conteúdo, ao passar um brief como texto |
| guidance | não | Requisitos extras, até 4.000 caracteres |

Devolve o rascunho como texto mais um id de rascunho. Salvo na Library.

Peça: "Escreva o artigo a partir daquele brief." ou "Aqui está um brief que eu escrevi, faça o rascunho para a Acme: ..."

### create_featured_image

Cria uma imagem destacada para um artigo, 1200 por 630, no seu estilo de imagem salvo quando houver um definido.

| Entrada | Obrigatório | Significado |
|---|---|---|
| draftId | um dos dois | Um rascunho feito no Hi, Moose |
| title e summary | um dos dois | O título do artigo e um resumo curto, até 6.000 caracteres, quando não há rascunho |
| styleIntent | não | Um desejo para esta imagem em particular: clima, cena, cores. O estilo salvo continua valendo. |

Devolve a imagem e um link para o PNG. O arquivo também é salvo no dispositivo host.

Peça: "Faça uma imagem destacada para aquele rascunho, luz de fim de tarde, sem pessoas."

### create_faqs

Escreve perguntas frequentes com respostas para um conteúdo, na voz da sua marca, mais o esquema FAQPage pronto para colar na página. Nas contas pagas, as perguntas são pesquisadas primeiro a partir do comportamento real de busca.

| Entrada | Obrigatório | Significado |
|---|---|---|
| draftId | um dos dois | Um rascunho salvo |
| url | um dos dois | Uma página publicada do seu site |
| guidance | não | Público, perguntas que devem aparecer, tom. Até 4.000 caracteres. |

Peça: "Escreva perguntas frequentes para https://acme.example/guides/sbom."

### create_key_points

Escreve os pontos-chave de um conteúdo: afirmações curtas e citáveis, na voz da sua marca, que os motores de resposta podem aproveitar.

| Entrada | Obrigatório | Significado |
|---|---|---|
| draftId | um dos dois | Um rascunho salvo |
| url | um dos dois | Uma página publicada do seu site |
| guidance | não | Público, pontos que devem aparecer, tom. Até 4.000 caracteres. |

Peça: "Me dê os pontos-chave do rascunho do guia de SBOM."

## Auditorias e links

### run_aeo_audit

Executa uma auditoria de otimização para motores de resposta em um conteúdo: uma pontuação de 0 a 100, pontuações por categoria (estrutura, extraibilidade, potencial de citação, sinais de confiança, atualidade, prontidão para resposta e mais), os problemas encontrados e mudanças concretas com texto proposto.

| Entrada | Obrigatório | Significado |
|---|---|---|
| url | um dos três | Uma página publicada. A melhor opção, porque verificações técnicas como acesso de rastreadores de IA e datas da página só rodam em uma página publicada. |
| draftId | um dos três | Um rascunho salvo |
| content | um dos três | O conteúdo como texto, para uma página ainda não publicada. Até 50.000 caracteres. |
| targetQuery | não | A pergunta ou prompt de busca que o conteúdo deve vencer, até 200 caracteres. Sem ele, o Hi, Moose infere um. |

Nas contas pagas, evidências de pesquisa ao vivo são incluídas.

Peça: "Audite https://acme.example/guides/sbom para a consulta 'ferramentas de geração de SBOM'."

### find_internal_links

Planeja links internos para um conteúdo usando o rastreamento do seu próprio site. Devolve duas listas: páginas para as quais este conteúdo deve apontar, cada uma com o texto âncora a usar, e páginas existentes que devem adicionar um link para este conteúdo, cada uma com o texto âncora a usar nessa página. Páginas já ligadas em qualquer direção ficam de fora.

| Entrada | Obrigatório | Significado |
|---|---|---|
| url | um dos três | Uma página publicada do seu site |
| draftId | um dos três | Um rascunho salvo |
| content | um dos três | O conteúdo como texto, até 50.000 caracteres |
| title | não | O título, ao passar o conteúdo como texto |

Os resultados cobrem as páginas rastreadas até agora e indicam a data do rastreamento. Páginas publicadas depois do último rastreamento não são incluídas.

Peça: "Planeje links internos para o rascunho do guia de SBOM."

## Visibilidade na pesquisa com IA

### visibility_check_topic

Responde a "aparecemos na pesquisa com IA para X" a partir dos resultados de visibilidade que o Hi, Moose guardou. Faça a pergunta com suas próprias palavras; o Hi, Moose a associa aos prompts acompanhados, em qualquer idioma.

| Entrada | Obrigatório | Significado |
|---|---|---|
| question | sim | O tema ou a pergunta, até 400 caracteres |
| lookbackDays | não | Quantos dias de resultados guardados ler. Padrão 90. |
| engine | não | Só este motor, pelo nome, como "ChatGPT" |

Devolve, por motor, se a marca foi mencionada ou citada na última execução e em uma execução anterior, as taxas de menção e citação no período, um breve trecho da última resposta em que a marca apareceu, os prompts associados e outras marcas vistas. Cada trecho traz um id de resposta para a próxima ferramenta. Os resultados cobrem apenas os prompts acompanhados nos motores acompanhados, nunca toda a pesquisa com IA. Ela lê resultados guardados e nunca executa novas verificações.

Peça: "Aparecemos na pesquisa com IA para geração de SBOM?"

### visibility_get_answer

Busca uma resposta guardada pelo seu id: o prompt, o motor, a data, se a marca foi mencionada ou citada, as fontes que o motor listou, as notas do avaliador e o texto completo da resposta. O texto é o que o motor escreveu na época.

Peça: "Me mostre a resposta completa do ChatGPT daquele resultado."

### visibility_list_opportunities

Devolve a fila de trabalho por prioridade que o Hi, Moose monta a partir dos resultados de visibilidade guardados, as mesmas linhas do separador Oportunidades. Cada linha indica a lacuna exata, o próximo passo em uma frase, a prioridade com seus motivos, com que consistência a lacuna se manteve ao longo das execuções, o esforço, o status definido pela equipe e um id de oportunidade.

| Entrada | Obrigatório | Significado |
|---|---|---|
| lookbackDays | não | Dias de resultados guardados a ler. Padrão 7, o mesmo do separador Oportunidades. No máximo 90. |
| limit | não | Linhas a devolver, as melhores primeiro. Padrão 10, no máximo 25. |
| action | não | Só um tipo de linha: `create-coverage`, `improve-page`, `earn-inclusion`, `correct-description` ou `investigate-change` |
| priority | não | `high`, `medium` ou `low` |
| includeClosed | não | Devolver também as linhas marcadas como concluídas, dispensadas ou adiadas. Padrão false. |
| opportunityId | não | Um id de um resultado anterior. Devolve as provas completas dessa linha em vez da lista. |

Os cinco tipos de linha: **create-coverage** (nenhuma página sua responde a um prompt que os concorrentes vencem), **improve-page** (uma página sua é citada ou é a correspondência mais próxima, mas a marca fica de fora ou atrás), **earn-inclusion** (uma página de terceiros que os motores citam menciona concorrentes mas não você), **correct-description** (as respostas repetem uma afirmação sobre a marca que precisa ser verificada) e **investigate-change** (a marca era mencionada ou citada antes e deixou de ser).

Peça: "No que devemos trabalhar para a pesquisa com IA esta semana?" e depois "Me mostre as provas da primeira."

## Áudio

### create_audio

Cria um episódio "ouça este artigo": uma conversa falada com duas vozes sobre o conteúdo, renderizada como MP3 e hospedada pelo Hi, Moose, mais o trecho HTML do player incorporável.

| Entrada | Obrigatório | Significado |
|---|---|---|
| url | um dos três | Uma página publicada |
| draftId | um dos três | Um rascunho salvo |
| content e title | um dos três | O artigo como texto, de 1.200 a 200.000 caracteres, com o título |
| length | não | `short` (cerca de 4 minutos), `standard` ou `deep`. Padrão short. |
| hostVoice, guestVoice | não | Duas vozes diferentes. Padrão Sulafat e Fenrir. |
| language | não | Idioma da narração. Padrão: o idioma do conteúdo. |
| focus | não | No que a conversa deve se concentrar, até 500 caracteres |
| theme, layout, color, showTitle, customTitle, showTranscript, hideAttribution | não | A aparência do player, veja abaixo |

A [página de configurações de áudio](https://himoose.com/hi-moose-mcp/audio/) permite ouvir cada voz, escolher a duração, o idioma e a aparência do player, e copiar uma linha de configurações para colar no chat. Enquanto o episódio é renderizado, o dispositivo host não trabalha em mais nada. Se o resultado disser que o episódio ainda está sendo renderizado, a próxima ferramenta o busca alguns minutos depois.

Peça: "Transforme https://acme.example/guides/sbom em áudio, curto, com Zephyr e Charon."

### get_audio_embed

Devolve o trecho do player de um episódio existente, com uma nova aparência quando campos do player são passados. O áudio não é renderizado de novo. É também o jeito de buscar um episódio que ainda estava sendo renderizado.

| Entrada | Obrigatório | Significado |
|---|---|---|
| audioId | sim | O id do episódio |
| theme | não | `dark`, `light` ou `auto`. Padrão dark. |
| layout | não | `full` ou `compact`. Padrão full. |
| color | não | Cor de destaque em hex, por exemplo `#5688b0` |
| showTitle, customTitle | não | Mostrar uma linha de título, ou definir o seu próprio |
| showTranscript | não | Mostrar o botão de transcrição. Padrão true. |
| hideAttribution | não | Ocultar a linha "Audio by Hi, Moose". Só nos planos pagos. |

Peça: "Me dê o player compacto claro daquele episódio."

## O que as ferramentas não podem fazer

Elas não podem alterar configurações nem membros da equipe, mudar o que o Hi, Moose acompanha, iniciar execuções de visibilidade nem excluir nada. Para painéis e automação, use a [Hi, Moose API](../developer-api.md).
