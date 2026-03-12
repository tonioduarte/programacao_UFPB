def separarCpf(cpfInput):

    cpfSeparado = []

    for i in cpfInput:
        if i != "." and i != "-":
            cpfSeparado.append(i)

    for i in range(11):
        cpfSeparado[i] = int(cpfSeparado[i])

    return cpfSeparado

def calcularD1(cpfSeparado):

    cpfSeparadoD1 = []
    pesoD1 = 10
    for i in range(9):
        cpfSeparadoD1.append(cpfSeparado[i] * pesoD1)
        pesoD1 -= 1

    somaD1 = 0
    for i in range(9):
        somaD1 += cpfSeparadoD1[i]

    verificacaoD1 = ""
    restosPermitidosD1 = [2,3,4,5,6,7,8,9,10]

    somaD1 %= 11

    if somaD1 == 0 or somaD1 == 1:
        if cpfSeparado[9] == 0:
            verificacaoD1 = "Autêntico"
        else:
            verificacaoD1 = "D1"

    elif somaD1 in restosPermitidosD1:
        if cpfSeparado[9] == 11 - somaD1:
            verificacaoD1 = "Autêntico"
        else:
            verificacaoD1 = "D1"

    return verificacaoD1

def calcularD2(cpfSeparado):

    cpfSeparadoD2 = []
    pesoD2 = 11
    for i in range(10):
        cpfSeparadoD2.append(cpfSeparado[i] * pesoD2)
        pesoD2 -= 1

    somaD2 = 0
    for i in range(10):
        somaD2 += cpfSeparadoD2[i]

    verificacaoD2 = ""
    restosPermitidosD2 = [2,3,4,5,6,7,8,9,10,11]

    somaD2 %= 11

    if somaD2 == 0 or somaD2 == 1:
        if cpfSeparado[10] == 0:
            verificacaoD2 = "Autêntico"
        else:
            verificacaoD2 = "D2"

    elif somaD2 in restosPermitidosD2:
        if cpfSeparado[10] == 11 - somaD2:
            verificacaoD2 = "Autêntico"
        else:
            verificacaoD2 = "D2"

    return verificacaoD2

def verificarCpf(cpfSeparado):

    verificacaoD1 = calcularD1(cpfSeparado)
    verificacaoD2 = calcularD2(cpfSeparado)

    if verificacaoD1 == verificacaoD2:
        print("Cpf Autentico!")
    else:
        print("CPF Inexistente!")

def main():

    cpfInput = input("Digite seu cpf: (xxx.xxx.xxx-xx) ")

    cpfSeparado = separarCpf(cpfInput)

    verificarCpf(cpfSeparado)

if __name__ == "__main__":
    main()