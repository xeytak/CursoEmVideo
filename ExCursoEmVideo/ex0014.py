c = float(input("Informe a temperatura em °C: \n"))
f1 = 9 * c       # ou -> f = (9 * c) / 5 + 32
f2 = 160 + f1
f3 = f2 / 5
print("Convertendo {}°C para Fahrenheit,será de {}".format(c, f3))
