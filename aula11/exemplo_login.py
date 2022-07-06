usuario = input("Nome de usuario: ")
senha = input("Senha do usuario: ")

usuario_bd = "Vinicius"
senha_bd = "123456"

if usuario == usuario_bd and senha == senha_bd:
    print("Voce esta logado no sistema")
else:
    print("Usuario ou senha invalidos.")