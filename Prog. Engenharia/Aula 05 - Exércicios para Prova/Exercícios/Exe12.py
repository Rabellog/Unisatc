moneyHour=float(input("Digite quanto de dinheiro você recebe por hora: "))  
hoursWorked=int(input("Digite a quantidade de horas trabalhadas no mês: "))
print(f"Seu salário no mês é de {moneyHour*hoursWorked}")
moneyMounth=moneyHour*hoursWorked
ir=(moneyMounth/100)*11
inss=(moneyMounth/100)*8
sindicate=(moneyMounth/100)*5
print(f"O salario bruto é de R${moneyMounth}")
print(f"O valor pago ao imposto de renda é de R${ir}")
print(f"O valor pago ao inss é de R${inss}")
print(f"O valor pago ao inss é de R${sindicate}")
print(f"O salário liquido é {moneyMounth-ir-sindicate-inss}")