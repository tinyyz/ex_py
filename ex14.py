print("\33[1;36;40mAnálise sobre o sexo:\33[m\n")

print ("\33[1;37;40mInforme 'F' para feminino.\33[m")
print ("\33[1;37;40mInforme 'M' para masculino.\33[m\n")

sexo = input("\33[1;37;40mInforme o sexo: \33[m")[0]

if(sexo in 'fF'):
    print("\33[1;35;40mFeminino.\33[m")
elif(sexo in 'mM'):
    print("\33[1;34;40mMasculino.\33[m")
else:
    print("\33[1;31;40mInválido.\33[m")