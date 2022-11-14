contnum = 0
media = 0
soma = 0
resp = "S"
maior = menor = 0

while resp == "S":
    num = int(input("Digite um numero: "))
    resp = str(input("Deseja prosseguir? [S/N]  ")).upper().strip()
    contnum += 1
    soma += num
    media = soma / contnum
    if contnum == 1:
      maior = menor = num
    else:
        if num > maior:  # o proximo valor que for digitado
            maior = num
        if num < menor:
            menor = num

print("Você digitou {} números. A soma entre eles foi {} ".format(contnum, soma))
print("A média entre eles foi {}".format(media))
print("O maior valor foi {} e o menor {}".format(maior, menor))



