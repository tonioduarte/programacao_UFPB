Valor = float(input("Qual o valor total dos produtos somados? "))
Pagamento = input("Qual a forma de pagamento? (Dinheiro ou Cheque). ")

if Valor >= 100 and Pagamento == "Dinheiro":
    Valor = Valor - Valor * 0.10
    print("Valor a ser pago = %.2f" % Valor)
elif Pagamento == "Cheque":
    print("Valor a ser pago = %.2f" % Valor)
else:
    print("Forma de pagamento inválida")