m = float(input("Uma distância em metros:"))
cm = m * 100
mm = m * 1000
km = m / 1000
print("A medida de {:.0f} metros em centímetros é {:.0f},em milimetros {:.0f},\nJá em Kilômetros é {}".format(m, cm, mm, km))
#Poderia ser: .format(m, m*100, m*1000)

