desconto=24.95*0.35
livro=24.95-desconto

quantidade=int(input("Digite a quantidade de livros: "))
if (quantidade >=1):
    transporte=3+((quantidade - 1)*0.75)
    total=transporte+(livro*(quantidade))
    print(f"O valor total é {total} R$")
else: 
    print("Valor inválido")