print("\33[1;32;40mCálculo de aumento de salário!!\33[m\n")
salario = float(input("\33[1;37;40mInforme o seu salário R$: \33[m"))
aumento = salario * 0.25
novo_s = salario + aumento

print(f"Seu salário era \33[1;32;40mR${salario}\33[m. Você receberá um aumento de \33[1;36;40mR${aumento}\33[m. Seu novo salário é \33[1;32;40mR${novo_s}\33[m")