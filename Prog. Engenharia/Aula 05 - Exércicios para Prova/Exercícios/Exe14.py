numberOne=float(input("Digite o primeiro número: "))
numberTwo=float(input("Digite o segundo número: "))
numberThree=float(input("Digite o terceiro número: "))
if (numberOne>numberTwo)and(numberOne>numberThree):
    print(f"O primeiro número ({numberOne}) é o maior.")
elif (numberTwo>numberOne)and(numberTwo>numberThree):
    print(f"O segundo número ({numberTwo}) é o maior.")    
elif (numberThree>numberOne)and(numberThree>numberTwo):
    print(f"O terceiro número ({numberThree}) é o maior.")  
else:
    print("Existem números iguais")