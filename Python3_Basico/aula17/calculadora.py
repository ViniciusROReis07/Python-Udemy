while True:
    print()
    num_1 = input("Digite um numero: ")
    num_2 = input("Digite outro numero: ")
    operator = input("Digite um operador: ")
    sair = input("Deseja sair? (s)im ou (n)ao: ")

    if sair == "s":
        break

    if not num_1.isnumeric() or not num_2.isnumeric():
        print("Voce precisa digitar um numero")
        continue

    num_1 = float(num_1)
    num_2 = float(num_2)

    if operator == '+':
        print(num_1 + num_2)
    elif operator == '-':
        print(num_1-num_2)
    elif operator == '*':
        print(num_1*num_2)
    elif operator == '/':
        print(num_1/num_2)
    else:
        print("Operador invalido")