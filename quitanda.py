from classeQuitanda import Quitanda

frutas = {
    'morango' : 1.0,
    'melancia': 20.0, 
    'laranja' : 3.0
}

comprarMais = 's'

pedido = {}

totalPedido = 0

limite = 0

print('\n\n  BEM-VINDO A QUITANDA DO JOAQUIM')
print('Preço | Qualidade | Bom Atendimento')

while (comprarMais != 'n'):
    venda = str(input('\nQual fruta você deseja comprar? (morango, melancia, laranja): '))
    preco = frutas[venda]
    
    print('\nO preço unitário da/do {} é {} '.format(venda, preco))

    qtd = int(input('\nQuantas unidades de {} você gostaria? '.format(venda)))
    print()
    
    total = qtd * preco

    totalPedido = totalPedido + total

    pedido[venda] = Quitanda(venda, qtd, preco)

    # Exibir pedido para o cliente
    print('RESUMO DA COMPRA:')
    print('----------------------------------------------------------------------')
    print('Produto          Quant.            Valor Unit.           Valor Total.')

    for compra in pedido.keys():
        pedido[compra].exibirPedido()

    print('----------------------------------------------------------------------')
    print('Total de Itens: {} - Valor total da Compra: R$ {}'.format(len(pedido.keys()),totalPedido))
    limite = len(pedido.keys())

    comprarMais = input('\nDeseja comprar mais alguma fruta (s/n)? ')
    print()
    print()

pagamento = int(input('Qual o valor do pagamento: '))

if(pagamento < totalPedido):
    print('O valor pago é menor que o valor da compra!')
    pagamento = int(input('Reveja o valor do pagamento: '))
    pedido[venda].calculaTroco(totalPedido, pagamento)
    
else:
    pedido[venda].calculaTroco(totalPedido, pagamento)

print()
print('Compra finalizada, a Quitando do Joaquim agradece... Volte sempre!')
print()