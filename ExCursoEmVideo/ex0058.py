import random
valores = [0, 1, 2]
maq = random.choice(valores)
conttentativa = 0

print("""\033[33mOlá, sou seu computador...
Pensei em um número entre 0 a 10.
Qual será seu palpite?""")

num = int(input("\033[mDiga seu palpite:  "))
while num != maq:
    num = int(input("tente novamente: "))
    conttentativa += 1
print("voce acertou. Tentou {} vezes".format(conttentativa))



