lista = []        #TERMINAR PROGRAMA
dados = {}
cont = 0
soma = 0
while True:
    dados['nome'] = str(input("Nome: "))
    dados['sexo'] = str(input("Sexo [M/F]: "))
    cont += 1
    while dados['sexo'] not in "MmFf":
        print("Erro! Tente novamente.")
        dados['sexo'] = str(input("Sexo [M/F]: "))

    dados['idade'] = int(input("Idade: "))
    resp = str(input("Continuar? [S/N]  ")).strip().upper()

    while resp not in "SsNn":
        print("Opção inválida.Tente novamente")
        resp = str(input("Continuar? [S/N]  "))

    soma += dados['idade']
    lista.append(dados.copy())
    if resp == "N":
        break
media = soma / cont
print("Ao todo tivemos {} pessoas ".format(cont))
print("A média das idades foi de {:.2f} anos".format(media))
for p in lista:
    if p['idade'] > media:
        for k, v in p.items():
            print("{} = {}".format(k, v))



