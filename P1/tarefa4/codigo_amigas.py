letras = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
codigo_Lista = []
codigo = 0
num = 1

while codigo != -1:
    codigo = int(input(f"Digite o numero {num} do codigo: (-1 para parar) "))
    num += 1
    if codigo != -1:
        codigo_Lista.append(codigo)
    
traducao = "" 

for i in range(len(codigo_Lista)):
    traducao += letras[codigo_Lista[i]]

print(traducao)