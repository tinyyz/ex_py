print ("\33[1;35;40mDepósito com rendimento!\33[m")

deposito = float(input("\33[1;37;40mInforme o valor do depósito: R$\33[m"))
taxa = float(input("\33[1;37;40mInforme o valor da taxa: %\33[m"))
rendimento = deposito * taxa

print ("\33[1;35;40mO seu rendimento foi: R$\33[m", rendimento)