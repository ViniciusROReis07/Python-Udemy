secreto = "perfume"
digitadas = []

chances = 3

while True:
    if chances > 0:
        letra = input("Digite uma letra: ")

        if len(letra) > 1:
            print("Ahh isso nao vale, digite apenas uma letra")
            continue

        digitadas.append(letra)

        if letra in secreto:
            print(f"UHUUUUL, a letra '{letra}' exite na palavra secreta.")
        else:
            print(f"AFFFzzz: a letra '{letra}' NAO EXIste na palavra secreta")
            digitadas.pop()
            chances -= 1
            print(f"Voce ainda tem {chances}")

        secreto_temporario = ""
        for letra_secreta in secreto:
            if letra_secreta in digitadas:
                secreto_temporario += letra_secreta
            else:
                secreto_temporario += "_"

        if secreto_temporario == secreto:
            print(f"Que legal, VOCE GANHOUU!!! A palavra secreta era {secreto_temporario}")
            break
        else:
            print(f"A palavra secreta esta assim: {secreto_temporario}")
    else:
        print("AAA NAO Voce pedeuuuuu !!!!!")
        break
