print ("\33[1;35;40mÁrea de um quadrado!\33[m")

altura = float(input("Informe o valor da altura do quadrado: "))
base = float(input("Informe o valor da base do quadrado: ")) 

if (altura != base): 
    print ("\33[1;35;40mEsta área não é de um quadrado!\33[m")
else:
    area = base * altura

print ("\33[1;35;40mA área do quadrado é: \33[m", area)