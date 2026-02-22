pontos = []
n = int(input("Quantos pontos? "))

for i in range(n):
    x = float(input("Digite x: "))
    y = float(input("Digite y: "))
    pontos.append((x, y))

distancias = []

for i in range(len(pontos)):
    for j in range(i+1, len(pontos)):
        x1, y1 = pontos[i]
        x2, y2 = pontos[j]
        distancia = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
        distancias.append(distancia)

menor = distancias[0]
maior = distancias[0]
soma = 0

for d in distancias:
    if d < menor:
        menor = d
    if d > maior:
        maior = d
    soma += d

print("Distância mínima:", menor)
print("Distância máxima:", maior)
print("Distância média:", soma / len(distancias))