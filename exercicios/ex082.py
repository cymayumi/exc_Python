i = "S"
listaNum = []
listaPar = []
listaImpar = []

while i != "N":
    num = int(input("Digite um valor: "))

    if num % 2 == 0:
        listaPar.append(num)
    else:
        listaImpar.append(num)

    listaNum.append(num)
    i = (input("Quer continuar? [S/N] ")).upper()

print("Você digitou a lista {}.".format(listaNum))
print("Os números pares da sua lista são {}.".format(listaPar))
print("Os números ímpares da sua lista são {}.".format(listaImpar))