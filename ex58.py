print("\33[1;35;40mOlá, seja bem-vindo ao posto de gasolina virtual YuZiee!\33[m")

print ("\nDigite\33[1;35;40m [G]\33[m para \33[1;35;40mGasolina\33[m.")
print ("Digite\33[1;34;40m [A]\33[m para \33[1;34;40mÁlcool\33[m.")

combustivel = input("\nInforme qual você deseja:")
combustivel = combustivel.upper()

if (combustivel == "G"):
  litros = float(input("Quantos litros deseja abastecer? "))
  if (litros <= 20):
    preco = litros * 5.50
    desconto = preco * 0.03
    total = preco - desconto
    print(f"\n\33[1;35;40mO valor a ser pago é R$\33[m: {total:.2f}")
  else:
    preco = litros * 5.50
    desconto = preco * 0.05
    total = preco - desconto
    print(f"\n\33[1;34;40mO valor a ser pago é R$\33[m: {total:.2f}")
elif (combustivel == "A"):
  litros = float(input("Quantos litros deseja abastecer? "))
  if (litros <= 20):
    preco = litros * 3.90
    desconto = preco * 0.04
    total = preco - desconto
    print(f"\n\33[1;35;40mO valor a ser pago é R$\33[m: {total:.2f}")
  else:
    preco = litros * 3.90
    desconto = preco * 0.06
    total = preco - desconto
    print(f"\n\33[1;35;40mO valor a ser pago é R$\33[m: {total:.2f}")
else:
  print("\33[1;31;40mOpção inválida.\33[m")