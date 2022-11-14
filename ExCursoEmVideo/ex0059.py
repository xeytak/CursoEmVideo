valor1 = int(input("Primeiro valor:  "))
valor2 = int(input("Segundo valor:  "))
escolha = 0
while escolha != 5:
        print('''        [ 1 ] somar 
        [ 2 ] multiplicar
        [ 3 ] maior
        [ 4 ] novos numeros
        [ 5 ] sair do programa''')
        escolha = int(input("sua opção:  "))
        if escolha == 1:
                soma = valor1 + valor2
                print("A soma entre {} e {} é {} \n".format(valor1, valor2, soma))
        elif escolha == 2:
                multiplic = valor1 * valor2
                print("A multiplicação entre {} e {} é {}".format(valor1, valor2, multiplic))
        elif escolha == 3:
                if valor1 > valor2:
                        print("O {} é maior que o valor {} \n ".format(valor1, valor2))
                else:
                        print("o valor {} é maior que o {} \n ".format(valor2, valor1))
        elif escolha == 4:
                valor1 = int(input("Primeiro valor:   "))
                valor2 = int(input("Segundo valor:  "))
        else:
                print("\033[31mOpção inválida.Tente novamente!")
        print("-=" * 20)
print("fim, volte sempre!")






