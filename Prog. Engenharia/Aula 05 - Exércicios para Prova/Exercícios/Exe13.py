numberOne=float(input("Digite a nota 01 do aluno: "))
numberTwo=float(input("Digite a nota 02 do aluno: "))
average=(numberOne+numberTwo)/2
if (average>=7):
    print(f"O aluno foi aprovado com média {average}")
elif (average<7):
    print(f"O aluno foi reprovado com média {average}")
elif (average==10):
    print(f"O aluno foi aprovado com distinção, com média {average}")