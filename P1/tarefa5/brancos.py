def tirarEspacos(frase):
    espacos = " "
    tirar = ""

    for i in range(len(frase)):
        if frase[i] != espacos:
            tirar += frase[i]

    return tirar
    
def main():
    frase = input("Digite sua frase: ")
    frase = list(frase)

    print(f"a frase sem espaços é {tirarEspacos(frase)}")

if __name__ == "__main__":
    main()
