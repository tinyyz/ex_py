notas = []
print ("Cálculo de média de notas.")
disciplinas = str (input("Informe a disciplina: "))
for i in range (0,4):
    notas.append(int(input(f"Informe a {i+1}º nota: ")))

media = (notas[0] + notas [1] + notas [2] + notas [3]) /4

if media >= 7:
    print (f"A média das notas desta disciplina é de: ", media)
    print (f"Você foi aprovado (a) nessa disciplina, parabéns!!!")
else:
    print (f"A média das notas desta disciplina é de: ", media)
    print (f"Você foi reprovado (a) nessa disciplina.")