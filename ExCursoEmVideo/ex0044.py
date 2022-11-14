p = float(input("Preço total das compras: \n R$"))
fp = print('''QUAL A FORMA DE PAGAMENTO?
[ 1 ] à vista no dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x vezes no vartão
[ 4 ] 3x ou mais no cartão''')
op = int(input("qual opção?: "))
din = p - (10/100 * p)
cart = p - (5/100 * p)
cart2x = p / 2
if op == 1:
    print("Você ganhou 10% de desconto, Total a ser pago: R${:.2f}".format(din))
elif op == 2:
    print("Você ganhou 5% de desconto, TOTAL A SER PAGO: RS${:.2f}".format(cart))
elif op == 3:
    print("Você parcelou em 2x. AS PARCELAS SERÃO RS${} CADA    ".format(cart2x))
elif op == 4:
    total = p + (20/100 * p)
    parcela = int(input("Em quantas vezes? :"))
    totalparc = total / parcela
    print("Você irá pagar com juros suas {} parcelas  de RS${:.2f} cada".format(parcela, totalparc ))
else:
    print("\033[33mOPÇÃO INVÁLIDA! Tente novamente.")






