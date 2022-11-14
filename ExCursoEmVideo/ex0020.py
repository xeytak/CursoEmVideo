#O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

# O primeiro sera fulano  \n O segundo X ....

import random
a1 = str(input("Primeiro aluno:"))
a2 = str(input("Segundo aluno:"))
a3 = str(input("Terceiro aluno:"))
a4 = str(input("Quarto aluno:"))
ordem = [a1, a2, a3, a4]
random.shuffle(ordem)
print("A ordem da apresentação será:")
print(ordem)

