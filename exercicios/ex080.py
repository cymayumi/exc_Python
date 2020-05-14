lista = []

# script irá ordenar cinco valores sem utilizar a função sort()

for i in range(5):
    num = int(input("Digite um valor: "))

    if i == 0 or num > lista[len(lista) - 1]:  # verifica se o num é maior do que o último da lista
        lista.append(num)
        print("Adicionado no final da lista...")
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print("Adicionado na posição {}.".format(pos))
                break
            pos += 1
print("Os valores digitados foram {}.".format(lista))