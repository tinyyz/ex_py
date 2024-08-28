print ("\33[1;35;40mExpoente de um número!\33[m")

numero = int(input("\33[1;37;40mInforme um número: \33[m"))
expoente = int(input("\33[1;37;40mInforme um expoente: \33[m"))

if(numero < 0):
    print("\33[1;31;40mEscolha outro número.\33[m")
elif(expoente > 10):
    print("\33[1;31;40mEscolha outro valor.\33[m")
else:
    print(numero**expoente)