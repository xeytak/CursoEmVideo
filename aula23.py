try:
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a / b

#except Exception as erro:
   #print(f'O problema encontrado foi {erro.__class__}')

except(ValueError, TypeError):
    print("Tivemos um erro nos dados")

except ZeroDivisionError:
    print("Não é possivel dividir por zero :( ")

except KeyboardInterrupt:
    print("O usuário preferiu não informar os dados")

else:
    print(f'O resultado é {r:.1f}')
finally:
    print("Volte sempre, muito obrigado!")
