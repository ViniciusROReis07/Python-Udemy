nome = input('Seu nome: ')
idade = int(input('Sua idade: '))
altura = float(input('Sua altura: '))
peso = float(input('Seu peso: '))
ano_atual = int(input('Ano atual: '))

ano_nascimento = ano_atual - idade
imc = peso/(altura**2)

print(f'{nome} tem {idade}, {altura:.2f} de altura e pesa {peso:.2f}kg.')
print(f'O IMC de {nome} e {imc:.2f}.')
print(f'{nome} nasceu em {ano_nascimento}.')
