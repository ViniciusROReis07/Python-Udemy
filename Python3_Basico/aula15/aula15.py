"""
Formatando valores com modificadores - Aula 5

:s - Texto (strings)
:d - Inteiros (int)
:f - Numeros de ponto flutuante (float)
:. (NUMEROS)F - Quantidade de casas decimais (float)
: (CARACTERE) (> ou <  ou ^) (QUANTIDADE) (TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""

num_1 = 1
num_2 = 3

divisao = num_1 / num_2

print('{:.2f}'.format(divisao))
print(f'{divisao:.2f}')

nome = "Vinicius Rhuan"

print(f'{nome:s}')
print(f'{num_1:0>5}') # Para adicionar casas a esquerda

num_3 = 1150
print(f'{num_3:0<6}')
print(f"{num_3:0>10.2f}")

print(f'{nome:#^50}')

nome_formatado = "{0:0<20}".format(nome)
print(nome_formatado)

print(nome.lower())
print(nome.upper())
print(nome.title())
