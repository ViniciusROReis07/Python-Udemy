string = "O Brasil e o pais do futebol, o Brasil e penta."

lista_1 = string.split(" ")
lista_2 = string.split(",")

print(lista_1)
print(lista_2)

palavra = ""
contagem = 0
for valor in lista_1:
    qtd_vezes = lista_1.count(valor)
    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor


print(f'A palavra que apareceu mais vezes e {palavra} ({contagem})x')

for valor in lista_2:
    print(valor.strip().capitalize())