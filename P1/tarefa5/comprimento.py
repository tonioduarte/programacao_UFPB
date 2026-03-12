def prints(str1, str2):
    print(f"\nTamanho da string 1 = {len(str1)}, Tamanho da string 2 = {len(str2)} ")

    if len(str1) == len(str2):
        print("\nElas possuem tamanhos iguais")

    if str1 == str2:
        print("\nElas possuem o mesmo conteúdo\n")

def main():
    str1 = input("Qual a string 1: ")
    str2 = input("Qual a string 2: ")
    prints(str1, str2)

if __name__ == "__main__":
    main()