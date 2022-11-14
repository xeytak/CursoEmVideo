import math
co = float(input("Digite o cateto oposto:"))
ca = float(input("Digite o cateto adjacente:"))
h = math.sqrt(co*co + ca*ca)
print("O comprimento da hipotenusa é {:.2f}".format(h))

#poderia ser :
# h = math.hypot(co,ca)