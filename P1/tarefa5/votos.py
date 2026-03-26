def votos(votosTotais):
    votosTotais = []

    for i in range(100):
        voto = int(input("Em quem vc vota? (10 Rep, 12 Dem)"))
        if voto == 10:
            votosTotais.append(10)
        elif voto == 12:
            votosTotais.append(12)
        else:
            print("Candidato inexistente")

    return votosTotais

def contar_votos(votosTotais):
    Rep = 0
    Dem = 0

    for i in votosTotais:
        if i == 10:
            Rep += 1
        else:
            Dem += 1
    
    return Rep, Dem

def main():
    votosTotais = []

    votosTotais = votos(votosTotais)
    Rep, Dem = contar_votos(votosTotais)
    print(Rep, Dem)

if __name__ == "__main__":
    main()




