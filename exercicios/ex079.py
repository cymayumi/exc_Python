i = "S"
listaNum = []
cont = 0

while i != "N":
    num = int(input("Digite um valor: "))

    if num not in listaNum:
        listaNum.append(num)
    else:
        print("Esse número já foi digitado e não será incluido novamente...")

    i = (input("Quer continuar? [S/N] ")).upper()

print("Sua lista é {}.".format(listaNum))
