def area(largura, comprimento):
    a = largura * comprimento
    print("As dimensões de {}x{} tem a área de {:.2f}m²".format(l, c, a))


#PROGAMA PRINCIPAL:

print(" Controle de Terrenos")
print("=" * 25)

l = float(input("Largura:  "))
c = float(input("comprimento:  "))
area(l, c)

