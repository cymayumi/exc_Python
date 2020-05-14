import random
from time import sleep

print("\033[1:33m-=-\033[m"*20)
print("\033[1:34mVou pensar em um número entre 0 e 5. Tente adivinhar.....")
print("\033[1:33m-=-\033[m"*20)

start = int(input("Vamos jogar? 1-SIM 2-NAO "))

while start == 1:
    jogador = int(input("\nEm qual número pensei? "))
    print("PROCESSANDO....")
    sleep(2)

    lista = [0, 1, 2, 3, 4, 5]
    computador = random.choice(lista)

    while jogador < 0 or jogador >= 6:
        print("\nPara brincarmos você deve digitar um número entre 0 e 5!")
        jogador = int(input("Vamos de novo! Em qual número pensei? "))
        print("PROCESSANDO....")
        sleep(2)

    if jogador == computador:
        print("\n\033[35mVOCÊ GANHOU!!! Parabéns! Nós pensamos no número {}!\033[m".format(jogador))
        start = int(input("\nVamos jogar de novo? 1-SIM 2-NAO "))
    else:
        print("\n\033[31mGANHEI!! Eu pensei no número {} e não no {}.\033[m".format(computador, jogador))
        start = int(input("\nVamos jogar de novo? 1-SIM 2-NAO "))