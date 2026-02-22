import random

n = int(input("Quantas vezes lançar o dado? "))

faces = [0, 0, 0, 0, 0, 0, 0]  

for i in range(n):
    numero = random.randint(1, 6)
    faces[numero] += 1   

for i in range(1, 7):
    percentual = (faces[i] / n) * 100
    print("Face", i, ":", percentual, "%")