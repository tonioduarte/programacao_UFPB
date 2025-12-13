multiplos = 0
soma = 0

while multiplos < 500:
    multiplos = multiplos + 1
    if multiplos % 2 != 0 and multiplos % 3 == 0:
        soma += multiplos
print(soma)
    