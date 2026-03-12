def escada(frase):
    for i in range(1, len(frase) + 1):
        print(frase[:i]) #Fatiar a frase, 0:0 nao tem nada, por isso começar do 1

def main():
    frase = input("Qual a frase desejada? ")
    escada(frase)

if __name__ == "__main__":
    main()