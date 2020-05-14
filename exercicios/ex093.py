jogador = {}
gol = []

jogador["Nome"] = input("Nome do Jogador: ")

num = int(input("Quantas partidas {} jogou? ".format(jogador["Nome"])))

for i in range(num):
    gol.append(int(input("Quantos gols na partida {}? ".format(i))))

# chave 'Gols' receberá uma cópia de gol[]
jogador["Gols"] = gol[:]
jogador["Total"] = sum(gol)

print("-=-" * 20)
print(jogador)

print("-=-" * 20)
for v, k in jogador.items():
    print("O campo {} tem valor {}".format(v, k))

print("-=-" * 20)
print("O jogador {} jogou {} partidas.".format(jogador["Nome"], len(jogador["Gols"])))
for i, v in enumerate(jogador["Gols"]):
    print("    => Na partida {}, fez {} gols.". format(i, v))
print("Foi um total de {} gols.".format(jogador["Total"]))

# enumerate() pega o indice da lista e seu valor!
# itens() pega chave e valor do dicionário!

# ao igualar uma lista com outra, elas ficam "ligadas" se mudarmos algum item em uma achando que a outra não irá alterar,
# dá errado, as duas vão mudar. (b = a)
# o correto é fazer uma cópia (b = a[:]), lê-se "B recebe uma cópia de A", assim conseguiremos alterar a lista B sem mexer em A.

# em dicionários usamos copy()