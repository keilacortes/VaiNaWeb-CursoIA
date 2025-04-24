import math

tabuleiro = [' '] * 9

# função para exibir o tabuleiro
def exibir_tabuleiro(tabuleiro):
    print("\nTabuleiro Atual:")
    print(" " + tabuleiro[0] + " | " + tabuleiro[1] + " | " + tabuleiro[2])
    print("-----------")
    print(" " + tabuleiro[3] + " | " + tabuleiro[4] + " | " + tabuleiro[5])
    print("-----------")
    print(" " + tabuleiro[6] + " | " + tabuleiro[7] + " | " + tabuleiro[8])

# função para verificar vencedor
def verificar_vencedor(tabuleiro, jogador):
    combinacoes_vencedoras = [
        # horizontais
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        # verticais
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        # diagonais
        (0, 4, 8), (2, 4, 6)
    ]
    for combinacao in combinacoes_vencedoras:
        idx1, idx2, idx3 = combinacao
        if tabuleiro[idx1] == jogador and tabuleiro[idx2] == jogador and tabuleiro[idx3] == jogador:
            return True
    return False 

# função para verificar empate
def verificar_empate(tabuleiro):
    return ' ' not in tabuleiro

# função Minimax
def minimax(tabuleiro, profundidade, maximizando):
    if verificar_vencedor(tabuleiro, 'X'):
        return -10 + profundidade
    if verificar_vencedor(tabuleiro, 'O'):
        return 10 - profundidade
    if verificar_empate(tabuleiro):
        return 0

    if maximizando:
        melhor_valor = -math.inf
        for i in range(9):
            if tabuleiro[i] == ' ':
                tabuleiro[i] = 'O'
                valor = minimax(tabuleiro, profundidade + 1, False)
                tabuleiro[i] = ' '
                melhor_valor = max(melhor_valor, valor)
        return melhor_valor

    else:
        melhor_valor = math.inf
        for i in range(9):
            if tabuleiro[i] == ' ':
                tabuleiro[i] = 'X'
                valor = minimax(tabuleiro, profundidade + 1, True)
                tabuleiro[i] = ' '
                melhor_valor = min(melhor_valor, valor)
        return melhor_valor

def melhor_jogada(tabuleiro):
    melhor_valor = -math.inf
    melhor_posicao = -1
    
    for i in range(9):
        if tabuleiro[i] == ' ':
            tabuleiro[i] = 'O'
            
            valor = minimax(tabuleiro, 0, False)
            
            tabuleiro[i] = ' '
            
            if valor > melhor_valor:
                melhor_valor = valor
                melhor_posicao = i
                
    return melhor_posicao

def jogar_jogo():
    while True:
        exibir_tabuleiro(tabuleiro)
        
        while True:
            try:
                jogada = int(input("\nDigite sua jogada (0-8): "))
                if 0 <= jogada <= 8 and tabuleiro[jogada] == ' ':
                    break
                else:
                    print("Posição inválida ou ocupada. Tente novamente.")
            except ValueError:
                print("Por favor, digite um número entre 0 e 8.")
        
        tabuleiro[jogada] = 'X'
        
        if verificar_vencedor(tabuleiro, 'X'):
            exibir_tabuleiro(tabuleiro)
            print("\nParabéns! Você venceu!")
            break
            
        if verificar_empate(tabuleiro):
            exibir_tabuleiro(tabuleiro)
            print("\nEmpate!")
            break
            
        print("\nComputador está pensando...")
        melhor_posicao = melhor_jogada(tabuleiro)
        tabuleiro[melhor_posicao] = 'O'
        
        if verificar_vencedor(tabuleiro, 'O'):
            exibir_tabuleiro(tabuleiro)
            print("\nO computador venceu!")
            break
            
        if verificar_empate(tabuleiro):
            exibir_tabuleiro(tabuleiro)
            print("\nEmpate!")
            break

if __name__ == "__main__":
    print("Bem-vindo ao Jogo da Velha com Minimax!")
    print("Posições do tabuleiro:")
    print(" 0 | 1 | 2 ")
    print("---+---+---")
    print(" 3 | 4 | 5 ")
    print("---+---+---")
    print(" 6 | 7 | 8 ")
    print("\nVocê joga como 'X'.")
    jogar_jogo()
    print("\nFim do jogo!")