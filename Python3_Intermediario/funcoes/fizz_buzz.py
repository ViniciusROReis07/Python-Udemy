def fizz_buzz(numero):
    if numero % 5 == 0 and numero % 3 == 0:
        return 'FizzBuzz'
    elif numero % 3 == 0:
        return 'fizz'
    elif numero % 5 == 0:
        return 'buzz'
    else:
        return numero

valor = float(input("Informe um valor: "))
var = fizz_buzz(valor)
print(var)
