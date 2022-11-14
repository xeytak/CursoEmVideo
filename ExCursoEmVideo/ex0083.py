#OS PARENTESES SEMPRE DEVEM ESTAR EM PARES ABRIR E FECHAR

exp = str(input("Digite sua expressão:  "))
dir = exp.count("(")
esq = exp.count(")")
#total = dir + esq

if dir == esq:
    print("expressao valida")
else:
    print("expressao invalida")

#REFAZER DEPOIS
