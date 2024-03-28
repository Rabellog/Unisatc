kiloFish=int(input("Digite a quantidade de peixe pescado: "))
fine=kiloFish-50
if (fine>0):
    print (f"O valor de peixe pescado excede o limite do estado, você tem que pagar R${fine*4} de multa")
else:
    print (f"O valor está dentro do limite do estado")