ganho = float(input("quanto você ganha por hora? "))
hora = float(input("quantas horas você trabalha? "))
salarioBruto = ganho * hora

print(" salário bruto: R$%.2f" % salarioBruto )
imposto_de_renda = salarioBruto * 0.11
print(" voce pagou: R$%.2f ao Imposto de Renda " % imposto_de_renda )
inss = salarioBruto * 0.08
print(" voce pagou R$%.2f ao INSS  " % inss)
sindicato = salarioBruto * 0.05
print(" voce pagou R$%.2f ao Sindicato " % sindicato)
salarioLiquido = salarioBruto * 0.76
print(" seu salário liquido é de: R$%.2f por dia trabalhado " % salarioLiquido)
dia_util = float(input(" quantos dias voce trabalha por mes? "))

salarioMensal = dia_util * salarioLiquido
print(" seu salário mensal é de R$%.2f " % salarioMensal )