class Quitanda:

    def __init__(self, produto, quantidade, valor):
        self.produto = str(produto)
        self.qtd = int(quantidade)
        self.preco = float(valor)
        self.total = quantidade * valor

    def exibirPedido(self):
        print(f' {self.produto}            {self.qtd}                  %4.2f               %4.2f' % (self.preco, self.total))

    def calculaTroco(self, divida, valorPago):
        tipoCedulas = [20, 10, 5, 2]
        tipoMoedas = [1, 0.5, 0.25, 0.1, 0.05]
        print('\nValor do Pedido:  R$ %4.2f' % (divida))
        print('Valor Pago:       R$ %4.2f' % (valorPago))
        troco = valorPago - divida
        print('Troco a Devolver: R$ %3.2f' % (troco))
        print()
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
        if (troco < 0.05 and troco >= 0.01):
            print('\nAinda falta devolver R$ %1.2f. Aceita uma balinha?' % (troco))
        else:
            print('\nConfira seu troco!')

frutas = {
    1 : 'Morango  ',
    2 : 'Melancia ', 
    3 : 'Laranja  ',
    4 : 'Tanjerina',
    5 : 'Caqui    ',
    6 : 'Damasco  ',
    7 : 'Uva Verde',
    8 : 'Banana   ',
    9 : 'Melão    ',
    10: 'Jaca     '}

precoFrutas = {
    1 : 1.79,
    2 : 19.99, 
    3 : 2.99,
    4 : 2.39,
    5 : 4.49,
    6 : 3.99,
    7 : 8.76,
    8 : 3.74,
    9 : 9.93,
    10: 24.99,
    }

comprarMais = 's'

pedido = {}

barra = '\u2550'

# Iniciando a Quitanda
print(f'\n\n\u2554{barra*41}\u2557') 
print('\u2551     BEM-VINDO A QUITANDA DO JOAQUIM     \u2551')
print(f'\u2560{barra*41}\u2563')
print('\u2551 Preço Bom | Qualidade | Bom Atendimento \u2551'),
print(f'\u255A{barra*41}\u255D') 

nome = input('\nQual seu nome: ')

# Laço do pedido de frutas
while (comprarMais != 'N'):

    # Exibindo os Códigos, Frutas e Preços
    print('\n____________________________________________________')
    print(f'{nome}, essas são nossas frutas disponíveis hoje:\n')
    for fruit in frutas:
        print('{} - {} (R$ {}/Unid)'.format(fruit, frutas[fruit], (precoFrutas[fruit])))
    print('____________________________________________________')

    # Recebendo e tratando o código da fruta que o cliente solicitou
    while True:
        try:
            venda = int(input('\nInforme o Código da fruta que você deseja comprar: '))
            print('')
            if not 1 <= venda <= len(frutas):
                raise ValueError()
        except ValueError:
            print(f'Atenção {nome}!!!\nUse apenas os números correspondentes as frutas disponíveis!')
        else:
            break
    
    # Exibindo o preço da fruta selecionada
    preco = precoFrutas[venda]
    print('\nCusta R$ {} cada unidade do(a) {} '.format(preco, frutas[venda]))

    # Solicitando a quantidade da Fruta desejada
    qtd = int(input('\nQuantas unidades você gostaria de comprar? '))
    print()

    # Anotando pedido na classe Quitanda

    pedido[frutas[venda]] = frutas[venda]

    pedido[frutas[venda]] = Quitanda(pedido[frutas[venda]], qtd, preco)

    # Exibir pedido para o cliente

    print('RESUMO DA COMPRA:')
    print('----------------------------------------------------------------------')
    print(' Produto          Quant.            Valor Unit.           Valor Total')
    print('----------------------------------------------------------------------')

    for compra in pedido.keys():
        pedido[compra].exibirPedido()

    print('----------------------------------------------------------------------')
    print(f'Total de Itens: {int(len(pedido))}')

    totalPedido = 0.0

    for valor in pedido.keys():
        totalPedido = pedido[valor].total + totalPedido

    print('Valor total da Compra: R$ %4.2f' % (totalPedido))
    
    # Encerrar laço do pedido de frutas - Sim/Não
    comprarMais = input('\nDeseja comprar mais alguma fruta (s/n)? ')
    comprarMais = comprarMais.upper()

# Teste para pagamento menor que valor do pedido, calculo de troco e quantidade de notas e moedas para devolver
while True:
    try:
        pagamento = int(input('\nInforme o valor do pagamento: '))
        print('')
        if(pagamento < totalPedido):
            raise ValueError()
    except ValueError:
        print('O valor pago é menor que o valor da compra, confira o valor para pagamento!')
    else:
        break

pedido[frutas[venda]].calculaTroco(totalPedido, pagamento)

# Finalizando programa
print()
print('----------------------------------------------------------------------')
print()
print(f'Compra finalizada!!!\n{nome}, a Quitando do Joaquim agradece a preferência...\nVolte sempre!')
print()