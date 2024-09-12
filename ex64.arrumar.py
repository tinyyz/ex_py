vogais = ["a","e","i","o","u","á", "à", "â", "ã", "é", "ê", "í", "ó", "õ",]
consoantes = []

frase = input("Informe a frase: ")

for i in range (0,len(frase)):
  if not frase[i] in vogais:
    consoantes.append(frase[i])

print(consoantes)