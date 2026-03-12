def soma(v1, v2, v3):

    somar = v1 + v2 + v3

    return somar

def main():
    v1 = int(input("Digite o valor 1 a ser somado: "))
    v2 = int(input("Digite o valor 2 a ser somado: "))
    v3 = int(input("Digite o valor 3 a ser somado: "))

    print(soma(v1, v2, v3))

if __name__ == "__main__":
    main()