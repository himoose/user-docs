---
source_hash: f081840e659e67696268902173c5c0f26e8413e1debac31049488ad42cb5c005
---
# Configurações

## Para que serve

Nas Configurações você gerencia seu perfil, seu plano, seus modelos, sua equipe e o comportamento do aplicativo neste computador. Elas estão organizadas em dez seções na coluna da esquerda.

| Seção | O que contém |
|---|---|
| Geral | Dados do perfil e comportamento do aplicativo neste computador |
| Uso | Saldo de créditos e data de renovação |
| Conta | E-mail, senha, plano, chave do OpenRouter |
| Local Model | Download e ativação do modelo no dispositivo |
| Equipe | Assentos, convites, funções |
| [Monitoramento do site](../site-monitoring/overview.md) | Agendamento do rastreamento, índice de busca, páginas monitoradas, caminhos bloqueados |
| [Marca](../agency/white-label.md) | Relatórios white label e atribuição de áudio (somente planos pagos) |
| Logs | Registros de ações e exportação CSV |
| Dados e backup | Backup e restauração locais |
| Solução de problemas | Cache, registro de diagnóstico, redefinição dos dados locais |

## Geral

**Dados do perfil**: seu nome preferido, sua função e sua localização. Servem para personalizar o aplicativo e deixar mais clara a atribuição do trabalho compartilhado.

**Comportamento do aplicativo** controla como o Hi, Moose roda neste computador:

- **Iniciar o Hi, Moose ao fazer login**: depois de reiniciar, o aplicativo abre discretamente em segundo plano para que o trabalho agendado continue. Você pode abrir a janela a qualquer momento pela bandeja do sistema ou pela barra de menus.
- **Compartilhar estatísticas de uso anônimas**: envia eventos anônimos e agregados (quais recursos rodam, versão do aplicativo, erros) para que possamos melhorar o produto. Nunca envia seu conteúdo, seus prompts, suas chaves ou os sites que você analisa, e seu IP é descartado. Você pode desativar quando quiser.

## Uso

Nos planos gerenciados, aqui você vê seu saldo de créditos e o que resta do mês.

!!! note "O mês é contado em UTC"
    Os créditos são renovados no início de cada mês em UTC, e não no seu fuso horário. As Configurações mostram a data correspondente onde você está, então, no fim do último dia do mês, pode parecer que a renovação chegou adiantada.

Os planos BYOK não consomem saldo de créditos do Hi, Moose para inferência, já que a geração roda com a sua chave. O custo dos modelos vai direto para o OpenRouter.

## Conta

- Atualize seu e-mail, verifique-o e redefina sua senha nas contas com e-mail e senha. As contas do Google são gerenciadas pelo Google.
- As alterações de e-mail aguardam sua confirmação por link antes de entrar em vigor e, em seguida, sua sessão no aplicativo é atualizada.
- Consulte seu plano atual e troque-o. Veja [Tipos de conta e planos](account-modes.md).

### Adicionar sua chave de API do OpenRouter

Nos planos BYOK, adicione aqui sua chave do [OpenRouter](https://openrouter.ai). O Hi, Moose valida a chave antes de direcionar o roteamento de IA para ela. Depois de adicionada:

- Os recursos de IA rodam localmente no aplicativo para desktop com a sua chave
- Você escolhe quais modelos compatíveis usar para chat e geração
- Sua chave e seus prompts nunca passam pelos servidores do Hi, Moose na inferência BYOK

A chave é salva por conta, e não por dispositivo, então acompanha você em uma nova instalação.

## Local Model

Baixe e ative um modelo aprovado no dispositivo, como o Gemma 4. A execução local não usa os modelos do Hi, Moose nem sua chave do OpenRouter: ela acontece inteiramente na sua máquina e é gratuita.

Os modelos locais estão disponíveis em todos os planos e são **obrigatórios** no Preview Mode para as [auditorias de AEO](../features/aeo-audits.md) e para a avaliação de visibilidade.

!!! note "O tamanho do contexto se ajusta à sua RAM"
    O Hi, Moose dimensiona a janela de contexto do modelo conforme a memória disponível na sua máquina, então o mesmo modelo usa uma janela menor em um notebook de 16 GB do que em uma estação de trabalho maior.

## Equipe

Convide membros, veja as funções e revogue acessos. Os limites de assentos dependem do seu plano. Veja [Gerenciamento da equipe](team-management.md) para o passo a passo completo.

## Monitoramento do site

Agendamento do rastreamento, índice de busca local, páginas monitoradas e caminhos bloqueados. É uma área extensa e tem página própria: **[Monitoramento do site](../site-monitoring/overview.md)**.

As conexões com CMS e fontes de dados são outra coisa e ficam na tela **Conexões**, não nas Configurações:

- [WordPress](../integrations/wordpress.md)
- [Webflow](../integrations/webflow.md)
- [Grav](../integrations/grav.md)
- [Google Search Console](../integrations/google-search-console.md)

## Marca

Aplique sua marca aos relatórios PDF exportados e aos players de áudio incorporados. Disponível em todos os planos pagos e editável pelo titular da assinatura. Veja **[Marca white label](../agency/white-label.md)**.

## Logs

Registros de ações do projeto atual, com tipo, usuário, data, status e metadados de cada ação registrada. Nos planos gerenciados, os registros compartilhados da equipe sincronizam junto com os seus locais.

**Exportar CSV** faz o download. A exportação dos registros de ações da equipe é restrita aos titulares de espaços de trabalho gerenciados pagos.

## Dados e backup

Crie um backup compactado `.hmbk` do seu histórico no dispositivo e importe-o depois para restaurá-lo.

**Os backups incluem** os registros do banco de dados local e os agendamentos de visibilidade BYOK salvos, de modo que seus briefings, auditorias, prévias, histórico de monitoramento do site, estado da Caixa de entrada e demais artefatos de trabalho não sigilosos continuem portáteis.

**Os backups não incluem** o estado de login, credenciais de conectores, chaves de API, arquivos de modelos locais nem anexos.

!!! warning "A importação sobrescreve os dados locais de forma permanente"
    Uma importação substitui os dados locais do Hi, Moose deste dispositivo pelo conteúdo do backup. A caixa de confirmação informa quantos registros serão restaurados e quando o backup foi criado. Reinicie o aplicativo em seguida para que todas as telas recarreguem a partir dos dados restaurados.

As importações aceitam somente arquivos `.hmbk` exportados pelo aplicativo para desktop do Hi, Moose.

## Solução de problemas

Três ferramentas de recuperação. Todas afetam apenas o estado local do desktop e nunca tocam os dados na nuvem.

**Limpar o cache temporário**: apaga o cache HTTP, os service workers e outros estados descartáveis. Mantém seu login e o histórico de trabalho local. Tente isso primeiro.

**Registro de diagnóstico**: o Hi, Moose mantém um pequeno registro de erros neste dispositivo. **Abrir a pasta de registros** leva você até ele; se o suporte pedir, envie o arquivo `main-errors.log`. O registro fica no seu dispositivo, a menos que você escolha compartilhá-lo.

**Redefinir os dados locais do aplicativo**: remove permanentemente artefatos, briefings, prévias, histórico de visibilidade e demais estados de trabalho locais do dispositivo. A ação não pode ser desfeita. Seu login e as credenciais salvas dos conectores permanecem.
