letra=str(input("Digite o sexo (M/F): "))
match letra:
    case "F":
        print("O sexo é feminino")
    case "M":
        print("O sexo é masculino")
    case _:
        print("Sexo inválido")