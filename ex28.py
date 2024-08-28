print ("\33[1;35;40mQual é o maior número?\33[m")

numeros = []

for i in range (0,3):
    numeros.append(int(input(f"Informe o {i+1}º número: ")))

numeros.sort()

print ("\33[1;35;40mO maior número é: ", numeros [-1])