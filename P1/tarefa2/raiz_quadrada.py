n = float(input("Digite o número que deseja calcular a raiz quadrada: "))
b = 2
p = (b + n / b) / 2

while abs(b - p) >= 0.0001:
    b = p
    p = (b + n / b) / 2

print(f"Raiz aproximada 1: {b:.1f}\nRaiz aproximada 2: {p:.1f}")
