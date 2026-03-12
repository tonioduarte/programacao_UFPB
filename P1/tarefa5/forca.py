import random

def escolher_palavra():
    palavras = ["abelha", "vaca", "ovelha"]
    return random.choice(palavras)

def criar_ocultos(palavra):
    ocultos = []
    for i in range(len(palavra)):
        ocultos.append("_")
    return ocultos

def jogar(descobrir, ocultos):

    vidas = 6

    while "".join(ocultos) != descobrir and vidas > 0:

        letra = input("Qual letra deseja escolher? ")

        if letra in descobrir:
            print("Acertou!")
        else:
            print("Errou")
            vidas -= 1
            print(f"Você tem {vidas} vidas restantes!")

        for i in range(len(descobrir)):
            if descobrir[i] == letra:
                ocultos[i] = letra

        print("".join(ocultos))

    if "".join(ocultos) == descobrir:
        print("Você ganhou da Forca!")
    else:
        print("Você perdeu!")


def main():

    descobrir = escolher_palavra()
    ocultos = criar_ocultos(descobrir)

    começar = int(input("Bem vindo à forca! Digite '1' para começar! "))

    if começar == 1:
        print(f"Sua palavra é {''.join(ocultos)}")
        jogar(descobrir, ocultos)


if __name__ == "__main__":
    main()