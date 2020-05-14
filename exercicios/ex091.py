from random import randint
from time import sleep
from operator import itemgetter

jogo = {"Jogador1": randint(1, 6),
        "Jogador2": randint(1, 6),
        "Jogador3": randint(1, 6),
        "Jogador4": randint(1, 6)}

ranking = []

print("Valores sorteados: ")

for k, v in jogo.items():
    print("{} tirou o valor {} no dado.".format(k, v))
    sleep(0.5)

print("-=-" * 15)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

# ranking é uma lista, vamos tratar ele como tal
for i, v in enumerate(ranking):
    print("{}º lugar: {} com {}.".format(i+1, v[0], v[1]))
    sleep(0.5)
