print ("\33[1;35;40mNúmeros em ordem decrescente!\33[m")

numeros = []

for i in range (0,3):
    numeros.append(int(input(f"\33[1;37;40mDigite o {i+1}º número: ")))

numeros.sort(reverse=True)
print (f"\33[1;35;40m{numeros}\33[m")