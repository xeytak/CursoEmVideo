#aça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.


f = str(input("Digite uma frase: \n")).upper().strip()          #importante por "str" para usar esses comandos
print("A letra 'A' aparece {} vezes ".format(f.count("A")))
print("A primeira letra 'A' está na posição {}".format(f.find("A")+1))

