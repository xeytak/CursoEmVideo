contmaior = 0
contmenor = 0
for nas in range(1, 8):
    nas = int(input("Em qual ano nasceu a {}ª pessoa?  ".format(nas)))     # idade = 2022 - ano de nascimento
    idade = 2022 - nas
    if idade >= 18:
        contmaior += 1
    elif idade < 18:
        contmenor += 1
print(" {} pessoa(s) são de maior {}  pessoa(s) são de menor".format(contmaior, contmenor))

#ver aula sobre contadores e endentação
