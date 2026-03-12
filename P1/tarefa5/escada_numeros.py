def escada(n):
    for i in range(1, n + 1):
        linha = []

        for j in range(i):
            linha.append(str(i))

        print(" ".join(linha))


def main():
    n = int(input("Digite um número para a escada: "))
    escada(n)


main()