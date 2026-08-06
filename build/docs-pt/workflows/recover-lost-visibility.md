---
source_hash: 7907c08f25052f66801891d4fc6f24fe3bdcd307070021aede9005fe5995996b
---
!!! note "Tradução automática"
    Esta página foi traduzida por IA. A versão em inglês é a versão oficial.

    [Ler em inglês](https://himoose.com/docs/workflows/recover-lost-visibility/)

# Recuperar a visibilidade perdida

## Para que serve

Esta é a receita de fluxo para o **conteúdo existente**: ela vigia seus resultados de [visibilidade](../visibility/overview.md) e, quando algo cai de forma significativa, descobre automaticamente se uma página existente pode ser corrigida ou se é preciso conteúdo novo, e prepara o trabalho para sua revisão.

## Montar o fluxo

O fluxo se lê como uma única frase, formada por estas escolhas:

> **Quando** [o share of mentions cair / o share of citations cair / o share of mentions subir / o share of citations subir] **em** [um limite, de 1 a 99 pontos] **para** [todos os temas / um tema monitorado específico], o Hi, Moose identifica os prompts afetados e então [prepara uma correção de conteúdo / me avisa].

- **Gatilho**: qual métrica vigiar e se você se importa com quedas ou com altas. Se escolher um gatilho de alta, a única ação final disponível é **me avisar**: altas não têm caminho de correção de conteúdo, porque não há o que consertar.
- **Limite**: quantos pontos de variação devem contar como significativos, para que o ruído normal não dispare o fluxo.
- **Escopo de tema**: aplicar este fluxo a tudo o que você monitora ou restringi-lo a um tema específico.
- **Ação final**: **preparar uma correção de conteúdo** (segue para a lógica de ramificação abaixo) ou **me avisar** (só cria um item na Caixa de entrada, sem preparar nenhuma ação de conteúdo).

## Quando a ação final é «preparar uma correção de conteúdo»

Mais duas escolhas se ramificam conforme exista ou não uma página adequada:

- **Se houver páginas correspondentes**: escolha o que o Hi, Moose deve fazer: **rodar uma auditoria de AEO**, **gerar FAQ e schema**, **gerar pontos principais** ou **nada**.
- **Se não houver página correspondente**: escolha entre **criar um briefing e um rascunho novo** ou **nada**.

Essa ramificação é o ponto central da receita: ela não recomenda às cegas um artigo novo toda vez que a visibilidade cai. Primeiro verifica se corrigir algo que você já tem é a melhor jogada, e só propõe conteúdo novo quando nada do existente serve.

## Como ele roda

Este fluxo não tem botão de execução manual. Ele se avalia automaticamente sempre que uma execução de visibilidade termina, comparando a última concluída com a anterior. Quando dispara, o resultado, incluindo os prompts afetados e a ação tomada, chega à sua [Caixa de entrada](../inbox/overview.md), ligado à mudança de visibilidade que o provocou.
