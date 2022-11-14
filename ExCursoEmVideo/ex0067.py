while True:
    print("-=" * 20)
    num = int(input("\033[mQuer ver a tabuada de qual valor?  "))
    print("-=" * 20)
    if num < 0:
        print("Programa encerrado")
        break
    for tab in range(1, 11):
        resultado = num * tab
        print("\033[34m{} x {} = \033[m{}".format(num, tab, resultado))

