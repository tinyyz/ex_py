print ("\33[1;35;40mGraus!\33[m")

graus = float(input("Informe a temperatura em graus °C: "))

fahrenheit = (graus * 1.8) + 32
kelvin = graus + 273.15

print ("\33[1;35;40mA temperatura em Fahrenheit é: °\33[m",fahrenheit)
print ("\33[1;35;40mA temperatura em Kelvin é: °\33[m",kelvin)