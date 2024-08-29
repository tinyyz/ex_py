print("\33[1;35;40mDescubra se o ano é bissexto!\33[m\n")

ano = int(input("\33[1;34;40mInforme o ano que deseja: \33[m"))

if ((ano % 4 == 0 and ano % 100 != 0 ) or ano % 400 ==0):
    print ("\33[1;35;40mEsse ano é bissexto.\33[m")
else:
    print ("\33[1;31;40mEsse ano não é bissexto.\33[m")