---
source_hash: 685c1e28ae96f03a47645cdef302b5b0d4b54afda3810ab2ce0dae64df47c45a
---
!!! note "Tradução automática"
    Esta página foi traduzida por IA. A versão em inglês é a versão oficial.

    [Ler em inglês](https://himoose.com/docs/inbox/notifications/)

# Notificações da Caixa de entrada

## Para que serve

As preferências de notificação da Caixa de entrada controlam como, e com que urgência, você é avisado quando chegam itens novos à [Caixa de entrada](overview.md) de um projeto. Essas configurações são por projeto, então um projeto de teste de baixa prioridade não precisa avisar você do mesmo jeito que o site em produção de um cliente.

## Configurações

- **Mostrar o indicador da Caixa de entrada neste aplicativo**: quando desativado, o indicador da barra lateral e do dock não é atualizado para este projeto, mesmo que os itens continuem chegando à Caixa de entrada.
- **Mostrar notificações do sistema**: notificações nativas do macOS ou do Windows quando um item atinge o limite de gravidade definido abaixo.
- **Gravidade mínima para notificações do sistema**: escolha a menor gravidade que deve disparar uma notificação. Os itens abaixo desse limite continuam aparecendo na Caixa de entrada, apenas não interrompem você.
- **Enviar um resumo diário por e-mail**: a configuração é salva, mas esse resumo ainda não é enviado; vem em breve.
- **Incluir alterações de AEO informativas**: desativado por padrão, para manter a Caixa de entrada focada no que importa. Quando ativado, alterações de baixo impacto também vão para a Caixa de entrada. Note que as notificações do sistema continuam respeitando o limite de gravidade acima, mesmo com essa opção ligada.

## Por que isso é separado da própria gravidade

A gravidade (crítica, aviso, notificação, informação) é atribuída ao próprio item conforme o que de fato aconteceu: não é algo que você configura. O que você controla aqui é quanto disso aparece como indicador, como notificação do sistema ou (em breve) como e-mail. Assim o sinal subjacente continua honesto enquanto você ajusta o volume da entrega.
