def mudarMes(data):
    meses = ["", "Janeiro","Fevereiro","Março","Abril","Maio","Junho",
             "Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]

    mes = int(data[1])
    data[1] = meses[mes]

def main():
    aniversario = input("Digite a data do seu aniversário: (dd/mm/aaaa) ")
    data = aniversario.split("/")

    mudarMes(data)

    print(f"Seu aniversário é {data[0]} de {data[1]} de {data[2]}")

if __name__ == "__main__":
    main()