import moeda
# esta com esse erro de referencia porque o pycharm intende que o modulo está num pacote ex107, poderiamos fazer
# from ex107 import moeda

p = float(input("Digite o preço: R$ "))

print("A metade do preço é R${}.".format(moeda.metade(p)))
print("A dobro do preço é R${}.".format(moeda.dobro(p)))
