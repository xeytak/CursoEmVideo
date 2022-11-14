
lista = list()
dados = list()

while True:
    nome = dados.append(str(input("Nome: ")))
    n1 = dados.append(int(input("Nota 1: ")))
    n2 = dados.append(int(input("Nota 2: ")))
    lista.append(dados[:])
    dados.clear()
    resp = str(input("Deseja por mais dados? [S/N]  ")).strip().upper()
    if resp == "N":
        break
for p in lista:                    # p = pessoa
    print(p[0].center(25), end="")
    print(lista.index(p), end="")


for m in lista:                # m = media
    media = (m[1] + m[2]) / 2






