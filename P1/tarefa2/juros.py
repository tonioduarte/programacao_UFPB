valor_Inicial = float(input("Qual o valor inicial da sua dívida? "))
juros = float(input("Qual o valor dos juros? "))
valor_Pago = float(input("Quanto vai ser pago por mês? "))
cont = 0
juros_Total = 0

if valor_Pago <= valor_Inicial * juros:
        print("A dívida nunca será paga.")

while valor_Inicial > 0:
    juros_Mes = valor_Inicial * juros
    valor_Inicial += juros_Mes        
    juros_Total += juros_Mes     
    valor_Inicial -= valor_Pago       
    cont += 1                          

valor_Total = valor_Pago * cont

print(f" A dívida será paga em {cont} meses\n o valor total pago foi de {valor_Total:.2f}\n e o total de juros pago foi de {juros_Total:.2f}")

