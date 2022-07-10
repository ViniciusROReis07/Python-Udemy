frase = "o rato roeu a roupa do rei de roma" # Iteravel
tamanho_frase = frase.__len__()

contator = 0
nova_string = ""

input_do_usuario = input("Qual letra deseja colocar maiuscula: ")

# Iteracao <- Iterar
while contator < tamanho_frase:
    #print(frase[contator], contator)
    letra = frase[contator]
    if letra == input_do_usuario:
        nova_string += input_do_usuario.upper()
    else:
        nova_string += letra
    contator += 1

print(nova_string)
