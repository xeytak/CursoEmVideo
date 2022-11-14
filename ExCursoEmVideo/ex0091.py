from random import randint   # MELHORAR O PROGRAMA DEPOIS

print("Valores sorteados: ")

jogadores = {}
jogadores['jogador 1'] = randint(1, 7)
jogadores['jogador 2'] = randint(1, 7)
jogadores['jogador 3'] = randint(1, 7)
cont = 1

for k, v in jogadores.items():
    print("O {} tirou {} no dado".format(k, v))
print("-=" * 20)
print("=== RANKING DOS JOGADORES ===")

for i in sorted(jogadores, key=jogadores.get, reverse=True):
    print("{}º lugar: {} com {}".format(cont, i, jogadores[i]))
    cont += 1





