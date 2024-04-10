theSum=0
value=0
maior=0
i=0
menor=999999999999999999
while (value!=-1):
    value=int(input("Digite o número: "))
    if (value>0):
        i=i+1
        theSum=value+theSum
        if (value<menor):
            menor=value

        if (value>maior):
            maior=value
    
    if (value<0) and(value!=1):
        print("Valor inválido")
        
average=theSum/i        
print(f"A soma de todos os números é {theSum}")
print(f"A média de todos os números é {average}")
print(f"O maior de todos os números é {maior}")
print(f"O menor de todos os números é {menor}")

