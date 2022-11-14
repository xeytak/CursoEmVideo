#Escreva um programa em Python que leia um número inteiro qualquer
# peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

n = int(input("\033[33mDigite um número inteiro: \n"))
c = print('''\033[34mQual será sua base de conversão?
[ 1 ] binário
[ 2 ] hexadecimal
[ 3 ] octal''')
op = int(input("sua opção é:"))
if op == 1:
    print("O numero {} em base binária é: {}".format(n, bin(n)))
elif op == 2:
    print("O numero {} em base hexadecimal é: {}".format(n, hex(n)))
elif op == 3:
    print("O numero {} em base octal é: {}".format(n, oct(n)))
else:
    print("\033[31mOpção inválida")



