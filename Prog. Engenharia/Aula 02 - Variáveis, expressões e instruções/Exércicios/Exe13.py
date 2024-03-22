diametro=float(input("Digite o diâmetro do tubo: "))
velocidade=float(input("Digite a velocidade da vazão (m/s): "))

area=3.14159265359*(diametro)
vazao=area*velocidade
print(f"A vazão é {vazao}m/s")