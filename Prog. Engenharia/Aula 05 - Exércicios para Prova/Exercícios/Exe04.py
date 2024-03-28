maxSpeed=float(input("Digite a velocidade máxima permitida: "))
driverSpeed=float(input("Digite a velocidade do motorista: "))
Diff=driverSpeed-maxSpeed

Fine=0

if(Diff>0)and(Diff<10):
    Fine=85.13

elif (Diff>10)and(Diff<=30):
    Fine=127.69

elif (Diff>=31):
    Fine=574.62

else:
    print("Tá dentro da velocidade")

if (Fine>0):
    print(f"A multa da entidade será de {Fine}R$")