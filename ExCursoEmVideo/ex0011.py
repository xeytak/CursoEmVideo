l = float(input("Qual a largura da parede? \n"))
h = float(input("Qual a altura da parede? \n"))
a = l * h
t = a / 2
print("A área da parede mede {}m²,logo, precisará de {:.0f}L de tinta!".format(a, t))
