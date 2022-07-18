import random

class Adversario:

    def __init__(self) -> None:
        self.nome = input('\nQual seu nome? ')
        
        self.nome = self.nome.upper()

    def par_ou_impar(self):

        # Usuário escolhendo "Par ou Impar"
        while True:
                try:
                    user = input('Escolha PAR ou IMPAR: ')
                    user = user.upper()
                    print()
                    if not (user == 'PAR' or user == 'IMPAR'):
                        raise ValueError()
                except ValueError:
                    print('Você deve digitar "PAR" ou "IMPAR"!')
                else:
                    break

        # Usuário escolhendo o número para jogar (0 a 5)
        while True:
                try:
                    userNumber = int(input('Digite um número de 0 a 5: '))
                    print()
                    if (userNumber > 5):
                        raise ValueError()
                except ValueError:
                    print('Escolha um número entre 0 e 5!\n')
                else:
                    break

        # Computador escolhendo aleatoriamente o número para jogar (0 a 5)
        listaNumeros = [0, 1, 2, 3, 4, 5]

        systemNumber = random.choices(listaNumeros)

        # Soma dos numeros (usuario e computador)
        soma = userNumber + systemNumber[0]

        # Imprimindo resultado da partida
        print(f'Seu número:           {userNumber}')
        print(f'Número do Computador: {systemNumber[0]}')
        print(f'Resultado:            {soma}')
        print()

        if (soma % 2) == 0:
            resultado = 'PAR'
        else:
            resultado = 'IMPAR'

        if (resultado == user):
            print('Você GANHOU essa partida!')
            print('-------------------------\n')
            return 0
        else:
            print('Você PERDEU essa partida!')
            print('-------------------------\n')
            return 1

    def campeonato(self):
        
        print(f'\n{self.nome}, vamos disputar um campeonato de PAR ou IMPAR!!!\n')
        
        #Defindo número de partidas
        numPartidas = int(input('Quantas partidas deseja disputar: '))
        print('\n-------------------------')
        
        jogadas = 0

        resultados = []

        # Laço para execução de todas as partidas do campeonato
        while not jogadas == numPartidas:

            for n in range(0, numPartidas):
                partida = self.par_ou_impar()

                jogadas += 1

                if partida == 0:
                    resultados.append(0)

                else:
                    resultados.append(1)
        
        zeros = 0

        uns = 0

        # Contador de vitórias de cada jogador (Usuário/Computador)
        for i in resultados:
            if resultados[i] == 0:
                zeros += 1
            elif resultados[i] == 1:
                uns += 1

        # Relatório do Campeonato
        print(f'\nJogamos {numPartidas} partida(s)')
        print(f'\nVocê ganhou {zeros} partida(s)')
        print(f'\nEu ganhei {uns} partida(s)')

        # Declaração do Vencedor
        if zeros > uns:
            print(f'\nPARABÉNS, {self.nome}, você venceu este Campeonato!!!\n')
        elif zeros < uns:
            print(f'\nÉ {self.nome}, desta vez que você não conseguiu me vencer... LOOSER!!!\n')
        else:
            print(f'\nEMPATE... {self.nome} te desafio a disputar mais um campeonato comigo!!!\n')


if __name__ == '__main__':

    jogador = Adversario()

    jogador.campeonato()