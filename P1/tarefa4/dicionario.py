frase = ""
contador = 1

while frase != "-1":
    frase = input(f"Digite a frase {contador} (-1 para sair): ")
    
    if frase != "-1":
        dicionario = {}
        for i in frase:
            if i in dicionario:
                dicionario[i] += 1
            else:
                dicionario[i] = 1
        print(dicionario)

    contador += 1