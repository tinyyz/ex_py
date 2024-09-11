print("\33[1;35;40mNúmeros divisores de números primos!\33[m\n")
divisor = 0
primo =  True
n = int(input("Informe seu número: "))
nums_primo = list()
for i in range(2,n+1,1):
    primo =  True    
    for d in range(2, i):
        divisor = divisor + 1
        if (i % d == 0):
            primo = False   
            d=i              
    
    if primo:  
        nums_primo.append(i)

print ("\n\33[1;35;40mNúmeros primos entre 1 e", n,"\33[m: ", nums_primo)
print ("\33[1;35;40mQuantidade de divisões feitas: \33[m", divisor)