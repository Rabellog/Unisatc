valor_original=float(input("Digite o valor original do seu produto: "))
desconto=(valor_original/100)*20
valor_descontado=valor_original-desconto
print(f"O valor original é {valor_original}")
print(f"O valor do desconto é {desconto}R$")
print(f"O valor do produto com o desconto aplicado é {valor_descontado}")