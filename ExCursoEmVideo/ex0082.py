lista = []
listaDeNumPares = []
listaDeNumImpar = []
while True:
    lista.append(int(input("Digite um número:  ")))
    resp = str(input("Quer continuar? [S/N]  ")).strip().upper()
    if resp == "N":
        break
for n in range(len(lista)):
    if lista[n] % 2 == 0:
        listaDeNumPares.append(lista[n])
    if lista[n] % 2 != 0:
        listaDeNumImpar.append(lista[n])
print("A lista completa é {}".format(lista))
print("A lista de números pares {}".format(listaDeNumPares))
print("A lista de números impares é {}".format(listaDeNumImpar))
