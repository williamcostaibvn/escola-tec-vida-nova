#Declarando variaveis
sequencia = 1
ultimo = 0
penultimo = 1
n = 0

#Looping para encerrar o app quando for digitado "0"
while(sequencia != 0):
	sequencia = int(input("\nQual número de fibonacci deseja encontrar? "))

	#Gerador em looping de sequencia Fibonatti com comando "while"
	while(n < sequencia):
	    print(n + 1,") ",ultimo)
	    proximo = ultimo + penultimo
	    ultimo = penultimo
	    penultimo = proximo
	    n += 1
	ultimo = 0
	penultimo = 1
	n = 0

#Fim