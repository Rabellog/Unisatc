import math

raio_maior=float(input("Digite o valor da maior coroa: "))
raio_menor=float(input("Digite o valor da menor coroa: "))
area=3.14159265359*(raio_maior**2-raio_menor**2)
print(f"A área da coroa é {area}m")