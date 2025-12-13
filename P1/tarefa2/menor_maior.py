valor = float(input("Digite o valor:\n(-1 para parar) "))
menor = maior = valor
soma = 0

while valor != -1:
    if valor > maior:
        maior = valor
    elif valor < menor:
        menor = valor
    soma += valor
    valor = float(input("Digite mais um valor: \n(-1 para parar) "))
    
print(f"O maior valor é {maior}, o menor valor é {menor} e a soma deles é {soma}")