import math
raio=(float(input("Digite o raio do hexágono: ")))
base= (raio*math.sqrt(3))/2
area= (base*raio)/2
hexagono=area*6
print(f"A área do hexágono é {hexagono}")