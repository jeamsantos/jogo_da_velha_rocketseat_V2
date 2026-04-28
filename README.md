🎮 Jogo da Velha em Python
Um jogo da velha para dois jogadores rodando no terminal, desenvolvido em Python puro — sem dependências externas.

📋 Sobre o projeto
Este é um jogo da velha (tic-tac-toe) para dois jogadores humanos, jogado via linha de comando. Os jogadores se alternam entre X e O, escolhendo posições no tabuleiro 3×3 até que haja um vencedor ou empate.

🚀 Como executar
Pré-requisitos

Python 3.6 ou superior instalado

Rodando o jogo
bashpython jogo_da_velha.py

🕹️ Como jogar

O jogo exibe o tabuleiro com as coordenadas de linha e coluna (de 0 a 2).
O jogador da vez digita o número da linha e depois o número da coluna onde deseja jogar.
Os jogadores se alternam entre X e O até que:

Um jogador complete uma linha, coluna ou diagonal → vitória
Todas as casas sejam preenchidas sem vencedor → empate



Coordenadas do tabuleiro
0 1 2
0  | |
  -----
1  | |
  -----
2  | |
Exemplo: para jogar no centro, digite linha 1 e coluna 1.

🏗️ Estrutura do código
FunçãoResponsabilidadecriar_tabuleiro()Inicializa o tabuleiro vazio 3×3exibir_tabuleiro()Imprime o tabuleiro com coordenadasjogada_valida()Valida se a posição escolhida é permitidafazer_jogada()Registra a jogada do jogador no tabuleiroverificar_ganhador()Checa linhas, colunas e diagonais por vitóriaverificar_empate()Checa se todas as casas estão preenchidasalternar_jogador()Troca o jogador atual entre X e Omain()Controla o loop principal do jogo

💡 Funcionalidades

✅ Validação de jogadas inválidas (posição ocupada ou fora do tabuleiro)
✅ Detecção de vitória por linha, coluna e diagonal
✅ Detecção de empate
✅ Exibição do tabuleiro com índices para facilitar a navegação
✅ Tratamento de erros para entradas não numéricas


📌 Exemplo de partida
  0 1 2
0  | |
  -----
1  | |
  -----
2  | |

Jogador da vez: X
Digite a linha (0-2): 1
Digite a coluna (0-2): 1

  0 1 2
0  | |
  -----
1  |X|
  -----
2  | |

Jogador da vez: O
...
🎉 Jogador X GANHOU!

📄 Licença
Este projeto é de uso livre para fins educacionais.
