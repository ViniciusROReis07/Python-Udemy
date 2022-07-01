nome = 'Vinicius Reis'
print(nome, type(nome))
idade = 19 # int
altura = 1.80 # float
e_maior = idade >= 18 # bool
peso = 80
imc = peso/(altura**2)

print(nome, 'tem', idade, 'anos de idade e seu imc e', imc)
print(f'{nome} tem {idade}  anosde idade e seu imc e {imc:.2f}')
print('{} tem {} anos de idade e seu imc e {:.2f}'.format(nome, idade, imc))
print('{0} tem {1} anos de idade e seu imc e {2:.2f}'.format(nome, idade, imc)) # e possivel definir quais serao os valores passando os indexs
print('{n} tem {i} anos de idade e seu imc e {imc:.2f}'.format(n=nome, i=idade, imc=imc)) # e possivel definir quais serao os valores passando os indexs
