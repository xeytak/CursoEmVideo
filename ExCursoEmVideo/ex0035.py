#Desenvolva um programa que leia o comprimento de três retas e
# diga ao usuário se elas podem ou não formar um triângulo.

# Propriedades :
#1) A soma de dois lados  tem que ser maior que o outro: a < b+c
#2)A diferença de dois lados tem que ser menor que o outro: a > b-c

import emoji
print("\033[0;31mANALISADOR DE TRIANGULOS\033[m")
a = float(input("Primeiro segmento:"))
b = float(input("Segundo segmento:"))
c = float(input("Terceiro segmento:"))
if a < b+c and b < a+c and c < b+a:
    print("Os três segmentos formam um triângulo!")
else:
    print("Os três segmentos não formam um triangulo!")


