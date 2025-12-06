nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))

media_notas = (nota1 + nota2 + nota3) / 3
print("Sua média é %.2f" % media_notas)

if media_notas > 9 and media_notas <= 10:
    print("Seu aproveitamento está no conceito A, parabéns!")
elif media_notas >= 7.5 and media_notas < 9: # se eu deixar só elif media_notas >= 7.5:, e a media do aluno for maior do que 10, ele vai entrar nesse conceito, valendo pras outras também.
    print("Seu aproveitamento está no conceito B, parabéns!")
elif media_notas >= 6 and media_notas < 7.5:
    print("Seu aproveitamento está no conceito C, parabéns!")
elif media_notas >= 4 and media_notas < 6:
    print("Seu aproveitamento está no conceito D")
elif media_notas >= 0 and media_notas < 4:
    print("Seu aproveitamento está no conceito E")

elif media_notas > 10:
    print("Sua média está acima do permitido (média deve ser < 10).")
else:
    print("Sua média está abaixo do permitido (média deve ser > 0).")