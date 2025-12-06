Valor = float(input("Qual o valor total dos produtos somados? "))
Pagamento = input("Qual a forma de pagamento? (Dinheiro, Cheque ou Cartão) ")

if Valor >= 100 and Pagamento == "Dinheiro":
    Valor = Valor - Valor * 0.10
    print("Valor a ser pago = %.2f" % Valor)
elif Pagamento == "Cheque":
    print("Valor a ser pago = %.2f" % Valor)
elif Pagamento == "Cartão":
    Cartão = input("Crédito ou Débito? ")
    if Cartão == "Débito":
        print("Valor a ser pago = %.2f" % Valor)
    elif Cartão == "Crédito":
        Parcela = input("Deseja Parcelar? (Sim ou Não) ")
        if Parcela == "Não":
            print("Valor a ser pago = %.2f " % Valor)
        elif Parcela == "Sim":
            num_Parcela = int(input("Qual o número de parcelas? (max: 3) "))
            if num_Parcela == 1:
                print("Valor a ser pago = %.2f " % Valor)
            elif num_Parcela == 2:
                valor_Parcela = Valor / 2
                print(f"Valor a ser pago = {Valor:.2f}\n 2 parcelas de {valor_Parcela:.2f}")
            elif num_Parcela == 3:
                valor_Parcela = Valor / 3
                print(f"Valor a ser pago = {Valor:.2f}\n 3 parcelas de {valor_Parcela:.2f}")
            else:
                print("Valor de parcelas inválido")
        else:
            print("Somente Sim ou Não.")
    else:
        print("Somente Crédito ou Débito.")
else:
    print("Forma de pagamento inválida.")