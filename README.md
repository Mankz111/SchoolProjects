# Jogo de Slot - SLOT-BONANZA 🎰

Bem-vindo ao **SLOT-BONANZA**, um jogo de slot desenvolvido em Python, que proporciona uma experiência divertida e interativa para os jogadores. Este projeto foi criado como parte do meu trabalho académico, com o objetivo de demonstrar as minhas habilidades em programação e desenvolvimento de jogos.

## Funcionalidades

- **Depósitos**: Permite aos jogadores depositar dinheiro na sua conta.
- **Levantamentos**: Os jogadores podem levantar o saldo disponível.
- **Jogo de Slot**: Possibilidade de definir uma aposta e jogar.
- **Regras do Jogo**: Explicações claras sobre como jogar e as condições para ganhar.
- **Relatório de Ganhos/Perdas**: Visualização detalhada do desempenho financeiro do jogador.

## Relatório

Para mais detalhes sobre o funcionamento do jogo e a sua implementação, consulte o [relatório do trabalho]((https://github.com/Mankz111/SchoolProjects/blob/main/relatorio.pdf)).

## Estrutura do Código

- `SYMBOLS`: Lista de símbolos que aparecem nas colunas da slot.
- `PAYOUTS`: Dicionário que define os pagamentos para combinações de símbolos.
- Funções principais:
  - `menu_principal()`: Exibe o menu principal do jogo.
  - `deposito()`: Permite aos jogadores realizar depósitos.
  - `levantar()`: Permite aos jogadores efetuar levantamentos.
  - `versaldo()`: Mostra o saldo atual do jogador.
  - `game_menu()`: Menu do jogo para iniciar a partida ou definir apostas.
  - `game_logic()`: Lógica principal do jogo, que gera as colunas e verifica ganhos.
  - `verificar_ganho()`: Função que avalia se o jogador ganhou e calcula o pagamento.
  - `ganhos_percas()`: Gera um relatório de ganhos e perdas do jogador.
