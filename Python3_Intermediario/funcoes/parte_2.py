def divisao(n1, n2):
    if n2 == 0:
     return

    return n1/n2

divide = divisao(10, 0)

if divide:
    print(divide)
else:
    print("Conta invalida")

def f(var):
    print(var)

def dumb():
    return f

var = dumb()
var("Pode imprimir na tela")


