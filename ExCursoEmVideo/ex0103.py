def ficha(nome="<desconhecido>", gol=0):
     print("O jogador {} fez {} gols".format(nome, gol))


#PROGRAMA PRINCIPAL:

jogador = str(input("Nome do jogador:  "))     #string
m = str(input("Gols marcados:  "))      #inteiro

if m.isnumeric():
    m = int(m)
else:
    m = 0
if jogador.strip() == "":
    ficha(gol=m)
else:
    ficha(jogador, m)






