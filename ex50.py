print("\33[1;35;40mFatorial de um número!\33[m\n")

n = int(input("Informe um número: "))

fatorial = 1
i = 0

for i in range(n,1,-1):
    fatorial = fatorial * i

print ("O fatorial do seu número é: ", fatorial)