#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#- O primeiro valor é maior
#- O segundo valor é maior
#- Não existe valor maior, os dois são iguais

v1 = int(input("\033[34mEscolha o primeiro valor: \n"))
v2 = int(input("Escolha o segundo valor: \n"))
if v1 > v2:
    print("\033[33mO primeiro valor é maior!")
elif v1 < v2:
    print("\033[33mO segundo valor é maior!")
else:
    print("\033[31mNão existe valor maior, os dois são iguais!")

