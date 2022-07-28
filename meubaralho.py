import random
import time

class Carta:

    def __init__(self, valor, naipe):
        self.valorCarta = [None, 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Q', 'J', 'K']

        self.dictValor = {'A' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9, '10': 10, 'Q' : 11, 'J' : 12, 'K' : 13}

        self.naipe_unicode = {'P' : '\u2663', 'C' : '\u2665', 'E' : '\u2660', 'O' : '\u2666'}
        
        self.valida_carta(valor, naipe)
        if type(valor) == int:
            self.valor = valor
        elif type(valor) == str:
            self.valor = self.dictValor[valor]
        self.naipe = naipe
        self.mostrar()

    def valida_carta(self, valor, naipe):
        if type(valor) == int:
            valor = self.valorCarta[valor]
            if valor not in self.valorCarta:
                raise Exception(f'Este valor não é um valor aceito: {valor}')
            if naipe not in self.naipe_unicode.keys():
                raise Exception(f'Este naipe não é um naipe aceito: {self.naipe_unicode[naipe]}')
        elif type(valor) == str:
            self.valor = self.dictValor[valor]
            if valor not in self.valorCarta:
                raise Exception(f'Este valor não é um valor aceito: {valor}')
            if naipe not in self.naipe_unicode.keys():
                raise Exception(f'Este naipe não é um naipe aceito: {self.naipe_unicode[naipe]}')

    def mostrar(self):
        print('\u2554\u2550\u2550\u2550\u2557')
        if len(self.valorCarta[self.valor]) == 1: print(f'\u2551 {self.valorCarta[self.valor]} \u2551')
        else: print(f'\u2551{self.valorCarta[self.valor]} \u2551')
        print('\u2560\u2550\u2550\u2550\u2563')
        print(f'\u2551 {self.naipe_unicode[self.naipe]} \u2551')
        print('\u255A\u2550\u2550\u2550\u255D')

    def __str__(self):
        naipe_unicode = self.naipe_unicode[self.naipe]
        return f'{self.valor}{naipe_unicode}'
    
    def __eq__(self, outro):
        print('\nAs cartas são IGUAIS?')
        return self.valor == outro
    
    def __lt__(self, outro):
        print('\nCarta do JOGADOR é MENOR que Carta do COMPUTADOR?')
        return self.valor < outro
    
    def __gt__(self, outro):
        print('\nCarta do JOGADOR é MAIOR que Carta do COMPUTADOR?')
        return self.valor > outro


class Baralho:

    def __init__(self):
        self.valorCarta = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.valorCarta_str = [None, 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Q', 'J', 'K']
        self.naipes = ['P', 'C', 'E', 'O']

        self.cartas = []

        self.baralhoCompleto = {}

        for y in self.valorCarta:
            for x in self.naipes:
                naipe = self.valorCarta_str[y]
                carta = naipe+x
                self.cartas.append(carta)

        for carta in self.cartas:
            listaCartas = []
            if len(carta) == 2:
                valor = self.valorCarta_str.index(carta[0])
                listaCartas.append(int(valor))
                listaCartas.append(str(carta[1]))
                self.baralhoCompleto[carta] = listaCartas
            else:
                valor = self.valorCarta_str.index(carta[0]+carta[1])
                listaCartas.append(int(valor))
                listaCartas.append(str(carta[2]))
                self.baralhoCompleto[carta] = listaCartas

    def monstrarBaralho(self, baralho):
        for c in baralho:
            Carta(self.baralhoCompleto[c][0], self.baralhoCompleto[c][1])
        
    def embaralhar(self):
        random.shuffle(self.cartas)
    
    def darCarta(self):
        self.last = self.cartas.pop()
        return self.last

    def devolverCarta(self, carta):
        if carta not in self.cartas:
            self.cartas.append(carta)

if __name__ == '__main__':

    # valor = input('Informe o valor da sua carta (Ex.: "2 a 10" ou "A / Q / J / K"): ')
    # valor = valor.title()

    # naipe = input("Informe o naipe da sua carta (somente a primeira letra - Ex.: 'P'aus, 'C'opas, 'E'spadas, 'O'uros): ")
    # naipe = naipe.title()

    # x = Carta(valor, naipe)

    dictValor = {'A' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9, '10': 10, 'Q' : 11, 'J' : 12, 'K' : 13}

    jogador1 = input('\nQual seu nome? ')

    if jogador1 == '':
        jogador1 = 'MONSTRO DO ZAP'

    input(f'\n{jogador1}, pressione a tecla <ENTER> para Iniciar')

    jogo = Baralho()

    print('\nGerando Baralho Francês de 52 Cartas...      0%')
    time.sleep(0.5)
    print('Gerando as Cartas do Naipe de PAUS(\u2663)...    25%')
    time.sleep(0.5)
    print('Gerando as Cartas do Naipe de COPAS(\u2665)...   50%')
    time.sleep(0.5)
    print('Gerando as Cartas do Naipe de ESPADAS(\u2660)... 75%')
    time.sleep(0.5)
    print('Gerando as Cartas do Naipe de OUROS(\u2666)...  100%')
    print('\nBaralho Francês gerado com sucesso!!!')
    time.sleep(0.5)

    # Embaralhar as cartas (random.shuffle)
    print('\nEmbaralhando as Cartas...')
    jogo.embaralhar()
    time.sleep(1.0)

    # Dar as cartas aos jogadores
    print('\nDistribuindo as CARTAS para os jogadores!')
    time.sleep(0.5)

    cartasJogador = []

    cartasComputador = []

    for index in range(3):

        carta = jogo.darCarta()

        cartasJogador.append(carta)

        carta = jogo.darCarta()

        cartasComputador.append(carta)

    partidas = 0

    vitoriaJogador = 0

    vitoriaComputador = 0

    # Iniciando o jogo de 3 rodadas

    print('\nEssas são as cartas do COMPUTADOR: ')

    versoCarta = 0
    
    while versoCarta < 3:
        print('\u2554\u2550\u2550\u2550\u2557')
        print('\u2551\u2663 \u2665\u2551')
        print('\u2560\u2550\u2550\u2550\u2563')
        print('\u2551\u2660 \u2666\u2551')
        print('\u255A\u2550\u2550\u2550\u255D')
        versoCarta += 1

    print(f'\n{jogador1}, essas são as suas cartas: ')
    jogo.monstrarBaralho(cartasJogador)

    while partidas < 3:

        print('\n-------------------------------------------------------------\n')

        while True:
            try:
                jogada = int(input('Qual carta deseja jogar (1, 2 ou 3): '))
                if jogada == 1:
                    teste = 0
                elif jogada == 2:
                    teste = 1
                elif jogada == 3:
                    teste = 2

                if cartasJogador[teste] == None:
                    raise ValueError()
            except ValueError:
                print('\nATENÇÃO... Esta carta já foi jogada ou não existe, escolha outra!')
            else:
                break

        descartarJogador = []

        descartarPC = []

        # Selecionando a carta escolhido na lista cartasJogador

        if jogada == 1:
            descartarJogador.append(cartasJogador[0])
        elif jogada == 2:
            descartarJogador.append(cartasJogador[1])
        elif jogada == 3:
            descartarJogador.append(cartasJogador[2])

        if len(descartarJogador[0]) == 2:
            valorCartaJogador = dictValor[descartarJogador[0][0]]
        elif len(descartarJogador[0]) == 3:
            valorCartaJogador = descartarJogador[0][0]+descartarJogador[0][1]

        valorCartaJogador = int(valorCartaJogador)

        # Imprimindo a carta escolhida

        print(f'\nCarta {jogada}:')

        if len(descartarJogador[0]) == 2:
            valorCartaJogador = dictValor[descartarJogador[0][0]]
            naipeCartaJogador = descartarJogador[0][1]
            jogador = Carta(valorCartaJogador, naipeCartaJogador)

        elif len(descartarJogador[0]) == 3:
            valorCartaJogador = descartarJogador[0][0]+descartarJogador[0][1]
            naipeCartaJogador = descartarJogador[0][2]
            jogador = Carta(valorCartaJogador, naipeCartaJogador)

        # Removendo carta selecinada da lista cartasJogador

        if jogada == 1:
            jogada = 0
        elif jogada == 2:
            jogada = 1
        elif jogada == 3:
            jogada = 2

        cartasJogador[jogada] = None
        
        # Jogada do Computador, sempre a ultima carta da lista cartasComputador

        print('\nJogada do COMPUTADOR: ')

        descartarPC.append(cartasComputador.pop())

        # Imprimindo a carta jogada pelo Computador

        if len(descartarPC[0]) == 2:
            valorCartaPC = dictValor[descartarPC[0][0]]
            naipeCartaPC = descartarPC[0][1]
            pc = Carta(valorCartaPC, naipeCartaPC)

        elif len(descartarPC[0]) == 3:
            valorCartaPC = descartarPC[0][0]+descartarPC[0][1]
            naipeCartaPC = descartarPC[0][2]
            pc = Carta(valorCartaPC, naipeCartaPC)

        valorCartaPC = int(valorCartaPC)

        # Validando a vitória na partida

        print('\n-------------------------------------------------------------')

        if int(valorCartaJogador) > int(valorCartaPC):
            print(f'\nRESULTADO: 1 ponto para {jogador1}!')
            vitoriaJogador += 1
        
        elif int(valorCartaJogador) < int(valorCartaPC):
            print('\nRESULTADO: 1 ponto para o COMPUTADOR!')
            vitoriaComputador += 1
        
        elif int(valorCartaJogador) == int(valorCartaPC):
            print('\nRESULTADO: EMPATE!')

        partidas += 1
    
    print('\n-------------------------------------------------------------')

    print(f'\nResultado do Jogo:\n{jogador1} venceu {vitoriaJogador} partida(s)\nCOMPUTADOR venceu {vitoriaComputador} partida(s)\n')
    
    if vitoriaJogador > vitoriaComputador:
        print(f'\nPARABÉNS, {jogador1}.... Você venceu o JOGO!!!')
        print('You are the Champion, my friend!!!')

    elif vitoriaJogador < vitoriaComputador:
        print(f'\nPERDEU, {jogador1}.... O COMPUTADOR venceu o JOGO!!!')
        print('Don\'t cry... :(')

    else:
        print('\nDeu EMPATE.... Jogue novamente até vencer o JOGO!!!')
        print('"Nem quem ganhar, nem quem perder, vai ganhar ou vai perder!')
        print(' Todo mundo vai PERDER... hehehehehehehe"')
        print(' (by ex-Presidenta Dilma Rousseff) :D')
    
    print('\n\n')