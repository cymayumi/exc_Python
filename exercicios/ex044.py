soma = 0
fim = 0
ok = 1

print("\033[35m-=-=-=-=-=-=-=-=-=-  LOJAS PYTHON  -=-=-=-=-=-=-=-=-=-\n\033[m")

print("Olá! Vamos verificar tudo o que foi comprado...")

while ok == 1:
    item = input("Digite qual o seu item: ")
    total = float(input("Digite o valor deste produto: R$"))
    soma = total + soma
    ok = int(input("\nContinuar adicionando produtos? 1-SIM 2-NAO "))

while fim != 1:
    menuPgto = int(input("\nO valor total da compra é \033[1:31mR${:.2f}\033[m. Estas são as opções de pagamento:"
                         "\n    1- À vista DINHEIRO/CHEQUE com 10% de desconto."
                         "\n    2- À vista no CARTÃO com 5% de desconto."
                         "\n    3- Em 2x NO CARTÃO com o preço normal."
                         "\n    4- Em 3x OUMAIS NO CARTÃO com 20% de juros."
                         "\nPor qual você irá optar? ".format(soma)))

    if menuPgto == 1:
        valorFinal = soma * 0.9
        print("\nVocê optou por \033[4mpagar à vista em dinheiro/cheque\033[m. Seu valor final ficou "
              "em \033[1:34mR${:.2f}\033[m".format(valorFinal))
        print("Obteve um desconto de \033[1:32mR${:.2f}\033[m".format(soma - valorFinal))
        fim = int(input("Finalizar pagamento ou escolher outra opção? 1-FINALIZAR 2-OUTRA "))

    elif menuPgto == 2:
        valorFinal = soma * 0.95
        print("\nVocê optou por \033[4mpagar à vista no cartão\033[m. Seu valor final ficou "
              "em \033[1:34mR${:.2f}\033[m".format(valorFinal))
        print("Obteve um desconto de \033[1:32mR${:.2f}\033[m".format(soma - valorFinal))
        fim = int(input("Finalizar pagamento ou escolher outra opção? 1-FINALIZAR 2-OUTRA "))

    elif menuPgto == 3:
        print("\nVocê optou por \033[4mpagar em 2x no cartão\033[m. Seu valor final ficou "
              "em \033[1:34mR${:.2f}\033[m".format(soma))
        print("Nenhum desconto ou juros será aplicado!")
        fim = int(input("Finalizar pagamento ou escolher outra opção? 1-FINALIZAR 2-OUTRA "))

    else:
        valorFinal = soma * 1.2
        print("\nVocê optou por \033[4mpagar em 3x ou mais no cartão\033[m. Seu valor final ficou "
              "em \033[1:34mR${:.2f}\033[m".format(valorFinal))
        print("Terá um acréscimo de \033[1:32mR${:.2f}\033[m".format(valorFinal - soma))
        fim = int(input("Finalizar pagamento ou escolher outra opção? 1-FINALIZAR 2-OUTRA "))

print("\n\033[1:31:40m  Você concluiu sua compra com sucesso!!!  \033[m")