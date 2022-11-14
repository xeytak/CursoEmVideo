def linha():             #Deixar após o comando def duas linhas em branco.
    print("-=" * 10)


linha()
print("Olá, Mundo!")
linha()
print("Vasco da Gama")
linha()
print("Pyhton!")
linha()


def titulo(txt):
    print("-=" * 10)
    print(txt)
    print("-=" * 10)

#PROGRAMA PRINCIPAL (o que vai ser mostrado na tela):

titulo("Aprenda Python")
titulo("Real Madrid")
titulo("Tiago Ferreira")


def soma(a, b):
    print("A = {} e B = {}".format(a, b))
    s = a + b
    print("A soma entre A + B = {}".format(s))

soma(5, 8)
   # soma(b=5, a=8) Caso queira deixar mais explícito.


print("=" * 20)


def contador(*num):     # O asterisco indica que a função irá receber vários valores.
    for valor in num:
        print("{}, ".format(valor), end="")


contador(3, 4, 5,)
contador(6, 7, 8)


def contador2(* num2):
    tam = len(num2)
    print("\nRecebi os valores {} que são {} ao todo".format(num2, tam))


contador2(6, 9, 10)

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [1, 2, 3, 4, 5]
dobra(valores)
print(valores)


def soma(* valores):                 #Desempacotamento
    s = 0
    for num in valores:
        s += num
    print("A soma dos valores {} é {}".format(valores, s))


soma(2, 3, 4, 5)

