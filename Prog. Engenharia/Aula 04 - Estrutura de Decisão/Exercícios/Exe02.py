nome=str(input("Digite o nome do correto: "))
quantidade=int(input("Digite a quantidade de imóveis vendidos: "))
valortotal=float(input("Digite o valor total de suas vendas: "))
salario=1500+(200*quantidade)+(valortotal/100*5)
print(f"O salário é {salario}")