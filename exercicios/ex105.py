def notas(*num, sit=False):
    r = {}
    r["total"] = len(num)
    r["maior"] = max(num)
    r["menor"] = min(num)
    r["media"] = sum(num)/len(num)
    if sit:
        if r["media"] >= 7:
            r["situação"] = "BOA"
        else:
            r["situação"] = "RUIM"
    return r


resposta = notas(9.5, 10, 3.2, sit=True)
print(resposta)