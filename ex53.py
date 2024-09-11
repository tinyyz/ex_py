print ("\33[1;35;40mVotação!\33[m")
print ("\nPara o 1º candidato: Digite 1.")
print ("Para o 2º candidato: Digite 2.")
print ("Para o 3º candidato: Digite 3.")
print ("Para votar Nulo: Digite 4.")
c1=0
c2=0
c3=0
nulo=0
i=0
voto=0
veleitores = 0
quantidade_eleitores = int(input("\nInforme a quantidade de eleitores: "))
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
    
print ("\nO 1º candidato teve ", c1, " votos!")
print ("O 2º candidato teve ", c2, " votos!")
print ("O 3º candidato teve ", c3, " votos!")
print ("O total de votos nulos foi de: ", nulo)