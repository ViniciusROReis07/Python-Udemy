variavel = ["Vincius Rhuan", "Marcia"]

for valor in variavel:
    if valor.lower().startswith("m"):
        break
else:
    print("Nao exite uma palavra que comeca com M")