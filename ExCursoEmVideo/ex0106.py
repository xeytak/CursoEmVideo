cores = {'semcor': '\033[m', 'verde': '\033[1;35m', 'azul': '\033[m'}

def titulo(msg, cor="semcor"):
    print()



def func(digit):
    while True:
        resp= str(input(digit))
        print(help(resp))
        if resp == "fim":
            print("Até logo")
            break

print("="*15)
print("Sistema de Ajuda PyHelp")
print("="*15)


resp = func("\033[mFunção ou Biblioteca:  ")


  #terminar hoje de manha
  