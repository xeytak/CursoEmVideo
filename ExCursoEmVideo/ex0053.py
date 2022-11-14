f = str(input("\033[35mDigite uma frase:  ").upper()).strip()
nome = f.replace(" ", "")
inv = f[::-1]
pld = inv.replace(" ", "")
print("\033[97mO inverso de  {} é {}".format(nome, pld))
if nome == pld:
    print("\033[34mÉ UM PALÍNDROMO!")
else:
    print("\033[31mNÃO É UM PALÍNDROMO!")
