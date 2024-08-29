numeros=[]

print ("\33[1;35;40mSoma e média.\33[m\n")
for i in range(5):
    numeros.append(float(input(f"\33[1;37;40mInforme o {i+1}° número: \33[m")))

soma = sum(numeros)
media = soma / 5

print("\n\33[1;34;40mA soma desses números é: \33[m", soma)
print ("\33[1;35;40mA média desses números é: \33[m", media)