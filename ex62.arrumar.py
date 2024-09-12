qtd_alunos = int(input("Informe a quantidade de alunos do 2°DS: "))
alunos = []

for i in range (0,qtd_alunos):
  alunos.append(input(f"Informe o nome do {i+1}º aluno: "))

print(f"A lista de alunos do 2°DS é:\n{alunos}")