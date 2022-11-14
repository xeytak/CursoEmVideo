num = 0
soma = 0
while True:                #enquento for verdade irá mostrar o "num"
    num = int(input("Digite um número:  "))
    if num == 999:         # porém, se for igual 999, que é o flag, irá parar.
        break              # A condicional sempre primeiro no aninhamento.
    soma += num
print("A soma vale {}".format(soma))
    #print(f"A soma vale {soma})    nova fomra de escrever.
