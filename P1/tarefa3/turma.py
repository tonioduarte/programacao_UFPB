qtd_Equipe = int(input("Quantas pessoas existem na equipe? "))
soma = 0

for i in range(qtd_Equipe):
    n = int(input("Coloque as idades de cada um: "))
    soma += n
media = soma / qtd_Equipe
if media <= 25:
    print("Sua turma é Jovem")
elif media <= 60 and media > 26:
    print("Sua turma é Adulta")
else:
    print("Sua turma é Idosa")