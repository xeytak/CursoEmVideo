num = ""
soma = ""
cont = 0
contnum = 0
digitos = ""

while num != 999:
    num = int(input("Digite um número [999 para parar] :  "))
    cont += num
    soma = cont - 999
    contnum += 1
    digitos = contnum - 1
print("\033[35mVocê digitou {} números".format(digitos))
print("\033[35mA soma foi entre eles foi {}".format(soma))
print("Fim.")

