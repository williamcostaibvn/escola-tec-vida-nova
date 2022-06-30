import random

import time

def mostra_pista(lista):
    for I in lista:
        print(I, end='')
    print()

def removeRepetidos(lista):
    naoRepetidosSet = set(lista)
    naoRepetidos = list(naoRepetidosSet)
    return naoRepetidos

def gerarLancamento(lista):
    lancamento = random.choices(lista, weights=[10, 10, 10, 10, 10, 10, 10, 10, 10, 10], k=10)
    lancamento = removeRepetidos(lancamento)

    for pino in lancamento:
        pista[pino] = ' '

pista = [
     'I', ' ', 'I', ' ', 'I', ' ', 'I', '\n', 
     ' ', 'I', ' ', 'I', ' ', 'I', ' ', '\n', 
     ' ', ' ', 'I', ' ', 'I', ' ', ' ', '\n', 
     ' ', ' ', ' ', 'I']

jogo = [27, 18, 20, 9, 11, 13, 0, 2, 4, 6]

mostra_pista(pista)

jogada1 = str(input('\nDeseja jogar a Primeira Bola (s/n)? '))
print()

result = ''

if(jogada1 == 's'):
    gerarLancamento(jogo)

else:
    exit()

mostra_pista(pista)

if(pista.count('I') == 1):
    print('\nFoi por pouco!!! Derrube o último pino para fazer um SPARE!\n')
    result = 'spare'
elif(pista.count('I') > 1):
    print(f'\nFoi por pouco!!! Derrube mais {pista.count("I")} pinos para fazer um SPARE!!!\n')
    result = 'spare'
else:
    print('SSSSS TTTTTTTT RRRRRR  II  KK  KK  EEEEE')
    time.sleep(0.5)
    print('SS       TT    RR  RR  II  KK KK   EE')
    time.sleep(0.5)
    print('SSSSS    TT    RRRRRR  II  KKKK    EEEE')
    time.sleep(0.5)
    print('   SS    TT    RR RR   II  KK KK   EE')
    time.sleep(0.5)
    print('SSSSS    TT    RR  RR  II  KK  KK  EEEEE')
    time.sleep(0.5)
    print('SHOWWWWWW... Você derrubou tudo... PARABÉNS!!!\n')
    exit()

if(result == 'spare'):
    jogada2 = str(input('Deseja jogar a Segunda Bola (s/n)? '))
    print()

    if(jogada2 == 's'):
        gerarLancamento(jogo)

    else:
        exit()

mostra_pista(pista)

if(pista.count('I') == 1):
    print('\nParabéns, só faltou 1 pino... Por pouco não foi um Spare!!!\n')

elif(pista.count('I') > 1):
    print(f'\nQuase heim... só sobraram {pista.count("I")} pinos!!!\n')
    
else:
    print('SSSSS  PPPPPP  AAAAAA  RRRRRR  EEEEE')
    time.sleep(0.5)
    print('SS     PP  PP  AA  AA  RR  RR  EE')
    time.sleep(0.5)
    print('SSSSS  PPPPPP  AAAAAA  RRRRRR  EEEE')
    time.sleep(0.5)
    print('   SS  PP      AA  AA  RR RR   EE')
    time.sleep(0.5)
    print('SSSSS  PP      AA  AA  RR  RR  EEEEE')
    time.sleep(0.5)
    print('\nWooowwww... Você fez um SPAREEEEE... PARABÉNS!!!\n')
