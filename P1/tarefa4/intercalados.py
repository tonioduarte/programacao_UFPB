lista1 = []
lista2 = []
lista3 = []

for i in range(5):
    vetor1 = int(input("Digite os numeros da lista 1: "))
    lista1.append(vetor1)

for i in range(5):
    vetor2 = int(input("Digite os numeros da lista 2: "))
    lista2.append(vetor2)

for i in range(5):
    lista3.append(lista1[i])
    lista3.append(lista2[i])

print(lista3)