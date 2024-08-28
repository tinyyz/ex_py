numeros = []
print ("\33[1;35;40mMultiplicação de números!\33[m")

for i in range (0,3):
    numeros.append(float(input(f"Informe o {i + 1}º número: ")))

multiplicacao = (numeros [0] * numeros [1]) * numeros [2]

print (f"\33[1;35;40mO valor da multiplicação é de:\33[1;35;40m \33[1;37;40m{multiplicacao}\33[m")