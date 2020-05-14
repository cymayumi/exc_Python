jogador = {}
gol = []
time = []

while True:
    jogador.clear() #apaga cada 'jogador' ao começar o laço, zera o dicionário
    jogador["Nome"] = input("Nome do Jogador: ")

    num = int(input("Quantas partidas {} jogou? ".format(jogador["Nome"])))
    gol.clear()
    for i in range(num):
        gol.append(int(input("Quantos gols na partida {}? ".format(i))))

    # chave 'Gols' receberá uma cópia de gol[]
    jogador["Gols"] = gol[:]
    jogador["Total"] = sum(gol)
    time.append(jogador.copy())

    resp = input("Quer continuar? [S/N] ").upper()
    if resp == "N":
        break

print("-=-" * 20)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()

print("-=-" * 20)
for k, v in enumerate(time):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()

print("-=-" * 20)
while True:
    busca = int(input("Mostrar dados de qual jogador? (999 para sair) "))
    if busca == 999:
        break
    if busca >= len(time):
        print("Não existe jogador com esse código!")
    else:
        print("Dados do jogador {} :".format(time[busca]["Nome"]))
        for i, g in enumerate(time[busca]["Gols"]):
            print(f'     No jogo {i+1} fez {g} gols.')
    print("-=-" * 20)
print("<< VOLTE SEMPRE!>>")
