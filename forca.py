# forca.py

def inicia_jogo():
    
    print("******************************")
    print("* Bem vindo ao jogo da Forca *")
    print("******************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    print(letras_acertadas)

    acertou = False
    enforcou = False
    erros = 0

    while(not enforcou and not acertou):

        chute = input("Uma letra: ")
        chute = chute.strip()

        if(chute in palavra_secreta):

            index = 0

            for letra in palavra_secreta:

                if(chute.upper() == letra.upper()):
                    print("{} na posição {}".format(chute, index))
                    letras_acertadas[index] = letra

                index += 1

            print(letras_acertadas)


        else:
            erros = erros + 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(erros)

    print("* Fim do jogo *")

if(__name__ == "__main__"):
    inicia_jogo()
