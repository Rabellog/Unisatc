base=float(input("Digite sua renda mensal: "))
if(base<=2259.20):
    aliquota=0

if(base>=2259.21)and(base<=2826.65):
    aliquota=0.075

if(base>=2826.66)and(base<=3751.05):
    aliquota=0.15

if(base>=3751.06)and(base<=4664.68):
    aliquota=0.225

if(base>4664.68):
    aliquota=0.225

imposto=base*aliquota
print(f"O imposto de renda é {imposto}")