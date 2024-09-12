unidades = {0:"Zero.",1:"Um.",2:"Dois.",3:"Três.",4:"Quatro.",5:"Cinco.",6:"Seis.",7:"Sete.",8:"Oito.",9:"Nove."}
familia_dez = {11:"Onze.",12:"Doze.",13:"Treze.",14:"Quatorze.",15:"Quinze.",16:"Dezesseis.",17:"Dezessete.",18:"Dezoito.",19:"Dezenove."}
dezenas = {1:"Dez.",2:"Vinte.",3:"Trinta.",4:"Quarenta.",5:"Cinquenta.",6:"Sessenta.",7:"Setenta.",8:"Oitenta.",9:"Noventa."}

print ("\33[1;35;40mNúmeros por extenso.\33[m")
num = int(input("\nDigite um número entre 1 e 99: "))

if num >= 1 and num <= 99:
    if num >= 1 and num <= 9:
        unidade = unidades.get(num)
        print(unidade)
    elif num >= 11 and num <= 19:
        unidade = familia_dez.get(num)
        print(unidade)
    else:
        dezena = num // 10
        dezena = dezenas.get(dezena)
        unidade = num % 10
        unidade = unidades.get(unidade) 
        print(dezena, " e ", unidade)