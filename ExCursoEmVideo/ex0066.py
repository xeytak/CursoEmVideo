soma = 0
contnum = 0
while True:
    num = int(input("Digite um número: \n "))
    if num == 999:
        break
    soma += num
    contnum += 1
print("\033[35mA soma dos números foi {}".format(soma))
print("Você digitou {} numeros".format(contnum))
print("\033[mfim.")
