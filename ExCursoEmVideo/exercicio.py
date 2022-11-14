idade = 2022 - int(input("ano de nascimento:  "))
sexo = str(input("Sexo [M/F]:  ")).strip().upper()
salario = float(input("Sálario mensal: "))
print("-="*20)
print("idade de {} anos ".format(idade))
print("Salário bruto de R${:.2f}".format(salario))

if sexo == "M":
    print("Sexo masculino")

elif sexo == "F":
    print("Sexo feminino")

if idade >= 40:
    abono = (15/100) * salario
    salarioabono = abono + salario
    print("Abono foi de R${:.2f}".format(abono))
    print("O salário bruto com abono é de R${:.2f}".format(salarioabono))

elif idade < 40:
    abono = (25/100) * salario
    salarioabono = abono + salario
    print("Abono foi de R${}".format(abono))
    print("O salário bruto com abono é de R${:.2f}".format(salarioabono))
