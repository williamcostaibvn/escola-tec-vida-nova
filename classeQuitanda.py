class Quitanda:
    def __init__(self, produto, quantidade, valor) -> None:
        self.compra = str(produto)
        self.qtd = int(quantidade)
        self.preco = float(valor)
        self.total = quantidade * valor

    def exibirPedido(self) -> None:
        print('%s            %s               %4.2f               %4.2f' % (self.compra, self.qtd, self.preco, self.total))

    def calculaTroco(self, divida, valorPago):
        tipoCedulas = [20, 10, 5, 2]
        tipoMoedas = [1, 0.5, 0.25, 0.1, 0.05]
        print('\nDivida:     R$ %4.2f' % (divida))
        print('Valor pago: R$ %4.2f' % (valorPago))
        troco = valorPago - divida
        print('Troco:      R$ %3.2f' % (troco))
        print('')
        if(troco > 0):
            print('Devolva:')
            for cedula in tipoCedulas:
                if troco >= cedula:
                    quantCedula = troco/cedula
                    print('%s nota(s) de R$ %3.2f' % (int(quantCedula), cedula))
                    resto = troco%cedula
                    troco = resto
            for moeda in tipoMoedas:
                if troco >= moeda:
                    quantMoeda = troco/moeda
                    print('%s moeda(s) de R$ %3.2f' % (int(quantMoeda), moeda))
                    resto = troco%moeda
                    troco = resto
        if troco < 0.05:
            print('\nAinda falta devolver R$ %1.2f. Aceita uma Bala?' % (troco))  # Hahahahaha simplesmente sensacional