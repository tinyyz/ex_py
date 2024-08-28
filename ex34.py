print ("\33[1;35;40mPeso ideal.\33[m")

print ("\nInformações sobre gênero.")
print ("Para \33[1;35;40mFeminino\33[m: Digite '\33[1;35;40mF\33[m'.")
print ("Para \33[1;34;40mMasculino\33[m: Digite '\33[1;34;40mM\33[m'.")

genero = input("\nInforme o seu gênero: ")[0].upper()

if(genero in 'FM'):
    altura = float(input("Informe a sua altura: ").replace(",","."))
    if(genero == 'F'):
        print ("\n\33[1;35;40mSeu peso ideal é: \33[m", (62.1 * altura) - 44.7,"\33[1;35;40mKg.\33[m")
    else:
        print("\n\33[1;34;40mSeu peso ideal é: \33[m", (72.7 * altura) - 58,"\33[1;34;40mKg.\33[m")
else:
    print ("\33[1;31;40mGênero inválido.\33[m")