# adivinhacao.py

import random

def inicia_jogo():

    print("************************************")
    print("* Bem vindo ao jogo da Adivinhação *")
    print("************************************")

    preco = 5.5
    pago = 10
    troco = pago - preco

    print("Preço: R$ {:5.2f}".format(preco))
    print("Pago:  R$ {:5.2f}".format(pago))
    print("---------------------")
    print("Troco: R$ {:5.2f}".format(troco))

    print("")

    print("Escolha a dificuldade: (1)Fácil (2)Médio (3)Difícil")
    nivel = int(input("Digite: "))

    total_de_tentativas = 0

    if(nivel == 1):
        total_de_tentativas = 8
    elif(nivel == 2):
        total_de_tentativas = 5
    else:
        total_de_tentativas = 3

    print("")

    numero_secreto = random.randrange(1, 11)

    rodada = 1

    pontos = 100

    # for rodada in range(1, total_de_tentativas + 1):
    while(rodada <= total_de_tentativas):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        rodada += 1

        chute_str = input("Digite seu número entre 1 e 10: ")

        chute = int(chute_str)

        if(chute < 1 or chute > 10):
            print("Voce deve chutar números entre 1 e 10!")
            continue

        print("Processando tentativa...")

        acertou = chute == numero_secreto
        menor = chute < numero_secreto
        maior = chute > numero_secreto

        if(acertou):
            print("Voce acertou e fez {} pontos!!".format(pontos))
            break
        else:
            if(menor):
                print("Você errou, seu número é menor que o número secreto")
            elif(maior):
                print("Você errou, seu número é maior que o número secreto")

            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("* Fim do jogo *")

if(__name__ == "__main__"):
    inicia_jogo()