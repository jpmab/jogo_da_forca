# TRABALHO FINAL DE COMPUTAÇÃO - JOGO DA FORCA

# Nome dos participantes do grupo(seguido do DRE): João Pedro Bianco(120064499), Nina Machado Fortes(120064978), Thiago Pereira Paura(120098943)


# Código com funções auxiliares para o código principal


#Definindo as listas de palavras a serem escolhidas:

filmes = ['Star Wars', 'Vingadores', 'Homem Aranha', 'Karate Kid', 'Matrix', 'Esqueceram de mim', 'Star Trek', 'Blade Runner', 'O Mágico de Oz', 'Psicose', 'Poltergeist', 'Jogos Mortais', 'Bastardos Inglórios', 'Pulp Fiction', 'Tubarão', 'Resgate do Soldado Ryan', 'De volta para o futuro', 'O Poderoso Chefão', 'Senhor dos Anéis', 'Clube da Luta', 'Forrest Gump', 'Cidade de Deus', 'Tropa de Elite', 'Indiana Jones', 'O Exterminador do Futuro', 'O Rei leão', 'Alien', 'Dr. Estranho', 'Thor', 'Wall e', 'Coração Valente', 'Toy Story', 'Rocky']

objetos = ['lápis', 'caneta', 'borracha', 'lâmpada', 'martelo', 'machado', 'faca', 'estetoscópio', 'microscópio', 'quadro', 'mouse', 'teclado', 'monitor', 'abajur', 'agulha', 'boia', 'cabide', 'castiçal', 'celular', 'dado', 'detergente', 'DVD', 'escova', 'escudo', 'espada', 'esponja', 'garrafa', 'isopor', 'jarro', 'jornal', 'lança', 'luminária', 'microfone', 'notebook', 'ombreira', 'ovo', 'panela', 'pincel', 'rádio', 'raquete', 'relógio', 'serrote', 'tabuleiro', 'telefone', 'urna', 'válvula', 'ventilador', 'zíper']

lugares = ['São Paulo', 'Rio de Janeiro', 'Pernambuco', 'João Pessoa', 'Holanda', 'Itália', 'França', 'Rússia', 'China', 'Japão', 'Coréia do Sul', 'Coréia do Norte', 'Madagascar', 'Brasília', 'Califórnia', 'Washington', 'São Francisco', 'Seattle', 'Veneza', 'Alasca', 'Chile', 'Argentina', 'Uruguai', 'Deserto do Atacama', 'Tóquio', 'Acre', 'Rio Branco', 'Tocantins', 'Palmas', 'Porto Rico', 'Jamáica', 'Cuba', 'Dinamarca', 'Barra da Tijuca', 'Flamengo', 'Méier', 'São Conrado', 'Recreio dos Bandeirantes', 'Cabo Frio', 'Búzios', 'Angra dos Reis', 'Bonito', 'Leblon', 'Ipanema', 'Copacabana']

marcas = ['Microsoft', 'Apple', 'Intel', 'Jaguar', 'Nescafé', 'Nestle', 'Sadia', 'Google', 'MasterCard', 'Amazon', 'Nike', 'Adidas', 'Sony', 'Samsung', 'Xiaomi', 'Coca cola', 'Audi', 'Honda', 'Mercedes Benz', 'Doriana', 'Dove', 'Lux', 'Loreal Paris', 'Yamaha', 'Asics', 'Garmim', 'Cassio', 'Mitsubshi', 'Ferrari', 'Gillette', 'Perdigão', 'Reebok', 'Puma', 'Timberland', 'Converse', 'Nissan', 'Itaú', 'Santander', 'Banco do Brasil', 'Caixa', 'Calvin Klein', 'Lacoste', 'Mizuno', 'Victorinox', 'Deca', 'Ford', 'Volkswagen', 'Oakley', 'Quicksilver', 'Hurley', 'Kpaloa']

animais = ['macaco', 'leão', 'tigre', 'onça pintada', 'tubarão', 'pinguim', 'peixe', 'elefante', 'girafa', 'rinoceronte', 'hipopótamo', 'mico', 'gato', 'cachorro', 'cobra', 'minhoca', 'leopardo', 'puma', 'pantera', 'enguia', 'coiote', 'lobo', 'raposa', 'águia', 'gavião', 'pardal', 'pombo', 'galinha', 'porco', 'tartaruga', 'água viva', 'tatuí', 'gaivota', 'alce', 'veado', 'cabra', 'bode', 'ovelha', 'carneiro', 'avestruz', 'camaleão', 'golfinho', 'abelha', 'foca', 'leão marinho', 'cegonha', 'chimpanze', 'cavalo', 'zebra', 'esponja', 'tamanduá', 'porco espinho', 'formiga', 'gambá', 'rato', 'barata', 'marimbondo', 'guaxinim', 'iguana', 'jabuti', 'jegue', 'lacraia', 'lesma', 'caracol', 'lula', 'mariposa', 'ostra', 'urso', 'coruja', 'vaca', 'aranha', 'coelho', 'lebre', 'zangão']

alimentos = ['macarrão', 'feijão', 'arroz', 'cuzcuz marroquino', 'banana', 'beterraba', 'batata', 'batata doce', 'abobrinha', 'berinjela', 'gengibre', 'maçã', 'abacaxi', 'morango', 'kiwi', 'lichia', 'pêssego', 'abóbora', 'tomate', 'abacate', 'queijo', 'mirtilo', 'carne', 'frango', 'hambúrguer', 'pão', 'pão de forma', 'pão de queijo', 'nozes', 'castanha', 'amêndoa', 'avelã', 'amendoim', 'ovo', 'peixe', 'pera', 'coco', 'aspargos', 'brócolis', 'couve flor', 'alho', 'couve', 'cebola', 'camarão', 'frutos do mar', 'aveia', 'lentilha', 'leite', 'iogurte', 'azeite', 'pimenta', 'pimentão', 'ameixa', 'uva passa', 'uva', 'cogumelo', 'shitake', 'lula', 'polvo']

categorias = [filmes, objetos, lugares, marcas, animais, alimentos]





# Funções responsáveis por printar as informações para o jogador

def menu():
    ''' Printa o menu do jogo e faz o jogador escolher a categoria de palavras desejada.

    none -> int'''

    print('\n')
    print('     ██╗ ██████╗  ██████╗  ██████╗     ██████╗  █████╗     ███████╗ ██████╗ ██████╗  ██████╗ █████╗ ')     # Créditos do título: site https://fsymbols.com/generators/carty/
    print('     ██║██╔═══██╗██╔════╝ ██╔═══██╗    ██╔══██╗██╔══██╗    ██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗')
    print('     ██║██║   ██║██║  ███╗██║   ██║    ██║  ██║███████║    █████╗  ██║   ██║██████╔╝██║     ███████║')
    print('██   ██║██║   ██║██║   ██║██║   ██║    ██║  ██║██╔══██║    ██╔══╝  ██║   ██║██╔══██╗██║     ██╔══██║')
    print('╚█████╔╝╚██████╔╝╚██████╔╝╚██████╔╝    ██████╔╝██║  ██║    ██║     ╚██████╔╝██║  ██║╚██████╗██║  ██║')
    print(' ╚════╝  ╚═════╝  ╚═════╝  ╚═════╝     ╚═════╝ ╚═╝  ╚═╝    ╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝')                                                                                                  
    print('\n'*2)
    print('Categorias: ')
    print('(1) - Filmes')
    print('(2) - Objetos')
    print('(3) - Lugares (nomes de bairros, cidades, estados e paises)')
    print('(4) - Marcas')
    print('(5) - Animais')
    print('(6) - Alimentos', '\n')

    categoria = int(input('Digite o número da categoria que deseja jogar: '))               # recebe a categoria escolhida

    while categoria not in [1,2,3,4,5,6]:                                                   # garante que a categoria escolhida seja válida
        categoria = int(input('Caractere inválido! Digite um número válido(1 até 6): '))

    return categoria



def tela_inicial(lista_tentativas, palavra_censurada, tentativas_restantes):
    '''Printa o desenho da forca da tela inicial ou quando não há nenhum erro do jogador.

    list, str, int -> none'''

    print('       _______               ')
    print('      |      |               ')                                                  # Desenho da forca feito por nós inspirado em versões da internet
    print('      |                      ')
    print(f'      |                  Tentativas restante: {tentativas_restantes}')  
    print('      |                      ')
    print(' _____|___________            ')
    print('/     |          /|           ')
    print('                / /           ')
    print(f'_______________/ /       Palavra: {palavra_censurada}')     
    print('_______________|/             ')



def tentativas_restantes_7(lista_tentativas, palavra_censurada, tentativas_restantes):
    '''Printa o desenho da forca quando há 7 tentativas restantes.

    list, str, int -> none'''
    
    print('       _______               ')
    print(f'      |      |            Lista de letras erradas: {lista_tentativas}')
    print('      |     ( )              ')
    print(f'      |                   Tentativas restante: {tentativas_restantes}')     
    print('      |                      ')
    print(' _____|___________            ')
    print('/     |          /|           ')
    print('                / /           ')
    print(f'_______________/ /        Palavra: {palavra_censurada}')
    print('_______________|/             ')



def tentativas_restantes_6(lista_tentativas, palavra_censurada, tentativas_restantes):
    '''Printa o desenho da forca quando há 6 tentativas restantes.

    list, str, int -> none'''

    print('       _______                ')
    print(f'      |      |           Lista de letras erradas: {lista_tentativas}')
    print('      |     ( )               ')
    print(f'      |      |           Tentativas restante: {tentativas_restantes}')
    print('      |                       ')
    print(' _____|___________            ')
    print('/     |          /|           ')
    print('                / /           ')
    print(f'_______________/ /        Palavra: {palavra_censurada}')
    print('_______________|/             ')



def tentativas_restantes_5(lista_tentativas, palavra_censurada, tentativas_restantes):
    '''Printa o desenho da forca quando há 5 tentativas restantes.

    list, str, int -> none'''

    print('       _______                ')
    print(f'      |      |            Lista de letras erradas: {lista_tentativas}')
    print('      |     ( )               ') 
    print(f'      |      |            Tentativas restante: {tentativas_restantes}')  
    print('      |      |\               ')
    print(' _____|___________            ')
    print('/     |          /|           ')
    print('                / /           ')
    print(f'_______________/ /        Palavra: {palavra_censurada}')
    print('_______________|/             ')



def tentativas_restantes_4(lista_tentativas, palavra_censurada, tentativas_restantes):
    '''Printa o desenho da forca quando há 4 tentativas restantes.

    list, str, int -> none'''

    print('       _______                ')
    print(f'      |      |            Lista de letras erradas: {lista_tentativas}')
    print('      |     ( )               ') 
    print(f'      |      |            Tentativas restante: {tentativas_restantes}')  
    print('      |     /|\               ')
    print(' _____|___________            ')
    print('/     |          /|           ')
    print('                / /           ')
    print(f'_______________/ /        Palavra: {palavra_censurada}')
    print('_______________|/             ')



def tentativas_restantes_3(lista_tentativas, palavra_censurada, tentativas_restantes):
    '''Printa o desenho da forca quando há 3 tentativas restantes.

    list, str, int -> none'''

    print('       _______                ')
    print(f'      |      |            Lista de letras erradas: {lista_tentativas}')
    print('      |     ( )               ') 
    print(f'      |      |            Tentativas restante: {tentativas_restantes}')  
    print('      |     /|\               ')
    print(' _____|______ \____           ')
    print('/     |        \ /|           ')
    print('                / /           ')
    print(f'_______________/ /        Palavra: {palavra_censurada}')
    print('_______________|/             ')



def tentativas_restantes_2(lista_tentativas, palavra_censurada, tentativas_restantes):
    '''Printa o desenho da forca quando há 2 tentativas restantes.

    list, str, int -> none'''

    print('       _______                ')
    print(f'      |      |            Lista de letras erradas: {lista_tentativas}')
    print('      |     ( )               ') 
    print(f'      |      |            Tentativas restante: {tentativas_restantes}')  
    print('      |     /|\              ')
    print(' _____|_____/ \___           ')
    print('/     |    /   \ /|          ')
    print('                / /          ')
    print(f'_______________/ /        Palavra: {palavra_censurada}')
    print('_______________|/             ')



def tentativas_restantes_1(lista_tentativas, palavra_censurada, tentativas_restantes):
    '''Printa o desenho da forca quando há 1 tentativas restantes.

    list, str, int -> none'''

    print('       _______                ')
    print(f'      |      |            Lista de letras erradas: {lista_tentativas}')
    print('      |     ( )               ') 
    print(f'      |      |            Tentativas restante: {tentativas_restantes}')  
    print('      |     /|\              ')
    print(' _____|_____/ \*__           ')
    print('/     |    /   \ /|          ')
    print('                / /          ')
    print(f'_______________/ /        Palavra: {palavra_censurada}')
    print('_______________|/             ')



def tentativas_restantes_0(lista_tentativas, palavra_censurada, tentativas_restantes):
    '''Printa o desenho da forca quando não há tentativas restantes.

    list, str, int -> none'''

    print('       _______                ')
    print(f'      |      |            Lista de letras erradas: {lista_tentativas}')
    print('      |     ( )               ') 
    print(f'      |      |            Tentativas restante: {tentativas_restantes}')  
    print('      |     /|\              ')
    print(' _____|____*/ \*__           ')
    print('/     |    /   \ /|          ')
    print('                / /          ')
    print(f'_______________/ /        Palavra: {palavra_censurada}')
    print('_______________|/             ')



def desenho_forca(lista_tentativas, palavra_censurada, erros):
    '''Analisa a lista das tentativas erradas anteriores e imprime o desenho
    da forca correspondente ao status atual do jogo.

    list, str, int -> none'''

    tentativas_restantes = 8 - erros        # cria a variável tentativas_restantes sendo o total de tentativas menos a quantidade de erros

    # Analisa a quantidade de tentativas restantes, e printa a interface correspondente
    
    if (tentativas_restantes) == 8:
        tela_inicial(lista_tentativas, palavra_censurada, tentativas_restantes)                          

    if (tentativas_restantes) == 7:
        tentativas_restantes_7(lista_tentativas, palavra_censurada, tentativas_restantes)

    if (tentativas_restantes) == 6:
        tentativas_restantes_6(lista_tentativas, palavra_censurada, tentativas_restantes)

    if (tentativas_restantes) == 5:
        tentativas_restantes_5(lista_tentativas, palavra_censurada, tentativas_restantes)

    if (tentativas_restantes) == 4:
        tentativas_restantes_4(lista_tentativas, palavra_censurada, tentativas_restantes)
        
    if (tentativas_restantes) == 3:
        tentativas_restantes_3(lista_tentativas, palavra_censurada, tentativas_restantes)

    if (tentativas_restantes) == 2:
        tentativas_restantes_2(lista_tentativas, palavra_censurada, tentativas_restantes)

    if (tentativas_restantes) == 1:
        tentativas_restantes_1(lista_tentativas, palavra_censurada, tentativas_restantes)

    if (tentativas_restantes) == 0:
        tentativas_restantes_0(lista_tentativas, palavra_censurada, tentativas_restantes)



def derrota(palavra):
    '''Printa a tela de derrota.

    none -> none'''

    print('\n')
    print(' ___________.._______    ')
    print('| .__________))______|   ')                                          # créditos da tela de derrota: https://ascii.co.uk/art/hangman
    print('| | / /      ||          ')
    print('| |/ /       ||          ')
    print('| | /        ||.-''.             VOCÊ PERDEU...')                
    print('| |/         |/  _  \            ')
    print(f'| |          ||  `/,|            A PALAVRA ERA: {palavra}')
    print('| |          (\\`_.`     ')
    print('| |         .-`--.       ')
    print('| |        /Y . . Y\     ')
    print('| |       // |   | \\    ')
    print('| |      //  | . |  \\   ')
    print('| |     ()   |   |   ()  ')
    print('| |          ||-||       ')
    print('| |          || ||       ')
    print('| |          || ||       ')
    print('| |          || ||       ')  
    print('| |         / | | \      ')      
    print('------------|_| |_|   |-|')
    print('|---------\ \       '"| | ")
    print('| |        \ \        | |')
    print(': :         \ \       : :')
    print('. .          `        . .')



def vitoria():
    '''Printa a tela de vitória.

    none -> none'''

    print('\n')
    print('███╗░░░███╗██╗░░░██╗██╗████████╗░█████╗░  ██████╗░███████╗███╗░░░███╗██╗██╗██╗')
    print('████╗░████║██║░░░██║██║╚══██╔══╝██╔══██╗  ██╔══██╗██╔════╝████╗░████║██║██║██║')     # Créditos do texto: site https://fsymbols.com/generators/carty/
    print('██╔████╔██║██║░░░██║██║░░░██║░░░██║░░██║  ██████╦╝█████╗░░██╔████╔██║██║██║██║')
    print('██║╚██╔╝██║██║░░░██║██║░░░██║░░░██║░░██║  ██╔══██╗██╔══╝░░██║╚██╔╝██║╚═╝╚═╝╚═╝')
    print('██║░╚═╝░██║╚██████╔╝██║░░░██║░░░╚█████╔╝  ██████╦╝███████╗██║░╚═╝░██║██╗██╗██╗')
    print('╚═╝░░░░░╚═╝░╚═════╝░╚═╝░░░╚═╝░░░░╚════╝░  ╚═════╝░╚══════╝╚═╝░░░░░╚═╝╚═╝╚═╝╚═╝')
    print('\n')
    print('Parabéns!!! Você acertou! =)')



def fim():
    '''Printa o menu final, após a pessoa ganhar ou perder o jogo, perguntando se ela deseja jogar novamente
    ou sair do jogo.

    none -> int'''

    print('\n')
    print('O que você deseja fazer: ')
    print('(1) Jogar novamente')
    print('(2) Sair do jogo')
    print('\n')

    decisao = int(input('Digite o número do que deseja fazer: '))                                       # recebe a decisão do jogador

    while decisao != 1 and decisao != 2:                                                                # garante que é uma decisão válida
        decisao = int(input('Caractere inválido! Digite o número do que deseja fazer: '))

    return decisao
