nome = str(input("Qual é o seu nome? \n")).capitalize()
if nome == "Tiago":
        print("Que nome lindo!")
else:
    print("Que nome feio!")
# ==================================================================================
nota1 = float(input("Digite sua primeira nota: \n"))
nota2 = float(input("Digite sua segunda nota: \n"))
m = (nota1 + nota2) / 2
if m >= 6:
    print("PARABÉNS!Você foi aprovado! A média foi: {:.1f}".format(m))
else:
    print("POXA! Precisa estudar mais! A média foi: {:.1f}".format(m))


