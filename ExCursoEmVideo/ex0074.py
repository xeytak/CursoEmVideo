import random
maior = 0
numeros = random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), \
          random.randint(1, 10)  #TUPLA
ordem = sorted(numeros)
print("Os valores sorteados foram : {}".format(numeros))
print("O maior valor é {}".format(ordem[-1]))
print("O menor valor é {}".format(ordem[0]))
