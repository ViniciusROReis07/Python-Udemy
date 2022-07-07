numero = input("Informe um numero: ")

if numero.isdigit():
    if int(numero) % 2 == 0:
        print("Par")
    else:
        print("impar")
else:
    print("Por favor informe um numero inteiro")