produto = int(input("Qual o número do produto? \n(1, 2, 3, 4 ou 5)\nAperte 0 para finalizar a compra "))
qtd_comprada = int(input("Qual a quantidade comprada? "))
soma = 0

while produto != 0:
    if produto == 1:
        soma += 5.50 * qtd_comprada
    elif produto == 2:
        soma += 2.30 * qtd_comprada
    elif produto == 3:
        soma += 4.75 * qtd_comprada
    elif produto == 4:
        soma += 6.80 * qtd_comprada
    elif produto == 5:
        soma += 9.30 *qtd_comprada
    produto = int(input("Qual o número do novo produto? \n(1, 2, 3, 4 ou 5)\nAperte 0 para finalizar a compra "))
print(f"o valor total da compra foi de {soma:.2f}")



