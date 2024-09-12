print ("\33[1;35;40mPalíndromo\33[m")

palavra = input("Informe uma palavra para analisarmos se ela é um palíndromo: ")

def substituir_acentos(string):
    acentos = ["á","à", "â", "ã", "ê", "é", "í", "ó", "õ", "ô", "ú", "ç", "-", "," , "."]
    for acento in acentos:
       string = string.replace(acento, ' ')
    return string

frase_invertida = palavra.lower()
frase_invertida = substituir_acentos(frase_invertida);
frase_invertida = frase_invertida.replace(" ", "")
frase_alternativa = frase_invertida
tamanho_frase = len(frase_invertida)
frase_invertida = frase_invertida[::-1]

for i in range (0, tamanho_frase):
    if(frase_invertida[i] == frase_alternativa[i]):
        condicao = True
    else:
        condicao = False
        break

if condicao == True:
    print(f"\n\33[1;34;40mA sequência \"{palavra}\" é um palíndromo.\33[m")
else:
    print(f"\n\33[1;31;40mA sequência \"{palavra}\" não é um palíndromo.\33[m")