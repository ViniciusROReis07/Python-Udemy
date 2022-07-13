texto = "Valor"
lista = [1, 2, 3, 4]
lista2 = [6, 7, 8, 9]

print(max(lista))

print(min(lista))

print(lista+lista2)

print(lista[::-1]) # Inverte lista

lista.append(5)

print(lista)

lista.insert(0, 0)

print(lista)

del(lista[0])

print(lista)

lista.pop()

print(lista)

lista.extend(lista2)

print(lista)

lista.clear()

print(lista)

lista3 = list(range(1, 10))

print(lista3)

soma = 0
for valor in lista2:
    soma += valor

print(soma)





