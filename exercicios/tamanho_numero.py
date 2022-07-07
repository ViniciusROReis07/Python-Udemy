nome = input("Informe seu nome: ")

if len(nome) <= 4:
    print("Seu nome e curto")
elif 5 <= len(nome) <= 6:
    print("Seu nome e normal")
else:
    print("Seu nome e muito grande")
