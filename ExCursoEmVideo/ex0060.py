# USANDO FOR :

n = int(input("Digite um número e veja seu fatorial:  "))
fatorial = 1
for antecessor in range(n, 1, -1):
    fatorial *= antecessor
print("\033[36mfatorial de {} é {}.".format(n, fatorial))

# DEPOIS FAZER USANDO WHILE
