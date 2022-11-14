#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
# de acordo com a média atingida:
#- Média abaixo de 5.0: REPROVADO
#- Média entre 5.0 e 6.9: RECUPERAÇÃO
#- Média 7.0 ou superior: APROVADO

n1 = float(input("\033[35mInforme sua primeira nota: \n"))
n2 = float(input("Informe sua segunda nota: \n"))
m = (n1 + n2) / 2
if m < 5:
    print("\033[31mVOCÊ ESTÁ REPROVADO!")
    print("Sua média foi {:.1f}".format(m))
elif 5 <= m <= 6.9:
    print(("\033[33mVOCÊ ESTÁ DE RECUPERAÇÃO!"))
    print("Sua média foi {:.1f}".format(m))
else:
    print("\033[32mPARABÉNS! APROVADO!")
    print("Sua média foi {:.1f}".format(m))

