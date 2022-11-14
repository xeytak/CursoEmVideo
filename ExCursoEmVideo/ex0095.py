time = []                #TERIMAR
jogador = {}
golpart = []

while True:
    jogador['nome'] = str(input("Nome: "))
    partidas = int(input("Quantas partidas jogou {}? ".format(jogador['nome'])))

    for gp in range(0, partidas):
         golpart.append(int(input("Quantos gols na partida {}? ".format(gp))))
         jogador['gols'] = golpart
         jogador['total'] = sum(golpart)
    while True:
         resp = str(input("Quer continuar? [S/N]  ")).strip().upper()
         if resp not in "SN":
          print("Opção inválida. Tente novamente.")

         if resp == "N":
                break
    for k, v in jogador.items():
        print("O campo {} tem valor {}".format(k, v))
    print(("O jogador {} jogou {} partidas ").format(jogador['nome'], partidas))

    for i, marcados in enumerate(jogador['gols']):
        print("Na partida {}, fez {} gols".format(i, marcados))


