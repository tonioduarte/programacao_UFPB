base = float(input("Qual número vai ser a base da potência? "))
potencia = int(input("Qual número vai ser a potência? "))
resultado = 1

for i in range(potencia):
    resultado = base * resultado
    
print(f"O resultado dessa potenciação é {resultado:.2f}")

