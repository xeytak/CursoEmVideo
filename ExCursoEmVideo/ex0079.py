lista = []
contrepetido = 0
while True:
    num = int(input("Digite um valor:  "))
    resposta = str(input("Deseja continuar ? [S/N]  ")).strip().upper()
    if num not in lista:
        lista.append(num)
        print("Valor armazenado com sucesso.")
    else:
        print("Número repetido, digite outro")
    lista.sort()
    if resposta == "N":
        print("fim do programa")
        break
print("Foi digitado os números {}".format(lista))






