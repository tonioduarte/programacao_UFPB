alturas = []
sexos = []

for i in range(10):
    altura = float(input(f"Altura {i+1}: "))
    sexo = input(f"Sexo {i+1} (M/F): ")
    alturas.append(altura)
    sexos.append(sexo)

maior = alturas[0]
menor = alturas[0]
indice_maior = 0
indice_menor = 0

for i in range(10):
    if alturas[i] > maior:
        maior = alturas[i]
        indice_maior = i
    if alturas[i] < menor:
        menor = alturas[i]
        indice_menor = i

print("Maior altura:", maior, "Sexo:", sexos[indice_maior])
print("Menor altura:", menor, "Sexo:", sexos[indice_menor])

soma_f = 0
cont_f = 0
soma_m = 0
cont_m = 0

for i in range(10):
    if sexos[i] == "F":
        soma_f += alturas[i]
        cont_f += 1
        
    elif sexos[i] == "M":
        soma_m += alturas[i]
        cont_m += 1

if cont_f > 0:
    print("Média feminino:", soma_f/cont_f)

if cont_m > 0:
    print("Média masculino:", soma_m/cont_m)

print("Total feminino:", cont_f)
print("Total masculino:", cont_m)