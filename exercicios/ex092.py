from datetime import datetime
dados = {}

dados["Nome"] = input("Digite o seu nome: ")
nascimento = int(input("Digite seu ano de nascimento: "))
dados["Idade"] = datetime.now().year - nascimento

dados["CTPS"] = int(input("Número da CTPS (caso não tenha digite 0): "))

if dados["CTPS"] != 0:
    dados["Contratacao"] = int(input("Digite seu ano de contratação: "))
    dados["Salario"] = float(input("Digite seu salário: R$ "))
    dados["Aposentadoria"] = dados["Idade"] + ((dados["Contratacao"] + 35) - datetime.now().year)

print("-=-" * 20)

for c, v in dados.items():
    print("   - {} tem o valor {}.".format(c, v))
