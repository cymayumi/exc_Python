contador = 1
totalIdade = 0
contaIdade = 0
maior = 0
menor = 0
nomeVelho = " "
nomeNovo = " "

for contador in range(1, 5):
    print("-----------  {}ª PESSOA  -----------".format(contador))
    nome = input("Nome: ").strip()

    idade = int(input("Idade: "))
    totalIdade = idade + totalIdade

    sexo = input("Sexo [F/M]: ").strip()

    if sexo.upper() == "F":
        if idade < 20:
            contaIdade = 1 + contaIdade

    if contador == 1:
        menor = idade
        nomeNovo = nome

    if sexo.upper() == "M" and contador > 1:
        if idade < menor:
            menor = idade
            nomeNovo = nome

    if sexo.upper() == "M":
        if idade > maior:
            maior = idade
            nomeVelho = nome


print("\nA idade média do grupo é {} anos.".format(totalIdade / 4))
print("O homem mais VELHO é o {} e ele tem {} anos.".format(nomeVelho, maior))
print("O homem mais NOVO é o {} e ele tem {} anos.".format(nomeNovo, menor))
print("Temos {} mulheres com menos de 20 anos".format(contaIdade))