# Código principal


# Importando módulos necessários para o programa:
import random

from auxiliar import * #Importando funções auxiliares criadas em outro código





# Definindo as funções do programa:

def sem_acento(palavra):
    '''Dada uma palavra, retorna a mesma sem acentos.

    str -> str'''
    
    modifica = list(palavra)                # Cria uma variável temporária, sendo a lista da palavra, para modificar a palavra

    for indice in range(len(palavra)):      # Para cada índice da palavra, analisa-se elemento a elemento:
        if palavra[indice] in 'áâã':        # Caso tenha caractere especial, retiramos ele; analisamos vogal por vogal.
            modifica[indice] = 'a'

        if palavra[indice] in 'éê':
            modifica[indice] = 'e'

        if palavra[indice] in 'í':
            modifica[indice] = 'i'

        if palavra[indice] in 'óôõ':
            modifica[indice] = 'o'

        if palavra[indice] in 'úû':
            modifica[indice] = 'u'

    palavra = ''.join(modifica)             # Transforma a variável temporária de lista em string e a associa a palavra

    return palavra



def escolhe_palavra(categoria):
    '''Escolhe aleatóriamente uma função da categoria selecionada pelo jogador.

    str -> str'''
    
    tamanho_categoria = len(categoria)
    indice = random.randint(0,tamanho_categoria-1)    # Sorteia um número de 0 até o tamanho da categoria
    palavra = categoria[indice]                       # Relaciona esse número com uma palavra da lista da categoria escolhida pelo jogador

    return palavra



def mascara_palavra(palavra):
    '''Dada a palavra resposta, retorna ela em formato censurado. Ex.: palavra = 'teste', palavra censurada = -----.

    str -> str'''
    
    palavra_censurada = len(palavra)*'-'            # Cria a máscara da palavra

    if ' ' in palavra:                              # Soluciona o problema para caso a palavra seja composta(tenha espaço)
        modifica = list(palavra_censurada)          # Cria uma variável temporária em formato de lista para alterarmos os elementos

        for indice in range(len(palavra)):          
            if palavra[indice] == ' ':
                modifica[indice] = ' '              # Modifica o '-' da máscara da palavra por ' ' na exata posição do espaço

        palavra_censurada = ''.join(modifica)       # Transforma novamente a variável temporária em string e a associamos com a palavra censurada

    return palavra_censurada



def acerto(letra, palavra, palavra_censurada):
    '''Caso o jogador tenha acertado a letra, atualiza a máscara da palavra.

    str, str, str -> str'''
    
    for indice in range(len(palavra)):                              # Analisa elemento a elemento da palavra
        palavra_censurada = list(palavra_censurada)                 # Transforma a palavra censurada em lista para conseguirmos alterá-la
        palavra_temp = sem_acento(palavra)                          # Cria uma variável temporária da palavra, sendo a palavra original sem nenhum acento

        if palavra_temp.lower()[indice] == letra:                   # Compara cada elemento da palavra sem acentos e sem maiúsculas com a letra inserida pelo jogador 
            palavra_censurada[indice] = palavra[indice]             # Troca a máscara '-' pela letra escolhida na posição correta

    print('\n')
    print(f'Parabéns a letra {letra} está na palavra')              # Printa uma mensagem informando que o jogador acertou a letra
    palavra_censurada = ''.join(palavra_censurada)                  # A variável palavra censurada volta a ser do tipo string

    return palavra_censurada



def erro(letra, lista_tentativas, erros):
    '''Caso o jogador tenha errado a letra, atualiza a lista de tentativas.

    str, list -> int'''
    
    lista_tentativas.append(letra)                      # Adiciona a letra errada na lista de tentativas
    erros += 1
    print('\n')
    print(f'A letra {letra} não está na palavra')       # Printa informando que o jogador errou a letra

    return erros





# Função Principal
def main():
    '''Função principal: gerencia as entradas e saídas para o jogador dependendo do que ele queira.

    none -> none'''

    # Criando variáveis nulas para serem incrementadas durante o uso
    categoria = ''
    palavra = ''
    palavra_censurada = ''
    letra = ''
    decisao = ''

    # Chamando as listas de palavras e a lista de categorias 
    global categorias, filmes, objetos, lugares, marcas, animais, alimentos
    
    # Início do jogo e da interação com o jogador
    while decisao != 2:                                                               # Repete o jogo até o jogador escolher encerrá-lo
        
        categoria = menu()                                                            # Carrega o menu do jogo e define qual a categoria o usuário escolheu
        indice = categoria - 1                                                        # Relaciona o seu valor da categoria a um índice
        categoria = categorias[indice]                                                # Utiliza o índice para associar a variável categoria a real categoria(como por exemplo: filmes, objetos, etc.)

        palavra = escolhe_palavra(categoria)                                          # Sorteia a palavra da categoria selecionada
        palavra_censurada = mascara_palavra(palavra)                                  # Faz a máscara da palavra selecionada
    
        lista_tentativas = []                                                         # Cria uma lista vazia que vai servir para registrar as tentativas do jogador que não estavam na palavra 
        erros = len(lista_tentativas)                                                 # Quantidade de erros
        
        desenho_forca(lista_tentativas, palavra_censurada, erros)                     # Printa o desenho da forca inicial

        
        while palavra != palavra_censurada and erros <= 8 :                           # Repete o processo enquanto a palavra for diferente da palavra censurada(enquanto o jogador não adivinhar a palavra)
                                                                                      #  ou até o jogador esgotar suas tentativas (máximo de 8 erros)

            letra = input('Digite a letra: ')                                         # Recebe o input da letra que o jogador quis saber se tem na palavra

            if len(letra) > 1:                                                        # Verifica se o jogador realmente digitou apenas uma letra
                print('\n')
                print('Digite apenas uma letra por vez.')

            elif letra in lista_tentativas or letra in sem_acento(palavra_censurada.lower()):    # Verifica se a letra já foi digitada anteriormente(seja certa ou errada)
                print('\n')
                print('Você já digitou essa letra')

            elif letra in sem_acento(palavra.lower()):                                # Verifica se a letra inserida está na palavra, ou seja, se está certa
                palavra_censurada = acerto(letra, palavra, palavra_censurada)         # Caso esteja correta, atualiza a variável palavra censurada com a função acerto

            elif letra not in palavra.lower() and erros <= 8:                         # Verifica se a letra não está na palavra e se a quantidade de erros é menor do que 8
                erros = erro(letra, lista_tentativas, erros)                          # Caso esteja errado, atualiza a lista de tentativas com a função erro
   

            desenho_forca(lista_tentativas, palavra_censurada, erros)                 # Analisa a quantidade de tentativas restantes, e printa a interface correspondente
            

            if erros > 8:                                                             # Caso o tamanho a quantidade de erros seja maior do 8, ou seja, o jogador tenha perdido
                derrota(palavra)                                                      # Printa a tela de derrota
                
                decisao = fim()                                                       # Printa o menu do fim do jogo, perguntando se o jogador deseja jogar novamente ou sair do jogo
            

        if palavra == palavra_censurada:
            vitoria()                       # Printa a tela de vitória
            
            decisao = fim()                 # Printa o menu do fim do jogo, perguntando se o jogador deseja jogar novamente ou sair do jogo


    input('Pressione a tecla enter para sair... ')
    return
    

# Chamando a função principal
if __name__ == "__main__":
    main()
