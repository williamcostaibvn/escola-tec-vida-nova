class Funcionario:
    def __init__(self, nomeFunc, sobrenomeFunc, cargoFunc, salarioFunc=False) -> None:
        self.nome = str(nomeFunc)
        self.sobrenome = str(sobrenomeFunc)
        self.cargo = str(cargoFunc)
        self.salario = float(salarioFunc)

    def mudarSalario(self, salarioFunc) -> float:
        self.salario = float(salarioFunc)

    def mudarCargo(self, novoCargo) -> str:
        self.cargo = str(novoCargo)

    def exibirFuncionario(self) -> None:
        print('Nome:       %s\nSobrenome:  %s\nCargo:      %s\nSalário: R$ %7.2f\n' % (self.nome, self.sobrenome, self.cargo, self.salario))

    def impostoDeRenda(self, salarioFunc) -> float:
        aliquota1 = 7.5
        aliquota2 = 15
        aliquota3 = 22.5
        aliquota4 = 27.5
        if (salarioFunc <= 1903.98):
            self.salarioLiquido = salarioFunc
            print('Aliquota de Imposto de Renda:      Isento')
            print('Salário Líquido (Já abatido o IR): R$ %7.2f\n' % (self.salarioLiquido))

        elif (salarioFunc >= 1903.99 and salarioFunc <= 2826.65):
            self.salarioLiquido = salarioFunc-(salarioFunc*aliquota1)/100
            print('Salário Bruto (Sem nenhum abatimento): R$ %7.2f' % (salarioFunc))
            print('Aliquota de Imposto de Renda:            ', aliquota1,'%')
            print('Valor do Imposto de Rende recolhido:   R$ %7.2f' % ((salarioFunc*aliquota1)/100))
            print('Salário Líquido (Já abatido o IR):     R$ %7.2f\n' % (self.salarioLiquido))
        
        elif (salarioFunc >= 2826.66 and salarioFunc <= 3751.05):
            self.salarioLiquido = salarioFunc-(salarioFunc*aliquota2)/100
            print('Salário Bruto (Sem nenhum abatimento): R$ %7.2f' % (salarioFunc))
            print('Aliquota de Imposto de Renda:            ', aliquota2,'%')
            print('Valor do Imposto de Rende recolhido:   R$ %7.2f' % ((salarioFunc*aliquota2)/100))
            print('Salário Líquido (Já abatido o IR):     R$ %7.2f\n' % (self.salarioLiquido))
           
        elif (salarioFunc >= 3751.06 and salarioFunc <= 4664.68):
            self.salarioLiquido = salarioFunc-(salarioFunc*aliquota3)/100
            print('Salário Bruto (Sem nenhum abatimento): R$ %7.2f' % (salarioFunc))
            print('Aliquota de Imposto de Renda:            ', aliquota3,'%')
            print('Valor do Imposto de Rende recolhido:   R$ %7.2f' % ((salarioFunc*aliquota3)/100))
            print('Salário Líquido (Já abatido o IR):     R$ %7.2f\n' % (self.salarioLiquido))
        
        elif (salarioFunc >= 4664.69):
            self.salarioLiquido = salarioFunc-(salarioFunc*aliquota4)/100
            print('Salário Bruto (Sem nenhum abatimento): R$ %7.2f' % (salarioFunc))
            print('Aliquota de Imposto de Renda:            ', aliquota4,'%')
            print('Valor do Imposto de Rende recolhido:   R$ %7.2f' % ((salarioFunc*aliquota4)/100))
            print('Salário Líquido (Já abatido o IR):     R$ %7.2f\n' % (self.salarioLiquido))