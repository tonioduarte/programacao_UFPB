def soma(v2):

    for i in range(1,4):
        v1 = int(input(f"Digite o valor {i} a ser somado: "))
        v2 += v1

    return v2

def main():

    v2 = 0
    print(f"Seu valor somado é {soma(v2)}")
    
if __name__ == "__main__":
    main()