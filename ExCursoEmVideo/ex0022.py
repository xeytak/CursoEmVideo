#Crie um programa que leia o nome completo de uma pessoa e mostre:
#- O nome com todas as letras maiúsculas e minúsculas.
#- Quantas letras ao todo (sem considerar espaços).
#- Quantas letras tem o primeiro nome.

nome = str(input("Digite seu nome compeleto: \n")).strip()
print("Seu nome só em letra maiúscula é: {}".format(nome.upper()))    # nome.upper()
print("Seu nome em minúscula é: {}".format(nome.lower()))    # nome.lower()
print("Seu nome tem ao todo {} letras".format(len(nome) - nome.count(" ")))    #len - count
#print("Seu primeiro nome tem {} letras ".format(nome.find(" ")))
separa = nome.split()
print("Seu primeiro nome é {} e tem {} letras".format(separa[0], len(separa[0])).strip())# <-- obs


