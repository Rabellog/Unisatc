pv=float(input("Digite o valor inicial do investimento: "))
n=int(input("Digite o número de meses: "))
i=float(input("Digite a rentabilidade mensal em %: "))
fv=pv*(1+i)**n
print(f"O valor final do investimento será {fv}")