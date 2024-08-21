print ("\33[1;36;40mConsulte seu salário!\33[m")

salario = float(input("\33[1;37;40mInforme o seu salário atual: \33[mR$"))
percentual = float(input("\33[1;37;40mInforme o percentual de aumento: \33[m%"))
percentual = percentual / 100
aumento = salario * percentual
novos = salario + aumento 

print (f"\n\33[1;37;40mSeu salário novo é: \33[m \33[1;35;40mR${novos}\33[m")