numeros = []

print ("Calculadora simples!")

for i in range (0,2):
    numeros.append(int(input(f"Informe o {i+1}º número: ")))

print ("Para soma: Informe '+'.")
print ("Para subtração: Informe '-'.")

operador = (input(f"Informe qual dos dois operadores você deseja: "))

if (operador == "+"):
    resultado = numeros [0] + numeros [1]
elif (operador == "-"):
    resultado = numeros [0] - numeros [1]
else:
    print("Operador inválido.")
print ("O resultado é: ", resultado)