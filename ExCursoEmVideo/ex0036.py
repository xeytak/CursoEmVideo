#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

vc = float(input("Informe o valor do imovél? \n"))
s = float(input("Quanto você ganha mensalmente? \n"))
t = float(input("Em quantos anos você irá pagar? \n"))
pm = vc / (12 * t)   # pagamento mensal
if pm > 30/100 * s:
    print("EMPRÉSTIMO NEGADO!. A parcela será de R${:.2f}".format(pm))
else:
    print("EMPRÉSTIMO ACEITO!. A parcela será de R${:.2f}".format(pm))

