
teste = list()
teste.append("Tiago")
teste.append(21)
galera = list()
galera.append(teste[:])  #O USO DO [:] É PARA O FATIAMENTO DOS DADOS DA LISTA TESTE.
teste[0] = 'Maria'
teste[1] = 20
galera.append(teste[:])  # uma lista dentro de outra.
print(galera)

print("-="*20)

galera = [["Tiago", 21], ["Maria", 20], ["Lucas", 18]]
#         0 - 0     1  / 1 - 0      1  / 2 - 0      1
print(galera)
print(galera[0])       # Apresenta apenas os dados da posição 0
print(galera[0][0])    # Apresenta a lista da posição 0 e a posição do seu item.

print("-="*20)

galera = [["Tiago", 21], ["Maria", 20], ["Lucas", 18]]
for pessoa in galera:
    #print(pessoa)       - Irá mostrar todas listas e seus itens dentro de "galera".
    #print(pessoa[0])    - Mostra cada item na posição zero de cada lista dentro de galera.
    #print(pessoa[1])    - Mesma coisa que em cima, porém posição 1.

    print("{} tem {} anos de idade".format(pessoa[0], pessoa[1]))

print("-="*20)

galera = list()
dado = list()
for contador in range(0, 3):
    dado.append(str(input("Digite um nome:  ")))
    dado.append(int(input("Digite a idade:  ")))
    galera.append(dado[:])
    dado.clear()       # O dado.clear

print("-="*20)

for pessoa in galera:     # galera [[nome, idade], [nome, idade]] cada nome e idade são itens com suas posições.
    if pessoa[1] >= 21:
        print("{} é maior de idade".format(pessoa[0]))
    else:
        print("{} é menor de idade".format(pessoa[0]))
print(galera)  # Se quisesse por as lista com os dados em cima, colocaria o print(galera) acima do ultimo for.





