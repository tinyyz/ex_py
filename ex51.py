print ("\33[1;35;40mEsse número é primo?\33[m")

num = int(input("\nInforme um número: "))

primo = True

if num < 2:
  primo = False
else:
  for i in range(1, num):
    if num % i == 0:
      primo = False
    else:
      primo = True

if primo == True:
  print("\n\33[1;35;40mO número informado é primo!\33[m")
else:
  print("\n\33[1;37;40mO número informado \33[1;31;40mnão\33[m \33[1;37;40mé primo!\33[m")