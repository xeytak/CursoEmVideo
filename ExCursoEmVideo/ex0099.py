from time import sleep
def linha():
    print("~"*40)
def num(* valores):
    tam = len(valores)
    linha()
    print("Processando valores...")
    sleep(1)
    print("Recebi ao todo {} valores: {}".format(len(valores), valores))
    maior = max(valores)
    print("O maior valor informado foi {}".format(maior))


#PROGRAM PRINCIPAL:

num(2, 4, 6, 8, 10)
num(4, 6, 75, 10, 33, 51)
num(77, 65, 23, 97, 88, 45, 67)

