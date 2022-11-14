#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

import math
num = float(input("Digite um numero:"))       #não se usa int
i = math.trunc(num)
print("A porção inteira do numero {} é {}".format(num, i))


