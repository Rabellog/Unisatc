frase=str(input("Digite sua frase: "))
palavra_antiga=str(input("Digite a palavra referente da frase: "))
palavra_nova=str(input("Digite a palavra que irá substituir: "))
nova_frase=frase.replace(palavra_antiga,palavra_nova)
print(f"Nova frase: {nova_frase}")