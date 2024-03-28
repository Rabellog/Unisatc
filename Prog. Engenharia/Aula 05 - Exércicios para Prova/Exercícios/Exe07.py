Year = int(input("Digite o ano: "))
if((Year % 4==0) and (Year % 100!=0) or (Year % 400 == 0)):
    print(f"O ano {Year} é um ano bissexto")