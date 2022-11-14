
pessoas = {'nome': 'Tiago', 'sexo': 'M', 'idade': 21}

print(pessoas)
print(pessoas['nome'])   # Nos dicionários se usa o nome das Keys para a saída
print(pessoas['idade'])
print("O {} tem {} anos".format(pessoas["nome"], pessoas["idade"]))  # Forma de escrever os valores no format

# Usar aspas simples no dicionário e aspas duplas no format !

print(pessoas.keys())    # Chaves dos valores. "
print(pessoas.values())  # valores.
print(pessoas.items())   # O comando retorna uma lista composta de 3 tuplas que são os valores.


for k in pessoas.keys():  # keys = Nome, sexo, idade.
    print(k)

for v in pessoas.values():  # valores das chaves
    print(v)

for k, v in pessoas.items():    # Tanto as chavens quantos os valores
    print("{} = {}".format(k, v))

dados = {'nome': 'tiago'}  # Para trocar um elemento dentro de uma chave
dados['nome'] = 'Juan'
dados['peso'] = 70.5     # Para adicionar um elemento novo no dicionário


brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}    # Forma de adicionar um dicionário dentro de uma lista.
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0])  # Posições dos dados do dicionário na lista.
print(brasil[1])  # RJ 0 e SP 1

print(brasil[0]['uf'])  # Mostrar apenas um valor do dicionário na lista.
print(brasil[1]['uf'])

# Trabalhando com input - adicionar dicionário na lista.

brasil2 = []
estados = {}
for c in range(1, 3):
    estados['uf'] = str(input("Unidade Federativa:  "))
    estados['sigla'] = str(input("Sigla do estado:  "))
    brasil2.append(estados.copy())
for e in brasil2:  # O "e" é estado, sua saída é cada dicionário dentro das listas. O "e" é o for para a lista.
    for k, v in e.items():
        print("O campo {} tem valor {}".format(k, v))
print(brasil2)

