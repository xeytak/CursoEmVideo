lista = ("Tiago", "Rayane", "Carro", "Moto")


for palavras in lista:
    print(" \n Na palavra {}, temos as vogais :  ".format(palavras), end="")      #dentro do parenteses
    for vogais in palavras:           #As palavras são listas que as vogais estão dentro, lê-se: "Para vogais nas palavras"
        if vogais.lower() in "aeiou":
            print(vogais, end="")


#MELHORAR ESSE PROGRAMA, POR OPÇÃO DO USUARIO ESCREVER
