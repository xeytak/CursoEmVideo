from random import randint


def sorteia(lista):
    for valores in range(0, 5):
        numeros.append(randint(1, 10))
    print("Sorteando 5 valores temos {}".format(numeros))


def somapar(lista):         # o argumento nos parenteses é um valor de entrada para outros.
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print("Somamdo os valores pares de {} temos {}".format(lista, soma))


numeros = []
sorteia(numeros)
somapar(numeros)


