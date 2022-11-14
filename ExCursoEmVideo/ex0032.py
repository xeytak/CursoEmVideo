#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
#Numero divisivel por 4
#Divisivel por 4, mas nao por 100
#Se for divisivel por 100, nao sera bisexto se for por 400

ano = int(input("Digite algum ano: \n")) #refazer hoje
b = ano % 4
nb = ano % 400
if b == 0:
    print("bissexto")
else:
    if nb > 0
    print("nao bissexto")


