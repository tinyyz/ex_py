print ("\33[1;35;40mSua idade em diferentes formas!!")

idade = int(input("\33[1;37;40mInforme o ano de seu nascimento: \33[m"))
ano = int(input("\33[1;37;40mInforme o ano atual: \33[m"))

idanos = ano - idade
idme = idanos * 12
iddia = idanos * 365
idse = idanos * 52
id = 2019 - idade

print("\33[1;35;40mA sua idade em anos é: \33[m", idanos)
print("\33[1;35;40mA sua idade em meses é: \33[m", idme)
print("\33[1;35;40mA sua idade em dias é: \33[m", iddia)
print("\33[1;35;40mA sua idade em semanas é: \33[m", idse)
print("\33[1;35;40mA sua idade em 2019 era: \33[m", id)