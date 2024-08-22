print ("\33[1;35;40mNúmero ao Cubo e ao Quuadrado!\33[m")

numero = int(input("Informe um número: "))

if (numero <= 0): 
    print ("\33[1;31;40mEscolha outro número.\33[m")

quadrado = numero * numero
cubo = (numero * numero) * numero

print ("\33[1;35;40mO quadrado do número {numero} é: \33[m", quadrado)
print ("\33[1;35;40mO cubo do número {numero} é: \33[m", cubo)