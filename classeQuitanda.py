class Quitanda:
    def __init__(self, produto, quantidade, valor) -> None:
        self.compra = str(produto)
        self.qtd = int(quantidade)
        self.preco = float(valor)
        self.total = quantidade * valor

    def exibirPedido(self) -> None:
        print('%s            %s               %7.2f               %7.2f' % (self.compra, self.qtd, self.preco, self.total))

    def calculaTroco(self, divida, valorPago):
        tipoCedulas = [int(20), int(5), int(1)]
        print('\nDivida:     R$ ', divida)
        print('Valor pago: R$ ', valorPago)
        troco = valorPago - divida
        print('Troco:      R$ ', troco)
        print('')
        print('Devolva:')
        if(troco > 0):
            for cedula in tipoCedulas:
                if troco >= cedula:
                    quantCedula = troco/cedula
                    print('%s notas de R$ %s.' % (int(quantCedula), cedula))
                    resto = troco%cedula
                    troco = resto