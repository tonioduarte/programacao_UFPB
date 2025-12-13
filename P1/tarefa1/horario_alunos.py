turno = input("Qual seu turno escolar? (M para matutino, V para vespertino, N para Noturno) ")

if turno == "M":
    print("Bom dia!")
elif turno == "V":
    print("Boa tarde!")
elif turno == "N":
    print("Boa noite!")
else:
    print("Valor inválido")