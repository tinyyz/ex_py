print ("\33[1;35;40mTurno escolar!\33[m")

print ("\33[1;37;40mInforme 'M' para Matutino.\33[m")
print ("\33[1;37;40mInforme 'V' para Vespertino.\33[m")
print ("\33[1;37;40mInforme 'N' para Noturno.\33[m\n")

turno = input("\33[1;37;40mInforme seu turno: \33[m")[0].upper()

if(turno in 'M'): 
    print("\33[1;33;40mBom diaa!\33[m")
elif(turno in 'V'):
    print("\33[1;32;40mBoa tardee!\33[m")
elif(turno in 'N'):
    print("\33[1;34;40mBoa noitee!\33[m")
else:
    print("\33[1;31;40mTurno inválido.\33[m")