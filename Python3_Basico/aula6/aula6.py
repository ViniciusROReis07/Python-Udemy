"""
 Inicir com letras, pode conter numeros, separar ..., letras minusculas
"""

nome = 'Vinicius Reis'
print(nome, type(nome))
idade = 19 # int
altura = 1.80 # float
e_maior = idade >= 18 # bool
peso = 80
imc = peso/(altura**2)

print(nome, 'tem', idade, 'de idade e seu imc e', imc)
