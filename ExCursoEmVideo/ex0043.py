#IMC é  calculado dividindo o peso (em kg) pela altura ao quadrado (em metros).

h = float(input("\033[97mINFORME SUA ALTURA (m) : \n"))
kg = float(input("INFORME SEU PESO (kg) : \n"))
imc = kg / (h * h)
if imc < 18.5:
    print("Seu IMC é {:.1f} = ABAIXO DO PESO".format(imc))
elif 18.5 <= imc <= 25:
    print("Seu IMC é {:.1f} = PESO IDEAL".format(imc))
elif 25 <= imc <= 30:
    print("Seu IMC é {:.1f} = SOBREPESO".format(imc))
else:
    print("Seu IMC é {:.1f} =  ACIMA DO PESO".format(imc))
#terminar
