pais_x = 70000
pais_y = 180000
cont = 0

while pais_x <= pais_y:
    pais_x = pais_x + (pais_x * 0.035)
    pais_y = pais_y + (pais_y * 0.015)
    cont = cont + 1

print(cont)