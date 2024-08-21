notas = []
print ("\33[1;35;46mCálculo de média de notas.\33[m")
disciplinas = str (input("\33[1;35;40mInforme a disciplina: \33[m"))
for i in range (0,4):
    notas.append(float(input(f"\33[1;37;40mInforme a {i+1}º nota: \33[m")))

media = (notas[0] + notas [1] + notas [2] + notas [3]) /4

if media >= 7:
    print (f"\33[1;36;40mA média das notas desta disciplina é de: \33[m", media)
    print (f"\33[1;36;40mVocê foi \33[1;32;40maprovado (a)\33[m \33[1;36;40mnessa disciplina, parabéns!!!\33[m")
else:
    print (f"\33[1;36;40mA média das notas desta disciplina é de: \33[m", media)
    print (f"\33[1;36;40mVocê foi \33[1;31;40mreprovado (a)\33[m \33[1;36;40mnessa disciplina.\33[m")