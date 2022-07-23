def saudacao(msg="Ola", nome="Usuario"):
    nome = nome.replace('V', '4')
    msg = msg.replace('V', '4')
    return f'{msg} {nome}'


variavel = saudacao()

print(variavel)
