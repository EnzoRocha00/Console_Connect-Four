# Enzo Rocha Portela - 190027282
# Desafio 1 - Ligue 4
# Resolvi fazer minhas próprias funções e personalizações
# SOMENTE PARA 2 JOGADORES

from os import system
from time import sleep

# Para IA dica usar Minimax
ALTURA = 6
LARGURA = 7
MATRIZ = []

VERMELHO = '\033[31m'
VERDE = '\033[32m'
AMARELO = '\033[33m'
BRANCO = '\033[m'

global Coords
Coords = list()

def Menu():
    print('='*13+'Ligue 4'+'='*13)
    print('-> 999-Sair')
    DrawLine()
    Show()

def DrawLine():
    print('='*33)

def SetMatrix(line=6, column=7):
    l = []
    for i in range(line):
        for j in range(column):
            l.append('0')
        MATRIZ.append(l.copy())
        l.clear()

def Show(line=6, column=7):
    for i in range(0,line):
        for j in range(0,column):
            if j == 0:
                print('\t', end='')
            if MATRIZ[i][j] == '1':
                print(VERMELHO, end='')
            elif MATRIZ[i][j] == '2':
                print(AMARELO, end='')
            else:
                print(BRANCO, end='')
            print(MATRIZ[i][j], end=' ')
            print(BRANCO, end='')
        print()
    print('\t^ ^ ^ ^ ^ ^ ^')
    print('\t1 2 3 4 5 6 7')
    print('='*33)

def GetOpc(player=int(1)):
    while True:
        try:
            opc = int(input(f'Player {player}: '))
            if (opc > 7 or opc < 1) and opc != 999:
                print('Digite uma coluna valida...')
                continue
        except:
            print('Erro de tipo...')
        else:
            break
    return opc

def CleanTerminal():
    system('cls')        

def Ending():
    print('Encerrando', end='')
    for i in range(3):
        print('.', end='', flush=True)
        sleep(1)

def UpdateMatrix(player = int(1), linha_opc = int(0), line=6, column=7):
    i = line-1
    while i < line:
        if i == -1:
            input('Coluna cheia...')
            return False
        valor = MATRIZ[i][linha_opc-1]
        if valor != '0':
            i-=1
            continue
        else:
            if player == 1:
                MATRIZ[i][linha_opc-1] = '1'
            else:
                MATRIZ[i][linha_opc-1] = '2'
            i = line-1
            return True

def Equal(n1, n2):
    if n1 == n2:
        return True
    else:
        return False

def Switch_Player(player):
    if player == 1:
        player = int(2)
    else:
        player = int(1)
    return player

def Check_H(player):
    result = False
    list_aux = list()
    for i in range(0, ALTURA):
        for j in range(0, LARGURA-3):
            if Equal(MATRIZ[i][j], str(player)) and (MATRIZ[i][j] == MATRIZ[i][j+1] == MATRIZ[i][j+2] == MATRIZ[i][j+3]):
                for aux in range(4):
                    list_aux.append(i)
                    list_aux.append(j+aux)
                    Coords.append(list_aux.copy())
                    list_aux.clear()
                result = True
                del list_aux
                break         
    return result

def Check_V(player):
    result = False
    list_aux = list()
    for i in range(0, ALTURA-3):
        for j in range(0, LARGURA):
            if Equal(MATRIZ[i][j], str(player)) and (MATRIZ[i][j] == MATRIZ[i+1][j] == MATRIZ[i+2][j] == MATRIZ[i+3][j]):
                for aux in range(4):
                    list_aux.append(i+aux)
                    list_aux.append(j)
                    Coords.append(list_aux.copy())
                    list_aux.clear()
                result = True
                del list_aux
                break         
    return result

def Check_D(player):
    list_aux = list()
    result = False
    for i in range(0, ALTURA-3):
        for j in range(0, LARGURA-3):
            if Equal(MATRIZ[i][j], str(player)) and (MATRIZ[i][j] == MATRIZ[i+1][j+1] == MATRIZ[i+2][j+2] == MATRIZ[i+3][j+3]):
                for aux in range(4):
                    list_aux.append(i+aux)
                    list_aux.append(j+aux)
                    Coords.append(list_aux.copy())
                    list_aux.clear()
                result = True
                del list_aux
                break
    for i in range(0, ALTURA - 3):
        for j in range(3, LARGURA):
            if Equal(MATRIZ[i][j], str(player)) and (MATRIZ[i][j] == MATRIZ[i+1][j-1] == MATRIZ[i+2][j-2] == MATRIZ[i+3][j-3]):
                for aux in range(4):
                    list_aux.append(i+aux)
                    list_aux.append(j-aux)
                    Coords.append(list_aux.copy())
                    list_aux.clear()
                result = True
                del list_aux
                break         
    return result
 
def Win(player):
    if (Check_V(player)):
        return True
    elif (Check_H(rotate)):
        return True
    elif (Check_D(rotate)):
        return True
    else:
        return False
    
def Tie():
    for i in range(ALTURA):
        for j in range(LARGURA):
            if MATRIZ[i][j] == '0':
                return False
    return True    
        
def SpecialShow(): 
    for i in range(0, ALTURA):
        for j in range(0, LARGURA):
            if j == 0:
                print('\t', end='')
            for c in Coords:
                if i == c[0] and j == c[1]:
                    print(VERDE, end='')    
                    break
                else:
                    print(BRANCO, end='')
            print(MATRIZ[i][j], end=' ')   
        print()
        
if __name__ == '__main__':

    SetMatrix()

    run = True
    rotate = int(1)
    
    while run:
        CleanTerminal()
        if Tie():
            DrawLine()
            Show()
            print('EMPATOU...')
            DrawLine()
            input('Digite qualquer tecla...')
            break
        
        Menu()  
        option = int(GetOpc(rotate))
        
        if(option==999):
            Ending()
            CleanTerminal()
            run = False 
        else:  
            if (UpdateMatrix(player=rotate,linha_opc=option)):
                if Win(rotate):
                    CleanTerminal()
                    DrawLine()
                    SpecialShow()
                    DrawLine()
                    print(f'Jogador {rotate} Ganhou!!!!!!!!')
                    DrawLine()
                    input('Digite qualquer tecla...')
                    break
                rotate = Switch_Player(rotate)
   
    CleanTerminal()    