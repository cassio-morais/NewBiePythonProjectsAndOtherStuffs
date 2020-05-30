from random import randint
import os
import time


jogo = [['   ','   ','   '],['   ','   ','   '],['   ','   ','   ']]
gabarito =  [[' 7 ',' 8 ',' 9 '],[' 4 ',' 5 ',' 6 '],[' 1 ',' 2 ',' 3 ']]


def mostrajogo(jogo): 

    os.system('cls')
    mostra = ''
    mostragab = ''
    for i in range(3):
        for j in range(3):
            mostra += jogo[i][j]+'|'
            for h in range(3):
                mostragab += gabarito[j][h]+'|'
    print('''         
        JOGO DA VELHA
Você é o 'X', a máquina é o 'O' 
    
''',
mostra[0:11],'''    ''',mostragab[0:11],
'''                                   
-----------      -----------
''',
mostra[12:22],'''     ''',mostragab[12:22],
'''
-----------      -----------
''',
mostra[24:35],'''    ''',mostragab[24:35],'''
''')     

def jogadaM():

    jogada = randint(1,9)
    return jogada


def jogadaJ():

    print('-'*30)
    jogada = ''
    while type(jogada) != int:
        try:
            jogada = int(input('Sua vez: '))
        except ValueError:
            print('Digite um número!')
            time.sleep(1)
            mostrajogo(jogo)
    return jogada


def vencedor(jogo):
    maquina = 'maquina'
    pessoa = 'pessoa'

    if jogo[0][0:3] == [' O ',' O ',' O ']: 
        return maquina

    elif jogo[1][0:3] == [' O ',' O ',' O ']: 
        return maquina
        
    elif jogo[2][0:3] == [' O ',' O ',' O ']: 
        return maquina
        
    elif jogo[0][0] ==' O ' and jogo[1][0]==' O ' and jogo[2][0]==' O ':
        return maquina

    elif jogo[0][1] ==' O ' and jogo[1][1]==' O ' and jogo[2][1]==' O ':
        return maquina

    elif jogo[0][2] ==' O ' and jogo[1][2]==' O ' and jogo[2][2]==' O ':
        return maquina
        
    elif jogo[0][0] ==' O ' and jogo[1][1]==' O ' and jogo[2][2]==' O ':
        return maquina

    elif jogo[0][2] ==' O ' and jogo[1][1]==' O ' and jogo[2][0]==' O ':
        return maquina
    
    elif jogo[0][0:3] == [' X ',' X ',' X ']:
        return pessoa
    
    elif jogo[1][0:3] == [' X ',' X ',' X ']: 
        return pessoa
        
    elif jogo[2][0:3] == [' X ',' X ',' X ']: 
        return pessoa
        
    elif jogo[0][0] ==' X ' and jogo[1][0]==' X ' and jogo[2][0]==' X ':
        return pessoa

    elif jogo[0][1] ==' X ' and jogo[1][1]==' X ' and jogo[2][1]==' X ':
        return pessoa

    elif jogo[0][2] ==' X ' and jogo[1][2]==' X ' and jogo[2][2]==' X ':
        return pessoa
        
    elif jogo[0][0] ==' X ' and jogo[1][1]==' X ' and jogo[2][2]==' X ':
        return pessoa

    elif jogo[0][2] ==' X ' and jogo[1][1]==' X ' and jogo[2][0]==' X ':
        return pessoa

    else:
        pass


vitoriasMaquina = vitoriasPessoa = QuantJogadas = empates = 0
vez = 'maquina'
while True: 

    alguemVenceu = vencedor(jogo)

    if alguemVenceu == 'pessoa':
        mostrajogo(jogo)
        print('-'*30)
        ganhador = 'VOCÊ VENCEU!'
        print(f'{ganhador:^30}')
        print('-'*30)
        vitoriasPessoa+=1
        vez = 'fim'
    
    elif alguemVenceu == 'maquina':
        mostrajogo(jogo)
        print('-'*30)
        ganhador = 'A MÁQUINA VENCEU!'
        print(f'{ganhador:^30}')
        print('-'*30)
        vitoriasMaquina+=1
        vez = 'fim'

    elif QuantJogadas == 9:
        (mostrajogo(jogo))
        empate = 'DEU EMPATE'
        print('-'*30)
        print(f'{empate:^30}')
        print('-'*30)
        empates+=1
        vez = 'fim'
        
    if vez == 'maquina':

        jogadaMaquina = jogadaM()
        if jogadaMaquina == 1:
            if jogo[2][0] == ' X ' or jogo[2][0] == ' O ':
                continue
            else:
                jogo[2][0] = ' O '
                vez = 'jogador'
                QuantJogadas+=1
        if jogadaMaquina == 2:
            if jogo[2][1] == ' X ' or jogo[2][1] == ' O ':
                continue
            else:
                jogo[2][1] = ' O '
                vez = 'jogador'
                QuantJogadas+=1
        if jogadaMaquina == 3:
            if jogo[2][2] == ' X ' or jogo[2][2] == ' O ':
                continue
            else:
                jogo[2][2] = ' O '
                vez = 'jogador'
                QuantJogadas+=1
        if jogadaMaquina == 4:
            if jogo[1][0] == ' X ' or jogo[1][0] == ' O ':
                continue
            else:
                jogo[1][0] = ' O '
                vez = 'jogador'
                QuantJogadas+=1
        if jogadaMaquina == 5:
            if jogo[1][1] == ' X ' or jogo[1][1] == ' O ':
                continue
            else:
                jogo[1][1] = ' O '
                vez = 'jogador'
                QuantJogadas+=1
        if jogadaMaquina == 6:
            if jogo[1][2] == ' X ' or jogo[1][2] == ' O ':
                continue
            else:
                jogo[1][2] = ' O '
                vez = 'jogador'
                QuantJogadas+=1
        if jogadaMaquina == 7:
            if jogo[0][0] == ' X ' or jogo[0][0] == ' O ':
                continue
            else:
                jogo[0][0] = ' O '
                vez = 'jogador'
                QuantJogadas+=1
        if jogadaMaquina == 8:
            if jogo[0][1] == ' X ' or jogo[0][1] == ' O ':
                continue
            else:
                jogo[0][1] = ' O '
                vez = 'jogador'
                QuantJogadas+=1
        if jogadaMaquina == 9:
            if jogo[0][2] == ' X ' or jogo[0][2] == ' O ':
                continue
            else:
                jogo[0][2] = ' O '
                vez = 'jogador'
                QuantJogadas+=1

    alguemVenceu = vencedor(jogo)

    if alguemVenceu == 'pessoa':
        mostrajogo(jogo)
        print('-'*30)
        ganhador = 'VOCÊ VENCEU!'
        print(f'{ganhador:^30}')
        print('-'*30)
        vitoriasPessoa+=1
        vez = 'fim'
        
    elif alguemVenceu == 'maquina':
        mostrajogo(jogo)
        print('-'*30)
        ganhador = 'A MÁQUINA VENCEU!'
        print(f'{ganhador:^30}')
        print('-'*30)
        vitoriasMaquina+=1
        vez = 'fim'

    elif QuantJogadas == 9:
        (mostrajogo(jogo))
        empate = 'DEU EMPATE'
        print('-'*30)
        print(f'{empate:^30}')
        print('-'*30)
        empates+=1
        vez = 'fim'
     
    if vez == 'jogador':

        time.sleep(0.5)
        mostrajogo(jogo)
        jogadaJogador = jogadaJ()
        if jogadaJogador == 1:
            if jogo[2][0] == ' X ' or jogo[2][0] == ' O ':
                    print('Faça sua jogada novamente!')
                    continue
            else:
                jogo[2][0] = ' X '
                vez = 'maquina'
                QuantJogadas+=1
        if jogadaJogador == 2:
            if jogo[2][1] == ' X ' or jogo[2][1] == ' O ':
                    print('Faça sua jogada novamente!')
                    continue
            else:
                jogo[2][1] = ' X '
                vez = 'maquina'
                QuantJogadas+=1
        if jogadaJogador == 3:
            if jogo[2][2] == ' X ' or jogo[2][2] == ' O ':
                    print('Faça sua jogada novamente!')
                    continue
            else:
                jogo[2][2] = ' X '
                vez = 'maquina'
                QuantJogadas+=1
        if jogadaJogador == 4:
            if jogo[1][0] == ' X ' or jogo[1][0] == ' O ':
                    print('Faça sua jogada novamente!')
                    continue
            else:
                jogo[1][0] = ' X '
                vez = 'maquina'
                QuantJogadas+=1
        if jogadaJogador == 5:
            if jogo[1][1] == ' X ' or jogo[1][1] == ' O ':
                    print('Faça sua jogada novamente!')
                    continue
            else:
                jogo[1][1] = ' X '
                vez = 'maquina'
                QuantJogadas+=1
        if jogadaJogador == 6:
            if jogo[1][2] == ' X ' or jogo[1][2] == ' O ':
                    print('Faça sua jogada novamente!')
                    continue
            else:
                jogo[1][2] = ' X '
                vez = 'maquina'
                QuantJogadas+=1
        if jogadaJogador == 7:
            if jogo[0][0] ==  ' X ' or jogo[0][0] == ' O ':
                    print('Faça sua jogada novamente!')
                    continue
            else:
                jogo[0][0] = ' X '
                vez = 'maquina'
                QuantJogadas+=1
        if jogadaJogador == 8:
            if jogo[0][1] == ' X ' or jogo[0][1] == ' O ':
                    print('Faça sua jogada novamente!')
                    continue
            else:
                jogo[0][1] = ' X '
                vez = 'maquina'
                QuantJogadas+=1
        if jogadaJogador == 9:
            if jogo[0][2] == ' X ' or jogo[0][2] == ' O ':
                    print('Faça sua jogada novamente!')
                    continue
            else:
                jogo[0][2] = ' X '
                vez = 'maquina'
                QuantJogadas+=1

    alguemVenceu = vencedor(jogo)

    if alguemVenceu == 'pessoa':
        mostrajogo(jogo)
        print('-'*30)
        ganhador = 'VOCÊ VENCEU!'
        print(f'{ganhador:^30}')
        vitoriasPessoa+=1
        print('-'*30)
        vez = 'fim'      

    elif alguemVenceu == 'maquina':
        (mostrajogo(jogo))
        print('-'*30)
        ganhador = 'A MÁQUINA VENCEU!'
        print(f'{ganhador:^30}')
        print('-'*30)
        vitoriasMaquina+=1
        vez = 'fim'       

    elif QuantJogadas == 9:
        (mostrajogo(jogo))
        empate = 'DEU EMPATE'
        print('-'*30)
        print(f'{empate:^30}')
        print('-'*30)
        empates+=1
        vez = 'fim'
       

    if vez == 'fim':
        FicaOuSai = input('Gostaria de continua? S|N ').upper()
        if FicaOuSai == 'S':
            jogo = [['   ','   ','   '],['   ','   ','   '],['   ','   ','   ']]
            vitoriasMaquina = vitoriasPessoa = QuantJogadas = empates = 0
            vez = 'maquina'
            continue
        elif FicaOuSai == 'N':
            os.system('cls')
            print('-'*30)
            fimdejogo = 'FIM DE JOGO!'
            print(f'{fimdejogo:^30}')
            print('-'*30)
            print(f'Você venceu {vitoriasPessoa} vezes!')
            print(f'A máquina venceu {vitoriasMaquina} vezes!')
            print(f'Houve {empates} empates!')
            print('-'*30)
            input()
            break

        else:
            vez = 'fim'

        
        