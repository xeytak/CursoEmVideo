def voto(idade):

    if 18 <= idade <= 69:
        print("Voto Obrigatório!")
    elif 16 <= idade <= 17 or idade >= 70:
        print("Voto Facultativo!")
    else:
        print("Não Vota!")




# Program principal

data = 2022 - int(input("Data de nascimento: "))
voto(data)
