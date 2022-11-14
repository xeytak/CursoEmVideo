
valores = (int(input("Digite um número: ")),  #PARA TUPLAS USA-SE ()
int(input("Digite de novo um número: ")),
int(input("Digite mais um número: ")),
int(input("Digite o último número: ")))

print("Você digitou os valores {}".format(valores))
if 9 in valores:
    print("O número 9 apareceu {} vezes".format(valores.count(9)))
else:
    print("O numero 9 não foi digitado!")
if 3 in valores:        #Se o numero 3 estiver em "valores"
    print("O numero 3 aparece na {}ª posição".format(valores.index(3)+1))  #posição mais um
else:
    print("O valor 3 não foi digitado!")
print("O valores pares digitados foram ", end='')
for n in valores:
    if n % 2 == 0:
        print(n, end="")

#USAR ESPAÇAMENTO NOS PRINT PARES
