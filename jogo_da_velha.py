# Requisitos
# Python 3.x

import os # Used to clear the screen

def jogador(tabuleiro):
    quantidade_x = 0
    quantidade_o = 0
    for i in tabuleiro:
        for j in i:
            if j == 'X':
                quantidade_x += 1
            elif j == 'O':
                quantidade_o += 1
    if quantidade_x > quantidade_o:
        return 'O'
    return 'X'

def acoes(tabuleiro):
    acoes_permitidas = []
    for row, i in enumerate(tabuleiro):
        for col, j in enumerate(i):
            if j == ' ':
                acoes_permitidas.append((row,col)) #row and column
    return acoes_permitidas

def resultado(tabuleiro, acao):
    row, col = acao
    novo_tabuleiro = [row[:] for row in tabuleiro] #making an "deep" copy of the matrix tabuleiro
    player_mark = jogador(tabuleiro)
    novo_tabuleiro[row][col] = player_mark
    return novo_tabuleiro

def ganhador(tabuleiro):
    rows_check = 0
    cols_check = [0,0,0]
    diagonal_check = [0,0]
    for i in tabuleiro:

        #checking the columns
        for k in range(3):
            if i[k] == 'X':
                cols_check[k] += 1
            if i[k] == 'O':
                cols_check[k] -= 1

        #checking the rows
        rows_check = 0
        for j in i:
            if j == 'X':
                rows_check += 1
            elif j == 'O':
                rows_check -= 1
        if rows_check == 3:
            return 'X'
        if rows_check == -3:
            return 'O'

    for k in range(3):
        if cols_check[k] == 3:
            return 'X'
        elif cols_check[k] == -3:
            return 'O'
        
    #checking the diagonal
    for i in range(3):
        if tabuleiro[i][i] == 'X':
            diagonal_check[0] += 1
        elif tabuleiro[i][i] == 'O':
            diagonal_check[0] -=1

        if tabuleiro[i][2-i] == 'X':
            diagonal_check[1] += 1
        elif tabuleiro[i][2-i] == 'O':
            diagonal_check[1] -= 1
    
    for i in range(2):
        if diagonal_check[i] == 3:
            return 'X'
        elif diagonal_check[i] == -3:
            return 'O'
    return ' '

def final(tabuleiro):
    win = ganhador(tabuleiro)
    end = True
    for i in tabuleiro:
        for j in i:
            if j == ' ':
                end = False

    if end or win != ' ': # If there are no more free positions or someone wins
        return True
    return False

def custo(tabuleiro):
    win = ganhador(tabuleiro)
    if win == 'X':
        return 1
    elif win == 'O':
        return -1
    return 0


def maxValor(tabuleiro):
    if final(tabuleiro) == False:
        valor_escolhido = -2
        acoes_permitidas = acoes(tabuleiro)
        for acao in acoes_permitidas:
            valor_retorno = minValor(resultado(tabuleiro, acao))
            if valor_retorno > valor_escolhido:
                valor_escolhido = valor_retorno
        return valor_escolhido
    else:
        return custo(tabuleiro)

def minValor(tabuleiro):
    if final(tabuleiro) == False:
        valor_escolhido = 2
        acoes_permitidas = acoes(tabuleiro)
        for acao in acoes_permitidas:
            valor_retorno = maxValor(resultado(tabuleiro, acao))
            if valor_retorno < valor_escolhido:
                valor_escolhido = valor_retorno
        return valor_escolhido
    else:
        return custo(tabuleiro)

def minimax(tabuleiro):
    player = jogador(tabuleiro)
    if player == 'X':
        acao_escolhida = None
        valor_escolhido = -2
        for acao in acoes(tabuleiro):
            valor_retorno = minValor(resultado(tabuleiro, acao))
            if valor_retorno > valor_escolhido:
                valor_escolhido = valor_retorno
                acao_escolhida = acao
        return acao_escolhida
    elif player == 'O':
        acao_escolhida = None
        valor_escolhido = 2
        for acao in acoes(tabuleiro):
            valor_retorno = maxValor(resultado(tabuleiro, acao))
            if valor_retorno < valor_escolhido:
                valor_escolhido = valor_retorno
                acao_escolhida = acao
        return acao_escolhida


def mostrarTabuleiro(tabuleiro):
    print("      1   2   3")
    print()
    for i_index, i in enumerate(tabuleiro):
        print(i_index+1,"  | ", end='')
        for j in i:
            print(j,"| ", end='')
        print()
        print("    -------------")


def game():
    tabuleiro = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    player = input("Escolha a sua peça (o X sempre começa): Digite X ou O: ")
    while(not final(tabuleiro)):
        os.system('cls' if os.name == 'nt' else 'clear')
        mostrarTabuleiro(tabuleiro)
        turno = jogador(tabuleiro)
        if turno == player:
            row = input("digite a linha:")
            col = input("digite a coluna:")
            tabuleiro[int(row)-1][int(col)-1] = turno
        else:
            acao = minimax(tabuleiro)
            row, col = acao
            tabuleiro[row][col] = turno
    os.system('cls' if os.name == 'nt' else 'clear')
    mostrarTabuleiro(tabuleiro)
    if custo(tabuleiro) == 1:
        print('X é o ganhador!')
    elif custo(tabuleiro) == -1:
        print('O é o ganhador!')
    else:
        print('Empate!')