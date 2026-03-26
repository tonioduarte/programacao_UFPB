def mediaA():
    soma = 0
    contador = 0
    n = int(input("Digite o número: "))

    while n >= 0:
        contador += 1
        soma += n
        n = int(input("Digite o número: "))

    media = soma / contador

    return media

def main():
    media = mediaA()
    print(media)

if __name__ == "__main__":
    main()



