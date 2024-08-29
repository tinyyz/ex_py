print ("\33[1;35;40mDias da semana!\33[m\n")

dias_semanas = ["", "Domingo!", "Segunda-feira!", "Terça-feira!", "Quarta-feira!", "Quinta-feira!", "Sexta-feira!", "Sábado!"]

print ("\33[1;34;40mInforme o dia da semana em número.\33[m\n")
print ("Obs: Sendo ele de 1 até 7.!")

dia = int(input("\n\33[1;35;40mInforme um número: \33[m"))

if (dia > 7 or dia <= 0):
    print ("\33[1;31;40mDia da semana inválido.\33[m")
else:
    print (dias_semanas[dia])