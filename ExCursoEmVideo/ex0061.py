print("\033[36mGerador de Progressão Aritmética")
print("-=" * 17)
a1 = int(input("\033[mDigite o primeiro termo:  "))
r = int(input("Razão:  "))
termo = a1
cont = 1
while cont <= 10:
    print(" {} ->".format(termo), end="")
    termo += r
    cont += 1
print(" Fim.")
