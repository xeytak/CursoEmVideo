
cadastro = {}
cadastro['nome'] = str(input("Nome: "))
cadastro['idade'] = 2022 - int(input("Ano de nascimento: "))
cadastro['carteira'] = int(input("Carteira de Trabalho (0 nã tem): "))

if cadastro['carteira'] != 0:
    cadastro['contrato'] = int(input("Ano de contrato: "))
    cadastro['salario'] = int(input("Salário: R$"))
    cadastro['aposentadoria'] = cadastro['idade'] + (cadastro['contrato'] + 35) - 2022

for k, v in cadastro.items():
    print(" - {} tem o valor {}".format(k, v))
