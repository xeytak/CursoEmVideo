num = [2, 5, 9, 1]  # ADICIONAR OUTRO NUMERO NO LUGAR DE OUTRO PELA SUA POSIÇÃO DA LISTA -> 0,1,2,3

num[1] = 2
num.append(7)             #PARA ACRESCENTAR UM NUMERO NA LISTA
num.sort()                #USADO PARA POR EM ORDEM UMA LISTA
num.sort(reverse=True)    #COLOCAR UMA LISTA AO CONTRÁRIO
num.insert(3, 8)          #INSERIR O NUMERO 8 NA POSIÇÃO 3, OU SEJA, INSERIR UM VALOR EM UMA DADA POSIÇÃO ESCOLHIDA
num.pop(2)                #PARA ELIMINAR UM ELEMENTO

if 5 in num:
    num.remove(5)        #PARA REMOVER O NUMERO DA LISTA
else:
    print("Não achei o numero 5")

print(num)
print("Essa lista tem {} elementos".format(len(num)))  #len conta quantos itens tem na lista e percorre eles.

print("-="*20)

valores = []
valores.append(7)
valores.append(8)
valores.append(9)

for p, v in enumerate(valores):
    print("Na posiçao {} achei o valor {}!".format(p+1, v))


print("-="*20)

valores = []
for dig in range(0, 4):            #Para ler valores e depois haver contagem das suas posições
    print(int(input("digite um valor:  ")))

    for p, v in enumerate(valores):
     print("Na posiçao {} achei o valor {}!".format(p+1, v))


print("-="*20)

a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print("A lista A: {}".format(a))
print("A lista B: {}".format(b))
