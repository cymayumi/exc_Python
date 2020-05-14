dados = {}
lista = []
soma = media = 0

while True:
    dados.clear()
    dados["nome"] = input("Nome: ")

    while True:
        dados["sexo"] = input("Sexo: [F/M] ").upper()
        if dados["sexo"] in "MF":
            break
        print("Erro! Digite apena F ou M.")

    dados["idade"] = int(input("Idade: "))
    soma += dados["idade"]
    lista.append(dados.copy())

    status = input("Quer continuar? [S/N] ").upper()
    if status == "N":
        break

print("-=-" * 30)
print("Ao todo temos {} pessoas cadastradas.".format(len(lista)))

media = soma/len(lista)
print("A média de idade é {:5.2f}".format(media))

print("As mulheres cadastradas foram:")
for p in lista:
    if p["sexo"] == "F":
        print(p["nome"])
