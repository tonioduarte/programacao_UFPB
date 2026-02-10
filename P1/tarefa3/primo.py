primo = int(input("Qual número deseja saber se é primo? "))
contador = 0

for i in range(1, primo + 1):
    if primo % i == 0:
        contador += 1

if contador == 2:
    print("Seu número é primo")
else:
    print("Seu número não é primo.")