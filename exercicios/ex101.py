def votar(anonascimento):
    from datetime import date
    # o escopo da importação está só dentro desta função (economiza memória pois não estará disponível em td código)

    idade = date.today().year - anonascimento
    if idade < 16:
        return "Você tem {} anos, portanto ainda NÃO VOTA.".format(idade)
    elif 16 >= idade < 18:
        return "Você tem {} anos, portanto voto OPICIONAL.".format(idade)
    else:
        return "Você tem {} anos, portanto voto OBRIGATORIO.".format(idade)


print("-=-" * 30)
ano = int(input("Em que ano você nasceu? "))
print(votar(ano))
