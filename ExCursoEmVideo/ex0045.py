import random
itens = ['Pedra', 'Papel', 'Tesoura']
escolhamaq = random.choice(itens)
op = print('''Suas opções:
[ 1 ] PEDRA
[ 2 ] PAPEL 
[ 3 ] TESOURA''')
escolha = int(input("Qual será sua esolha?  "))

print("A maquina escolheu {}".format(escolhamaq))
print("jogador {}".format((escolha)))

#REFAZER




