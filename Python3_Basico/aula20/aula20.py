"""
For in Em Python
Iterando com strings com for
Funcao range(start=0, stop, strp=1)
"""

texto = 'Python'

for letra in texto:
    print(texto)

print()

for numero in range(20, 10, -1):
    print(numero)

for n in range(0, 100, 8):
    if n % 2 == 0:
        print(n)

print()

for n in range(100):
    if n % 8 == 0:
        print(n)
