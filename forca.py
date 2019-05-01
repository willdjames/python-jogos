# forca.py

import random

def inicia_jogo():
    
    print("******************************")
    print("* Bem vindo ao jogo da Forca *")
    print("******************************")


    arquivo_palavra = open("palavra.txt", "r")
    palavras = []

    for linha in arquivo_palavra:
        palavras.append(linha.strip())

    arquivo_palavra.close()

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()
    print(palavra_secreta)

    letras_acertadas = ["_" for letra in palavra_secreta]

    print(letras_acertadas)

    acertou = False
    enforcou = False
    erros = 0

    while(not enforcou and not acertou):

        chute = input("Uma letra: ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):

            index = 0

            for letra in palavra_secreta:

                if(chute == letra):
                    print("{} na posição {}".format(chute, index))
                    letras_acertadas[index] = letra

                index += 1

            print(letras_acertadas)

        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas

        print("Você tem {} tentativas ". format(6 - erros))

    print("* Fim do jogo *")

if(__name__ == "__main__"):
    inicia_jogo()
