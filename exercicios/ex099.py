def maior(* num):
    cont = maior = 0
    print("Analisando os valores passados...")
    for valor in num:
        print("{}".format(valor), end=' ')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print("Foram informados {} valores ao todo.".format(cont))
    print("O maior valor informado foi {}.".format(maior))

maior(10, 8, 11, 2, 3)
