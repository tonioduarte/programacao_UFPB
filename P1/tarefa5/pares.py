def lista_pares(lista):
    par = []

    for n in lista:
        if n % 2 == 0:
            par.append(n)
    
    return par

def main():
    numeros = []

    for i in range(10):
        n = int(input("Quais o numeros que quer checar? "))
        numeros.append(n)

    par = lista_pares(numeros)
    print(f"Esses números: {par} são pares! ")

if __name__ == "__main__":
    main()
    

