lista = []
dados = []
maior = 0
menor = 0
while True:
    dados.append(str(input("Nome:  ")))
    peso = dados.append(float(input("Peso:  ")))
    if len(lista) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]

    lista.append(dados[:])       #fatiamento
    dados.clear()
    resp = str(input("Deseja por mais dados? [S/N]  ")).strip().upper()
    if resp == "N":
        break
print("Ao todo, foi {} pessoas cadastradas".format(len(lista)))
print("O maior peso foi {:.2f}Kg".format(maior))
print("O menor peso foi {:.2f}".format(menor))
