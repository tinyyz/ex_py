numeros = []
for i in range (0,2):
    numeros.append(int(input(f"Informe o {i+1}º número: ")))
print (numeros)
numeros.sort()
print (numeros)
print (numeros [-1])
