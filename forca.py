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

    while(not enforcou and not acertou):

       chute = input("Uma letra: ")
       chute = chute.strip()

       index = 0

       for letra in palavra_secreta:

           if(chute.upper() == letra.upper()):
                print("{} na posição {}".format(chute, index))
                letras_acertadas[index] = letra

           index += 1

       print(letras_acertadas)

    print("* Fim do jogo *")

if(__name__ == "__main__"):
    inicia_jogo()
