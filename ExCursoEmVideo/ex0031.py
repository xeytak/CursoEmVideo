#Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

d = int(input("Qual é a distância da susa viagem em KM? \n"))
if d <= 200:
    pag = d * 0.50
    print("Você irá pagar R${}".format(pag))
else:
    pag = d * 0.45
    print("Você irá pagar R${}".format(pag))



