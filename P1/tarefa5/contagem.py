def contagem(frase):

    contar = {}

    for i in frase:
        if i in contar:
            contar[i] += 1
        else:
            contar[i] = 1
        
    return contar 

frase = input("qual frase deseja testar? ")
print(contagem(frase))