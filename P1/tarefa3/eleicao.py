eleitores = int(input("Digite a quantidade de eleitores: "))
candidato1 = 0
candidato2 = 0
candidato3 = 0

for i in range(eleitores):
    votar = int(input("Em que você vai votar? Candidato 1, 2 ou 3?"))

    if  votar == 1:
        candidato1 += 1
    elif votar == 2:
        candidato2 += 1
    elif votar == 3:
        candidato3 += 1

print(f"Candidato 1 recebeu {candidato1} votos!")
print(f"Candidato 2 recebeu {candidato2} votos!")
print(f"Candidato 3 recebeu {candidato3} votos!")