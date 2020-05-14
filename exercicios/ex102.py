def fatorial(numero, show=False):
    """
    Função irá calcular o fatorial de um número. Com a OPÇÃO de mostrar ou não o cálculo!
    False = não mostra
    True = mostra o cálculo.

    """
    fat = 1
    for cont in range(1, numero+1):
        if show:
            print(cont, end=' ')
            if cont < numero:
                print(" x ", end=' ')
            else:
                print(" = ", end='')
        fat = cont * fat
    return fat


print(fatorial(5, True))
help(fatorial)
