lista = []
cont = 0
while True:
    lista.append(int(input("Digite um valor: ")))
    lista.sort(reverse=True)
    cont += 1
    continuar = str(input("Deseja continuar? [S/N]  ")).strip().upper()
    if continuar == "N":
        break
if 5 not in lista:
    print("O número 5 não está contido na lista!")
else:
    print("O número 5 está contido na lista!")
print("Você digitou {} elementos".format(cont))  # Poderia usar o len
print("A lista em ordem decrescente é {}".format(lista))
