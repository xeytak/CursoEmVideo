import aula22uteis      # Forma indicada de escrever o import para evitar conflitos entre bibliotecas de mesmo nome.

#PROGRAMA PRINCIPAL:

num = int(input("Digite um número:  "))
fat = aula22uteis.fatorial(num)               # Após importar os módulos, utilize o nome delas nos comandos
print("O número {} tem o fatorial {}".format(num, fat))
print("O dobro de {} é {}".format(num, aula22uteis.dobro(num)))
print("O triplo de {} é {}".format(num, aula22uteis.triplo(num)))





