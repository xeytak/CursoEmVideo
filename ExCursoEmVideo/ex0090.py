'''aluno = {}
aluno['nome'] = str(input("Nome: "))
aluno['media'] = float(input("Média de {}:  ".format(aluno['nome'])))
print("-="*20)
print("- Nome é igual a {}".format(aluno['nome']))
print("- Média é igual a {}".format(aluno['media']))

if aluno['media'] < 6:
    print("- Situação é Reprovado")
else:
    print("- Situação é igual a \033[35mAprovado")'''
# CODIGO DO PROFESSOR:

aluno = {}
aluno['nome'] = str(input("Nome: "))
aluno['media'] = float(input("Média: "))
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
for k, v in aluno.items():
    print("{} é igual a {}".format(k, v))  # chave e valor = itens

print(aluno)
