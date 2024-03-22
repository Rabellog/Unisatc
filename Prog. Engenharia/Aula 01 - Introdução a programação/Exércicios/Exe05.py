continuar = "A"
while continuar != "N":
    print ("=======CÁLCULO DE NOTAS=======")
    nome=input("Digite o nome do aluno: ")
    n1=float(input("Digite a nota 01: "))
    n2=float(input("Digite a nota 02: "))
    n3=float(input("Digite a nota 03: "))
    media=float(n1+n2+n3)/3
    if (media>=6):
        print ("O aluno passou!")
    else:
        print ("O aluno rodou!")
    continuar=input("Deseja continuar?")