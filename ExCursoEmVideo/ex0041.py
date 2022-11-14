#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade:
#- Até 9 anos: MIRIM
#- Até 14 anos: INFANTIL
#- Até 19 anos: JÚNIOR
#- Até 25 anos: SÊNIOR
#- Acima de 25 anos: MASTER

ano = int(input("\033[34mInforme seu ano de nascimento: \n"))
idade = 2022 - ano
print("\033[97mO(A) atleta tem {} anos".format(idade))
if idade <= 9:
    print("SUA CATEGORIA É A MIRIM!")
elif 9 < idade <= 14:
    print("SUA CATEGORIA É A INFANTIL")
elif 14 < idade <=19:
    print("SUA CATEGORIA É A JÚNIOR")
elif 19 < idade <= 25:
    print("SUA CATEGORIA É A SÊNIOR")
else:
    print("SUA CATEGORIA É A MASTER")
