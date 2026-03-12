def escada(frase):
    frase = list(frase)

    fraseEscada = ''

    for i in range(len(frase)):
        fraseEscada += frase[i]
        print(fraseEscada)
        
def main():
    frase = input("Qual a frase desejada? ")
    escada(frase)

if __name__ == "__main__":
    main()