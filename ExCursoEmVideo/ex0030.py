# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input("Digite um número: \n"))
r = num % 2
if r == 0:
    print("PAR")
else:
    print("IMPAR")
