# Para saber a função de um comando usa-se:

help(input)         #help() nome do comando dentro

#Também ultiliza-se:

print(input.__doc__)

#Uso da docstring (exemplo com código):

def contador(i, f, p):
                             #Para abrir uma docstring, aperte aspas duplas 3 vezes.
    """
    Faz uma contagem e mostra na tela.
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print("{}".format(c))
        c += p
    print("fim!")

help(contador)

# Parâmetros Opcionais:


def somar(a, b, c=0):     # Caso não seja informado um valor para o terceiro parametro, o "C" será igual a zero.

    s = a + b + c
    print(s)


somar(3, 4)
#somar(a=3, b=4)  -> outra forma de informar.


# Escopo de variáveis:

def funcao():
    n1 = 4
    print("N1 dentro vale {}".format(n1))  #Variável local, só vale dentro do def.


n1 = 2
funcao()
print("N1 fora vale {}".format(n1))   # Nesse caso, trata-se de uma variável global, assume valor em qualquer lugar.

# Variável local para global:

def teste(b):
    global a          # tanto dentro quanto fora possue o mesmo valor
    a = 8
    b += 4
    c = 2
    print("a dentro vale {}".format(a))
    print("b dentro vale {}".format(b))
    print("c dentro vale {}".format(c))



a = 5
teste(a)
print("a fora vale {}".format(a))

# Com o comando global a, é o valor de a fora que passará a ser 8. O programa reutilizará o "a" de fora.

# Retornando Valores:


def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)

print("Os resultados foram {}, {}, {}".format(r1, r2, r3))
      