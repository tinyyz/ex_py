import math 

print("\33[1;35;40mSeja bem vindo (a), a Loja de tintas YuZiee!\33[m")
print("\nInforme o tamanho do local a ser pintado em metros quadrados: ")

area = float(input())

qtd_latas = math.ceil((area/3) / 18)

preco = qtd_latas * 80

print ("\n\33[1;35;40mA quantidade de latas de tinta usadas é: \33[m", qtd_latas)
print ("\33[1;34;40mO valor total será de: \33[mR$",preco)