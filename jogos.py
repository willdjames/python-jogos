# jogos.py

import adivinhacao
import forca

print("***********************")
print("* Bem vindo aos jogos *")
print("***********************")

print("(1)Adivinhação (2)Forca")

jogo = int(input("Escolha um jogo: "))

print("Jogo escolhido: {} ".format(jogo))
print("")

if(jogo == 1):
    adivinhacao.inicia_jogo()
elif(jogo == 2):
    forca.inicia_jogo()

