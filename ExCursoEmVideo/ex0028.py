#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e
# peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
import emoji
a = [0, 1, 2, 3, 4, 5]
s = random.choice(a)      #Poderia ter sido: s = randint(0,5), sem a variavel "a"
print(emoji.emojize("Hmmmm... Estou pensando em um número,tente adivinhar :robot:"))
n = int(input("Adivinhe:"))
print("PROCESSANDO...")
if n == s:
    print("Parabéns,ACERTOU!")
else:
    print("Você errou!")
