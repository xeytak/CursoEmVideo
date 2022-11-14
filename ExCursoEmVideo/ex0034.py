# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

s = float(input("Qual é o seu salário: \n"))
if s > 1250:
    a1 = s * 1.10
    print("Você terá aumento de 10%,e receberá agora {}".format(a1))
if s <= 1250:
    a2 = s * 1.15
    print("Você terá aumento de 15%, e receberá agora {}".format(a2))
