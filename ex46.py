print ("\33[1;35;40mTabuada!\33[m")

numero = int(input("\33[1;37;40mInforme um número: \33[m"))
i = 0
while (i < 10):
    print (numero, "X", i+1, "=", numero * (i+1))
    i += 1