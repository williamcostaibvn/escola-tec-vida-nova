sequencia = int(input("Qual numero de Fibonacci deseja encontrar? "))
                      
ultimo = 0
penultimo = 1
n = 0

while(n < sequencia):
    print(n + 1,") ",ultimo)
    proximo = ultimo + penultimo
    ultimo = penultimo
    penultimo = proximo
    n += 1