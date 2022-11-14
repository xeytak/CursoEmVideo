
from time import sleep               # REFAZER COM FUNÇÃO
print("Contagem de 1 até 10 de 1 em 1:")
for num in range(1, 11):
    print(num, end=", ")
    sleep(0.5)
print()
print("\ncontagem de 10 até 0 de 2 em 2:")
for num2 in range(10, -2, -2):
    print(num2, end=", ")
print("\nAgora a sua vez")

print()
inicio = int(input("Inicio: "))
ultimo = int(input("ultimo: "))
passo = int(input("passo: "))
print("A contagem de {} até {} de {} em {} é:".format(inicio, ultimo, passo, passo))
for val in range(inicio, ultimo, passo):
    print(val, end=", ")
