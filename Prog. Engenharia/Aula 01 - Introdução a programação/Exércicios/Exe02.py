fv=float(input("Digite o valor final que deseja obter ao final do investimento: "))
n=int(input("Digite o número de meses: "))
i=float(input("Digite a rentabilidade mensal em %: "))
pv=fv/(1+i)**n
print(f"O valor inicial do investimento será {pv}")