sequencia = int(input("Qual numero de fibonacci deseja encontrar? "))

penultimo = 0
ultimo = 1
i = 1

for n in range(0, sequencia):
    print(i,") ", penultimo)
    proximo = penultimo + ultimo
    penultimo = ultimo
    ultimo = proximo
    i += 1