
matriz = [[], [], []]
cont = 0

for linha in range(1, 4):
    for coluna in range(1, 4):
        num = matriz.append(int(input("Digite um valor para a posição a{}{}:  ".format(linha, coluna))))
        cont += 1
        if cont == 3:
            matriz[0].append(num)
        if 3 < cont < 6:
            matriz[1].append(num)
        else:
            matriz[2].append(num)
print("{}\n{}\n{}".format(matriz[0], matriz[1], matriz[2]))

#TERMINAR
