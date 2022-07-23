def percentual(n1, n2):
    valor_percentual = (n1*n2)/100
    return n1+valor_percentual

valor_1 = float(input("Informe um valor: "))
valor_2 = float(input("Informe percentual: "))

total = percentual(valor_1, valor_2)
print(total)
