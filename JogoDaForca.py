#Projeto 1 DSA - Construção de um Jogo da Forca 

import random
from os import system, name


def limpa_tela():

    if name == "nt":
        _ = system("cls")

    else: 
        _ = system("clear")


def display_hangman(chances):

    # Lista de estágios da forca
    stages = [  # estágio 6 (final)
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # estágio 5
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # estágio 4
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # estágio 3
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # estágio 2
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # estágio 1
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # estágio 0
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[chances]

def comecar_jogo():

    limpa_tela()

    print("--------- JOGO DA FORCA ---------\n")
    print("Digite uma letra")

    lista_palavras = ['abelha', 'águia', 'alpaca', 'antílope', 'aranha', 'atum', 'avestruz', 'baleia', 'bicho-preguiça', 
                        'bode', 'borboleta', 'búfalo', 'cachorro', 'camaleão', 'camarão', 'camelo', 'canário', 'capivara', 
                        'caracol', 'caranguejo', 'cavalo', 'cervo', 'chacal', 'chimpanzé', 'cobra', 'coelho', 'coruja', 'corvo', 
                        'crocodilo', 'doninha', 'elefante', 'enguia', 'esquilo', 'falcão', 'flamingo', 'formiga', 'furão', 
                        'galo', 'gambá', 'ganso', 'gato', 'gaivota', 'gavião', 'girafa', 'golfinho', 'gorila', 'grilo', 
                        'guaxinim', 'hamster', 'hiena', 'hipopótamo', 'iguana', 'jacaré', 'jaguar', 'javali', 'joaninha', 
                        'jumento', 'lagartixa', 'lagarto', 'leão', 'leopardo', 'lhama', 'libélula', 'lobo', 'lontra', 'louva-a-deus', 
                        'macaco', 'morcego', 'mula', 'naja', 'ocapi', 'onça', 'orangotango', 'ornitorrinco', 'ostra', 'ouriço', 
                        'ovelha', 'panda', 'pato', 'pavão', 'pelicano', 'pinguim', 'polvo', 'porco', 'porquinho-da-índia', 
                        'raposa', 'rato', 'rena', 'rinoceronte', 'salamandra', 'sapo', 'suricate', 'tamanduá', 'tartaruga', 
                        'tigre', 'touro', 'tubarão', 'urso', 'urubu', 'veado', 'vaca', 'zebra']
    
    palavra = random.choice(lista_palavras)

    tabuleiro = ["_"] * len(palavra)

    letras_descobertas = ['_' for letra in palavra]

    chances = 6

    letras_erradas = []

# A função join() em Python é utilizada para concatenar os elementos de uma lista ou outro iterável em uma única string,
# com um separador entre os elementos. O separador é definido pela string na qual o método join() é chamado.

    while chances > 0:
        print(display_hangman(chances))
        print(" ".join(letras_descobertas))
        print("Chances restantes: ", chances)
        print("Letras erradas: ", " ".join(letras_erradas))

        tentativa = input("\nDigite uma letra: ").lower()

        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else: 
            chances -= 1
            letras_erradas.append(tentativa)
        
        if "_" not in letras_descobertas:
            print(f"Você venceu! A palavra é {palavra}")
            break

    if "_" in letras_descobertas:
        print(f"Você perdeu! a palavra era {palavra}")

comecar_jogo()