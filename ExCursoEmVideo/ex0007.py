n1 = float(input("Primeira nota do aluno:")) # não é "int", pois notas são decimais (float)
n2 = float(input("Segunda nota do aluno:"))
m = (n1 + n2) / 2
print("A média do aluno foi: {:.1f}".format(m)) #1f reduz casa decimal


