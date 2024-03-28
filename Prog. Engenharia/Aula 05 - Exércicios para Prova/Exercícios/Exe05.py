numberOne = float(input("O número 01: "))
numberTwo = float(input("O número 02:: "))

print(f"O número 01 é {numberOne}")
print(f"O número 02 é {numberTwo}")
numberOne,numberTwo=numberTwo,numberOne

print(f"O valor 01 virou {numberOne} e o valor 02 virou {numberTwo}")