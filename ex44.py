print ("\33[1;35;40mNúmeros inteiros entre x e y!\33[m")

numero1 = int(input("Informe o 1° número: "))
numero2 = int(input("Informe o 2° número: "))

passo = 1

if numero1 > numero2:
    numero1 = numero1 - 2
    passo = -1

for numero in range (numero1+1,numero2,passo):
    print (numero)