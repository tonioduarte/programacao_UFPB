def negativo(n):
    if n > 0:
        return print("seu número é positivo")
    else:
        return print("seu número é negativo")
    
def main():
    n = int(input("Digite o número: "))
    negativo(n)

if __name__ == "__main__":
    main()