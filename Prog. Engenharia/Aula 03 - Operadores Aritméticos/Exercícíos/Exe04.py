frase=str(input("Digite a sua frase minúscula: "))
frase_maiuscula=frase.upper()
frase_espaco=frase_maiuscula.replace(" ","")
print(f"Frase em uppercase e strip: {frase_espaco}")