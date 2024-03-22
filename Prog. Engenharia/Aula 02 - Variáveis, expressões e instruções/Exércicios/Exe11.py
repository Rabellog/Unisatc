valor_original=float(input("Digite o valor original do seu produto: "))
valor_desconto=float(input("Digite o desconto em % do seu produto: "))
desconto=(valor_original/100)*valor_desconto
valor_descontado=valor_original-desconto
print(f"O valor original é {valor_original}")
print(f"O valor do desconto é {desconto}R$")
print(f"O valor do produto com o desconto aplicado é {valor_descontado}")