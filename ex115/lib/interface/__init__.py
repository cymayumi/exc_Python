def linha(tam = 42):
    return "-" * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print("\n\033[31m ERRO: Por favor, digite um número inteiro válido. \033[m")
            continue
        except(KeyboardInterrupt):
            print("\n\033[31m Usuário preferiu não digitar esse número. \033[m")
            return 0
        else:
            return n


def menu(lista):
    cabecalho("MENU PRINCIPAL")
    c = 1
    for item in lista:
        print("   {} - {}".format(c, item))
        c += 1
    print(linha())
    opc = leiaInt("Sua opção: ")
    return opc