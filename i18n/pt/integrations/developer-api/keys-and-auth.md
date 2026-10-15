---
source_hash: eef50f1fe484ff2af95068f006064217adac902f902e7159b98801260bb5cb9a
---

# Chaves e autenticação

## Criar uma chave

1. Abra o Hi, Moose e entre como proprietário da conta. Só o proprietário pode criar, ver e revogar chaves.
2. Vá em **Configurações → Hi, Moose REST API**.
3. Dê um nome à chave, escolha os projetos que ela pode ler (todos ou um), escolha quando ela expira e marque as permissões de que ela precisa.
4. Clique em **Criar chave** e copie a chave. Ela é mostrada uma única vez. O Hi, Moose não pode mostrá-la de novo; se você perdê-la, revogue-a e crie outra.

As chaves começam com `hmk_live_` seguido de 64 caracteres. A tabela abaixo do formulário lista cada chave ativa com suas permissões, a data de criação, o último uso e a expiração. **Revogar** interrompe uma chave na hora.

O Hi, Moose guarda apenas um hash da chave, do mesmo jeito que senhas são guardadas, então ninguém no Hi, Moose consegue recuperar uma chave.

## Uma chave por app

Crie uma chave separada para cada app ou script, com um nome que diga para que ela serve. Assim uma chave pode ser revogada sem quebrar mais nada, e a coluna **último uso** em Configurações mostra qual app fez as chamadas.

## Permissões

| Permissão | O que a chave pode fazer |
|---|---|
| Ler dados de visibilidade | Todos os endpoints `GET`. Sempre ativa. |
| Gerenciar o acompanhamento | Criar projetos, definir termos de marca e concorrentes, adicionar, alterar e excluir prompts, definir motores e agendamento, registrar e excluir webhooks. |
| Iniciar execuções | Iniciar uma execução de visibilidade. As execuções gastam o saldo da conta em motores na nuvem, então dê isso só a uma chave que precise. |

Uma chamada sem a permissão necessária responde `403 insufficient_scope` e informa a permissão que falta. Escolha as permissões ao criar a chave; elas não podem ser alteradas depois. Crie uma chave nova em vez disso.

Na API as permissões aparecem como `visibility:read`, `tracking:write` e `runs:execute`, por exemplo na resposta de `GET /me`.

## Acesso a projetos

Uma chave lê todos os projetos da conta ou um só projeto, escolhido ao criar a chave. Um projeto que a chave não pode ler responde `404 not_found`, o mesmo que um projeto que não existe, então uma chave não serve para descobrir quais projetos uma conta tem.

## Autenticação

Envie a chave como token Bearer no cabeçalho `Authorization` em toda requisição:

```bash
curl https://api.himoose.com/v1/me \
  -H "Authorization: Bearer hmk_live_..."
```

A resposta informa a chave, suas permissões e os ids de projeto que ela pode ler. É uma boa primeira chamada para verificar que uma chave funciona.

Uma requisição sem chave, ou com uma chave malformada, revogada ou expirada, responde `401` com um destes códigos:

| Código | Significado |
|---|---|
| `invalid_key` | Sem cabeçalho `Authorization`, uma chave no formato errado ou uma chave que o Hi, Moose não conhece |
| `key_revoked` | A chave foi revogada em Configurações |
| `key_expired` | A chave passou da data de expiração |

## Mantenha a chave no seu servidor

Use a chave apenas a partir do seu próprio servidor. A API não envia cabeçalhos CORS, então uma página web não consegue chamá-la diretamente. Um painel no navegador deve chamar o seu backend, e o seu backend chama a API. Assim a chave fica fora da página e fora do registro de rede do navegador.

Guarde a chave em uma variável de ambiente ou em um gerenciador de segredos, nunca no controle de versão. Se uma chave vazar, revogue-a em Configurações e crie uma nova. A revogação tem efeito na hora.

## Expiração

Uma chave pode expirar depois de 30, 90 ou 365 dias, ou nunca. Uma chave com expiração é a opção mais segura para um script que vai ser substituído; uma chave sem expiração serve para um painel de longa duração cuja chave vive em um gerenciador de segredos. A tabela em Configurações mostra a data de expiração de cada chave.
