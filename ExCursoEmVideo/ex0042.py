a = float(input("Primeiro segmento: \n"))
b = float(input("Segundo segmento: \n"))
c = float(input("Terceiro segmento: \n"))
eq = a == b == c
iso = a == b != c or a == c != b or b == c != a and  a < b+c and b < a+c and c < b+a
esc = a != b != c and  a < b+c and b < a+c and c < b+a
if iso:
    print("isoceles")
elif eq:
    print("equilatero")
elif esc:
    print("escaleno")
else:
    print("não é triangulo")
