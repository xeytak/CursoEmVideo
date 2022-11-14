#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

c = str(input("Em que cidade você nasceu? \n"))
separa = c.split()
sant = separa[0]
cidade = sant == "santo"
print(cidade)

#O certo seria:

#cid = str(input("Qual cidade você nasceu?")).strip()
#print(cid[0:5].upper == "SANTO")    # a função [] conta do a partir do zero e elimina a ultima posição




