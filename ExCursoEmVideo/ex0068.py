from random import randint
contvitoria = 0

print("\033[m=" * 25)    #REFAZER!!
print("\033[35mVAMOS JOGAR PAR OU ÍMPAR!")
print("\033[m=" * 25)

while True:
    num = int(input("Digite um  valor:  "))
    escolha = str(input("Par ou Impar? [P/I]  ")).upper().strip()
    comp = randint(0, 10)
    print("=" * 25)
    resultado = num + comp
    print("Você jogou {} e o computador {}. O total deu {}".format(num, comp, resultado))

    if resultado % 2 == 0:
        if escolha == "P":
            print("Deu par. Você venceu!")
            contvitoria += 1
        else:
            print("GAMER OVER!")
            break
    if resultado % 2 != 0:
        if escolha == "I":
            print("Deu ímpar. Você venceu")
            contvitoria += 1
        else:
            print("GAMER OVER!")
            break
print("Voce venceu {} vezes".format(contvitoria))


