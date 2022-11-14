num = int(input("Digite um número: \n"))
for v in range(1, num+1):
    if num % v == 0:
        print("\033[33m", end=" ")
    else:
        print("\033[31m", end=" ")
    print("{}".format(v), end=" ")

#refazer
