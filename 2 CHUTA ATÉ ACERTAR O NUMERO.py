#CHUTA ATÉ ACERTAR 
import random
def gera():
    return random.randint(-0,11)

def game():
    resposta = gera()
    tentativa = 0
    print("\nPalpite gerado!\n")

    chute=0
    while chute is not resposta:
        tentativa +=1
        chute = int(input("Qual seu chute: "))
        if chute > resposta:
            print("Errou! É um valor MENOR - que ", chute)
        elif chute < resposta:
            print("Errou! É um valor MAIOR + que ", chute)
        else:
            print("Parabéns! O número gerado foi ",resposta, \
                  " Acertou em  ",tentativa,"  tentativas!")
    
while True:
    game()