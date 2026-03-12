def data(mes):
    if mes == 1:
        mes = "Janeiro"
    if mes == 2:
        mes = "Fevereiro"
    if mes == 3:
        mes = "Março"
    if mes == 4:
        mes = "Abril"
    if mes == 5:
        mes = "Maio"
    if mes == 6:
        mes = "Junho"
    if mes == 7:
        mes = "Julho"
    if mes == 8:
        mes = "Agosto"
    if mes == 9:
        mes = "Setembro"
    if mes == 10:
        mes = "Outubro"
    if mes == 11:
        mes = "Novembro"
    if mes == 12:
        mes = "Dezembro"
    return mes

def main():
    dia = int(input("Qual o dia do seu aniversário? "))
    mes = int(input("Qual o mes do seu aniversário? "))
    ano = int(input("Qual o ano do seu aniversário? "))
    
    print(f"Seu aniversário é {dia} de {data(mes)} de {ano}")

if __name__ == "__main__":
    main()