print ("\33[1;35;40mConsulte seu salário!\n\33[m")

salario = float(input("\33[1;37;40mInforme o seu salário: R$\33[mR$"))
aumento = salario * 0.05
salario = salario + aumento
imposto = salario * 0.07
salario = salario - imposto

print ("\33[1;35;40mO seu salário atual é: R$\33[m R$", salario)