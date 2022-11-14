jogador = {}
golpart = []

jogador['nome'] = str(input("Nome: "))
partidas = int(input("Quantas partidas jogou {}? ".format(jogador['nome'])))

for gp in range(0, partidas):
     golpart.append(int(input("Quantos gols na partida {}? ".format(gp))))
     jogador['gols'] = golpart
     jogador['total'] = sum(golpart)

print(jogador)

for k, v in jogador.items():
    print("O campo {} tem valor {}".format(k, v))
print(("O jogador {} jogou {} partidas ").format(jogador['nome'], partidas))

for i, marcados in enumerate(jogador['gols']):   # Para cada item "marcados" dentro da chave gols, retorna a posição i (índice) de marcados
    print("Na partida {}, fez {} gols".format(i, marcados))

 # íníndice = posição
