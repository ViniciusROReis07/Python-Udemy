"""
Manipulando strings - Aula 6
* String indices
* Fatiamento de strings [inicio:fim:passo]
* Funcoes built-in len, abs, type, print, etc...
Essas funcoes podem ser usadas diretamente em cada tipo

"""
#positivos [01245678]
texto =    'Python s2'
#negativo  [987654321]

print(texto[6])

url = 'www.google.com.com.br/'
# ele nao pega o caracter limitador
print(url[:-1])

nova_string = texto[0:6]
print(nova_string)

nova_string = texto[:6]
print(nova_string)

print(texto[7:])

print(texto[-9:-3])

print(texto[0:6:2])
