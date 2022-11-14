p = float(input("Qual é o preço? \n R$" ))
d = (5 * p) / 100
n = p - d
print("O desconto de 5% do produto vale R${:.1f} e passará a custar R${}".format(d, n))


