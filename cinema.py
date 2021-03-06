#Criando função que exibirá a sala de cinema para o usuário
def salaDeCinema():
    linha = 1
    print("\n****** T E L A ******")
    print("a b c d e f g h i j |")
    for montagem in range (0, totalCadeiras):
        print(cinema[montagem], end = ' ')
        # Numerando as fileiras da sala de cinema
        if ((montagem + 1) % 10 == 0):
            print(linha)
            linha += 1

    # Opção 1: para exibição da numeração da ultima fileira
    # if (((montagem + 1) % 10 == 0) == False):
    #     print(linha)
    
    # Opção 2: para exibição da numeração da ultima fileira
    # if if ((montagem + 1) % 10):
    #     print(linha)

    # Opção 3: para exibição da numeração da ultima fileira
    if (len(cinema) % 10):
        print(linha)
    print("\n******* FUNDO *******")

#Recebendo a quantidade de cadeiras que terão na sala de cinema
totalCadeiras = int(input("\nQuantos acentos possui sua sala de cinema? "))

#Letreiro (arte moderna, rsrsrsrs)
print("\nw   w  eeee  l    l         cccc oooo  mm mm  eeee      ttttt oooo")
print("w w w  eee   l    l         c    o  o  m m m  eee         t   o  o")
print("ww ww  eeee  llll llll      cccc oooo  m   m  eeee        t   oooo")
print("\ncccc  i  nn  n  eeee     nn  n  eeee  w   w     l     i  ffff eeee")
print("c     i  n n n  eee      n n n  eee   w w w     l     i  fff  eee")
print("cccc  i  n  nn  eeee     n  nn  eeee  ww ww     llll  i  f    eeee")

#Criando a lista das cadeiras da sala de cinema
cinema = ['_'] * totalCadeiras
salaDeCinema()

#Biblioteca de posições
posicao = {'A' : str(0),'B' : str(1),'C' : str(2),'D' : str(3),'E' : str(4),'F' : str(5),'G' : str(6),'H' : str(7),'I' : str(8),'J' : str(9)}

#Loop para finalizar o app quando a sala estiver toda reservada
while('_' in cinema):
    #Iniciando a reserva das cadeiras
    entrada = str(input("\nInforme o Acento em que deseja assistir ao filme? (Ex: \"F1\"): "))
    reserva = entrada.upper()
    reservaList = list(reserva)
    #Solucinando escolha errada de coluna
    if ((reservaList[0] in posicao) == False):
        print("\n*************** A T E N Ç Ã O ****************")
        print("* Acento indisponível, escolha outro acento. *")
        print("**********************************************")
    else:
        coluna = str(reservaList[0])
        dezena = str(posicao[coluna])

        if (len(reservaList) == 3):
            reservaNumerica = str(reservaList[1] + reservaList[2] + dezena)
        elif (len(reservaList) == 4):
            reservaNumerica = str(reservaList[1] + reservaList[2] + reservaList[3] + dezena)
        else:
            reservaNumerica = str(reservaList[1] + dezena)

        cadeira = int(reservaNumerica)
        cadeiraReservada = int(cadeira - 10)

        #Solucinando escolha errada de fileira
        if (cadeiraReservada >= len(cinema)):
            print("\n*************** A T E N Ç Ã O ****************")
            print("* Acento indisponível, escolha outro acento. *")
            print("**********************************************")
        #Solucinando escolha de acento já reservado
        elif (cinema[cadeiraReservada] == 'x'):
            print("\n************* A T E N Ç Ã O *************")
            print("* Acento ocupado, escolha outro acento. *")
            print("*****************************************")
        #Reservando acento
        else:
            cinema[cadeiraReservada] = 'x'
            salaDeCinema()
            print("\nAcento reservado com sucesso!")

#Encerrando o programa
print("\nTODOS EM SEUS LUGARES!!!")
print("A sessão já vai começar.\n")

#Fim