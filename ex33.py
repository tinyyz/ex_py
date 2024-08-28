numeros = []

numeros.insert(0, int(input("\33[1;35;40mInforme o 1° número inteiro: \33[m")))
numeros.insert(1, int(input("\33[1;35;40mInforme o 2° número inteiro: \33[m")))
numeros.insert(2, float(input("\33[1;35;40mInforme o 3° número, sendo ele em casa decimal: \33[m")))

print ("O resultado é: ", (numeros[0]**2) * (numeros[1]/2))

print ("\nO resultado é: ", (numeros[0]**3) + numeros[1])

print ("\nO resultado é: ", (numeros[1]**3))