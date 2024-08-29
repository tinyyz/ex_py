print("\33[1;35;40mEquação de 2º grau!\33[m")

a = int(input("Informe o valor de 'A': "))
b = int(input("Informe o valor de 'B': "))
c = int(input("Informe o valor de 'C': "))

delta = 0

if (a == 0):
    print ("\33[1;31;40mEssa equação não é de 2° grau.\33[m")
else:
    delta = (b * b) - (4 * a) * c   
    if (delta < 0):
        print ("\33[1;31;40mA equação não possui raízes.\33[m")
    elif (delta == 0):
        print ("\33[1;35;40mA equação possui apenas uma raíz real.\33[m")
    else:
        print ("\33[1;35;40mA equação possui duas raízes\33[m")