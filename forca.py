from getpass import getpass

# Função para Desenhar a Forca
def montarForca():
    if(chances - erros == 6):
        print('.____.')
        print('|    |')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('##########')
    elif(chances - erros == 5):
        print('.____.')
        print('|    |')
        print("|  ('_')")
        print('|')
        print('|')
        print('|')
        print('|')
        print('##########')
    elif(chances - erros == 4):
        print('.____.')
        print('|    |')
        print("|  ('_')")
        print('|   | |')
        print('|   |_|')
        print('|')
        print('|')
        print('##########')
    elif(chances - erros == 3):
        print('.____.')
        print('|    |')
        print("|  ('_')")
        print('|  -| |')
        print('| / |_|')
        print('|')
        print('|')
        print('##########')
    elif(chances - erros == 2):
        print('.____.')
        print('|    |')
        print("|  ('_')")
        print('|  -| |-')
        print('| / |_| \\')
        print('|')
        print('|')
        print('##########')        
    elif(chances - erros == 1):
        print('.____.')
        print('|    |')
        print("|  ('_')")
        print('|  -| |-')
        print('| / |_| \\')
        print('|  _|')
        print('|')
        print('##########')        
    elif(chances - erros == 0):
        print('.____.')
        print('|    |')
        print('|  (x_x)')
        print('|  -| |-')
        print('| / |_| \\')
        print('|   | |')
        print('|  /   \\')
        print('|')
        print('##########')

# Inicializando variáveis
chances = 6
erros = 0
acerteiTudo = False
letrasUsadas = []

# Iniciando o Jogo
print('\nVAMOS JOGAR FORCA, ACEITA O DESAFIO???')
print()
montarForca()

# Solicitando palavra da partida em modo invisível, biblioteca GETPASS
palavraInicial = getpass('\nInforme a palavra desta partida: ')
print()

# Validando palavra da partida
is_valid = palavraInicial.isalpha()
if not is_valid:
    print('Texto digitado não contem apenas letras!')
    exit()

# Tratando palavra da partida
palavraInicial = palavraInicial.strip().upper()

# Laço de Palpites 
while erros < chances and not acerteiTudo:

    # Gerando a visualização da Palavra da partida na tela com _ no lugar das letras
    for letra in palavraInicial:
        if letra in letrasUsadas:
            print(letra, end=' ')
        else:
            print('_', end=' ')      
    print()

    # Solicitando palpite
    palpite = input('Diga uma letra: ')

    # Validando palpite
    palpiteValid = palpite.isalpha() and len(palpite) == 1

    while not palpiteValid:
        palpite = input('Palpite inválido, informe outro: ')
        palpiteValid = palpite.isalpha() and len(palpite) == 1

    palpite = palpite.upper()

    # Verificar se a letra ja foi usada
    if palpite in letrasUsadas:
        print('Essa letra já foi usada. Tente novamente!')
    else:
        letrasUsadas.append(palpite)

        # Palpite CORRETO
        ponto = 0
        if palpite in palavraInicial:
            print('Bom palpite!')

            #Verificar Vitoria
            for letra in palavraInicial:
                if letra in letrasUsadas:
                    ponto = ponto + 1

            if ponto == len(palavraInicial):
                acerteiTudo = True

        # Palpite ERRADO
        else:
            print('Erroooou')
            erros += 1
        print('Você ainda pode errar:', chances - erros,'vez(es)')

    #Exibir Palpites
    print('Palpites: ')
    for letras in letrasUsadas:
        print(letras, end='-')
    print()

    #Desenhando a Forca
    montarForca()

#Encerrando o programa (Vitória/Derrota)

## Gerando a visualização da Palavra da partida na tela com _ no lugar das letras
for letra in palavraInicial:
    if letra in letrasUsadas:
        print(letra, end=' ')
    else:
        print('_', end=' ')

## Vitória
if acerteiTudo:
    print()
    print('\nParabéns... Vc venceu a partida!!!\n')

## Derrota
else:
    print()
    print('\nNão foi desta vez... Tente de novo!!!\n')

# FIM