def notas(*n, sit=False):

    cont = len(n)
    resp = {}
    resp['total'] = cont
    resp['maior'] = max(n)
    resp['menor'] = min(n)
    resp['media'] = sum(n) / len(n)
    if sit:
        if resp['media'] >= 7:
            resp['situação'] = "Boa"
        elif resp['media'] >= 5:
            resp['situação'] = "Razoável"
        else:
            resp['situação'] = "Ruim"
    return resp

resp = notas(5, 9, 7, sit=True)
print(resp)
help(notas)

# usar a docstring depois






# porque o print(resp) nao funciona fora ?