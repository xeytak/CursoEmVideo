times = ("Palmeiras", "Internacional", "Fluminense", "Flamengo", "Corinthians", "Atlético-PR", "Atletico-MG",
              "America-MG", "Goias", "Sao Paulo", "Botafogo", "Vasco", "Cuiaba", "Juventude",
          "Santos", "Grêmio", "Bragantino", "Fortaleza", "Ceará", "Coritiba")
print("A lista de times do Brasileirão: {}".format(times))
print("-="*40)
print("Os 5 primeiros colocados são: {}".format(times[:5]))  # do começo ao quinto
print("-="*40)
print("Os rebaixados são: {}".format(times[-4:]))
print("-="*40)
print("times em ordem alfabética: {}".format(sorted(times)))
print("-="*40)
print("O Vasco está na {}ª posição".format(times.index("Vasco")+1))
