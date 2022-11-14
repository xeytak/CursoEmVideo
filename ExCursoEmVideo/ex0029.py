# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

v = int(input("Velocidade atual do carro: \n"))
lim = 80
if v > lim:
    multa = (v - lim) * 7
    print("Você ultrapassou o limite de 80km/h, terá de que pagar R${} de multa.".format(multa))
else:
    print("Está na velocidade permitida,boa viajem!")


