lista = []
for posicao in range(0, 5):
     lista.append(int(input("Digite um valor para a posição {}:  ".format(posicao))))

print("-="*25)

print("Você digitou os valores: {}".format(lista))
print("O maior valor digitado foi o {} na posição {} ".format(max(lista), lista.index(max(lista))))
print("O menor valor digitado foi o {} na posição {}".format(min(lista), lista.index(min(lista))))

#COLOCAR MAIS POSIÇÕES DOS REPETIDOS
