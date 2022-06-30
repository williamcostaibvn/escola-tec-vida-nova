import random

from PIL import Image

# Função para Desenhar a Forca
def montarForca():

    # Usa em todos
    if(erros == 0):
        print('.____.')
        print('|    |')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('##########')

    # Usa em chances = 10 com 1 erro
    elif(chances - erros == 9):
        print('.____.')
        print('|    |')
        print("|  (   )")
        print('|')
        print('|')
        print('|')
        print('|')
        print('##########')

    # Usa em Chances = 10 com 2 erros
    # Usa em Chances = 8 com 1 erro 
    elif((chances == 10 and erros == 2) or (chances == 8 and erros == 1)):
        print('.____.')
        print('|    |')
        print("|  ('  )")
        print('|')
        print('|')
        print('|')
        print('|')
        print('##########')

    # Usa em Chances = 10 com 3 erros
    # Usa em Chances = 8 com 2 erros
    elif((chances == 10 and erros == 3) or (chances == 8 and erros == 2)):
        print('.____.')
        print('|    |')
        print("|  (' ')")
        print('|')
        print('|')
        print('|')
        print('|')
        print('##########')
    
    # Usa em Chances = 10 com 4 erros
    # Usa em Chances = 8 com 3 erros
    # Usa em Chances = 6 com 1 erro
    # Usa em Chances = 4 com 1 erro 
    elif((chances == 10 and erros == 4) or (chances == 8 and erros == 3) or (chances == 6 and erros == 1) or (chances == 4 and erros == 1)):
        print('.____.')
        print('|    |')
        print("|  ('_')")
        print('|')
        print('|')
        print('|')
        print('|')
        print('##########')

    # Usa em Chances = 10 com 5 erros
    # Usa em Chances = 8 com 4 erros
    # Usa em Chances = 6 com 2 erros
    elif((chances == 10 and erros == 5) or (chances == 8 and erros == 4) or (chances == 6 and erros == 2)):
        print('.____.')
        print('|    |')
        print("|  ('_')")
        print('|   | |')
        print('|   |_|')
        print('|')
        print('|')
        print('##########')
    
    # Usa em Chances = 10 com 6 erros
    # Usa em Chances = 8 com 5 erros
    # Usa em Chances = 6 com 3 erros
    elif((chances == 10 and erros == 6) or (chances == 8 and erros == 5) or (chances == 6 and erros == 3)):
        print('.____.')
        print('|    |')
        print("|  ('_')")
        print('|  -| |')
        print('| / |_|')
        print('|')
        print('|')
        print('##########')

    # Usa em Chances = 10 com 7 erros
    # Usa em Chances = 8 com 6 erros
    # Usa em Chances = 6 com 4 erros
    # Usa em Chances = 4 com 2 erros
    elif((chances == 10 and erros == 7) or (chances == 8 and erros == 6) or (chances == 6 and erros == 4) or (chances == 4 and erros == 2)):
        print('.____.')
        print('|    |')
        print("|  ('_')")
        print('|  -| |-')
        print('| / |_| \\')
        print('|')
        print('|')
        print('##########')

    # Usa em Chances = 10 com 8 erros
    # Usa em Chances = 8 com 7 erros
    # Usa em Chances = 6 com 5 erros
    elif((chances == 10 and erros == 8) or (chances == 8 and erros == 7) or (chances == 6 and erros == 5)):
        print('.____.')
        print('|    |')
        print("|  ('_')")
        print('|  -| |-')
        print('| / |_| \\')
        print('|  _|')
        print('|')
        print('##########')
    
    # Usa em Chances = 10 com 9 erro
    # Usa em Chances = 4 com 3 erros
    elif((chances == 10 and erros == 9) or (chances == 4 and erros == 3)):
        print('.____.')
        print('|    |')
        print("|  ('_')")
        print('|  -| |-')
        print('| / |_| \\')
        print('|  _| |_')
        print('|')
        print('##########')
    
    # Usa em Chances = 10 com 10 erros
    # Usa em Chances = 8 com 8 erros
    # Usa em Chances = 6 com 6 erros
    # Usa em Chances = 4 com 4 erros
    elif((chances == 10 and erros == 10) or (chances == 8 and erros == 8) or (chances == 6 and erros == 6) or (chances == 4 and erros == 4)):
        print('.____.')
        print('|  (x_x)')
        print('|  -| |-')
        print('| / |_| \\')
        print('|   | |')
        print('|  /   \\')
        print('|')
        print('##########')

# Dicionario de Categorias de Palavras Secretas disponíveis para o jogo
categorias = {
    'Animais' : ['abelha', 'aguia', 'alce', 'aranha', 'avestruz', 'babuino', 'baiacu', 'baleia', 'borboleta', 'capivara',
    'cavalo', 'cachorro', 'canguru', 'camundongo', 'crocodilo', 'carrapato', 'caranguejo', 'dromedario', 'dinossauro',
    'elefante', 'escorpiao', 'esquilo', 'falcao', 'flamingo', 'formiga', 'gafanhoto', 'gaivota', 'gaviao', 'girafa',
    'golfinho', 'gorila', 'guepardo', 'hamster', 'hiena', 'hipopotamo', 'iguana', 'impala', 'jabuti', 'jacare', 'jaguatirica',
    'javali', 'jiboia', 'jumento', 'coala', 'lagartixa', 'lagosta', 'leao', 'leopardo', 'macaco', 'marimbondo', 'minhoca',
    'morcego', 'mosquito', 'onca', 'ornitorrinco', 'ovelha', 'panda', 'pantera', 'papagaio', 'pelicano', 'perereca',
    'periquito', 'pernilongo', 'pinguim', 'preguica', 'ratazana', 'rinoceronte', 'rouxinol', 'salamandra', 'sanguessuga',
    'sardinha', 'serpente', 'suricato', 'tamandua', 'tartaruga', 'tilapia', 'toupeira', 'tubarao', 'tucunare', 'urubu',
    'urso', 'veado', 'vibora', 'zebra', 'zangao'],

    'Cidades' : ['guarulhos', 'campinas', 'osasco', 'sorocaba', 'maua', 'santos', 'diadema', 'jundiai', 'piracicaba',
    'carapicuiba', 'bauru', 'itaquaquecetuba', 'franca', 'guaruja', 'taubate', 'limeira', 'suzano', 'sumare', 'barueri',
    'indaiatuba', 'americana', 'itapevi', 'marilia', 'araraquara', 'hortolandia', 'araçatuba', 'itapetininga', 'botucatu',
    'atibaia', 'araras', 'valinhos', 'sertaozinho', 'birigui', 'caraguatatuba', 'votorantim', 'barretos', 'catanduva',
    'guaratingueta', 'ourinhos', 'paulinia', 'itanhaem', 'caieiras', 'mairipora', 'votuporanga', 'ubatuba', 'cruzeiro',
    'vinhedo', 'jaboticabal', 'pirassununga', 'cosmopolis', 'fernandopolis', 'bertioga', 'penapolis', 'louveira',
    'pedreira', 'buritama', 'zacarias', 'planalto', 'turiuba', 'aparecida', 'iracemapolis', 'paranapanema'],

    'Comidas' : ['feijoada', 'moqueca', 'aracaje', 'galinhada', 'virado', 'arroz', 'bombocado', 'bacalhoada', 'buchada',
    'croquete', 'calzone', 'pizza', 'cheeseburguer', 'churrasco', 'dobradinha', 'escondidinho', 'ensopado', 'espaguete',
    'farofa', 'frango', 'figado', 'galinhada', 'guisado', 'guacamole', 'hamburguer', 'iogurte', 'joelho',
    'kafta', 'kibe', 'lasanha', 'lagarto', 'lentilha', 'linguiça', 'lagosta', 'lombo', 'leitoa', 'macarrão', 'macarronada',
    'maionse', 'mingau', 'moqueca', 'mortadela', 'mussarela', 'nhoque', 'nuggets', 'omelete', 'ostra', 'paçoca', 'pamonha',
    'panqueca', 'pastel', 'picanha', 'pipoca', 'pudim', 'quiabo', 'quiche', 'rabada', 'rabanada', 'rapadura', 'ratatouille',
    'ravioli', 'risoto', 'salpicao', 'sopa', 'sonho', 'salsicha', 'salame', 'tacos', 'talharim', 'tapioca', 'torresmo', 
    'torta', 'tutu', 'vinagrete', 'wafer', 'wasabi', 'yakissoba'],

    'Nomes' : ['miguel', 'arthur', 'heitor', 'gabriel', 'gabriela', 'bernardo', 'samuel', 'joao', 'pedro', 'helena', 'valentina',
    'antonela', 'antonio', 'amanda', 'alexandre', 'adriano', 'adriana', 'agostinho', 'alessandro', 'alessandra', 'andre',
    'andressa', 'aparecida', 'aparecido', 'ariadne', 'anastacia', 'adelaide', 'albertina', 'augusto', 'anderson', 'aguinaldo',
    'adalberto', 'agostinho', 'astrogildo', 'aquiles', 'absalao', 'bernadete', 'berenice', 'barbara','benjamim', 'bartolomeu',
    'belarmino', 'baltazar', 'beraldo', 'bernardino', 'catarina', 'camilo', 'camila', 'cristiano', 'cristina', 'claudete',
    'cristiane', 'cleonice', 'cassandra', 'cassiane', 'cleopatra', 'clemente', 'chistopher', 'custodio', 'constantino',
    'cordeiro', 'clementina', 'clodoaldo', 'celestino', 'carmelinda', 'conceicao', 'cordeiro', 'claudiano', 'dominique',
    'daniel', 'daniele', 'debora', 'doralice', 'domingos', 'dionisio', 'demetrio', 'diogenes', 'davidson', 'dagoberto',
    'donatello', 'deocleciano', 'diolindo', 'eduarda', 'eduardo', 'emanuelly', 'emanuel', 'elisangela', 'elisabete',
    'edilaine', 'ermelinda', 'eucadia', 'fernanda', 'fernando', 'franciele', 'francisco', 'filipe', 'fabiano', 'fabiana',
    'flavio', 'flavia', 'giovana', 'giovane', 'giselle', 'gilmara', 'gilmar', 'guilherme', 'heloisa', 'helio', 'ingrid',
    'isadora', 'isabele', 'isabel', 'iolanda', 'ivaneide', 'ivonete', 'larissa', 'leticia', 'lorena', 'luciana', 'lorraine',
    'ludmila', 'lourdes', 'leandro', 'lucilene', 'luzinete', 'laudiceia', 'laurindo', 'lissandra', 'lavinea', 'mariana',
    'mariano', 'manuela', 'manuel', 'marcela', 'marcelo','melissa', 'mirella', 'manuella', 'margarida', 'mauricio',
    'matilde', 'monalisa', 'margarete', 'michael', 'margareth', 'magnolia', 'marcolino', 'monique', 'moacir', 'marcelino',
    'michele', 'marieta', 'madalena', 'manuelito', 'miracema', 'maximiliano', 'marcilio', 'natalia', 'naiara', 'natanael',
    'nicolas', 'neemias', 'natalino', 'norberto', 'olivia', 'ophelia', 'orlando', 'osvaldo', 'otacilio', 'otaviano',
    'priscila', 'penelope', 'pollyanna', 'paulo', 'paula', 'petronia', 'petronio', 'pedro', 'pietro', 'peterson', 'patricia',
    'patricio', 'pericles', 'pitagoras', 'petronio', 'perminio', 'pascoal', 'quiteria', 'quelen', 'quintino', 'rafaela',
    'rafael', 'roberta', 'roberto', 'rosangela', 'rosilene', 'rosemary', 'rihanna', 'rosineide', 'rosamaria', 'renata',
    'renato', 'rodrigo', 'rogerio', 'raimundo', 'raimunda', 'reginaldo', 'reinaldo', 'riquelme', 'romario', 'ramses',
    'romilda', 'romildo', 'romualdo', 'roberval', 'robson', 'robinson', 'rosivaldo', 'raquel', 'ricardino', 'rodolfo',
    'stephanie', 'sabrina', 'samara', 'silvano', 'silvana', 'samantha', 'sulamita', 'soraya', 'sebastiana', 'silmara',
    'shakira', 'silvana', 'silvano', 'suzane', 'samuel', 'santiago', 'sebastiao', 'sebastiana', 'silverio', 'socrates',
    'salustiano', 'severino', 'severina', 'solomon', 'sadraque', 'salviano', 'stanislau', 'simplicio', 'saladino',
    'schimitid', 'sergio', 'simone', 'tatiane', 'tatiana', 'tainara', 'thamires', 'thaynara', 'terezinha', 'toninha',
    'toninho', 'teodora', 'teodoro', 'thamiris', 'thiago', 'theodoro', 'tarcisio', 'thalisson', 'teobaldo', 'timoteo',
    'ursula', 'ulisses', 'ubirajara', 'vanessa', 'viviane','veronica', 'valquiria', 'valdirene', 'veridiana', 'vinicius',
    'valentin', 'vanderlei', 'valdemar', 'valdomiro', 'vicenzo', 'valdivino', 'venceslau', 'valeria', 'valeriano',
    'vladimir', 'walquiria', 'walesca', 'wellington', 'william', 'wanderson', 'washington', 'whindersson', 'wanderley',
    'xayane', 'yasmim', 'yohanna', 'yolanda', 'yvonne', 'yago', 'zulmira', 'zenaide', 'zaqueu', 'zedequias'],
}

# Dicionario númerico das Categorias
categNum = {
    1 : 'Animais',
    2 : 'Cidades',
    3 : 'Comidas',
    4 : 'Nomes'
}

# Inicializando variáveis
erros = 0
acerteiTudo = False
letrasUsadas = []
pontos = 0

# Iniciando o Jogo
print('\nVAMOS JOGAR FORCA, ACEITA O DESAFIO???')

# Informando as Categorias de Palavras Secretas disponíveis
print()
print('ESCOLHA UMA DAS CATEGORIAS ABAIXO')
print('---------------------------------')
for opcao in categNum:
    print(f'|  {opcao} --> {categNum[opcao]}')
print('---------------------------------\n')

# Solicitando a Categoria desejada
while True:
    try:
        numEscolha = int(input('Digite o número da Categoria desejada: '))
        if not 1 <= numEscolha <= len(categNum):
            raise ValueError()
    except ValueError:
        print()
        print('ATENÇÃO!!! Use apenas os números correspondentes as Categorias disponíveis!')
    else:
        break

escolha = categNum[numEscolha]

# Selecionando de forma Randomica e tratando a palavra secreta da Forca
palavra = random.choices(categorias[escolha])
palavraInicial = (''.join(palavra))
palavraInicial = palavraInicial.upper()

# Fornecendo número de chances
if(len(palavraInicial) <= 6):
    chances = 4

elif(len(palavraInicial) >= 7 and len(palavraInicial) <= 9):
    chances = 6

elif(len(palavraInicial) >= 10 and len(palavraInicial) <= 11):
    chances = 8

elif(len(palavraInicial) >= 12):
    chances = 10

# Exibindo a Categoria Escolhida e o número de chances fornecidas para a palavra secreta selecionada
print(f'\nCategoria escolhida: {escolha.upper()}')
print(f'Você pode errar: {chances} vezes')

# Exibindo diagrama da Forca Vazia
montarForca()

# Laço de Palpites 
while erros < chances and not acerteiTudo:

    # Gerando a visualização da Palavra da partida na tela com '_' no lugar das letras ainda não encontradas
    for letra in palavraInicial:
        if letra in letrasUsadas:
            print(letra, end=' ')
        else:
            print('_', end=' ')      
    print()

    # Solicitando palpite
    palpite = input('\nDigite uma letra: ')

    # Validando e tratando o palpite 
    palpiteValid = palpite.isalpha() and len(palpite) == 1

    while not palpiteValid:
        palpite = input('Palpite inválido, digite "uma letra": ')
        palpiteValid = palpite.isalpha() and len(palpite) == 1

    palpite = palpite.upper()

    # Verificar se a letra ja foi usada, senão inclui-la na lista 'letrasUsadas'
    if palpite in letrasUsadas:
        print('Essa letra já foi usada. Digite outra!')
    else:
        letrasUsadas.append(palpite)

        # Palpite CORRETO
        ponto = 0
        if palpite in palavraInicial:
            if (chances - erros == 1):
                print('Bom palpite... Você ainda pode errar: 1 vez')
            else:
                print(f'Bom palpite... Você ainda pode errar: {chances - erros} vezes')

            # Verificar Vitoria
            for letra in palavraInicial:
                if letra in letrasUsadas:
                    ponto = ponto + 1
                    pontos = pontos + 1

            if ponto == len(palavraInicial):
                acerteiTudo = True

        # Palpite ERRADO
        else:
            erros += 1
            if (chances - erros == 0):
                print('Erroooou... Você não tem mais chances! :(')
            elif (chances - erros == 1):
                print('Erroooou... Você ainda pode errar: 1 vez')
            else:
                print(f'Erroooou... Você ainda pode errar: {chances - erros} vezes')
            
    # Exibir Palpites já utilizados
    print('Palpites: ')
    for letras in letrasUsadas:
        print(letras, end='-')
    print()

    # Desenhando a Forca conforme numero de chances e erros já contabilizados
    print(f'\nCategoria escolhida: {escolha}')
    montarForca()

# Encerrando o programa (Vitória/Derrota)
## Gerando a visualização da Palavra da partida na tela com '_' no lugar das letras não acertadas
for letra in palavraInicial:
    if letra in letrasUsadas:
        print(letra, end=' ')
    else:
        print('_', end=' ')

## Informando a Vitória
if acerteiTudo and erros == 0:
    print()
    print('\nVocê é muito bom mesmo, não errou nenhuma letra... Parabéns!!!\n')

    # Exibindo Troféu na Tela
    trofeu = Image.open('Trofeu.jpg')
    trofeu.show()

elif acerteiTudo:
    print()
    print('\nParabéns... Você venceu a partida!!!\n')

    # Exibindo Joinha na Tela
    joia = Image.open('Joinha.jpg')
    joia.show()

## Informando a Derrota

elif pontos == 0:
    print()
    print('\nPrecisa estudar mais, heim... Não acertou nenhuma letra... Lamentável!!!\n')
    print(f'A "Palavra Secreta" selecionada foi: {palavraInicial}\n')

    # Exibindo Deslike na Tela
    decepcao = Image.open('Decepcao.jpg')
    decepcao.show()

else:
    print()
    print('\nNão foi desta vez... Tente de novo!!!')
    print(f'A "Palavra Secreta" selecionada foi: {palavraInicial}\n')

    # Exibindo Caveirinha na Tela
    caveirinha = Image.open('Esqueleto.jpg')
    caveirinha.show()

# FIM