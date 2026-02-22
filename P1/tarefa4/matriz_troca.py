matriz = [[None]*3 for i in range(0,3)]

for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input("Digite o valor da matriz: "))


for i in range(3):
    for j in range(3):
        if i == 1: 
            matriz[i][j], matriz[j][i] = matriz[j][i], matriz[i][j]

print("Matriz:")
for i in matriz:
    print(i)