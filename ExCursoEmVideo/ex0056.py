contidade = 0   # quantidade de mulher menor que idade (20)
maioridadeh = 0
nomevelho = ""
contmulher = 0
for pessoa in range(1, 4):
    print("---- {}ª pessoa ----".format(pessoa))
    nome = str(input("NOME:  "))
    idade = int(input("IDADE:  "))
    sexo = str(input("SEXO [M/F]:  ")).upper()
    contidade += idade / 4                       #somatório de todas idades
    if pessoa == 1 and sexo == "M":           # Se a primeira pessoa for homem a maior idade, até o momento, será dela.
        maioridadeh = idade
        nomevelho = nome
    if sexo == "M" and idade > maioridadeh:         #proxima idade digitada > maioridadehomem
        maioridadeh = idade                         # a maior idade será a idade digitada antes maior que a inicial
        nomevelho = nome
    if sexo == "F" and idade < 20:
        contmulher += 1
print("média idade foi {}".format(contidade))
print("O homem mais velho tem {} anos e se chama {}".format(maioridadeh, nomevelho))
print("Ao todo {} mulheres com menos de 20 anos".format(contmulher))
