letra = input("\33[1;36;40mDigite uma letra para analisar: \33[m")[0]

if (letra in "aeiou"):
    print("\33[1;37;40mA letra é:\33[m \33[4;35;40mVogal.\33[m")
else:
    print("\33[1;37;40mA letra é:\33[m \33[4;35;40mConsoante.\33[m")