fibo = int(input("Qual número deseja conferir a sequência Fibonacci? "))
fibo_Qtd = int(input("Quantos números deseja ter na sequência?"))
resultado = 0

for i in range(fibo_Qtd):
    print(resultado)
    soma = resultado + fibo
    resultado = fibo
    fibo = soma