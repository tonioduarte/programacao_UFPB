deposito = int(input("Qual o valor do depósito? "))
juros = int(input("Qual o valor da porcentagem do juros? ")) * 0.01
deposito_Novo = 0

for i in range(1,25):
    deposito_Novo = deposito * juros
    deposito += deposito_Novo
    print(f"Valor do depósito no mês {i} = {deposito:.2f}")
