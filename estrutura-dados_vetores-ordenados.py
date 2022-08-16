#Implementar a classe de vetores ordenados

class vetorOrdenado:

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
            return
        
        posicao = 0
        for i in range(self.ultimaPosicao + 1):
            posicao = i
            if self.valores[i] > valor:
                break
            if i == self.ultimaPosicao:
                posicao = i + 1
        
        x = self.ultimaPosicao
        while x >= posicao:
            self.valores[x + 1] = self.valores[x]
            x = x - 1

        self.valores[posicao] = valor
        self.ultimaPosicao = self.ultimaPosicao + 1

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

    vetor = vetorOrdenado(8)

    print('Incluindo carros na pista:')
    vetor.insercao(2)
    vetor.insercao(5)
    vetor.insercao(8)
    vetor.insercao(3)
    vetor.insercao(10)
    vetor.insercao(7)
    vetor.insercao(33)
    vetor.insercao(1)
    vetor.imprime()
    print('-------------------------')
    print('Pesquisando posição dos carros na pista:')
    if vetor.pesquisa(6) == -1:
        print('Carro 6: Não está na pista')
    print('Carro 3: está na posição ', vetor.pesquisa(3)+1)
    print('-------------------------')
    print('Retirando Carro 3 e incluindo Carro 6:')
    vetor.excluir(3)
    vetor.insercao(6)
    vetor.imprime()
    print('-------------------------')
    print('Retirando Carro 33 e incluindo Carro 10:')
    vetor.excluir(33)
    vetor.insercao(10)
    vetor.imprime()
    print('-------------------------')
    print('Incluindo carros 11 e 12 na pista:')
    vetor.insercao(11)
    vetor.insercao(12)
    vetor.imprime()