nome = input("Qual seu nome? ")
idade = int(input("Qual a sua idade? "))

idade_menor = 20
idade_maior = 30

if idade >= idade_menor and idade <= idade_maior:
    print(f"{nome} pode pegar o emprestimo")
else:
    print(f"{nome } NAO pode pegar o emprestimo")

