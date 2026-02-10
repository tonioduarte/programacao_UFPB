num_Tabuada = int(input("Qual número deseja consultar a tabuada? (1 a 10) "))
multiplicação = 0

if num_Tabuada <= 10:
    for i in range(10):
       multiplicação += 1
       produto = num_Tabuada * multiplicação
       print(f"{num_Tabuada} x {multiplicação} = {produto}")
else:
    print("Somente números entre 0 e 10.")
             


