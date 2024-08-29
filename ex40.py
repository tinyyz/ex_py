nota = float(input("\33[1;35;40mInforme a sua nota: \33[m"))
while (nota < 0 or nota > 10):
    nota = float(input("\33[1;34;40mInforme a sua nota: \33[m"))

print ("\33[1;37;40mVocê conseguiu!!\33[m")