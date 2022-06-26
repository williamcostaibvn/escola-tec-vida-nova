from classeQuitanda import Quitanda

frutas = {
    1 : 'Morango  ',
    2 : 'Melancia ', 
    3 : 'Laranja  ',
    4 : 'Tanjerina',
    5 : 'Caqui    ',
    6 : 'Damasco  '
    }

precoFrutas = {
    1 : 1.79,
    2 : 19.99, 
    3 : 2.99,
    4 : 2.39,
    5 : 4.49,
    6 : 3.99
    }

comprarMais = 's'

pedido = {}

totalPedido = 0

# Iniciando a Quitanda 
print('\n\n    BEM-VINDO A QUITANDA DO JOAQUIM    ')
print()
print('Preço bom | Qualidade | Bom Atendimento')

# Laço do pedido de frutas
while (comprarMais != 'N'):

    # Exibindo as Códigos, Frutas e Preços
    print('\n____________________________________________________')
    print('Essas são nossas frutas disponíveis hoje:\n')
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
            print('Querido cliente... ATENÇÃO!!! Use apenas os números correspondentes as frutas disponíveis!')
        else:
            break
    
    # Exibindo o preço da fruta selecionada
    preco = precoFrutas[venda]
    print('\nCusta R$ {} cada unidade do(a) {} '.format(preco, frutas[venda]))

    # Solicitando a quantidade desejada da Fruta solicitada
    qtd = int(input('\nQuantas unidades de você gostaria? '))
    print()
    
    # Calculando valor de cada item e do total do pedido 
    total = qtd * preco

    totalPedido = totalPedido + total

    # Anotando pedido na classeQuitanda.py
    pedido[frutas[venda]] = Quitanda(frutas[venda], qtd, preco)

    # Exibir pedido para o cliente
    print('RESUMO DA COMPRA:')
    print('----------------------------------------------------------------------')
    print('Produto          Quant.            Valor Unit.           Valor Total.')

    for compra in pedido.keys():
        pedido[compra].exibirPedido()

    print('----------------------------------------------------------------------')
    print('Total de Itens: {} - Valor total da Compra: R$ %4.2f'.format(int(len(pedido.keys()))) % (totalPedido))

    # Encerrar laço do pedido de frutas - Sim/Não
    comprarMais = input('\nDeseja comprar mais alguma fruta (s/n)? ')
    comprarMais = comprarMais.upper()

# Recebendo pagamento
pagamento = int(input('\nQual o valor do pagamento: '))

# Teste para pagamento menor que valor do pedido, calculo de troco e quantidade de notas e moedas para devolver
if(pagamento < totalPedido):
    print('O valor pago é menor que o valor da compra!')
    pagamento = int(input('Reveja o valor do pagamento: '))
    pedido[frutas[venda]].calculaTroco(totalPedido, pagamento)
    
else:
    pedido[frutas[venda]].calculaTroco(totalPedido, pagamento)

# Finalizando programa
print()
print('----------------------------------------------------------------------')
print()
print('Compra finalizada, a Quitando do Joaquim agradece... Volte sempre!')
print()