lista = []
maior = 0
menor = 0
listPosMenor = []
listPosMaior = []

for i in range(5):
    lista.append(int(input("Digite o valor para a posição {}: ".format(i))))

    if i == 0:
        maior = menor = lista[i]
    else:
        if lista[i] > maior:
            maior = lista[i]
        if lista[i] < menor:
            menor = lista[i]

for indice, valor in enumerate(lista):
    if valor == maior:
        listPosMaior.append(indice)

for indice, valor in enumerate(lista):
    if valor == menor:
        listPosMenor.append(indice)

print("Você digitou a seguinte lista {}: ".format(lista))
print("O maior número é {} e está nas posições {}.".format(maior, listPosMaior))
print("O menor número é {} e está nas posições {}.".format(menor, listPosMenor))
