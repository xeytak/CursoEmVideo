print("         NÚMEROS MEGA SENA")
print("="*35)

from random import randint
from time import sleep

lista = []
cont = 0

totjogos = int(input("Quantos jogos você quer gerar?  "))

for p in range(1, totjogos+1):
    num = randint(1, 61)
    if num not in lista:
        lista.append(num)
        cont += 1
    if cont >= 6:
        break
    print("Jogo {}: {}".format(p, lista))
    sleep(1)

# VOLTAR EM TERMINAR !!!!

















