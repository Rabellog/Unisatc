number = int(input("Digite um número inteiro para a conversão: "))
numberHex=hex(number)
numberBin=bin(number)
numberOct=oct(number)
print(f"O número em hexadecimal é {numberHex}")
print(f"O número em binário é {numberBin}")
print(f"O número em octal é {numberOct}")