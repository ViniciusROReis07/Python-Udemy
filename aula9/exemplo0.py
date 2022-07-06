"""
Entrada de dados
"""

nome = input("Qual seu nome? ")
print(f"O usuario digitou {nome} e o tipo da variavel e {type(nome)}")
idade = input("Qual a sua idade? ")

ano_nascimento = 2022 - int(idade)

print(f"{nome} tem {idade} anos")
print(f"{nome} Nasceu em {ano_nascimento}")
