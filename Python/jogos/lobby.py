import adivinhacao
import forca

def escolha():
    print("=*=*"*20)
    print("Escolha qual jogo quer jogar")
    print("=*=*"*20, "\n")

    print("Digite 1 - Forca ou Digite 2 - Adivinhação")
    jogo_escolhido = int(input("Escolha: "))

    if (jogo_escolhido == 1):
        forca.jogar()
    elif(jogo_escolhido == 2):
        adivinhacao.jogar()


if (__name__ == "__main__"):
    escolha()
    