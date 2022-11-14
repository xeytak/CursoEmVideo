extenso = ("zero", "um", "dois", "tres", "quatro", "cinco", "seis",
           "sete", "oito", "nove", "dez")
resposta = ""

while True:
    numero = int(input("Digite um número entre 0 e 10: "))
    if numero <= 10:
        print("O número em extenso é {}.".format(extenso[numero]))  # O [numero] é a posição das truplas.
    if numero > 10:
        numero = int(input("Tente novamente! Digite um número entre 0 e 10:  "))
        print("O número em extenso é {}.".format(extenso[numero]))
    resposta = str(input("Deseja continuar? [S/N]  ")).strip().upper()
    if resposta == "N":
        print("\033[35mFIM DO PROGRAMA!")
        break
