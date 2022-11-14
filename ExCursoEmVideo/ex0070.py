print("LOJA VEM QUE TEM!")
print("-=" * 15)
somapreco = 0
produtomil = 0
menorpreco = 0
cont = 0
while True:
    produto = str(input("Nome do produto:  ")).strip()
    preco = float(input("Qual o preço do produto? R$"))
    continuar = str(input("deseja continuar? [S/N]  ")).strip().upper()
    print("-~"*15)
    cont += 1
    somapreco += preco
    if preco > 1000:
        produtomil += 1
    if preco > menorpreco:
        menorpreco = preco
    if continuar == "N":
        break
    if cont == 1:
        menorpreco = preco
    else:
        if preco < menorpreco:
         menorpreco = preco
print("O total da sua compra foi de R${:.2f}".format(somapreco))
print("Tivemos {} produtos acima de R$1000".format(produtomil))
print("O produto mais barato custou R${}".format(menorpreco))

#TERMINAR ULTIMA PARTE
