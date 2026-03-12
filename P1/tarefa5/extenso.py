def enxtenso(valor):
    num = [
    "um", "dois", "três", "quatro", "cinco",
    "seis", "sete", "oito", "nove", "dez",
    "onze", "doze", "treze", "quatorze", "quinze",
    "dezesseis", "dezessete", "dezoito", "dezenove", 
    "vinte"]

    dez = [
    "vinte", "trinta", "quarenta", "cinquenta",
    "sessenta", "setenta", "oitenta", "noventa"]

    if valor <= 20:
        return num[valor-1]
    
    valorStr = str(valor)

    valor1 = int(valorStr[0])
    valor2 = int(valorStr[1])

    if valor2 == 0:
        return dez[valor1-2]

    return dez[valor1-2] + " e " + num[valor2-1]


def main():
    valor = int(input("Digite um número de 1 a 99: "))
    print(enxtenso(valor))

if __name__ == "__main__":
    main()