#Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
# An = a1 + (n-1).r

a1 = int(input("Primeiro termo: "))
r = int(input("razão: "))
for pa in range(0, 10):
    n = a1 + pa * r
    print("\033[35m{:.0f}".format(n), end=" , ")
print("FIM")
