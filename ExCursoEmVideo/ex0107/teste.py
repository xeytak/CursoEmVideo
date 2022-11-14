#PROGRAMA PRINCIPAL

import moeda

p = float(input("Digite um valor: R${} ").format(moeda(p)))
print("A metade de R${:.2f} é R${:.2f}".format(p, moeda.metade(p)))
print("O dobro de R${} é R${}".format(p, moeda.dobro(p)))
print("Aumetando preço em 10%, temos R$ ".format(moeda.aumentar(p, 10)))

 #Transformar em str