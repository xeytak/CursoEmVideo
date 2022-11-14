def leiaint(digit):

    while True:
        try:
            n = int(input(digit))
        except(ValueError, TypeError):
            print("Por Favor, digite algo válido")
        else:
            return n


def leiafloat(digit):
    while True:
        try:
            r = float(input(digit))
        except (ValueError, TypeError):
            print(f'tivemos erro nos dados')
            continue
        else:
            return r



n1 = leiaint("Inteiro:  ")
n2 = leiafloat("Real: ")
print(f'{n1} e {n2}')

