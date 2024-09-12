import os

intervalos = [0,0,0,0,0]
numero = 1

while numero >= 0:
    numero = int(input("Informe um número: "))
    os.system('cls')
    if numero >= 0 and numero <= 25:
        intervalos[0] = intervalos[0]+1
    elif numero > 24 and numero <= 50:
        intervalos[1] = intervalos[1]+1
    elif numero > 50 and numero <= 75:
        intervalos[2] = intervalos[2]+1
    elif numero > 75 and numero <= 100:
        intervalos[3] = intervalos[3]+1
    elif numero > 100:
        intervalos[4] = intervalos[4]+1

print("\33[1;35;40mQuantidade de números nos intervalos!\33[m\n")

print(f"\33[1;35;40mIntervalo [0-25]: \33[m\n {intervalos[0]} \33[1;35;40mnúmeros.\33[m")
print(f"\33[1;35;40mIntervalo [26-50]: \33[m\n {intervalos[1]} \33[1;35;40mnúmeros.\33[m")
print(f"\33[1;35;40mIntervalo [51-75]: \33[m\n {intervalos[2]} \33[1;35;40mnúmeros.\33[m")
print(f"\33[1;35;40mIntervalo [76-100]: \33[m\n {intervalos[3]} \33[1;35;40mnúmeros.\33[m")
print(f"\33[1;35;40mNúmeros maiores que 100: \33[m {intervalos[4]} \33[1;35;40mnúmeros.\33[m")