numeros = []

print ("\33[1;35;40mCalculadora!\33[m")

for i in range (0,2):
    numeros.append(int(input(f"Informe o {i+1}º número: ")))

operador = (input(f"Informe qual operador você deseja: "))

if (operador == "+"):
    resultado = numeros [0] + numeros [1]
elif (operador == "-"):
    resultado = numeros [0] - numeros [1]
elif (operador == "/"):
    resultado = numeros [0] / numeros [1]
elif (operador == "*"):
    resultado = numeros [0] * numeros [1]
else:
    print("\33[1;31;40mOperador inválido.\33[m")
print ("\33[1;35;40mO resultado é: \33[m", resultado)