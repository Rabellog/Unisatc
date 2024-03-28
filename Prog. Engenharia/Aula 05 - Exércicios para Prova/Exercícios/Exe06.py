import math
radius = float(input("Digite o raio do círculo: "))
if radius<0:
    print ("Números negativos não são permitidos")
else:
    print(f"A área do círculo é {math.pi*radius**2}")