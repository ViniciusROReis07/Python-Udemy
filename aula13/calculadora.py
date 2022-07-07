num1 = input("Digite um numero: ")
num2 = input("Digite outro numero: ")

try: # Tenta execultar o codigo
    num1 = float(num1)
    num2 = float(num2)
    print(num1+num2)
except: # Caso ocorra um erro entrara nesse bloco
    print("ERROR")




