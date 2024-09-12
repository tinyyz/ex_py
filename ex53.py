import os
print ("\33[1;35;40mUrna eletrônica.\33[m")

print ("\n\33[1;37;40mPara o 1º candidato: Digite 1.\33[m")
print ("\33[1;37;40mPara o 2º candidato: Digite 2.\33[m")
print ("\33[1;37;40mPara o 3º candidato: Digite 3.\33[m")
print ("\33[1;31;40mPara votar Nulo: Digite 4.\33[m")

c1=0
c2=0
c3=0
nulo=0
i=0
voto=0
veleitores = 0

quantidade_eleitores = int(input("\nInforme a quantidade de eleitores: "))
os.system('cls')
for i in range(0, quantidade_eleitores):
    voto = int(input("\nDigite o número do seu candidato: "))
    if (voto == 1):
        c1 = c1 +1
    elif (voto == 2):
        c2 = c2 + 1
    elif (voto == 3):
        c3 = c3 + 1
    else:
        nulo = nulo + 1
    
print ("\n\33[1;35;40mO 1º candidato teve \33[m", c1, " \33[1;35;40mvotos!\33[m")
print ("\33[1;35;40mO 2º candidato teve \33[m", c2, " \33[1;35;40mvotos!\33[m")
print ("\33[1;35;40mO 3º candidato teve \33[m", c3, " \33[1;35;40mvotos!\33[m")
print ("\33[1;35;40mO total de votos nulos foi de: \33[m", nulo)