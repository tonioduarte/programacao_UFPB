genero = input(" deseja saber seu peso ideal com base no cálculo masculino ou feminino? ")
if genero == 'masculino':
	alturaM = float(input(" qual sua altura? "))
	peso_idealM = (72.7*alturaM) - 58
	print(" seu peso ideal é: %.2f " % peso_idealM)
elif genero == 'feminino':
    alturaF = float(input(" qual sua altura? "))
    peso_idealF = (62.1*alturaF) - 44.7
    print(" seu peso ideal é: %.2f" % peso_idealF)