from classeFuncionario import Funcionario

# Funções
def menu():
    print('\n-----------------------------')
    print('|          M E N U          |')
    print('-----------------------------')
    print('| 1 - Cadastrar Funcionário |')
    print('| 2 - Exibir Funcionário    |')
    print('| 3 - Gerenciar Salários    |')
    print('| 4 - Gerenciar Cargos      |')
    print('| 5 - Imposto de Renda      |')
    print('-----------------------------')
    print('| 0 - SAIR                  |')
    print('-----------------------------')

def aindaNao():
    print('\n************** A T E N Ç Ã O ****************')
    print('Ainda não há Funcionário cadastrado, utilize')
    print('a Opção 1 para Cadastrar um Novo Funcionário.')
    print('______________________________________________________________________________')

def naoCadastrado():
    print('\n***************** A T E N Ç Ã O *******************')
    print('Funcionário(a) "{}" ainda não está cadastrado(a), '.format(exibir))
    print('utilize a Opção 1 para Cadastrar um Novo(a) Funcionário(a).')
    print('______________________________________________________________________________')

# Iniciando variáveis
opcao = 1
cadFunc = {}

# Nome e Versão
print('\n\n//////// Sistema de Gestão de Pessoas - 1.0 ////////')

# Exibindo Menu
menu()

# Laço de repetição para definir 'Zero' para saida do programa
while(opcao != 0):

    while True:
        try:
            opcao = int(input('\nInforme a opção desejada (6 - Exibe MENU): '))
            print('')
            if not 0 <= opcao <= 6:
                raise ValueError()
        except ValueError:
            print('\n******************** A T E N Ç Ã O ************************')
            print('Informe corretamente a Opção, digite um numero entre 1 e 6.')
            print('______________________________________________________________________________')
        else:
            break
    
# Função 1 - Cadastrar Funcionario
    if(opcao == 1):
        print('-> Opção 1 - Cadastrar Funcionário(a)')
        nome =      str(input('\nInforme o Nome do(a) Novo(a) Funcionário(a):            '))
        sobrenome = str(input('Informe o Sobrenome do(a) Novo(a) Funcionário(a):       '))
        cargo =     str(input('Informe o Cargo ocupado pelo(a) Novo(a) Funcionário(a): '))
        cadFunc[nome] = nome
        cadFunc[nome] = Funcionario(nome, sobrenome, cargo)
        print('______________________________________________________________________________')

# Função 2 - Consultar funcionários (apenas um ou todos)
    elif(opcao == 2):
        if(cadFunc == {}):
            aindaNao()

        else:
            print('-> Opção 2 - Exibir Cadastro de Funcionário')
            print('\nInforme qual Funcionário(a) deseja exibir ')
            exibir = str(input("(Digite 'todos' para ver todos os funcionários): "))
            if(exibir == 'todos'):
                for func in cadFunc.keys():
                    print()
                    cadFunc[func].exibirFuncionario()
                    print('______________________________________________________________________________')
            elif(exibir not in cadFunc.keys()):
                naoCadastrado()
            else:
                print()
                cadFunc[exibir].exibirFuncionario()
                print('______________________________________________________________________________')

# Função 3 - Alterar o Salário do Funcionário
    elif(opcao == 3):
        if(cadFunc == {}):
            aindaNao()
        else:
            print('-> Opção 3 - Gerenciador de Salários')
            exibir = str(input('\nQual Funcionário deseja alterar o Salário: '))
            if(exibir not in cadFunc.keys()):
                naoCadastrado()
            else:
                print()
                while True:
                    try:
                        novoSalario = float(input('\nQual o Salário de {} (Ex: R$ 0000.00)? R$ '.format(exibir)))
                        if not 0 <= novoSalario <= 1000000:
                            raise ValueError()
                    except ValueError:
                        print('\n*************** A T E N Ç Ã O *****************')
                        print('Informe o valor corretamente, conforme exemplo.')
                    else:
                        break

                cadFunc[exibir].mudarSalario(novoSalario)
                print()
                cadFunc[exibir].exibirFuncionario()
                print('______________________________________________________________________________')


# Função 4 - Alterar o Cargo do Funcionário
    elif(opcao == 4):
        if(cadFunc == {}):
            aindaNao()
        else:
            print('-> Opção 4 - Gerenciador de Cargos')
            exibir = str(input('\nQual Funcionário deseja trocar o Cargo: '))
            if(exibir not in cadFunc.keys()):
                naoCadastrado()       
            else:
                print()
                cadFunc[exibir].mudarCargo(input('Qual o Novo Cargo de {}? '.format(exibir)))
                print()
                cadFunc[exibir].exibirFuncionario()
                print('______________________________________________________________________________')
    
# Função 5 - Calcular Imposto de Renda
    elif(opcao == 5):
        if(cadFunc == {}):
            aindaNao()
        else:
            print('-> Opção 5 - Imposto de Renda (Salário Líquido)')
            exibir = str(input('\nPara qual Funcionário deseja calcular o IR: '))
            if(exibir not in cadFunc.keys()):
                naoCadastrado()
            elif(cadFunc[exibir].salario == False):
                print('\n****************** A T E N Ç Ã O *********************')
                print('Ainda não há salário definido para este funcionário,')
                print('utilize a Opção 3 para Gerenciar Salários.')
                print('______________________________________________________________________________')
            elif(cadFunc[exibir].salario != False):
                print()
                cadFunc[exibir].impostoDeRenda(cadFunc[exibir].salario)
                print('______________________________________________________________________________')

# Função 6 - Exibir Menu
    elif(opcao == 6):
        menu()

# Fim do programa