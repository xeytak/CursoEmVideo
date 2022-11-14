lanche = ("Hamburguer", "Pizza", "Suco", "Pudim")   #TUPLA
#         (0              1         2       3  ) posições
#Tuplas são imutáveis:
#           ex:   lanche[1] = "doce" -> gera erro no programa.

print(lanche)
print(lanche[1])      #FORMA USADA NO EX 72
print(lanche[1:3])    # do 1 até o 2 pois ignora o ultimo termo
print(lanche[-1])     # o último, -2 penúltimo, -3 antepenúltimo e assim por diante.
print(lanche[0:])     # do primeiro até o final
print(lanche[2:])

print("-=" * 25)
for comida in lanche:     # Para comida têm-se os lanches
    print("Eu vou comer {}".format(comida))
print("Comerei pra caramba!")

print("-="*25)

for cont in range(0, len(lanche)):  #len conta quantos valores tem na variavel
    print("Eu vou comer {}".format(lanche[cont]))

print("-="*25)

for pos, comida in enumerate(lanche):    #Para a posição dos itens (comidas) da tupla lanche
    print("Eu vou comer {} na posição {}".format(comida, pos))

print("-="*25)
#duas formas de se usar.

print(sorted(lanche))  # sorted é usado para odernar uma lista

print("-="*25)

a = (0, 1, 2)
b = (3, 4, 5)
c = b+a
print(c) # nesse caso, o sinal + irá juntas os itens das variáveis na ordem de cada uma.

print(len(c))   #mostra quantos itens tem na lista

print(c.count(2))  #conta quantos itens, que voce escolhe, tem na lista.

print("-="*25)

