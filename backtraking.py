# imprime o tabuleiro
def mostrar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print("| " + " | ".join(linha) + " |")

# verifica se um movimento é válido
def movimento_valido(tabuleiro, linha, coluna):
    num_linhas = len(tabuleiro)
    num_colunas = len(tabuleiro[0])
    if (num_linhas > linha >= 0) and (num_colunas > coluna >= 0) and (tabuleiro[linha][coluna] not in ['X', '*']):
        return True
    else:
        return False

# verifica se chegou ao destino
def chegou_destino(linha, coluna, linha_destino, coluna_destino):
    return (linha == linha_destino) and (coluna == coluna_destino)

# função recursiva principal do backtracking
def proximo_movimento(tabuleiro, linha_atual, coluna_atual, profundidade, linha_destino, coluna_destino, caminho_atual, melhor_caminho):
    melhor_profundidade = float('inf')
    melhor_linha = linha_atual
    melhor_coluna = coluna_atual
    direcoes = [
        (0, 1), # direita
        (0, -1), # esquerda
        (1, 0), # baixo
        (-1, 0) # cima
    ]

     # se chegamos ao destino
    if chegou_destino(linha_atual, coluna_atual, linha_destino, coluna_destino):
        # se encontramos um caminho melhor
        if len(melhor_caminho[0]) == 0 or len(caminho_atual) < len(melhor_caminho[0]):
            melhor_caminho[0] = caminho_atual.copy()
        return (linha_atual, coluna_atual, len(caminho_atual)-1)

    # explora todas as direções possíveis
    for dr, dc in direcoes:
        nova_linha = linha_atual + dr
        nova_coluna = coluna_atual + dc

        if movimento_valido(tabuleiro, nova_linha, nova_coluna):
            # marca a posição como visitada
            tabuleiro[nova_linha][nova_coluna] = '*'
            caminho_atual.append((nova_linha, nova_coluna))
            
            # se o caminho atual já é maior que o melhor caminho encontrado, não continua
            if len(melhor_caminho[0]) > 0 and len(caminho_atual) >= len(melhor_caminho[0]):
                tabuleiro[nova_linha][nova_coluna] = ' '
                caminho_atual.pop()
                continue
            
            # chama recursivamente
            resultado = proximo_movimento(tabuleiro, nova_linha, nova_coluna, profundidade + 1, 
                            linha_destino, coluna_destino, caminho_atual, melhor_caminho)
            
            # desmarca a posição
            tabuleiro[nova_linha][nova_coluna] = ' '
            caminho_atual.pop()
    if len(melhor_caminho[0]) > 0:
        return (melhor_caminho[0][-1][0], melhor_caminho[0][-1][1], len(melhor_caminho[0])-1)
    else:
        return (linha_atual, coluna_atual, float('inf'))

# função principal
def main():
    # definir tabuleiro
    N = 5 # tabuleiro 5x5
    tabuleiro = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', 'X', 'X', 'X', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', 'X', ' ', 'X', ' '],
        [' ', ' ', ' ', ' ', ' ']
    ]

    # define início e fim
    linha_inicial, coluna_inicial = 4, 0
    linha_final, coluna_final = 0, 4

    # marca início e destino
    tabuleiro[linha_inicial][coluna_inicial] = '*'
    tabuleiro[linha_final][coluna_final] = '#'

    # mostra tabuleiro inicial
    print("Tabuleiro Inicial:")
    mostrar_tabuleiro(tabuleiro)

    # inicializa para armazenar o melhor caminho
    melhor_caminho = [[]]
    caminho_atual = [(linha_inicial, coluna_inicial)]

    # chama função backtracking
    final_l, final_c, final_profundidade = proximo_movimento(
        tabuleiro,
        linha_inicial,
        coluna_inicial,
        0,
        linha_final,
        coluna_final,
        caminho_atual,
        melhor_caminho
    )

    # interpreta e mostrar o resultado
    print("\n--- Resultado ---")
    if final_profundidade == float('inf'):
        print("Não foi encontrado um caminho para o destino.")
    else:
        print(f"Caminho encontrado com {final_profundidade} passos!")
        
        # marca o caminho no tabuleiro
        for passo in range(1, len(melhor_caminho[0])):
            linha, coluna = melhor_caminho[0][passo]
            tabuleiro[linha][coluna] = '*'
        
        print("\nTabuleiro com Caminho Marcado:")
        mostrar_tabuleiro(tabuleiro)

if __name__ == "__main__":
    main()