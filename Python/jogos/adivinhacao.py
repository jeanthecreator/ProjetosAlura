import random as rd

print("=*=*"*20)
print("Jogo de adivinhação")
print("=*=*"*20)

numero_secreto = rd.randint(1,100)
total_de_tentativas = 0
pontos = 1000
print(numero_secreto)

print("Escolha o nivel de dificuldade para jogar")
dificuldade = int(input("Nivel 1 (Facil) / Nivel 2 (Médio) / Nivel 3 (Dificil)\nEscolha: "))

if (dificuldade == 1):
    print("Facil")
    total_de_tentativas = 15
elif(dificuldade == 2):
    print("Médio")
    total_de_tentativas = 10
elif(dificuldade == 3):
    print("Dificil")
    total_de_tentativas = 5
else:
    print("Dificuldade inesistente")  


# while(total_de_tentativas > 0):
for rodada in range(1,total_de_tentativas+1):

    print("Numero de tentativa {} de {}".format(rodada, total_de_tentativas))
    
    chute= int(input("Tente acertar o numero entre 1 e 100: "))

    if (chute <= 0 or chute > 100):
        print("Voce deve digitar um numero entre 1 e 100")
        continue

    acertou = numero_secreto == chute
    maior = numero_secreto > chute
    menor = numero_secreto < chute

    print("Voce chutou o {:d}".format(chute))

    if (acertou):
        print("Voce acertou e ganhou {} pontos".format(pontos))
        break
    else:
        if(maior):
            print("Você errou - Numero digitado é maior que o numero secreto")
        elif(menor):
            print("Você errou - Numero digitado é menor que o numero secreto")   
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos
print("Fim do jogo")
