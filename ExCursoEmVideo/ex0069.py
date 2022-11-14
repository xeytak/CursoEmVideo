print("CADASTRE UMA PESSOA")
print("-="*10)
conthomem = 0
contmulher = 0     #TIRAR DUVIDA SOBRE BREAK E CONTADORES
contpessoas = 0

while True:
    idade = int(input("idade:  "))
    sexo = str(input("sexo [M/F]:  ")).strip().upper()
    continuar = str(input("Deseja continuar? [S/N]  ")).strip().upper()
    print("-~"*10)
    if sexo == "M":
        conthomem += 1
    if sexo == "F" and idade < 20:
        contmulher += 1
    if idade > 18:
        contpessoas += 1
    if continuar == "N":
        break
print("Tivemos {} pessoas com idade acima dos 18 anos".format(contpessoas))
print("Ao todo foi {} homens cadastrados".format(conthomem))
print("E tivemos {} mulheres com menos de 20".format(contmulher))

