s = str(input("Informe seu sexo [M/F]:  ")).upper().strip()
while s != "M" and s != "F":
    s = str(input("Dados invalidos,digite novamente:  ")).upper().strip()
print("sexo {} registrado".format(s))

