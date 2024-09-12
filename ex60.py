print ("\33[1;35;40mTábuadas!\33[m\n")
num = int(input("\33[1;37;40mInforme o número para a tabuada: \33[m"))
num_2 = int(input("\33[1;37;40mInforme o número inicial para a tabuada: \33[m"))
num_3 = int(input("\33[1;37;40mInforme o número final para a tabuada: \33[m"))

for i in range (num_2, num_3+1):
  print(f"\n{num} x {i} = {num*i}")