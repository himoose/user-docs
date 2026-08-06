---
source_hash: 1d027fe8d7c0bf155818720c05a7777b1744c302a9ab057860377dc301df1947
---
# Grav

## Para que serve

Conectar um site [Grav](https://getgrav.org) em produção pelo plugin do Hi, Moose para Grav, para que o aplicativo para desktop possa examinar o conteúdo do Grav e executar remotamente, de forma direta, ações de criar, atualizar, publicar e reverter.

## Instalar o plugin

1. Em **Conexões → Grav** no aplicativo para desktop, abra o link de download e baixe o ZIP do plugin do Hi, Moose. A versão atual é a **0.1.1** e exige Grav 1.7.0 ou superior.
2. No painel do Grav, abra **Plugins**, envie o ZIP e conclua a instalação.
3. Ative o plugin e depois abra as configurações dele no painel do Grav.
4. Copie o pacote de conexão exibido ali: você vai colá-lo no Hi, Moose no passo seguinte.

## Conectar no Hi, Moose

1. Abra **Conexões** no aplicativo para desktop e escolha Grav.
2. Informe a URL do seu site Grav.
3. Deixe a rota do conector em branco, a menos que seu plugin do Grav use uma rota diferente da padrão. Do contrário, o Hi, Moose usa a rota do pacote de conexão ou recorre a `/himoose-connector`.
4. Cole o pacote de conexão copiado do plugin e salve.
5. Clique em **Testar conector** para validar a conexão com seu site Grav em produção.

## Estado da conexão

Depois do teste, o Hi, Moose reporta um entre vários estados: o conector ainda não está totalmente configurado, está salvo mas ainda não validado, respondeu mas as ações remotas de escrita não estão plenamente liberadas (somente leitura), está inteiramente pronto para ações de leitura e escrita remota, ou a última validação falhou e as configurações do site ou os segredos do plugin precisam de atenção.

## O que a conexão permite

Uma vez pronta, o conector do Grav consegue listar conteúdo, ler conteúdo bruto e criar, atualizar e publicar conteúdo diretamente, seguindo o mesmo caminho preparado e revisável que [Rascunhos, prévia e publicação](../features/drafts-and-publishing.md) usa nas outras conexões.

## Segurança

A URL do seu site Grav e o pacote de conexão ficam salvos localmente e acessíveis só ao processo em segundo plano do aplicativo para desktop; nunca são expostos à interface.
