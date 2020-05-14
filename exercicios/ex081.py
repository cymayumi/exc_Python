i = "S"
listaNum = []


while i != "N":
    num = listaNum.append(int(input("Digite um valor: ")))
    i = (input("Quer continuar? [S/N] ")).upper()

if 5 not in listaNum:
    print("Sua lista não tem o número 5!")
else:
    print("O número 5 se encontra em sua lista!")

print("Você digitou {} números.".format(len(listaNum)))
listaNum.sort(reverse=True)
print("Sua lista em ordem decrescente é {}".format(listaNum))
