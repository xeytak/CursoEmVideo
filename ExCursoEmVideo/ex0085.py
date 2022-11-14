valores = [[], []]

for pergunta in range(1, 8):
    num = int(input("Digite o {} valor:  ".format(pergunta)))
    if num % 2 == 0:
        valores[0].append(num)
    else:
        valores[1].append(num)

valores[0].sort()
valores[1].sort()
print("Os valores pares foram {}".format(valores[0]))
print("Os valores ímpares foram {}".format(valores[1]))
