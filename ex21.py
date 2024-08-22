import math
print("\33[1;36;40mEquação de 2º grau!\33[m")
a = int(input("\33[1;37;40mInforme o valor de 'a': \33[m"))
b = int(input("\33[1;37;40mInforme o valor de 'b': \33[m"))
c = int(input("\33[1;37;40mInforme o valor de 'c': \33[m"))

if(a!=0 and b!=0 and c!=0):
    delta = (b * b) * -4 * a * c   
    x1 = (-b + math.isqrt(delta)) / (2 * a) 
    x2 = (-b - math.isqrt(delta)) / 2 * a

    print ("\33[1;36;40mA raíz de 'X1' é de: {0:.1f}\33[m".format(x1))
    print ("\33[1;36;40mA raíz de 'X2' é de: {0:.1f}\33[m".format(x2))
else:
    print("\33[1;31;40mNão é uma equação de 2º grau completa.\33[m")
#print (f"A raíz X1 é de {math.ceil(x1)}")
#print (f"A raíz X1 é de {math.floor(x1)}")