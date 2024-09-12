print("\33[1;35;40mNúmeros primos!\33[m\n")

n = int(input("Informe um número: "))

divisor=0 
valor=1

if (n > 0):
    while (valor <= n):
        if (n % valor == 0):
            divisor++
            valor++
            if (divisor == 2):
                print ("O número ", n , " é primo.\n")
elif: 
print ("O número ", n , " não é primo.\n" )
elif:
print ("O número é negativo ou igual a zero.")