import random

def mostra_pista(pinos):
    for x in pinos:
        print(x, end='')
    print()

def remove_repetidos(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l

pista = [
     'I', ' ', 'I', ' ', 'I', ' ', 'I', '\n', 
     ' ', 'I', ' ', 'I', ' ', 'I', ' ', '\n', 
     ' ', ' ', 'I', ' ', 'I', ' ', ' ', '\n', 
     ' ', ' ', ' ', 'I']

posicao_dos_pinos = {
     '1' : 27,
     '2' : 18,
     '3' : 20,
     '4' : 9,
     '5' : 11,
     '6' : 13,
     '7' : 0,
     '8' : 2,
     '9' : 4,
     '10': 6
}

jogo = [27, 18, 20, 9, 11, 13, 0, 2, 4, 6]

jogada1 = str(input('\nDeseja jogar a Primeira Bola (s/n)? '))

result = ''

if(jogada1 == 's'):

    for x in range(1): 
        lancamento = random.choices(jogo, weights=[7, 8, 6, 8, 7, 8, 6, 8, 5, 10], k=10)
        lancamento = remove_repetidos(lancamento)

        for pino in lancamento:
            pista[pino] = ' '

else:
    exit()

mostra_pista(pista)

if('I' in pista):
    print('\nParabéns... você precisa derrubar', pista.count('I'),'pino(s) para fazer um SPARE\n')
    result = 'spare'
else:
    print('\nSTRIIIIIKE... Você derrubou tudo... PARABÉNS!!!\n')
    exit()

if(result == 'spare'):
    jogada2 = str(input('Deseja jogar a Segunda Bola (s/n)? '))

    if(jogada2 == 's'):

        for x in range(1): 
            lancamento2 = random.choices(jogo, weights=[5, 5, 6, 8, 4, 5, 4, 8, 5, 10], k=10)
            lancamento2 = remove_repetidos(lancamento2)

            for pino in lancamento2:
                pista[pino] = ' '

    else:
        exit()

    mostra_pista(pista)

if('I' in pista):
    print('\nQue pena, só faltou derrubar', pista.count('I'),'pino(s)\n')
    
else:
    print('\nWooowwww... Você fez um SPAREEEEE... PARABÉNS!!!\n')