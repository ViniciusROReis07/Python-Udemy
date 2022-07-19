nome = input("Qual o seu nome? ")

print(nome or None or False or 0 or "Voce nao digitou nada")

a = 0
b = None
c = False
d = []
e = {}
f = 22
g = "Luiz"

variavel = a or b or c or f or e or f or g

print(variavel)