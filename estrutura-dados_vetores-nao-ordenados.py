#Implementar a classe de vetores não ordenados

class vetorNaoOrdenado:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultimaPosicao = -1
        self.valores = self.capacidade*[0]

    def imprime(self):
        if self.ultimaPosicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultimaPosicao + 1):
                print(i+1, ' - ', self.valores[i])

    def insercao(self, valor):

        if valor in self.valores:
            print(f'{valor} já foi incluído')
            return
        if self.ultimaPosicao == self.capacidade - 1:
            print('Capacidade máxima atingida!')
        else:
            self.ultimaPosicao = self.ultimaPosicao + 1
            self.valores[self.ultimaPosicao] = valor
    
    def pesquisa(self, valor):
        for i in range(self.ultimaPosicao + 1):
            if self.valores[i] == valor:
                return i
        return -1

    def excluir(self, valor):
        posicao = self.pesquisa(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultimaPosicao):
                self.valores[i] = self.valores[i + 1]
            self.ultimaPosicao = self.ultimaPosicao - 1

if __name__ == '__main__':

    vetor = vetorNaoOrdenado(8)
    print()
    print('Incluindo carros na pista:')
    vetor.insercao(4)
    vetor.insercao(2)
    vetor.insercao(1)
    vetor.insercao(6)
    vetor.insercao(5)
    vetor.insercao(12)
    vetor.insercao(7)
    vetor.insercao(10)
    vetor.imprime()

    print('-------------------------')
    print('Incluindo Carro 20 na pista:')
    vetor.insercao(20)
    print()

    print('-------------------------')
    print('Pesquisando posição dos carros na pista:')
    print('Carro 12: está na posição', vetor.pesquisa(12)+1)
    if vetor.pesquisa(49) == -1:
        print('Carro 49: Não está na pista')
    print()

    print('-------------------------')
    print('Retirando Carro 1 da pista:')
    vetor.excluir(1)
    vetor.imprime()
    print()

    print('-------------------------')
    print('Incluindo carro 10 na pista:')
    vetor.insercao(10)
    print()