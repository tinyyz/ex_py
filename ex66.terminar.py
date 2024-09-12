print("\33[1;35;40mMédia disciplinar!\33[m\n")

nome = [4]
notas = [4][5]

for i in range (0,4):
    nome[i] = input(f"Informe o nome do (a) {i+1}º aluno (a): ")
    for j in range (0,5): 
        notas[i][j] = float(input(f"Informe a nota do {j+1}º bimestre: "))

for i in range (0,4):
    notas[i][4]