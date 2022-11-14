print("\033[35m=" * 24)
print("\033[35mSequência de Fibonacci")
print("=" * 24)
termos = int(input("\033[mQuantos termos deseja na sequencia?  "))
cont = 3
a1 = 0
a2 = 1
print("{} -> {} ".format(a1, a2), end="")
while cont <= termos:
    a3 = a2 + a1
    print("-> {}".format(a3), end="")
    a1 = a2
    a2 = a3
    cont += 1
print("\n\033[32mA sequência teve {} termos!".format(termos))
