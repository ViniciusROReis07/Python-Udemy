string = "O Brasil e o pais do futebol, o Brasil e penta."

lista = string.split(" ")

for index, valor in enumerate(lista):
    print(index, valor)

print()

lista = [
    [0, "Luiz"],
    [1, "Joao"],
    [2, "Maria"]
]

for indice, nome in lista:
    print(indice, nome)