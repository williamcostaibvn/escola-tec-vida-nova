from classeQuitanda import Quitanda

frutas = {
    1 : 'morango',
    2 : 'melancia', 
    3 : 'laranja'
    }

precoFrutas = {
    1 : 1.00,
    2 : 20.00, 
    3 : 3.00
    }

comprarMais = 's'

pedido = {}

totalPedido = 0

# Iniciando a Quitanda 
print('\n\n    BEM-VINDO A QUITANDA DO JOAQUIM    ')
print()
print('Preço bom | Qualidade | Bom Atendimento')

# Laço do pedido de frutas
while (comprarMais != 'n'):
    print('\n____________________________________________________')
    print('Essas são nossas frutas disponíveis hoje:\n')
    for fruit in frutas:
        print('{} - {} (R$ {}/Unid)'.format(fruit, frutas[fruit], (precoFrutas[fruit])))
    print('____________________________________________________')
    while True:
        try:
            venda = int(input('\nInforme o número da fruta que você deseja comprar: '))
            print('')
            if not 1 <= venda <= len(frutas):
                raise ValueError()
        except ValueError:
            print('Querido cliente... ATENÇÃO!!! Use apenas os números correspondentes as frutas disponíveis!')
        else:
            break
    
    preco = precoFrutas[venda]
    print('\nO preço unitário do(a) {} é {} '.format(frutas[venda], preco))

    qtd = int(input('\nQuantas unidades de {} você gostaria? '.format(frutas[venda])))
    print()
    
    total = qtd * preco

    totalPedido = totalPedido + total

    pedido[frutas[venda]] = Quitanda(frutas[venda], qtd, preco)

    # Exibir pedido para o cliente
    print('RESUMO DA COMPRA:')
    print('----------------------------------------------------------------------')
    print('Produto          Quant.            Valor Unit.           Valor Total.')

    for compra in pedido.keys():
        pedido[compra].exibirPedido()

    print('----------------------------------------------------------------------')
    print('Total de Itens: {} - Valor total da Compra: R$ {}'.format(len(pedido.keys()),totalPedido))

    comprarMais = input('\nDeseja comprar mais alguma fruta (s/n)? ')

# Recebendo pagamento
pagamento = int(input('\nQual o valor do pagamento: '))

# Teste para pagamento menor que valor do pedido
if(pagamento < totalPedido):
    print('O valor pago é menor que o valor da compra!')
    pagamento = int(input('Reveja o valor do pagamento: '))
    pedido[frutas[venda]].calculaTroco(totalPedido, pagamento)
    
else:
    pedido[frutas[venda]].calculaTroco(totalPedido, pagamento)

# Finalizando programa
print()
print('Compra finalizada, a Quitando do Joaquim agradece... Volte sempre!')
print()