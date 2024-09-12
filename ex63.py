impares = []

print ("\33[1;35;40mNúmeros ímpares!\33[m\n")
for i in range (0,100):
  if not (i % 2 == 0):
    impares.append(i)

print (impares)