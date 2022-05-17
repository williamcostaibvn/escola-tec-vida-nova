# aliquotas de IR%
aliquota1 = 7.5
aliquota2 = 15
aliquota3 = 22.5
aliquota4 = 27.5

# entrada de dados -> Salário Bruto
salarioBruto = float(input("Qual o seu Salário Bruto: R$ "))

# Exibindo Aliquota de IR e Salário Líquido
if (salarioBruto <= 1903.98):
    print("Valor isento de cobrança de Imposto de Renda")
    print("Salário Líquido = R$",salarioBruto)
    print("\n\n")
elif (salarioBruto >= 1903.99 and salarioBruto <= 2826.65):
    print("Aliquota (%) de IR:",aliquota1)
    print("Salário Líquido = R$",salarioBruto-(salarioBruto*aliquota1)/100)
    print("\n\n")
elif (salarioBruto >= 2826.66 and salarioBruto <= 3751.05):
    print("Aliquota (%) de IR:",aliquota2)
    print("Salário Líquido = R$",salarioBruto-(salarioBruto*aliquota2)/100)
    print("\n\n")
elif (salarioBruto >= 3751.06 and salarioBruto <= 4664.68):
    print("Aliquota (%) de IR:",aliquota3)
    print("Salário Líquido = R$",salarioBruto-(salarioBruto*aliquota3)/100)
    print("\n\n")
elif (salarioBruto >= 4664.69):
    print("Aliquota (%) de IR:",aliquota4)
    print("Salário Líquido = R$",salarioBruto-(salarioBruto*aliquota4)/100)
    print("\n\n")