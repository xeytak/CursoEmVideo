km = float(input("Quantos km foi percorrido? \n"))
d = float(input("Quantos dias ficou alugado? \n"))
p = km * 0.15 + d * 60
print("O total a ser pago será de R${:.2f}".format(p))


