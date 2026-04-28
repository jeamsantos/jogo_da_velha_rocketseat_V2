VAZIO = ' '

def criar_tabuleiro():
    return [[VAZIO] * 3 for _ in range(3)]

def exibir_tabuleiro(tabuleiro):
    print("\n  0 1 2")
    for i, linha in enumerate(tabuleiro):
        print(f"{i} {'|'.join(linha)}")
        if i < 2:
            print("  -----")
    print()

def jogada_valida(tabuleiro, linha, coluna):
    return 0 <= linha <= 2 and 0 <= coluna <= 2 and tabuleiro[linha][coluna] == VAZIO

def fazer_jogada(tabuleiro, linha, coluna, jogador):
    tabuleiro[linha][coluna] = jogador

def verificar_ganhador(tabuleiro, jogador):
    # Linhas e colunas
    for i in range(3):
        if all(tabuleiro[i][j] == jogador for j in range(3)):
            return True
        if all(tabuleiro[j][i] == jogador for j in range(3)):
            return True
    # Diagonais
    if all(tabuleiro[i][i] == jogador for i in range(3)):
        return True
    if all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True
    return False

def verificar_empate(tabuleiro):
    return all(tabuleiro[i][j] != VAZIO for i in range(3) for j in range(3))

def alternar_jogador(jogador):
    return 'O' if jogador == 'X' else 'X'

def main():
    tabuleiro = criar_tabuleiro()
    jogador = 'X'

    while True:
        exibir_tabuleiro(tabuleiro)
        print(f'Jogador da vez: {jogador}')
        try:
            linha = int(input('Digite a linha (0-2): '))
            coluna = int(input('Digite a coluna (0-2): '))
        except ValueError:
            print('Digite apenas números inteiros!\n')
            continue

        if not jogada_valida(tabuleiro, linha, coluna):
            print('Jogada inválida! Tente novamente.\n')
            continue

        fazer_jogada(tabuleiro, linha, coluna, jogador)

        if verificar_ganhador(tabuleiro, jogador):
            exibir_tabuleiro(tabuleiro)
            print(f'🎉 Jogador {jogador} GANHOU!')
            break

        if verificar_empate(tabuleiro):
            exibir_tabuleiro(tabuleiro)
            print('🤝 Empate!')
            break

        jogador = alternar_jogador(jogador)

if __name__ == '__main__':
    main()
