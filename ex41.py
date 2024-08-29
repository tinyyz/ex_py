print ("\33[1;35;40mQual é o maior número?\n\33[m")

numeros=[]

for i in range(5):
    numeros.append(float(input(f"\33[1;37;40mInforme o {i+1}° número: \33[m")))

print("\33[1;35;40mO maior número é: \33[m", max(numeros))

#Isso aqui abaixo funciona tmb!
# if (numeros[0] > numeros[1] and numeros[0] > numeros[2] and numeros[0] > numeros[3] and numeros[0] > numeros[4]):
#    print("O maior número é: ", numeros[0])
# else:
#    if (numeros[1] > numeros[0] and numeros[1] > numeros[2] and numeros[1] > numeros[3] and numeros[1] > numeros[4]):
#       print("O maior número é: ",numeros[1])
#    else:
#       if (numeros[2] > numeros[0] and numeros[2] > numeros[1] and numeros[2] > numeros[3] and numeros[2] > numeros[4]):
#          print("O maior número é: ", numeros[2])
#       else:
#           if (numeros[3] > numeros[0] and numeros[3] > numeros[1] and numeros[3] > numeros[2] and numeros[3] > numeros[4]):
#              print("O maior número é: ", numeros[3])
#           else:
#              print("O maior número é: ",numeros[4])