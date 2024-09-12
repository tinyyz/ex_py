print("\33[1;35;40mMaior ou menor?\33[m\n")

numeros = []

for i in range(0,10):
    numeros.append(float(input(f"Informe o {i+1}º número: ")))

menor_num = min (numeros)
maior_num = max (numeros)

print(f"\n\33[1;35;40mO maior número é:\33[m {maior_num} \33[1;35;40me o menor número é:\33[m {menor_num}.\33[m")