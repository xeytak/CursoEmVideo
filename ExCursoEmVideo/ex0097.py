# Meu código:
def escreva(texto):
    c = len(texto)
    b = c * "~"
    print(b)
    print(texto)
    print(b)


escreva("Tiago")
escreva("Cristiano Ronaldo")
escreva("Vasco da Gama, Gigante da Colina")


#aula:
def digite(msg):
     tam = len(msg) + 4    # 4 = dois caracteres para cada lado.
     print("~" * tam)
     print("  {}".format(msg))    #dois espaço para os caracteres
     print("~" * tam)


digite("Curso em Video")
digite("carro")
