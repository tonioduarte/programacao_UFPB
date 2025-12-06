lado1 = float(input("Digite o lado 1 do triângulo: "))
lado2 = float(input("Digite o lado 2 do triângulo: "))
lado3 = float(input("Digite o lado 3 do triângulo: "))

if lado1 == lado2 and lado1 == lado3:
    print("Esse triângulo é Equilátero!")
elif lado1 != lado2 and lado1 == lado3 or lado1 != lado3 and lado3 == lado2 or lado1 != lado3 and lado1 == lado2:
    print("Esse triângulo é Isósceles! ")
else:
    print("Esse triângulo é Escaleno!")

