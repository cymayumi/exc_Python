from random import randint


def sorteia(lista):
    for cont in range(0, 5):
        lista.append(randint(1, 10))
    print(lista)


def somaPar(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    print("A soma dos valores pares é {}.".format(soma))


numeros = []
sorteia(numeros)
somaPar(numeros)
