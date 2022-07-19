cpf = input("Informe o CPF: ")
novo_cpf = cpf[:-2]

contator_primeiro_digito = 10
soma_primeiro_digito = 0

for digito in cpf:
    if contator_primeiro_digito > 1:
        soma_primeiro_digito += int(digito) * contator_primeiro_digito
        contator_primeiro_digito -= 1
    else:
        break

primeiro_digito = 0
if (11 - (soma_primeiro_digito % 11)) <= 9:
        primeiro_digito = 11 - (soma_primeiro_digito % 11)

contator_segundo_digito = 11
soma_segundo_digito = 0

for digito in cpf:
    if contator_segundo_digito > 1:
        soma_segundo_digito += int(digito) * contator_segundo_digito
        contator_segundo_digito -= 1
    else:
        break

segundo_digito = 0
if (11 - (soma_segundo_digito % 11)) <= 9:
    segundo_digito = 11 - (soma_segundo_digito % 11)

novo_cpf += str(primeiro_digito)+str(segundo_digito)

if novo_cpf == cpf:
    print(f"O CPF {cpf} e valido!")
else:
    print(f"O CPF {cpf} e invalido")
