import random as rd
def jogar():

    abertura_apresentacao()
    palavra_secreta = carregamento_palavras()
    palavra_acerto = preenchimento_acertos(palavra_secreta)
    
    enforcou = False
    venceu = False
    tentativas = 0


    while (not enforcou and not venceu):
       
        letra_escolhida = chute_jogador()

        if(letra_escolhida in palavra_secreta):
            verificar_acerto(letra_escolhida, palavra_acerto, palavra_secreta)
        else:
            tentativas +=1
            desenha_forca(tentativas)

        venceu = "_" not in palavra_acerto
        enforcou = tentativas == 7    
       

    if(enforcou):
        mensagem_perdedor(palavra_secreta)
    else:
        mensagem_vencedor()

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def verificar_acerto(letra_escolhida, palavra_acerto, palavra_secreta):
        index = 0
        for letra in palavra_secreta:

            if (letra_escolhida == letra):
                print("Letra escolhida {}, existe nas posições {}".format(letra, index))
                palavra_acerto[index] = letra 
            index = index + 1    

def chute_jogador():
    letra_escolhida = input("Digite uma letra: ").upper()
    letra_escolhida = letra_escolhida.strip()
    return letra_escolhida


def abertura_apresentacao():
    print("=*=*"*20)
    print("Jogo da forca")
    print("=*=*"*20)

def carregamento_palavras():
    arquivo = open("C:\ProjetosAlura\Python\jogos\palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    
    numero = rd.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta

def preenchimento_acertos(palavra):

    return ["_" for letra in palavra]


if(__name__ == "__main__"):
    jogar()
