#Declarando variaveis
penultimo = 0
ultimo = 1
sequencia = 1
i = 1

#Looping para encerrar o app quando for digitado "0"
while (sequencia != 0):
    sequencia = int(input("\nQual número de fibonacci deseja encontrar? "))

    #Gerador em looping de sequencia Fibonatti com comando "for"
    for n in range(0, sequencia):
        print(i,") ", penultimo)
        proximo = penultimo + ultimo
        penultimo = ultimo
        ultimo = proximo
        i += 1
    penultimo = 0
    ultimo = 1
    i = 1

#Fim